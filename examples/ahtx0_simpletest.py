# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""
Basic `AHTx0` example test
"""

import time
import board
import busio
import adafruit_ahtx0

# Create the sensor object using I2C
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_ahtx0.AHTx0(i2c)

while True:
    print("\nTemperature: %0.1f C" % sensor.temperature)
    print("Humidity: %0.1f %%" % sensor.relative_humidity)
    time.sleep(2)
