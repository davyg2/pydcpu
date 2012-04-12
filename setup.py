#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

if sys.platform == 'win32':
    from cx_Freeze import setup, Executable
    exs=[Executable("pydcpu-dbg", shortcutName='pydcpu-dbg', shortcutDir='DesktopFolder'),Executable("pydcpu-emul"),Executable("pydcpu-asm")]
else:
    from distutils.core import setup
    exs=[]

setup(name='pydcpu',
      version='0.1',
      description='Dcpu toolkit',
      author='Guillaume DAVY',
      author_email='davyg2@gmail.com',
      url='http://github.com/davyg/pydcpu',
      scripts=['pydcpu-asm', 'pydcpu-dbg', 'pydcpu-emul'],
      packages=['pydcpu'],
      executables = exs
     )

