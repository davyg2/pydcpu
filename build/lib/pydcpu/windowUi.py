# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pydcpu/window.ui'
#
# Created: Thu Apr 12 21:38:20 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.open = QtGui.QPushButton(self.centralwidget)
        self.open.setObjectName(_fromUtf8("open"))
        self.horizontalLayout_2.addWidget(self.open)
        self.contin = QtGui.QPushButton(self.centralwidget)
        self.contin.setObjectName(_fromUtf8("contin"))
        self.horizontalLayout_2.addWidget(self.contin)
        self.step = QtGui.QPushButton(self.centralwidget)
        self.step.setObjectName(_fromUtf8("step"))
        self.horizontalLayout_2.addWidget(self.step)
        self.reload = QtGui.QPushButton(self.centralwidget)
        self.reload.setObjectName(_fromUtf8("reload"))
        self.horizontalLayout_2.addWidget(self.reload)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.breaks = QtGui.QTableView(self.centralwidget)
        self.breaks.setMaximumSize(QtCore.QSize(200, 16777215))
        self.breaks.setObjectName(_fromUtf8("breaks"))
        self.breaks.horizontalHeader().setVisible(False)
        self.breaks.horizontalHeader().setDefaultSectionSize(200)
        self.breaks.verticalHeader().setVisible(False)
        self.verticalLayout_3.addWidget(self.breaks)
        self.addBreak = QtGui.QPushButton(self.centralwidget)
        self.addBreak.setObjectName(_fromUtf8("addBreak"))
        self.verticalLayout_3.addWidget(self.addBreak)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.consol = QtGui.QPlainTextEdit(self.centralwidget)
        self.consol.setEnabled(True)
        self.consol.setAcceptDrops(False)
        self.consol.setReadOnly(True)
        self.consol.setObjectName(_fromUtf8("consol"))
        self.verticalLayout_2.addWidget(self.consol)
        self.command = QtGui.QLineEdit(self.centralwidget)
        self.command.setDragEnabled(True)
        self.command.setObjectName(_fromUtf8("command"))
        self.verticalLayout_2.addWidget(self.command)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.vars = QtGui.QTableView(self.centralwidget)
        self.vars.setMaximumSize(QtCore.QSize(180, 16777215))
        self.vars.setObjectName(_fromUtf8("vars"))
        self.vars.horizontalHeader().setVisible(False)
        self.vars.horizontalHeader().setDefaultSectionSize(80)
        self.vars.verticalHeader().setVisible(False)
        self.verticalLayout_6.addWidget(self.vars)
        self.addVar = QtGui.QPushButton(self.centralwidget)
        self.addVar.setObjectName(_fromUtf8("addVar"))
        self.verticalLayout_6.addWidget(self.addVar)
        self.horizontalLayout.addLayout(self.verticalLayout_6)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.blayout = QtGui.QHBoxLayout()
        self.blayout.setObjectName(_fromUtf8("blayout"))
        self.ram = QtGui.QTableView(self.centralwidget)
        self.ram.setObjectName(_fromUtf8("ram"))
        self.ram.horizontalHeader().setVisible(True)
        self.ram.horizontalHeader().setDefaultSectionSize(80)
        self.blayout.addWidget(self.ram)
        self.verticalLayout.addLayout(self.blayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Dbg", None, QtGui.QApplication.UnicodeUTF8))
        self.open.setText(QtGui.QApplication.translate("MainWindow", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.contin.setText(QtGui.QApplication.translate("MainWindow", "Continue", None, QtGui.QApplication.UnicodeUTF8))
        self.step.setText(QtGui.QApplication.translate("MainWindow", "Step", None, QtGui.QApplication.UnicodeUTF8))
        self.reload.setText(QtGui.QApplication.translate("MainWindow", "Reload", None, QtGui.QApplication.UnicodeUTF8))
        self.addBreak.setText(QtGui.QApplication.translate("MainWindow", "Add breakpoint", None, QtGui.QApplication.UnicodeUTF8))
        self.addVar.setText(QtGui.QApplication.translate("MainWindow", "Add Variable", None, QtGui.QApplication.UnicodeUTF8))

