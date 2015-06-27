#!/bin/sh

swig -python lirc_client.i -I/usr/include

gcc -fpic -c lirc_client_wrap.c -o lirc_client_wrap.o -I/usr/include/python3.4m
gcc -fpic -shared -o _lirc_client.so lirc_client_wrap.o -lpython3.4m -llirc_client

cp _lirc_client.so ..
cp lirc_client.py ..
