# The MIT License (MIT)
#
# Copyright (c) 2020 Kattni Rembor for Adafruit Industries
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
"""
`adafruit_ahtx0`
================================================================================

CircuitPython driver for the Adafruit AHT10 Humidity and Temperature Sensor


* Author(s): Kattni Rembor

Implementation Notes
--------------------

**Hardware:**

.. todo:: Add links to any specific hardware product page(s), or category page(s). Use unordered list & hyperlink rST
   inline format: "* `Link Text <url>`_"

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://github.com/adafruit/circuitpython/releases

.. todo:: Uncomment or remove the Bus Device and/or the Register library dependencies based on the library's use of either.

# * Adafruit's Bus Device library: https://github.com/adafruit/Adafruit_CircuitPython_BusDevice
# * Adafruit's Register library: https://github.com/adafruit/Adafruit_CircuitPython_Register
"""

import time
from adafruit_bus_device.i2c_device import I2CDevice
from micropython import const

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_AHTx0.git"

AHT10_I2CADDR_DEFAULT = const(0x38)  # Default I2C address
AHT10_CMD_CALIBRATE = const(0xE1)  # Calibration command
AHT10_CMD_TRIGGER = const(0xAC)  # Trigger reading command
AHT10_CMD_SOFTRESET = const(0xBA)  # Soft reset command
AHT10_STATUS_BUSY = const(0x80)  # Status bit for busy
AHT10_STATUS_CALIBRATED = const(0x08)  # Status bit for calibrated


class AHTx0:
    def __init__(self, i2c_bus, address=AHT10_I2CADDR_DEFAULT):
        self.i2c_device = I2CDevice.(i2c_bus, address)
        time.sleep(0.02)  # 20ms delay


