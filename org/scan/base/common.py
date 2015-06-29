# -*- coding: utf-8 -*-
'''
Common functions
'''

import inspect

def get_func_name() :
    return inspect.stack()[0][3]
