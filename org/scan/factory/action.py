# -*- coding: utf-8 -*-

from org.scan.action.init import InitAction
from org.scan.action.clone import CloneAction

class ActionFactory :

    @staticmethod
    def create(cmd) :
        return {
                'init' : InitAction(),
                'clone' : CloneAction(),
                }[cmd]
