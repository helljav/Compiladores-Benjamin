from PyQt4 import QtGui
import sys
from presentacion.Alex_Final import Ventana

# Comandos para iniciar la Ventana
def main():

    app = QtGui.QApplication(sys.argv)
    GUI = Ventana()
    sys.exit(app.exec_())

main()