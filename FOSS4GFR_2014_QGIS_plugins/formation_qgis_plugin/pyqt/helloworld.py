
import sys
# import des modules PyQt necessaires
from PyQt4.QtGui import QApplication, QPushButton
# on ne lance les commandes suivantes que si on est dans un script

def on_clicked():
	print "bouton clicked"


if __name__=='__main__':
    # Tous les programmes Qt ont besoin d'une
    # instance de QApplication
    # On passe les arguments de la ligne de commande car Qt
    # sait en interpreter certain
    app = QApplication(sys.argv)
    # On cree un bouton avec un texte dessus
    button = QPushButton("Hello World !")
    button.clicked.connect( app.quit )
    # on doit explicitement demander l'affichage du bouton
    button.show()
    # On lance la boucle evenementielle
    sys.exit(app.exec_())
