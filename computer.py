# -*- coding: utf-8 -*-
"""
           DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
                   Version 2, December 2004

Copyright (C) 2012 Guillaume DAVY <davyg2 at gmail dot com>

Everyone is permitted to copy and distribute verbatim or modified
copies of this license document, and changing it is allowed as long
as the name is changed.

           DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
  TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

 0. You just DO WHAT THE FUCK YOU WANT TO.
"""

import os,sys
import emulateur

from PyQt4 import QtCore,QtGui

class Computer(QtGui.QWidget):
	def __init__(self, emul):
		QtGui.QWidget.__init__(self)
		self.setGeometry(300, 300, 384, 256)
		self.emul = emul

	def paintEvent(self, event):
		qp = QtGui.QPainter()
		qp.begin(self)
		qp.setPen(QtGui.QColor(168, 34, 3))
		qp.setFont(QtGui.QFont('Monospace', 12))
		for i in range(0, 16):
			for j in range(0, 32):
				c = self.emul[0x8000+j+i*32] & 0xff
				if c:
					qp.drawText(QtCore.QPoint(j*12,(i+1)*16), chr(c))      
		qp.end()

