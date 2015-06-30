# -*- coding: utf-8 -*-

class Action :
    '''interface to act command in multigits'''

    def parse(self, argv) :
        raise NotImplementedError('need to implemented this function')

    def execute(self) :
        raise NotImplementedError('need to implemented this function')

    def error(self) :
        raise NotImplementedError('need to implemented this function')
