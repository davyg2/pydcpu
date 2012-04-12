#!/usr/bin/python3
# -*- coding: utf-8 -*-

from distutils.core import setup

setup(name='pydcpu',
      version='0.1a',
      description='Dcpu toolkit',
      author='Guillaume DAVY',
      author_email='davyg2@gmail.com',
      url='http://github.com/davyg/pydcpu',
      scripts=['pydcpu-asm', 'pydcpu-dbg', 'pydcpu-emul'],
      packages=['pydcpu'],
     )
