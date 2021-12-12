from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
import sys
from conexion import *


def agregar():
    print("Hola, soy la acción de agregar")
    nombre = ventana.txtNombre.text() # es como el get de tkinter
    correo = ventana.txtCorreo.text()
    print(nombre, correo)
    obj_contactos = Contactos()
    contactos = obj_contactos.crear_contacto((nombre, correo))
    consultar()

def modificar():
    print("Hola, soy la acción de modificar")
    id = ventana.txtId.text()
    nombre = ventana.txtNombre.text()
    correo = ventana.txtCorreo.text()

    obj_contactos = Contactos()
    contactos = obj_contactos.modificar_contacto((nombre, correo, id))
    consultar()

def eliminar():
    print("Hola, soy la acción de eliminar")
    id = ventana.txtId.text()
    obj_contactos = Contactos()
    obj_contactos.borrar_contacto(id)
    consultar()

def cancelar():
    print("Hola, soy la acción de cancelar")

def consultar():
    ventana.tableContactos.setRowCount(0) # limpiar la tabla 
    indice_control = 0
    obj_contactos = Contactos()
    contactos = obj_contactos.leer_contactos()
    for contacto in contactos:
        ventana.tableContactos.setRowCount(indice_control + 1)
        ventana.tableContactos.setItem(indice_control, 0, QTableWidgetItem(str(contacto[0])))
        ventana.tableContactos.setItem(indice_control, 1, QTableWidgetItem(str(contacto[1])))
        ventana.tableContactos.setItem(indice_control, 2, QTableWidgetItem(str(contacto[2])))
        indice_control += 1

def seleccionar():
    id = ventana.tableContactos.selectedIndexes()[0].data()
    nombre = ventana.tableContactos.selectedIndexes()[1].data()
    correo = ventana.tableContactos.selectedIndexes()[2].data()
    print(id, nombre, correo)
    ventana.txtId.setText(id)
    ventana.txtNombre.setText(nombre)
    ventana.txtCorreo.setText(correo)

aplicacion = QtWidgets.QApplication([])

ventana = uic.loadUi("ventana.ui")
ventana.show()
consultar()
#Poner nombre a los campos
ventana.tableContactos.setHorizontalHeaderLabels(['ID', 'Nombre', 'Correo'])
ventana.tableContactos.setEditTriggers(QTableWidget.NoEditTriggers)
ventana.tableContactos.setSelectionBehavior(QTableWidget.SelectRows)

ventana.tableContactos.cellClicked.connect(seleccionar)

ventana.btnAgregar.clicked.connect(agregar)
ventana.btnModificar.clicked.connect(modificar)
ventana.btnEliminar.clicked.connect(eliminar)
ventana.btnCancelar.clicked.connect(cancelar)

sys.exit(aplicacion.exec())
