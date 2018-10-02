'''... import sys
from PyQt4 import QtGui


class ventana(QtGui.QMainWindow):
    def __init__(self):
        super(ventana,self).__init__()
        self.setGeometry(50,50,500,300)
        self.setWindowTitle("Segunda ventana de prueba")
        
        #Creacion de un menu para salir
        EventoSalir = QtGui.Action(QtGui.QIcon("salir.jpg"),"Salir",self)
        EventoSalir.setShortcut("Ctrl+Q")
        ventana.show()
        '''
#coding=utf-8


import sys


from PyQt4 import QtGui


aplicacion = QtGui.QApplication(sys.argv)


ventana = QtGui.QWidget()
ventana.setWindowTitle('Primera ventana') 
ventana.resize(220, 150)  
ventana.move(200, 200) 
ventana.show()



sys.exit(aplicacion.exec_())
        


