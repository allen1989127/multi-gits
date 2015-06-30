#!/usr/bin/env python2

from command import Command

if __name__ == '__main__' :
    ls_cmd = Command('ls')

    print 'run with system'
    res = ls_cmd.runBackResult(['-al'])
    print 'res is %d' % (res)
    print ''
    res = ls_cmd.runBackResult(None)
    print 'res is %d' % (res)
    print ''

    print 'run with popen'
    res = ls_cmd.runBackStr(['-al'])
    print res
    res = ls_cmd.runBackStr(None)
    print res
    res = ls_cmd.runBackStr(123)

