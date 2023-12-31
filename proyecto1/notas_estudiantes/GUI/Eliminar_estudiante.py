# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Eliminar_estudiante.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Eliminar_estudiante(object):
    def setupUi(self, Eliminar_estudiante):
        Eliminar_estudiante.setObjectName("Eliminar_estudiante")
        Eliminar_estudiante.resize(321, 161)
        Eliminar_estudiante.setMinimumSize(QtCore.QSize(321, 161))
        Eliminar_estudiante.setMaximumSize(QtCore.QSize(321, 161))
        self.gridLayout = QtWidgets.QGridLayout(Eliminar_estudiante)
        self.gridLayout.setObjectName("gridLayout")
        self.lay_ver_principal = QtWidgets.QVBoxLayout()
        self.lay_ver_principal.setObjectName("lay_ver_principal")
        self.lbl_eliminar_estudiante = QtWidgets.QLabel(Eliminar_estudiante)
        self.lbl_eliminar_estudiante.setStyleSheet("font: 35pt \"Gill Sans MT Condensed\";")
        self.lbl_eliminar_estudiante.setObjectName("lbl_eliminar_estudiante")
        self.lay_ver_principal.addWidget(self.lbl_eliminar_estudiante, 0, QtCore.Qt.AlignHCenter)
        self.lay_frm_datos = QtWidgets.QFormLayout()
        self.lay_frm_datos.setObjectName("lay_frm_datos")
        self.lbl_codigo = QtWidgets.QLabel(Eliminar_estudiante)
        self.lbl_codigo.setStyleSheet("font: 11pt \"Gill Sans MT\";")
        self.lbl_codigo.setObjectName("lbl_codigo")
        self.lay_frm_datos.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_codigo)
        self.txt_codigo = QtWidgets.QLineEdit(Eliminar_estudiante)
        self.txt_codigo.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border: none;\n"
"border-bottom: 2px solid rgba(0, 0, 0, 255);\n"
"padding-bottom: 5px;\n"
"font: 10pt \"Gill Sans MT\";")
        self.txt_codigo.setObjectName("txt_codigo")
        self.lay_frm_datos.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txt_codigo)
        self.lay_ver_principal.addLayout(self.lay_frm_datos)
        self.btn_eliminar_estudiante = QtWidgets.QPushButton(Eliminar_estudiante)
        self.btn_eliminar_estudiante.setStyleSheet("QPushButton#btn_eliminar_estudiante {\n"
"    background-color: rgba(255,175,15,156);\n"
"    border-radius: 5px;\n"
"    font: 15pt \"Gill Sans MT Condensed\";\n"
"}\n"
"\n"
"QPushButton#btn_eliminar_estudiante:hover {\n"
"    background-color: rgba(255,200,15,156);\n"
"    border-radius: 5px;\n"
"    \n"
"    font: 15pt \"Gill Sans MT Condensed\";\n"
"}\n"
"\n"
"QPushButton#btn_eliminar_estudiante:pressed {\n"
"    background-color: rgba(115,0,15,115);\n"
"    border-radius: 5px;\n"
"    \n"
"    font: 15pt \"Gill Sans MT Condensed\";\n"
"}")
        self.btn_eliminar_estudiante.setObjectName("btn_eliminar_estudiante")
        self.lay_ver_principal.addWidget(self.btn_eliminar_estudiante)
        self.gridLayout.addLayout(self.lay_ver_principal, 0, 0, 1, 1)

        self.retranslateUi(Eliminar_estudiante)
        QtCore.QMetaObject.connectSlotsByName(Eliminar_estudiante)

    def retranslateUi(self, Eliminar_estudiante):
        _translate = QtCore.QCoreApplication.translate
        Eliminar_estudiante.setWindowTitle(_translate("Eliminar_estudiante", "Eliminar Estudiante"))
        self.lbl_eliminar_estudiante.setText(_translate("Eliminar_estudiante", "Eliminar estudiante"))
        self.lbl_codigo.setText(_translate("Eliminar_estudiante", "ID/Codigo: "))
        self.txt_codigo.setPlaceholderText(_translate("Eliminar_estudiante", "Inserte ID/codigo"))
        self.btn_eliminar_estudiante.setText(_translate("Eliminar_estudiante", "Eliminar"))
