# -*- coding: utf-8 -*-
'''
Tool class to run system command
'''

import common
import subprocess
import os

class Command :

    def __init__(self, baseCommand) :
        self.base_command = baseCommand

    def __get_class_function_name(self) :
        claz = 'Class %s' % (self.__class__.__name__)
        func = 'Function %s' % (common.get_func_name())
        message_list = [claz, func]
        message = ', '.join(message_list)

        return message

    def runBackResult(self, args) :
        if not isinstance(args, list) and args is not None :
            raise TypeError(str(args) + ' is error in ' + self.__get_class_function_name())

        if args is None :
            args = []

        args_copy = args[0:]
        args_copy.insert(0, self.base_command)
        command = ' '.join(args_copy)

        return os.system(command)

    def runBackStr(self, args) :
        if not isinstance(args, list) and args is not None :
            raise TypeError(str(args) + ' is error in ' + self.__get_class_function_name())

        if args is None :
            args = []

        command = args[0:]
        command.insert(0, self.base_command)

        popen = subprocess.Popen(command, stdout = subprocess.PIPE, stderr = subprocess.PIPE)

        content = ''
        while True :
            next_line = popen.stdout.readline()
            if next_line == '' and popen.poll() != None :
                break
            content += next_line

        return content
