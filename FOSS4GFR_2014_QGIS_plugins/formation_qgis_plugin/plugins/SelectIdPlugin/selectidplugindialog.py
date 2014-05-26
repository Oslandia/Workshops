# -*- coding: utf-8 -*-
"""
/***************************************************************************
 SelectIdPluginDialog
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
"""

from PyQt4 import QtCore, QtGui
from ui_selectidplugin import Ui_SelectIdPlugin
# create the dialog for zoom to point


class SelectIdPluginDialog(QtGui.QDialog):
    def __init__(self, iface):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.iface = iface
        self.ui = Ui_SelectIdPlugin()
        self.ui.setupUi(self)

        # On connecte tous les signaux necessaires
        # la methode (privee) appelee est creee ci dessous
        self._connectSlots()
        # Par defaut la liste est vide donc on ne peut rien supprimer
        # on desactive le bouton delete
        # tous les objets graphiques fait avec qt designer
        # sont dans l objet ui qui est
        # une instance de notre classe generee
        # trouver la méthode du bouton delete qui le desactive
        # et remplacer la ligne suivante
        self.ui.del_button.setEnabled(False)

    def _connectSlots(self):
        # On connecte les signaux des boutons a nos methodes definies ci dessous
        # connexion du signal du bouton d'ajout
        self.connect(self.ui.add_button, QtCore.SIGNAL('clicked()'), self._slotAddClicked)
        # on connecte maintenant le bouton delete a notre slot dedie
        self.connect(self.ui.del_button, QtCore.SIGNAL('clicked()'), self._slotDeleteClicked)
        self.connect(self.ui.select_button, QtCore.SIGNAL('clicked()'),\
            self._slotSelectClicked)
        self.connect(self.ui.clear_button, QtCore.SIGNAL('clicked()'),\
            self._slotClearAllClicked)

    # la methode appelee lorsque le bouton d ajout est clique
    def _slotAddClicked(self):
        # On lit le texte du LineEdit
        # remplacer None par la recuperation du texte du QLineEdit
        text = self.ui.text.text()
        # Si le texte n'est pas vide
        if text:
            # On insere un nouveau listviewitem
            # avec le texte du LineEdit
            # Trouver la méthode pour ajouter un element dans le ListViewItem
            self.ui.todo_liste.addItem(text)
            # On vide le LineEdit
            self.ui.text.clear()
            # On active le bouton de suppression car on est surs
            # que le listview contient au moins un element
            self.ui.del_button.setEnabled(True)

    # la methode appelee lorsque le bouton delete est clique
    def _slotDeleteClicked(self):
        # On enleve l'item courant du listview (takeItem)
        self.ui.todo_liste.takeItem(self.ui.todo_liste.currentRow())
        # On verifie si la liste est vide ( count() )
        # remplacer le False par le vrai test
        # si oui on desactive le bouton de suppression
        if not self.ui.todo_liste.count():
            self.ui.del_button.setEnabled(False)

    def _slotClearAllClicked(self):
        self.ui.todo_liste.clear()
        self.ui.del_button.setEnabled(False)
        
    def _slotSelectClicked(self):
        l = self.iface.activeLayer()
        # print l.name()
        # QtGui.QMessageBox.information(self, "Info layer", "Layer actif : %s" % l.name())
        if l is not None:
            l.removeSelection()
            l.select([int(self.ui.todo_liste.item(i).text()) for i in range(self.ui.todo_liste.count())])
        self.iface.mapCanvas().zoomToSelected()
