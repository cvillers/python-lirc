// Builds the lirc_client.py module and backing _lirc_client extension.

%module (package="lirc.lirc_internal") lirc_client

%{
#include <lirc/lirc_client.h>
%}

%ignore lirc_readconfig;
%ignore lirc_readconfig_only;
%ignore lirc_freeconfig;

%include <lirc_client.h>
