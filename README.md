# USB Serial Port Finder

This Python script detects and lists USB serial ports that are currently connected to the system. It works on both Windows and Linux platforms.

## Overview

The script uses the `serial` module from the `pyserial` library to find available serial ports. It filters the ports to include only those that are likely connected to USB devices.

## Features

- Cross-platform support (Windows and Linux)
- Automatically identifies USB serial ports
- Simple output of found ports

## Requirements

- Python 3.x
- `pyserial` library

You can install `pyserial` using pip:

```bash
pip install pyserial
