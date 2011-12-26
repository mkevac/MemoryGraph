__author__ = 'marko'

import time
import sys

def get_memory(pid=1):
    with open("/proc/%s/status" % pid) as f:
        data = f.readlines()
        for line in data:
            lines = line.split()
            if lines[0] == "VmRSS:":
                return lines[1]

def main():

    if len(sys.argv) < 3:
        print "usage: %s <pid> <output data file> [period]" % sys.argv[0]
        sys.exit(0)

    pid = sys.argv[1]
    path = sys.argv[2]

    try:
        period = int(sys.argv[3])
    except KeyError:
        period = 60

    while True:
        with open(path, "a") as f:
            f.writelines("%s;%s\n" % (time.strftime("%H:%M"), get_memory(pid)))

        time.sleep(period)

if __name__ == "__main__":
    main()