# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_selectidplugin.ui'
#
# Created: Wed Nov 20 14:31:36 2013
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_SelectIdPlugin(object):
    def setupUi(self, SelectIdPlugin):
        SelectIdPlugin.setObjectName(_fromUtf8("SelectIdPlugin"))
        SelectIdPlugin.resize(581, 562)
        self.gridLayout = QtGui.QGridLayout(SelectIdPlugin)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.add_button = QtGui.QPushButton(SelectIdPlugin)
        self.add_button.setObjectName(_fromUtf8("add_button"))
        self.gridLayout.addWidget(self.add_button, 0, 3, 1, 1)
        self.todo_liste = QtGui.QListWidget(SelectIdPlugin)
        self.todo_liste.setAlternatingRowColors(True)
        self.todo_liste.setObjectName(_fromUtf8("todo_liste"))
        self.gridLayout.addWidget(self.todo_liste, 1, 0, 1, 4)
        self.clear_button = QtGui.QPushButton(SelectIdPlugin)
        self.clear_button.setObjectName(_fromUtf8("clear_button"))
        self.gridLayout.addWidget(self.clear_button, 2, 3, 1, 1)
        self.del_button = QtGui.QPushButton(SelectIdPlugin)
        self.del_button.setObjectName(_fromUtf8("del_button"))
        self.gridLayout.addWidget(self.del_button, 2, 2, 1, 1)
        self.text = QtGui.QLineEdit(SelectIdPlugin)
        self.text.setObjectName(_fromUtf8("text"))
        self.gridLayout.addWidget(self.text, 0, 0, 1, 3)
        self.select_button = QtGui.QPushButton(SelectIdPlugin)
        self.select_button.setObjectName(_fromUtf8("select_button"))
        self.gridLayout.addWidget(self.select_button, 2, 1, 1, 1)

        self.retranslateUi(SelectIdPlugin)
        QtCore.QMetaObject.connectSlotsByName(SelectIdPlugin)

    def retranslateUi(self, SelectIdPlugin):
        SelectIdPlugin.setWindowTitle(_translate("SelectIdPlugin", "SelectIdPlugin", None))
        self.add_button.setText(_translate("SelectIdPlugin", "&Ajouter", None))
        self.clear_button.setText(_translate("SelectIdPlugin", "Supprimer &tout", None))
        self.del_button.setText(_translate("SelectIdPlugin", "S&upprimer", None))
        self.text.setPlaceholderText(_translate("SelectIdPlugin", "Feature ID", None))
        self.select_button.setText(_translate("SelectIdPlugin", "Sélectionner", None))

