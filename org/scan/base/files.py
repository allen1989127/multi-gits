# -*- coding: utf-8 -*-

'''
tool module to operate files or dirs
'''

import os
import shutil

def safe_mkdir(path) :
    if isinstance(path, str) or len(path) >= 256 :
        raise ValueError('Error path : ' + path)

    res = os.path.isabs(path)
    abs_path = None
    if res :
        abs_path = path
    else :
        abs_path = os.path.join(os.getcwd(), os.path.sep, path)

    if not os.path.exists(abs_path) :
        os.mkdirs(abs_path)

def isexist(path) :
    return os.path.exists(path)

def copyfile(src, dest) :
    if not isinstance(src, str) or not isinstance(dest, str) :
        return False

    try :
        shutil.copyfile(src, dest)
    except IOError, e:
        return False

    return True
