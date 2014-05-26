# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_selectaroundpostgis.ui'
#
# Created: Fri Nov 22 09:58:52 2013
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

class Ui_SelectAroundPostGIS(object):
    def setupUi(self, SelectAroundPostGIS):
        SelectAroundPostGIS.setObjectName(_fromUtf8("SelectAroundPostGIS"))
        SelectAroundPostGIS.resize(490, 359)
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.gridLayout = QtGui.QGridLayout(self.dockWidgetContents)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.dockWidgetContents)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.dockWidgetContents)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.coords = QtGui.QLineEdit(self.dockWidgetContents)
        self.coords.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.coords.sizePolicy().hasHeightForWidth())
        self.coords.setSizePolicy(sizePolicy)
        self.coords.setBaseSize(QtCore.QSize(0, 0))
        self.coords.setObjectName(_fromUtf8("coords"))
        self.gridLayout.addWidget(self.coords, 3, 0, 1, 2)
        self.pick_button = QtGui.QPushButton(self.dockWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pick_button.sizePolicy().hasHeightForWidth())
        self.pick_button.setSizePolicy(sizePolicy)
        self.pick_button.setCheckable(True)
        self.pick_button.setObjectName(_fromUtf8("pick_button"))
        self.gridLayout.addWidget(self.pick_button, 3, 2, 1, 1)
        self.search_button = QtGui.QPushButton(self.dockWidgetContents)
        self.search_button.setObjectName(_fromUtf8("search_button"))
        self.gridLayout.addWidget(self.search_button, 4, 0, 1, 3)
        self.results = QtGui.QTableView(self.dockWidgetContents)
        self.results.setObjectName(_fromUtf8("results"))
        self.gridLayout.addWidget(self.results, 5, 0, 1, 3)
        self.distance = QtGui.QSpinBox(self.dockWidgetContents)
        self.distance.setMinimum(10)
        self.distance.setMaximum(1000)
        self.distance.setSingleStep(10)
        self.distance.setProperty("value", 100)
        self.distance.setObjectName(_fromUtf8("distance"))
        self.gridLayout.addWidget(self.distance, 0, 1, 1, 2)
        self.label_2 = QtGui.QLabel(self.dockWidgetContents)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.table = QtGui.QComboBox(self.dockWidgetContents)
        self.table.setEditable(True)
        self.table.setObjectName(_fromUtf8("table"))
        self.table.addItem(_fromUtf8(""))
        self.table.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.table, 1, 1, 1, 2)
        self.load_button = QtGui.QPushButton(self.dockWidgetContents)
        self.load_button.setObjectName(_fromUtf8("load_button"))
        self.gridLayout.addWidget(self.load_button, 6, 2, 1, 1)
        self.layer_name = QtGui.QLineEdit(self.dockWidgetContents)
        self.layer_name.setObjectName(_fromUtf8("layer_name"))
        self.gridLayout.addWidget(self.layer_name, 6, 1, 1, 1)
        SelectAroundPostGIS.setWidget(self.dockWidgetContents)

        self.retranslateUi(SelectAroundPostGIS)
        QtCore.QMetaObject.connectSlotsByName(SelectAroundPostGIS)

    def retranslateUi(self, SelectAroundPostGIS):
        SelectAroundPostGIS.setWindowTitle(_translate("SelectAroundPostGIS", "Select Around Point", None))
        self.label.setText(_translate("SelectAroundPostGIS", "Search for features within :", None))
        self.label_3.setText(_translate("SelectAroundPostGIS", "Around (x, y) :", None))
        self.pick_button.setText(_translate("SelectAroundPostGIS", "Pick", None))
        self.search_button.setText(_translate("SelectAroundPostGIS", "Search", None))
        self.distance.setSuffix(_translate("SelectAroundPostGIS", " m", None))
        self.label_2.setText(_translate("SelectAroundPostGIS", "On table :", None))
        self.table.setItemText(0, _translate("SelectAroundPostGIS", "geo_parc_pol", None))
        self.table.setItemText(1, _translate("SelectAroundPostGIS", "geo_bati_pol", None))
        self.load_button.setText(_translate("SelectAroundPostGIS", "Load layer", None))
        self.layer_name.setPlaceholderText(_translate("SelectAroundPostGIS", "Layer Name", None))

