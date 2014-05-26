# -*- coding: utf-8 -*-
"""
/***************************************************************************
 SelectAroundPostGIS
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
 This script initializes the plugin, making it known to QGIS.
"""

def classFactory(iface):
    # load SelectAroundPostGIS class from file SelectAroundPostGIS
    from selectaroundpostgis import SelectAroundPostGIS
    return SelectAroundPostGIS(iface)
