%module lirc_client
%{
#include <lirc/lirc_client.h>
%}

%ignore lirc_readconfig;
%ignore lirc_readconfig_only;
%ignore lirc_freeconfig;

%include <lirc/lirc_client.h>
