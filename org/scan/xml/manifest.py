# -*- coding: utf-8 -*-

from xml.etree import ElementTree
import hashlib

CHECK_SUM_ERROR = 0

class ManifestError(Exception) :

    def setCode(self, code) :
        self.code = code

    def getCode(self) :
        return self.code

class ManifestHandler :

    __git_node__ = './git'

    __remote_path__ = 'remote-path'
    __local_path__ = 'local-path'
    __check_sum__ = 'check-sum'
    
    def __init__(self, path) :
        self.path = path
        with open(path, 'rt') as f :
            self.xml_tree = ElementTree.parse(f)
            f.close()

    def __cal_check_sum(self, node) :
        local_path = node.attrib[self.__local_path__]
        remote_path = node.attrib[self.__remote_path__]
        return hashlib.sha1(local_path + ',' + remote_path).hexdigest()

    def addCheckSum(self) :
        git_nodes = self.xml_tree.findall(self.__git_node__)
        for git_node in git_nodes :
            check_sum = self.__cal_check_sum(git_node)
            git_node.attrib[self.__check_sum__] = check_sum

        self.xml_tree.write(self.path)

    def getPaths(self) :
        git_nodes = self.xml_tree.findall(self.__git_node__)
        nodes_paths = {}
        for git_node in git_nodes :
            if git_node.attrib[self.__check_sum__] != self.__cal_check_sum(git_node) :
                e = ManifestError('Error when compare check sum in node')
                e.setCode(CHECK_SUM_ERROR)
                raise e
            else :
                nodes_paths[git_node.attrib[self.__check_sum__]] = (git_node.attrib[self.__local_path__], git_node.attrib[self.__remote_path__])

        return nodes_paths
