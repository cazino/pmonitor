Works only on linux !

Deliberate use of python stdlib only (could have used psutil, or other packages).
Does not handle child process (damn psutil would have been handy)


Requirements:

 - Tested in python 3.4, requires setuptools
 - gdb (we use gcore)


 Install:
  - python setup.py install


Usage: 

 - pmonitor --pid=XX --maxfd=YY

pmonitor whatches the process specified through '--pid' option
and dumps some informations on it when watched process opens
more file descriptor than the number specified through '--maxfd' option.

Information dumped are the following files:
 - loadavg
 - proc_meminfo
 - %PID%_meminfo
 - %PID%_fdlist
 - %PID%_core.%PID%


pmonitor might need to be run as root (gcore complains about it in my environnment).


 Dummy daemon used for testing:

 - pmonitor-dd --fdnum=XXX --tick=YY

 I will open a new file descriptor
 until it reaches the number specified through '--fdnum' option.
 The time elapsed between each file description opening is specified trough 
 '--tick option' (in seconds)


