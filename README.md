# Python LIRC client

This is a simple client for LIRC. It is complete enough to suit my needs.

## Requirements

This module has been tested with the following:

* LIRC 0.9.2
* Python 3.4
* SWIG 3.0.5

## Installation

The project is built with setuptools. The generated SWIG files are included in case you do not have SWIG on your system.
Simply type:

    setup.py install

## Usage

See `examples/client.py` for the high-level interface. See `examples/internal.py` for the low-level interface.

# TODO ideas

## Don't use SWIG

I used SWIG because it let me get up and running very quickly (it also helps that lirc_client.h is very simple). Replace it
with ctypes (see `experimental/lircclient_ctypes.py` for an example) or Cython.

## Non-blocking commands

`lirc_command_run` can communicate with the LIRC daemon asynchronously. It would be neat to offer non-blocking versions
 of functions.