Introduction
============

.. image:: https://readthedocs.org/projects/adafruit-circuitpython-ahtx0/badge/?version=latest
    :target: https://circuitpython.readthedocs.io/projects/ahtx0/en/latest/
    :alt: Documentation Status

.. image:: https://img.shields.io/discord/327254708534116352.svg
    :target: https://adafru.it/discord
    :alt: Discord

.. image:: https://github.com/adafruit/Adafruit_CircuitPython_AHTx0/workflows/Build%20CI/badge.svg
    :target: https://github.com/adafruit/Adafruit_CircuitPython_AHTx0/actions
    :alt: Build Status

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
    :alt: Code Style: Black

CircuitPython driver for the Adafruit AHT10 or AHT20 Humidity and Temperature Sensor


Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_
* `Bus Device <https://github.com/adafruit/Adafruit_CircuitPython_BusDevice>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://circuitpython.org/libraries>`_.

Installing from PyPI
=====================

On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally `from
PyPI <https://pypi.org/project/adafruit-circuitpython-ahtx0/>`_. To install for current user:

.. code-block:: shell

    pip3 install adafruit-circuitpython-ahtx0

To install system-wide (this may be required in some cases):

.. code-block:: shell

    sudo pip3 install adafruit-circuitpython-ahtx0

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .env
    source .env/bin/activate
    pip3 install adafruit-circuitpython-ahtx0

Usage Example
=============

.. code-block:: python

    import time
    import board
    import busio
    import adafruit_ahtx0

    # Create library object using our Bus I2C port
    i2c = busio.I2C(board.SCL, board.SDA)
    sensor = adafruit_ahtx0.AHTx0(i2c)

    while True:
        print("\nTemperature: %0.1f C" % sensor.temperature)
        print("Humidity: %0.1f %%" % sensor.relative_humidity)
        time.sleep(2)


Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/adafruit/Adafruit_CircuitPython_AHTx0/blob/master/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

Documentation
=============

For information on building library documentation, please check out `this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.
