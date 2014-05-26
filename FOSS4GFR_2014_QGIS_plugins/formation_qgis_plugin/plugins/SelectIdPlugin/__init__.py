# -*- coding: utf-8 -*-
"""
/***************************************************************************
 SelectIdPlugin
                                 A QGIS plugin
 Select features by entering IDs
                             -------------------
        begin                : 2013-11-20
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
    # load SelectIdPlugin class from file SelectIdPlugin
    from selectidplugin import SelectIdPlugin
    return SelectIdPlugin(iface)
