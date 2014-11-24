Works only on linux !

Deliberate use of python stdlib only (could have used psutil, or other packages).


Requirements:
 - Tested in python 3.4
 - gdb (we use gcore)

Usage: 

 - pmonitor --pid=XX --maxfd=YY

 pmonitor might need to be run as root (because it uses gcore)


 Dummy daemon used for testing:

 - pmonitor-dd --fdnum=XXX

 I will open a new file descriptor every 5 seconds 
 until it reaches the number specified through '--fdnum' option.


