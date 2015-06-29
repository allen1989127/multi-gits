#/usr/bin/env python2
#-*- coding:utf-8 -*-

'''
main tool command, is the interface user run every command.
'''

import sys

import org.scan.base.constants as constants

def usage() :
    print '[usage] multigits'
    for key in constants.COMMAND_LIST :
        print '\t%-12s%s' % (key, constants.COMMAND_LIST[key])

def main(argv) :
    if len(argv) < 2 :
        usage()
        sys.exit(1)

    if argv[1] not in constants.COMMAND_LIST :
        usage()
        sys.exit(2)

    action = ActionFactory.create(argv[2])

if __name__ == '__main__' :
    main(sys.argv)
