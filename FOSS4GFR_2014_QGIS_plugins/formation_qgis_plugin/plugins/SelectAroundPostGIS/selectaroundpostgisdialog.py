# -*- coding: utf-8 -*-
"""
/***************************************************************************
 SelectAroundPostGISDialog
                                 A QGIS plugin
 Search specific tables for features within given distance
                             -------------------
        begin                : 2013-11-21
        copyright            : (C) 2013 by Vincent Picavet
        email                : vincent.picavet@oslandia.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from PyQt4 import QtCore, QtGui, QtSql
from qgis.gui import *
from qgis.core import *
from ui_selectaroundpostgis import Ui_SelectAroundPostGIS

class SelectAroundPostGISDialog(QtGui.QDockWidget):
    def __init__(self, iface):
        QtGui.QDockWidget.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_SelectAroundPostGIS()
        self.ui.setupUi(self)
        self.iface = iface
        self.ui.coords.setText("0, 0")
        self.query = """select 
            *
        from
            %s as t
        where
            st_dwithin(the_geom, st_setsrid(st_makepoint(%s, %s), 21781), %s)
        """
        self.oldMapTool = self.iface.mapCanvas().mapTool()
        # create MapTool
        self.mapTool = QgsMapToolEmitPoint(self.iface.mapCanvas())
        # connect maptool click event to slot
        self.connect(self.mapTool, QtCore.SIGNAL("canvasClicked(const QgsPoint&, Qt::MouseButton)"), self._slotCanvasClicked)
        # enable maptool by default
        # self.iface.mapCanvas().setMapTool(self.mapTool)
        # connect pick button to slot
        self.connect(self.ui.pick_button, QtCore.SIGNAL("toggled(bool)"), self._slotPickToggled)
        # connect search button
        self.connect(self.ui.search_button, QtCore.SIGNAL("clicked()"),
        self._slotSearchClicked)
        # connect load button
        self.connect(self.ui.load_button, QtCore.SIGNAL("clicked()"),
        self._slotLoadClicked)

    
    def _slotCanvasClicked(self, point):
        self.ui.coords.setText("%s, %s" % (point.x(), point.y()))
        
    def _slotPickToggled(self, checked):
        # if button is selected, our tool is activated
        if checked:
            # save old map tool to restore it later
            self.oldMapTool = self.iface.mapCanvas().mapTool()
            # activate our map tool
            self.iface.mapCanvas().setMapTool(self.mapTool)
            # disable coords manual input
            self.ui.coords.setEnabled(False)
        else:
            # if pick button is not checked then reenable old map tool
            self.iface.mapCanvas().setMapTool(self.oldMapTool)
            # enable manual coords input
            self.ui.coords.setEnabled(True)

    
    def _slotSearchClicked(self):
        search_coords = [float(d.strip()) for d in self.ui.coords.text().split(",")]
        qm = QtSql.QSqlQueryModel()
        # DB type, host, user, password...
        db = QtSql.QSqlDatabase.addDatabase("QPSQL");
        db.setHostName("lsnpgt01")
        db.setDatabaseName("voiriegeo")
        db.setUserName("voiriegeo_adm")
        db.setPassword("Ls3Qt6msjmok")
        ok = db.open()
        
        # True if connected
        if ok:
        	print 'Connected to Postgresql'
        else:
        	print 'Postgresql'
        # do a query "on" a DB connection
        query = self.query % (self.ui.table.currentText(), search_coords[0]
                , search_coords[1], self.ui.distance.value())
        print query
        qm.setQuery(query)
        self.ui.results.setModel(qm)
        db.close()

    def _slotLoadClicked(self):
        search_coords = [float(d.strip()) for d in self.ui.coords.text().split(",")]    
        uri = QgsDataSourceURI()
        uri.setConnection("lsnpgt01", "5432", "voiriegeo", "voiriegeo_adm", "Ls3Qt6msjmok")
        query = self.query % (self.ui.table.currentText(), search_coords[0]
                , search_coords[1], self.ui.distance.value())
        uri.setDataSource("", "(%s)" % query, "the_geom", "", "id")
        self.iface.addVectorLayer(uri.uri(), self.ui.layer_name.text(), "postgres")

