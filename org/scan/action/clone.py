# -*- coding: utf-8 -*-

from optparse import OptionParser

from org.scan.base import files
import org.scan.base.constants as constants
from org.scan.base.command import Command
from org.scan.xml.manifest import ManifestHandler
from org.scan.xml.manifest import ManifestError

from base import Action

import os
import sys

INIT_MULTIGITS = 'some errors in .multigits, remove it and init again or just init it'

def default_handle(val = None) :
    if not files.isexist(os.path.join(constants.MULTIGITS_PATH, 'readers')) :
        print INIT_MULTIGITS
        sys.exit(8)

    reader_manifest = ManifestHandler(os.path.join(constants.MULTIGITS_PATH, 'readers'))
    try :
        paths = reader_manifest.getPaths()
    except ManifestError, e :
        print e
        sys.exit(9)

    git_cmd = Command('git')
    for check_sum, path in paths.items() :
        git_cmd.runBackResult(['clone', path[1], path[0]])

clone_handler = {
        'default' : default_handle,
        }

class CloneAction(Action) :

    def __init__(self) :
        self.parser = OptionParser(prog = 'multigits.py clone')

    def parse(self, argv) :
        return True

    def error(self) :
        self.parser.parse_args(['-h'])

    def execute(self) :
        clone_handler['default']()
