# -*- coding: utf-8 -*-

from org.scan.action.init import InitAction

class ActionFactory :

    @staticmethod
    def create(cmd) :
        return {
                'init' : InitAction(),
                }[cmd]
