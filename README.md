# Python LIRC client

This is a simple client for LIRC. It is complete enough to suit my needs.

## Requirements

This module has been tested with the following:

* LIRC 0.9.2
* Python 3.4
* SWIG 3.0.5

## Building

Run `swig/make.sh` to build the library and dump `lirc_client.py` and `_lirc_client.so` into the top-level directory.

## Installation

Copy `lircclient.py`, `lirc_client.py` and `_lirc_client.so` to a directory on your PYTHONPATH.

## Usage

See `sample.py` for the high-level interface. See `swig/sample.py` for the low-level interface.

# TODO ideas

## Don't use SWIG

I used SWIG because it let me get up and running very quickly (it also helps that lirc_client.h is very simple). Replace it
with ctypes (see `lircclient_ctypes.py` for an example) or Cython.

## Real installation script

Use `distutils` and a real `setup.py`.

## Non-blocking commands

`lirc_command_run` can communicate with the LIRC daemon asynchronously. It would be neat to offer non-blocking versions
 of functions.