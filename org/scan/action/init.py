# -*- coding: utf-8 -*-

'''
This action is to parse and execute multigits init command
'''

from optparse import OptionParser

class InitAction(Action) :

    def parse(self, argv) :
        parser = OptionParser()

