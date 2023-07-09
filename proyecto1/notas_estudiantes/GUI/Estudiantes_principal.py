# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Estudiantes_principal.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EstudiantesPrincipal(object):
    def setupUi(self, EstudiantesPrincipal):
        EstudiantesPrincipal.setObjectName("EstudiantesPrincipal")
        EstudiantesPrincipal.resize(765, 568)
        EstudiantesPrincipal.setMinimumSize(QtCore.QSize(640, 480))
        EstudiantesPrincipal.setMaximumSize(QtCore.QSize(35287, 283225))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/colegio.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        EstudiantesPrincipal.setWindowIcon(icon)
        EstudiantesPrincipal.setStyleSheet("")
        self.wdg_principal = QtWidgets.QWidget(EstudiantesPrincipal)
        self.wdg_principal.setStyleSheet("")
        self.wdg_principal.setObjectName("wdg_principal")
        self.gridLayout = QtWidgets.QGridLayout(self.wdg_principal)
        self.gridLayout.setObjectName("gridLayout")
        self.lay_ver_principal = QtWidgets.QVBoxLayout()
        self.lay_ver_principal.setObjectName("lay_ver_principal")
        self.mdiArea = QtWidgets.QMdiArea(self.wdg_principal)
        self.mdiArea.setObjectName("mdiArea")
        self.lay_ver_principal.addWidget(self.mdiArea)
        self.gridLayout.addLayout(self.lay_ver_principal, 0, 0, 1, 1)
        EstudiantesPrincipal.setCentralWidget(self.wdg_principal)
        self.mbr_barra_estudiantes = QtWidgets.QMenuBar(EstudiantesPrincipal)
        self.mbr_barra_estudiantes.setGeometry(QtCore.QRect(0, 0, 765, 21))
        self.mbr_barra_estudiantes.setObjectName("mbr_barra_estudiantes")
        self.mnu_archivo = QtWidgets.QMenu(self.mbr_barra_estudiantes)
        self.mnu_archivo.setObjectName("mnu_archivo")
        self.mnu_estudiantes = QtWidgets.QMenu(self.mbr_barra_estudiantes)
        self.mnu_estudiantes.setObjectName("mnu_estudiantes")
        self.mnu_reporte = QtWidgets.QMenu(self.mbr_barra_estudiantes)
        self.mnu_reporte.setObjectName("mnu_reporte")
        self.mnu_acerca_de = QtWidgets.QMenu(self.mbr_barra_estudiantes)
        self.mnu_acerca_de.setObjectName("mnu_acerca_de")
        EstudiantesPrincipal.setMenuBar(self.mbr_barra_estudiantes)
        self.stt_principal = QtWidgets.QStatusBar(EstudiantesPrincipal)
        self.stt_principal.setObjectName("stt_principal")
        EstudiantesPrincipal.setStatusBar(self.stt_principal)
        self.mni_salir = QtWidgets.QAction(EstudiantesPrincipal)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/salir.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mni_salir.setIcon(icon1)
        self.mni_salir.setObjectName("mni_salir")
        self.mni_agregar_estudiante = QtWidgets.QAction(EstudiantesPrincipal)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/agregar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mni_agregar_estudiante.setIcon(icon2)
        self.mni_agregar_estudiante.setObjectName("mni_agregar_estudiante")
        self.mni_remover_estudiante = QtWidgets.QAction(EstudiantesPrincipal)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/basura.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mni_remover_estudiante.setIcon(icon3)
        self.mni_remover_estudiante.setObjectName("mni_remover_estudiante")
        self.mni_buscar_estudiante = QtWidgets.QAction(EstudiantesPrincipal)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/lupa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mni_buscar_estudiante.setIcon(icon4)
        self.mni_buscar_estudiante.setObjectName("mni_buscar_estudiante")
        self.mni_top_5_estudiantes = QtWidgets.QAction(EstudiantesPrincipal)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/images/corona.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mni_top_5_estudiantes.setIcon(icon5)
        self.mni_top_5_estudiantes.setObjectName("mni_top_5_estudiantes")
        self.mni_listado_estudiantes = QtWidgets.QAction(EstudiantesPrincipal)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/images/lista.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mni_listado_estudiantes.setIcon(icon6)
        self.mni_listado_estudiantes.setObjectName("mni_listado_estudiantes")
        self.mni_hecho_por = QtWidgets.QAction(EstudiantesPrincipal)
        self.mni_hecho_por.setObjectName("mni_hecho_por")
        self.mni_version = QtWidgets.QAction(EstudiantesPrincipal)
        self.mni_version.setObjectName("mni_version")
        self.mni_agregar_notas = QtWidgets.QAction(EstudiantesPrincipal)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/images/notas.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mni_agregar_notas.setIcon(icon7)
        self.mni_agregar_notas.setObjectName("mni_agregar_notas")
        self.mni_cargar = QtWidgets.QAction(EstudiantesPrincipal)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/images/cargar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mni_cargar.setIcon(icon8)
        self.mni_cargar.setObjectName("mni_cargar")
        self.mni_guardar = QtWidgets.QAction(EstudiantesPrincipal)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/images/guardar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mni_guardar.setIcon(icon9)
        self.mni_guardar.setObjectName("mni_guardar")
        self.mnu_archivo.addAction(self.mni_salir)
        self.mnu_archivo.addAction(self.mni_cargar)
        self.mnu_archivo.addAction(self.mni_guardar)
        self.mnu_estudiantes.addAction(self.mni_agregar_estudiante)
        self.mnu_estudiantes.addAction(self.mni_remover_estudiante)
        self.mnu_estudiantes.addAction(self.mni_buscar_estudiante)
        self.mnu_estudiantes.addAction(self.mni_agregar_notas)
        self.mnu_reporte.addAction(self.mni_top_5_estudiantes)
        self.mnu_reporte.addAction(self.mni_listado_estudiantes)
        self.mnu_acerca_de.addAction(self.mni_hecho_por)
        self.mnu_acerca_de.addAction(self.mni_version)
        self.mbr_barra_estudiantes.addAction(self.mnu_archivo.menuAction())
        self.mbr_barra_estudiantes.addAction(self.mnu_estudiantes.menuAction())
        self.mbr_barra_estudiantes.addAction(self.mnu_reporte.menuAction())
        self.mbr_barra_estudiantes.addAction(self.mnu_acerca_de.menuAction())

        self.retranslateUi(EstudiantesPrincipal)
        QtCore.QMetaObject.connectSlotsByName(EstudiantesPrincipal)

    def retranslateUi(self, EstudiantesPrincipal):
        _translate = QtCore.QCoreApplication.translate
        EstudiantesPrincipal.setWindowTitle(_translate("EstudiantesPrincipal", "Principal"))
        self.mnu_archivo.setTitle(_translate("EstudiantesPrincipal", "Archivo"))
        self.mnu_estudiantes.setTitle(_translate("EstudiantesPrincipal", "Estudiantes"))
        self.mnu_reporte.setTitle(_translate("EstudiantesPrincipal", "Reporte"))
        self.mnu_acerca_de.setTitle(_translate("EstudiantesPrincipal", "Acerca de"))
        self.mni_salir.setText(_translate("EstudiantesPrincipal", "Salir"))
        self.mni_salir.setShortcut(_translate("EstudiantesPrincipal", "Ctrl+Q"))
        self.mni_agregar_estudiante.setText(_translate("EstudiantesPrincipal", "Agregar estudiante"))
        self.mni_agregar_estudiante.setShortcut(_translate("EstudiantesPrincipal", "Ctrl+A"))
        self.mni_remover_estudiante.setText(_translate("EstudiantesPrincipal", "Remover estudiante"))
        self.mni_remover_estudiante.setShortcut(_translate("EstudiantesPrincipal", "Ctrl+E"))
        self.mni_buscar_estudiante.setText(_translate("EstudiantesPrincipal", "Buscar estudiante"))
        self.mni_buscar_estudiante.setShortcut(_translate("EstudiantesPrincipal", "Ctrl+B"))
        self.mni_top_5_estudiantes.setText(_translate("EstudiantesPrincipal", "Top 5 mejores estudiantes"))
        self.mni_top_5_estudiantes.setShortcut(_translate("EstudiantesPrincipal", "Ctrl+T"))
        self.mni_listado_estudiantes.setText(_translate("EstudiantesPrincipal", "Listado estudiantes"))
        self.mni_listado_estudiantes.setShortcut(_translate("EstudiantesPrincipal", "Ctrl+L"))
        self.mni_hecho_por.setText(_translate("EstudiantesPrincipal", "Hecho por..."))
        self.mni_version.setText(_translate("EstudiantesPrincipal", "Versión"))
        self.mni_agregar_notas.setText(_translate("EstudiantesPrincipal", "Agregar notas"))
        self.mni_agregar_notas.setShortcut(_translate("EstudiantesPrincipal", "Ctrl+N"))
        self.mni_cargar.setText(_translate("EstudiantesPrincipal", "Cargar"))
        self.mni_cargar.setShortcut(_translate("EstudiantesPrincipal", "Ctrl+C"))
        self.mni_guardar.setText(_translate("EstudiantesPrincipal", "Guardar"))
        self.mni_guardar.setShortcut(_translate("EstudiantesPrincipal", "Ctrl+G"))
from notas_estudiantes.images import imagenes_rc
