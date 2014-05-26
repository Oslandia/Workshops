# import des modules Qt
from PyQt4 import QtGui, QtCore
import sys

if __name__=='__main__':

    # creation de l'application
    app = QtGui.QApplication(sys.argv)

    # creation d'une fenetre principale
    window = QtGui.QWidget()
    # changeons le titre de la fenetre
    window.setWindowTitle("Signal")
    # ajout d'un bouton dans la fenetre
    # Le bouton sera enfant de la fenetre
    button = QtGui.QPushButton("Cliquer ici", window)
    # redimensionnons le bouton
    button.resize(150, 50)
    # connectons le signal de clic au slot quit() de l'application
    button.connect(button, QtCore.SIGNAL("clicked()"),\
        app, QtCore.SLOT("quit()"))
    # affichons la fenetre
    window.show()
    # lancons la boucle evenementielle
    app.exec_()
