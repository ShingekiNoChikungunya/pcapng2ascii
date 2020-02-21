#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys
from keypress import hexcodes_to_ascii

def usage():
    print("\nUsage python p2a.py <file_in.pcapng>")
    exit(0)


def main():
    if len(sys.argv) != 2:
        usage()
    pcapng = sys.argv[1]
    cmd = "tshark -r " + pcapng + "  -Y 'usb.capdata' -T fields -e usb.capdata > keypress"
    os.system(cmd)
    result = hexcodes_to_ascii('keypress')
    print("\n", result, "\n")

main()

