"""
"""

import argparse
import os
import sys
import subprocess
import time


class PMonitor(object):
    """ Process Monitor, a process gets identified by its PID
    """
    def __init__(self, pid, maxfd):
        self._pid = pid
        self._maxfd = maxfd
        self._proc_dir = '/proc/%s' % self._pid

    def _list_fd(self):
        """List file descriptors.

        TODO add option to ignore or not deleted files, sockets, pipes.
        """
        links = list()
        fd_dir = self._proc_dir + '/fd'
        for f in os.listdir(fd_dir):
            links.append(os.path.join(fd_dir, f))
        return [os.readlink(l) for l in links]

    def _count_fd(self):
        return len(self._list_fd())

    def _read_meminfo(self):
        with open(self._proc_dir + '/status', 'rb') as f:
            return f.read()

    def _write_corefile(self, path):
        subprocess.call(["gcore", "-o", path, "%s" % self._pid])

    def _dump_infos(self):
        with open("%s_meminfo" % self._pid, 'wb') as f:
            f.write(self._read_meminfo())
        with open("proc_meminfo", 'wb') as f:
            f.write(read_meminfo())
        with open("loadavg", 'wb') as f:
            f.write(read_loadavg())
        self._write_corefile('%s_core' % self._pid)

    def run_forever(self):
        while True:
            current_fdnum = self._count_fd()
            if current_fdnum > self._maxfd:
                sys.stdout.write("Max fd reached, dumping infos...\n")
                self._dump_infos()
                return
            else:
                time.sleep(1)


def read_meminfo():
    with open('/proc/meminfo', 'rb') as f:
        return f.read()


def read_loadavg():
    with open('/proc/loadavg', 'rb') as f:
        return f.read()


def run():
    parser = argparse.ArgumentParser(description='Pmonitor')
    parser.add_argument(
        '--pid', dest='pid', action='store', type=int,
        help='PID of the process to watch')
    parser.add_argument(
        '--maxfd', dest='maxfd', action='store', type=int,
        help='Max number of file descriptors')
    args = parser.parse_args()
    daemon = PMonitor(args.pid, args.maxfd)
    daemon.run_forever()
