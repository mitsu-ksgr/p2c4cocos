#!/usr/bin/python
# coding: utf-8

import argparse
import plistlib

def dump_plist(plist_path) :
    base = plistlib.readPlist(plist_path)

    for key, val in base.items():
        v = val
        if isinstance(val, str) and len(val) > 20:
            v = 'string data. Size = {0}'.format(len(val))
        print '{0:<30}: {1}'.format(key, v)


if __name__ == '__main__':
    # parse cli args.
    parser = argparse.ArgumentParser(
        description = 'dump plist.',
        version = '0.0.1')
    parser.add_argument('plist_path',
            help='Path to plist-file of the Particle System.')
    args = parser.parse_args()

    # dump
    dump_plist(args.plist_path)

