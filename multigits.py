#/usr/bin/env python2
#-*- coding:utf-8 -*-

'''
main tool command, is the interface user run every command.
'''

import sys

import org.scan.base.constants as constants

from org.scan.factory.action import ActionFactory

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

    argv = argv[1:]

    action = None
    try :
        action = ActionFactory.create(argv[0])
    except KeyError, e :
        usage()
        sys.exit(3)

    res = action.parse(argv)
    if not res :
        action.error()

    action.execute()

if __name__ == '__main__' :
    main(sys.argv)
