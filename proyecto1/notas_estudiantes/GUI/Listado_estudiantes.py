# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Listado_estudiantes.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Listado_estudiantes(object):
    def setupUi(self, Listado_estudiantes):
        Listado_estudiantes.setObjectName("Listado_estudiantes")
        Listado_estudiantes.resize(589, 257)
        Listado_estudiantes.setMinimumSize(QtCore.QSize(589, 257))
        Listado_estudiantes.setMaximumSize(QtCore.QSize(589, 257))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/lista.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Listado_estudiantes.setWindowIcon(icon)
        Listado_estudiantes.setStyleSheet("QWidget #Listado_estudiantes {\n"
"background-color: qlineargradient(spread:pad, x1:0.763, y1:0.00568182, x2:0.761, y2:0.954545, stop:0.146893 rgba(255, 255, 255, 255), stop:0.80791 rgba(149, 0, 0, 255));\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(Listado_estudiantes)
        self.gridLayout.setObjectName("gridLayout")
        self.lay_ver_principal = QtWidgets.QVBoxLayout()
        self.lay_ver_principal.setObjectName("lay_ver_principal")
        self.tbl_tabla_estudiantes = QtWidgets.QTableWidget(Listado_estudiantes)
        self.tbl_tabla_estudiantes.setStyleSheet("")
        self.tbl_tabla_estudiantes.setObjectName("tbl_tabla_estudiantes")
        self.tbl_tabla_estudiantes.setColumnCount(5)
        self.tbl_tabla_estudiantes.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_tabla_estudiantes.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_tabla_estudiantes.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_tabla_estudiantes.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_tabla_estudiantes.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_tabla_estudiantes.setHorizontalHeaderItem(4, item)
        self.lay_ver_principal.addWidget(self.tbl_tabla_estudiantes)
        self.gridLayout.addLayout(self.lay_ver_principal, 0, 0, 1, 1)

        self.retranslateUi(Listado_estudiantes)
        QtCore.QMetaObject.connectSlotsByName(Listado_estudiantes)

    def retranslateUi(self, Listado_estudiantes):
        _translate = QtCore.QCoreApplication.translate
        Listado_estudiantes.setWindowTitle(_translate("Listado_estudiantes", "Listado estudiantes"))
        item = self.tbl_tabla_estudiantes.horizontalHeaderItem(0)
        item.setText(_translate("Listado_estudiantes", "ID/Codigo"))
        item = self.tbl_tabla_estudiantes.horizontalHeaderItem(1)
        item.setText(_translate("Listado_estudiantes", "Nombre"))
        item = self.tbl_tabla_estudiantes.horizontalHeaderItem(2)
        item.setText(_translate("Listado_estudiantes", "Puesto"))
        item = self.tbl_tabla_estudiantes.horizontalHeaderItem(3)
        item.setText(_translate("Listado_estudiantes", "Promedio"))
        item = self.tbl_tabla_estudiantes.horizontalHeaderItem(4)
        item.setText(_translate("Listado_estudiantes", "Foto"))
from notas_estudiantes.images import imagenes_rc
