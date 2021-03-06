"""
author: deadc0de6 (https://github.com/deadc0de6)
Copyright (c) 2017, deadc0de6

Catcli generic compressed data lister
----------------------------------------------------------------------------------------
author for modifications to add rar support: focalfocal (https://github.com/focalfocal)
Copyright (c) 2020, focalfocal for the modifications
"""

import os
import tarfile
import zipfile
from unrar import rarfile

class Decomp:

    def __init__(self):
        self.ext = {
            'tar': self._tar,
            'tgz': self._tar,
            'gz': self._tar,
            'tar.gz': self._tar,
            'xz': self._tar,
            'tar.xz': self._tar,
            'lzma': self._tar,
            'tar.lzma': self._tar,
            'tlz': self._tar,
            'bz2': self._tar,
            'tar.bz2': self._tar,
            'zip': self._zip,
            'rar': self._rar}

    def get_format(self):
        '''return list of supported extensions'''
        return list(self.ext.keys())

    def get_names(self, path):
        '''get tree of compressed archive'''
        ext = os.path.splitext(path)[1][1:]
        if ext in list(self.ext.keys()):
            return self.ext[ext](path)
        return None

    def _tar(self, path):
        '''return list of file names in tar'''
        if not tarfile.is_tarfile(path):
            return None
        tar = tarfile.open(path, "r")
        return tar.getnames()

    def _zip(self, path):
        '''return list of file names in zip'''
        if not zipfile.is_zipfile(path):
            return None
        z = zipfile.ZipFile(path)
        return z.namelist()

    def _rar(self, path):
        '''return list of file names in rar'''
        if not rarfile.is_rarfile(path):
            return None
        r = rarfile.RarFile(path)
        return r.namelist()
