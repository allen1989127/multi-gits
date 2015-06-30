# -*- coding: utf-8 -*-

'''
This action is to parse and execute multigits init command
'''

import os

from optparse import OptionParser
from base import Action

from org.scan.base import files
import org.scan.base.constants as constants
from org.scan.base.command import Command

RESET_MULTIGITS = u'multigits inited, remove .multigits before init'

def url_handle(url) :
    git_cmd = Command('git')
    ret = files.isexist(constants.MULTIGITS_PATH)
    if ret :
        print RESET_MULTIGITS
    else :
        git_cmd.runBackResult(['clone', url, os.path.join(constants.MULTIGITS_PATH ,constants.MANIFEST_PATH)])

def sync_handle(sync) :
    git_cmd = Command('git')
    ret = files.isexist(os.path.join(constants.MULTIGITS_PATH ,constants.MANIFEST_PATH ,r'.git'))
    if not ret :
        print RESET_MULTIGITS
    else :
        save_cwd = os.getcwd()
        os.chdir(os.path.join(save_cwd, constants.MULTIGITS_PATH, constants.MANIFEST_PATH))
        git_cmd.runBackResult(['pull'])
        os.chdir(save_cwd)

init_handler = {
        'url' : url_handle,
        'sync' : sync_handle,
        }

class InitAction(Action) :

    def __init__(self) :
        self.parser = OptionParser(prog = 'multigits.py init')

    def parse(self, argv) :
        self.parser.add_option('-u', '--manifest-url',
                dest = 'url', 
                help = 'manifest repository location')
        self.parser.add_option('-s', '--sync',
                dest = 'sync', default = False, action = 'store_true',
                help = 'sync manifest repository in multigits')

        (options, args) = self.parser.parse_args(argv)

        (option, res) = self.__checkArgs(options)
        if not res :
            return False

        self.option = option
        return True

    def error(self) :
        self.parser.parse_args(['-h'])

    def __checkArgs(self, options) :
        options_dict = {}

        if options.url != None :
            options_dict['url'] = options.url

        if options.sync :
            options_dict['sync'] = options.sync

        if len(options_dict) != 1 :
            return (None, False)

        return (options_dict, True)

    def execute(self) :
        for (k, v) in self.option.items() :   # never loop twice
            init_handler[k](v)
