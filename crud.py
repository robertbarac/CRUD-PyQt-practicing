from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
import sys
from conexion import *


def agregar():
    print("Hola, soy la acción de agregar")
    obj_contactos = Contactos()
    obj_contactos.iniciar_conexion()

def modificar():
    print("Hola, soy la acción de modificar")

def eliminar():
    print("Hola, soy la acción de eliminar")

def cancelar():
    print("Hola, soy la acción de cancelar")

aplicacion = QtWidgets.QApplication([])

ventana = uic.loadUi("ventana.ui")
ventana.show()
#Poner nombre a los campos
ventana.tableContactos.setHorizontalHeaderLabels(['ID', 'Nombre', 'Correo'])
ventana.tableContactos.setEditTriggers(QTableWidget.NoEditTriggers)
ventana.tableContactos.setSelectionBehavior(QTableWidget.SelectRows)

ventana.btnAgregar.clicked.connect(agregar)
ventana.btnModificar.clicked.connect(modificar)
ventana.btnEliminar.clicked.connect(eliminar)
ventana.btnCancelar.clicked.connect(cancelar)

sys.exit(aplicacion.exec())