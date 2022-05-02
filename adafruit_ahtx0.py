# SPDX-FileCopyrightText: 2020 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
`adafruit_ahtx0`
================================================================================

CircuitPython driver for the Adafruit AHT10/AHT20 Temperature & Humidity Sensor


* Author(s): Kattni Rembor

Implementation Notes
--------------------

**Hardware:**

* `Adafruit AHT20 Temperature & Humidity Sensor breakout:
  <https://www.adafruit.com/product/4566>`_ (Product ID: 4566)

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://circuitpython.org/downloads

* Adafruit's Bus Device library:
  https://github.com/adafruit/Adafruit_CircuitPython_BusDevice

"""

import time

try:
    # This is only needed for typing
    import busio  # pylint: disable=unused-import
except ImportError:
    pass


from adafruit_bus_device.i2c_device import I2CDevice
from micropython import const

__version__: str = "0.0.0-auto.0"
__repo__: str = "https://github.com/adafruit/Adafruit_CircuitPython_AHTx0.git"

AHTX0_I2CADDR_DEFAULT: int = const(0x38)  # Default I2C address
AHTX0_CMD_CALIBRATE: int = const(0xE1)  # Calibration command
AHTX0_CMD_TRIGGER: int = const(0xAC)  # Trigger reading command
AHTX0_CMD_SOFTRESET: int = const(0xBA)  # Soft reset command
AHTX0_STATUS_BUSY: int = const(0x80)  # Status bit for busy
AHTX0_STATUS_CALIBRATED: int = const(0x08)  # Status bit for calibrated


class AHTx0:
    """
    Interface library for AHT10/AHT20 temperature+humidity sensors

    :param ~busio.I2C i2c_bus: The I2C bus the AHT10/AHT20 is connected to.
    :param int address: The I2C device address. Default is :const:`0x38`

    **Quickstart: Importing and using the AHT10/AHT20 temperature sensor**

        Here is an example of using the :class:`AHTx0` class.
        First you will need to import the libraries to use the sensor

        .. code-block:: python

            import board
            import adafruit_ahtx0

        Once this is done you can define your `board.I2C` object and define your sensor object

        .. code-block:: python

            i2c = board.I2C()  # uses board.SCL and board.SDA
            aht = adafruit_ahtx0.AHTx0(i2c)

        Now you have access to the temperature and humidity using
        the :attr:`temperature` and :attr:`relative_humidity` attributes

        .. code-block:: python

            temperature = aht.temperature
            relative_humidity = aht.relative_humidity

    """

    def __init__(
        self, i2c_bus: busio.I2C, address: int = AHTX0_I2CADDR_DEFAULT
    ) -> None:
        time.sleep(0.02)  # 20ms delay to wake up
        self.i2c_device = I2CDevice(i2c_bus, address)
        self._buf = bytearray(6)
        self.reset()
        if not self.calibrate():
            raise RuntimeError("Could not calibrate")
        self._temp = None
        self._humidity = None

    def reset(self) -> None:
        """Perform a soft-reset of the AHT"""
        self._buf[0] = AHTX0_CMD_SOFTRESET
        with self.i2c_device as i2c:
            i2c.write(self._buf, start=0, end=1)
        time.sleep(0.02)  # 20ms delay to wake up

    def calibrate(self) -> bool:
        """Ask the sensor to self-calibrate. Returns True on success, False otherwise"""
        self._buf[0] = AHTX0_CMD_CALIBRATE
        self._buf[1] = 0x08
        self._buf[2] = 0x00
        with self.i2c_device as i2c:
            i2c.write(self._buf, start=0, end=3)
        while self.status & AHTX0_STATUS_BUSY:
            time.sleep(0.01)
        if not self.status & AHTX0_STATUS_CALIBRATED:
            return False
        return True

    @property
    def status(self) -> int:
        """The status byte initially returned from the sensor, see datasheet for details"""
        with self.i2c_device as i2c:
            i2c.readinto(self._buf, start=0, end=1)
        # print("status: "+hex(self._buf[0]))
        return self._buf[0]

    @property
    def relative_humidity(self) -> int:
        """The measured relative humidity in percent."""
        self._readdata()
        return self._humidity

    @property
    def temperature(self) -> int:
        """The measured temperature in degrees Celsius."""
        self._readdata()
        return self._temp

    def _readdata(self) -> None:
        """Internal function for triggering the AHT to read temp/humidity"""
        self._buf[0] = AHTX0_CMD_TRIGGER
        self._buf[1] = 0x33
        self._buf[2] = 0x00
        with self.i2c_device as i2c:
            i2c.write(self._buf, start=0, end=3)
        while self.status & AHTX0_STATUS_BUSY:
            time.sleep(0.01)
        with self.i2c_device as i2c:
            i2c.readinto(self._buf, start=0, end=6)

        self._humidity = (
            (self._buf[1] << 12) | (self._buf[2] << 4) | (self._buf[3] >> 4)
        )
        self._humidity = (self._humidity * 100) / 0x100000
        self._temp = ((self._buf[3] & 0xF) << 16) | (self._buf[4] << 8) | self._buf[5]
        self._temp = ((self._temp * 200.0) / 0x100000) - 50
