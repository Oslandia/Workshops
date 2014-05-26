l = qgis.utils.iface.activeLayer()
pr = l.dataProvider()
feat = QgsFeature()

# filtre des features
filter = QgsFeatureRequest()

# sous ensemble
extent = QgsRectangle(-27,42,20,52)
filter.setFilterRect( extent )

filter.setSubsetOfAttributes([3])

it = pr.getFeatures( filter )
while it.nextFeature(feat):
    geom = feat.geometry()
    print feat.attributes()[3], geom.area()
