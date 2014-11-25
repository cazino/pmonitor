"""
"""

import argparse
import os
import sys
import tempfile
import time


def run():
    """ Runs a dummmy daemon who open a new file descriptor every 0.5 second
    until it reaches the number specified trough command line.
    """

    parser = argparse.ArgumentParser(description='Pmonitor Dummy daemon')
    parser.add_argument(
        '--fdnum', dest='fdnum', action='store', type=int,
        help='Number of file descriptor to open')
    parser.add_argument(
        '--tick', dest='tick', action='store', type=float,
        help='A new file descriptor will be opened every tick (in seconds)')
    args = parser.parse_args()
    daemon = DummyDaemon(args.fdnum, args.tick)
    daemon.run_forever()


class DummyDaemon(object):

    def __init__(self, fdnum, tick):
        self.fdnum = fdnum
        self.pid = os.getpid()
        self.tick = tick

    def run_forever(self):
        """What about closed fd ?
        """
        sys.stdout.write("Pid: %s\n" % self.pid)
        fd_created = []
        msg_displayed = False
        while True:
            # GOTCHA: counting files in a directory
            # implies opening a file descriptor....
            current_fdnum = self._count_fd() - 1
            # END GOTCHA
            if current_fdnum < self.fdnum:
                fd, fobj = tempfile.mkstemp()
                fd_created.append(fd)
            elif not msg_displayed:
                sys.stdout.write("%s fd were opened.\n" % current_fdnum)
                msg_displayed = True
            time.sleep(self.tick)

    def _count_fd(self):
        listdir = os.listdir("/proc/%s/fd" % self.pid)
        return len(listdir)
