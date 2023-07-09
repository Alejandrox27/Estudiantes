# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Agregar_notas.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Agregar_notas(object):
    def setupUi(self, Agregar_notas):
        Agregar_notas.setObjectName("Agregar_notas")
        Agregar_notas.resize(320, 217)
        Agregar_notas.setMinimumSize(QtCore.QSize(320, 217))
        Agregar_notas.setMaximumSize(QtCore.QSize(320, 217))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/notas.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Agregar_notas.setWindowIcon(icon)
        Agregar_notas.setStyleSheet("")
        self.gridLayout = QtWidgets.QGridLayout(Agregar_notas)
        self.gridLayout.setObjectName("gridLayout")
        self.lay_ver_principal = QtWidgets.QVBoxLayout()
        self.lay_ver_principal.setObjectName("lay_ver_principal")
        self.lbl_Agregar_Notas = QtWidgets.QLabel(Agregar_notas)
        self.lbl_Agregar_Notas.setStyleSheet("font: 35pt \"Gill Sans MT Condensed\";")
        self.lbl_Agregar_Notas.setObjectName("lbl_Agregar_Notas")
        self.lay_ver_principal.addWidget(self.lbl_Agregar_Notas, 0, QtCore.Qt.AlignHCenter)
        self.lay_frm_datos = QtWidgets.QFormLayout()
        self.lay_frm_datos.setObjectName("lay_frm_datos")
        self.lbl_codigo = QtWidgets.QLabel(Agregar_notas)
        self.lbl_codigo.setStyleSheet("font: 11pt \"Gill Sans MT\";")
        self.lbl_codigo.setObjectName("lbl_codigo")
        self.lay_frm_datos.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_codigo)
        self.lbl_Nota = QtWidgets.QLabel(Agregar_notas)
        self.lbl_Nota.setStyleSheet("font: 11pt \"Gill Sans MT\";")
        self.lbl_Nota.setObjectName("lbl_Nota")
        self.lay_frm_datos.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbl_Nota)
        self.txt_codigo = QtWidgets.QLineEdit(Agregar_notas)
        self.txt_codigo.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border: none;\n"
"border-bottom: 2px solid rgba(0, 0, 0, 255);\n"
"color: rgba(0,0,0,255);\n"
"padding-bottom: 5px;")
        self.txt_codigo.setObjectName("txt_codigo")
        self.lay_frm_datos.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txt_codigo)
        self.spb_nota = QtWidgets.QDoubleSpinBox(Agregar_notas)
        self.spb_nota.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border: none;\n"
"border-bottom: 2px solid rgba(0, 0, 0, 255);\n"
"color: rgba(0,0,0,255);\n"
"padding-bottom: 5px;")
        self.spb_nota.setMaximum(5.0)
        self.spb_nota.setObjectName("spb_nota")
        self.lay_frm_datos.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.spb_nota)
        self.lay_ver_principal.addLayout(self.lay_frm_datos)
        self.btn_agregar_nota = QtWidgets.QPushButton(Agregar_notas)
        self.btn_agregar_nota.setStyleSheet("QPushButton#btn_agregar_nota {\n"
"    background-color: rgba(145,12,115,116);\n"
"    border-radius: 5px;\n"
"    font: 15pt \"Gill Sans MT Condensed\";\n"
"}\n"
"\n"
"QPushButton#btn_agregar_nota:hover {\n"
"    background-color: rgba(175,12,175,116);\n"
"    border-radius: 5px;\n"
"    \n"
"    font: 15pt \"Gill Sans MT Condensed\";\n"
"}\n"
"\n"
"QPushButton#btn_agregar_nota:pressed {\n"
"    background-color: rgba(225,0,225,255);\n"
"    border-radius: 5px;\n"
"    \n"
"    font: 15pt \"Gill Sans MT Condensed\";\n"
"}")
        self.btn_agregar_nota.setObjectName("btn_agregar_nota")
        self.lay_ver_principal.addWidget(self.btn_agregar_nota)
        self.gridLayout.addLayout(self.lay_ver_principal, 0, 0, 1, 1)

        self.retranslateUi(Agregar_notas)
        QtCore.QMetaObject.connectSlotsByName(Agregar_notas)

    def retranslateUi(self, Agregar_notas):
        _translate = QtCore.QCoreApplication.translate
        Agregar_notas.setWindowTitle(_translate("Agregar_notas", "Agregar Notas"))
        self.lbl_Agregar_Notas.setText(_translate("Agregar_notas", "Agregar notas"))
        self.lbl_codigo.setText(_translate("Agregar_notas", "ID/codigo: "))
        self.lbl_Nota.setText(_translate("Agregar_notas", "Nota: "))
        self.txt_codigo.setPlaceholderText(_translate("Agregar_notas", "Inserte ID/codigo"))
        self.btn_agregar_nota.setText(_translate("Agregar_notas", "Agregar Nota"))
from notas_estudiantes.images import imagenes_rc
