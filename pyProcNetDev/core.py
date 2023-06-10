#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

class ProcNetDev(object):

    def __init__(self, path='/proc/net/dev'):
        self.path = path

    def fileobj(self):
        return open(self.path, 'r')

    def __str__(self):
        with self.fileobj() as f:
            lines = [line.strip() for line in f]
        return '\n'.join(lines)

    def __repr__(self):
        return self.__str__()

    def dict(self):
        d = {}
        # parse field names from first two lines
        with self.fileobj() as f:
            rxtxNames = [ x.strip() for x in re.split("\|", f.readline()) ][1:]
            rxtxFields = [ x.strip() for x in re.split("\|", f.readline()) ][1:]
            headers = {}
            for direction, subfields in list(zip(rxtxNames, rxtxFields)):
                headers[direction] = re.split(" +", subfields)
            for line in f:
                ifname_and_values = [ x.strip() for x in re.split(":", line) ]
                ifname = ifname_and_values[0]
                values = re.split(" +", ifname_and_values[1])
                d[ifname] = {}
                i = 0
                for direction in rxtxNames:
                    d[ifname][direction] = {}
                    for field_name in headers[direction]:
                        d[ifname][direction][field_name] = int(values[i])
                        i = i + 1
        return d

    def search(self, regex):
        with self.fileobj() as f:
            matcher = re.compile(regex, re.IGNORECASE)
            return [k for k in f if matcher.match(k)]

    # get() reparses the file so use dict() if you need more than one
    # interface's stats
    def get(self, ifname):
        return self.dict()[ifname]

if __name__ == '__main__':
    """ test the class """
    import pprint
    pp = pprint.PrettyPrinter()
    # next is for debugging with a saved copy of the live file
    # procNetDev = ProcNetDev("t:\proc-net-dev-202306091541.txt")
    procNetDev = ProcNetDev()
    print("================\nnext for representation")
    print(procNetDev)
    print("================\nnext for demonstrating searching for interface names")
    pp.pprint(procNetDev.search(".*em.*"))
    print("================\nnormal use as a dictionary")
    pp.pprint(procNetDev.dict())
