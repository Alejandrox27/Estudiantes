import sys
from notas_estudiantes.modelos.Estudiantes import Estudiantes
from notas_estudiantes.modelos.estudiante import Estudiante
import os
import re
import markdown
import sqlite3

from PyQt5.QtGui import QPixmap, QIntValidator, QCursor
from PyQt5.QtCore import pyqtSignal, Qt, QModelIndex
from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog,QVBoxLayout, QPushButton, QMessageBox, QWidget, QLabel, QFileDialog, QTreeView, QFileSystemModel
from .GUI.Estudiantes_principal import Ui_EstudiantesPrincipal 
from .GUI.Agregar_estudiante import Ui_Agregar_estudiante
from .GUI.Eliminar_estudiante import Ui_Eliminar_estudiante
from .GUI.Buscar_estudiante import Ui_Buscar_estudiante
from .GUI.Agregar_notas import Ui_Agregar_notas
from .GUI.Listado_estudiantes import Ui_Listado_estudiantes
from .GUI.Reporte_top_5 import Ui_Top_5_mejores_estudiantes

class Estudiantes_principal(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.estudiantes = Estudiantes()
        self.gui = None
        self.inicializarGui()
    
    def inicializarGui(self):
        """
        inicializar la ventana principal y la función 'cargar_datos_gui'
        """
        self.ui = Ui_EstudiantesPrincipal()
        self.ui.setupUi(self)
        
        self.ui.mni_agregar_estudiante.triggered.connect(self.agregar_estudiantes)
        self.ui.mni_remover_estudiante.triggered.connect(self.remover_estudiantes)
        self.ui.mni_buscar_estudiante.triggered.connect(self.buscar_estudiante)
        self.ui.mni_agregar_notas.triggered.connect(self.agregar_notas_estudiante)
        self.ui.mni_top_5_estudiantes.triggered.connect(self.top_5_estudiantes)
        self.ui.mni_listado_estudiantes.triggered.connect(self.listado_estudiantes)
        self.ui.mni_cargar.triggered.connect(self.cargar_datos_gui)
        self.ui.mni_guardar.triggered.connect(self.guardar_datos_gui)
        self.ui.mni_hecho_por.triggered.connect(self.hecho_por)
        self.ui.mni_version.triggered.connect(self.version)
        self.ui.mni_salir.triggered.connect(self.close)
        
        self.show()
        self.cargar_datos_gui()
    
    def closeEvent(self, event):
        """
        función que detecta el evento de cerrar la ventana,
        sí la ventana se cierra se inicializa la función 'guardar_datos_gui',
        para posteriormente cerrarse la ventana.
        """
        if len(self.estudiantes.estudiantes) or len(self.estudiantes.promedios_id):
            if self.guardar_datos_gui():
                self.close()
        else:
            self.close()
        
    def agregar_estudiantes(self):
        """
        función que inicializa la ventana 'Agregar_estudiantes'
        y agregar la subventana al mdiArea.
        """
        self.gui = Agregar_estudiantes(self.estudiantes)
        self.ui.mdiArea.addSubWindow(self.gui)
        self.gui.show()
        
    def remover_estudiantes(self):
        """
        función que inicializa la ventana 'Remover_estudiante'
        y agregar la subventana al mdiArea.
        """
        self.gui = Remover_estudiante(self.estudiantes)
        self.ui.mdiArea.addSubWindow(self.gui)
        self.gui.show()
        
    def buscar_estudiante(self):
        """
        función que inicializa la ventana 'Buscar_estudiante'
        y agregar la subventana al mdiArea.
        """
        self.gui = Buscar_estudiante(self.estudiantes)
        self.ui.mdiArea.addSubWindow(self.gui)
        self.gui.show()
    
    def agregar_notas_estudiante(self):
        """
        función que inicializa la ventana 'Agregar_notas_estudiantes'
        y agregar la subventana al mdiArea.
        """
        self.gui = Agregar_notas_estudiantes(self.estudiantes)
        self.ui.mdiArea.addSubWindow(self.gui)
        self.gui.show()
    
    def top_5_estudiantes(self):
        """
        función que inicializa la ventana 'Top_5_estudiantes'
        y agregar la subventana al mdiArea.
        """
        self.gui = Top_5_estudiantes(self.estudiantes)
        self.ui.mdiArea.addSubWindow(self.gui)
        self.gui.show()
    
    def listado_estudiantes(self):
        """
        función que inicializa la ventana 'Listado_estudiantes'
        y agregar la subventana al mdiArea.
        """
        self.gui = Listado_estudiantes(self.estudiantes)
        self.ui.mdiArea.addSubWindow(self.gui)
        self.gui.show()
    
    def cargar_datos_gui(self):
        """
        función que permite cargar los datos de los estudiantes
        de una base de datos seleccionada.
        """
        confirmacion = QMessageBox()
        texto = '¿Quiere cargar los datos de los estudiantes?'
        confirmacion.setText(texto)
        confirmacion.setIcon(QMessageBox.Question)
        confirmacion.setWindowTitle('Cargar...')
        confirmacion.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        boton_yes = confirmacion.button(QMessageBox.Yes)
        
        confirmacion.exec_()
        
        self.ruta_seleccionada = None
        
        if confirmacion.clickedButton() == boton_yes:
            self.gui = ExploradorArchivosCargar()
            self.gui.show()
            
            
            self.gui.treeview.doubleClicked.connect(self.archivo_seleccionado)
        
    def archivo_seleccionado(self, index: QModelIndex):
        """
        función que toma el index del archivo seleccionado,
        lo convierte en una ruta y se conecta a una base de datos,
        en donde seguido se cargan los datos en una lista de estudiantes
        y en un diccionario de promedios.
        """
        self.estudiantes.estudiantes.clear()
        self.estudiantes.promedios_id.clear()
        
        self.ruta_seleccionada = self.gui.model.filePath(index)
        
        conexion = sqlite3.connect(self.ruta_seleccionada)
        cursor = conexion.cursor()
        sql = 'SELECT * FROM estudiantes'
        estudiantes = cursor.execute(sql)
        
        for e in estudiantes:
            estudiante = {'id': 0, 'nombre': '', 'notas': '', 'puesto': 0, 'promedio': 5.0, 'foto': None}
            for i, c in enumerate(e):
                if i == 0:
                    estudiante['id'] = c
                if i == 1:
                    estudiante['nombre'] = c
                if i == 2:
                    estudiante['notas'] = c
                if i == 3:
                    estudiante['puesto'] = c
                if i == 4:
                    estudiante['promedio'] = c
                if i == 5:
                    estudiante['foto'] = c
                    
            estudiante = Estudiante(str(estudiante['id']), estudiante['nombre'], estudiante['notas'], estudiante['puesto'], 
                                    estudiante['promedio'], estudiante['foto'])
            
            self.estudiantes.agregar_estudiante(estudiante)
            
        self.estudiantes.agregar_promedios()
            
        self.gui.close()

    def guardar_datos_gui(self):
        """
        función que permite guardar los datos de los estudiantes
        de una base de datos seleccionada o una nueva.
        """
        confirmacion = QMessageBox()
        texto = '¿Quiere guardar los datos de los estudiantes?'
        confirmacion.setText(texto)
        confirmacion.setIcon(QMessageBox.Question)
        confirmacion.setWindowTitle('Guardar')
        confirmacion.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        boton_yes = confirmacion.button(QMessageBox.Yes)
        
        confirmacion.exec_()
        
        if confirmacion.clickedButton() == boton_yes:
            self.gui = ExploradorArchivosGuardar(self.estudiantes)
            self.gui.show()
    
    def hecho_por(self):
        mensaje = QMessageBox(self)
        mensaje.setIcon(QMessageBox.Information)
        mensaje.setWindowTitle('Hecho por...')
        mensaje.setText('Alejandro Mejía')
        mensaje.exec_()
    
    def version(self):
        mensaje = QMessageBox(self)
        mensaje.setIcon(QMessageBox.Information)
        mensaje.setWindowTitle('Version')
        mensaje.setText('V. 1.0')
        mensaje.resize(50,50)
        mensaje.exec_()
    
class ExploradorArchivosGuardar(QWidget):
    def __init__(self, estudiantes):
        super().__init__()
        self.estudiantes = estudiantes
        self.inicializarGui()
        
    def inicializarGui(self):
        """
        Inicializa la ventana de guardar archivo en base de datos.
        """
        self.setWindowTitle('Guardar en...')
        self.setFixedSize(400, 360)
        
        ruta_absoluta = str(os.path.abspath('notas_estudiantes/database'))
        ruta_absoluta = ruta_absoluta.replace("\\", "/")
        
        layout = QVBoxLayout(self)
        
        self.treeview = QTreeView(self)
        self.model = QFileSystemModel()
        self.model.setRootPath(ruta_absoluta)
        self.treeview.setModel(self.model)
        self.treeview.setRootIndex(self.model.index(self.model.rootPath()))
        
        layout.addWidget(self.treeview)
        
        self.treeview.doubleClicked.connect(self.archivo_seleccionado)
        
        boton = QPushButton('Nuevo', self)
        boton.clicked.connect(self.nuevo)
        layout.addWidget(boton)
        
    def archivo_seleccionado(self, index: QModelIndex):
        ruta_seleccionada = self.model.filePath(index)
        
        self.guardar_datos_en_base(ruta_seleccionada)
        
    def nuevo(self):
        """
        Crea una nueva base de datos con el nombre que le coloque el usuario,
        crea una tabla de 'estudiantes' sí la base no está creada aún
        y solo agrega los datos sí ya está creada.
        """
        patron = r'[a-zA-Z]+'
        regex = re.compile(patron)
        nombre, ok = QInputDialog.getText(self, 'Guardar datos...','Escriba el nombre del archivo donde se guardará la información')
        
        if ok:
            nombre = nombre.strip()
            if len(nombre) == 0:
                mensaje = QMessageBox()
                mensaje.setText('Inserte un nombre para su base de datos')
                mensaje.setIcon(QMessageBox.Warning)
                mensaje.setWindowTitle('Guardar')
                mensaje.exec_()
                self.guadar_datos_gui(Estudiantes)
                return
            
            if regex.match(nombre):
                
                nombre_archivo = f'notas_estudiantes/database/{nombre}.db'
                
            else:
                mensaje = QMessageBox()
                mensaje.setText('Inserte un nombre valido para su base de datos')
                mensaje.setIcon(QMessageBox.Warning)
                mensaje.setWindowTitle('Guardar')
                mensaje.exec_()
                self.guardar_datos_gui(Estudiantes)
                return
                
            
            if not os.path.exists(nombre_archivo):
                try:
                    conexion = sqlite3.connect(nombre_archivo)
                    cursor = conexion.cursor()
                    sql_estudiantes = '''CREATE TABLE estudiantes (
                        ID INTEGER PRIMARY KEY NOT NULL,
                        nombre TEXT NOT NULL,
                        notas TEXT,
                        puesto INTEGER,
                        promedio REAL,
                        foto BLOB NOT NULL
                        )'''
                    cursor.execute(sql_estudiantes)
                    
                    for e in self.estudiantes.estudiantes:
                        id = int(e.id)
                        nombre = e.nombre
                        notas = e.notas
                        puesto = int(e.puesto)
                        promedio = float(e.promedio)
                        foto = e.foto
                        sql_guardar = "INSERT INTO estudiantes VALUES (?, ?, ?, ?, ?, ?)"
                        cursor.execute(sql_guardar, (id, nombre, notas, puesto, promedio, foto))
                    
                    cursor.close()
                    conexion.commit()
                    return True
                
                except sqlite3.Error:
                    mensaje = QMessageBox()
                    mensaje.setIcon(QMessageBox.Warning)
                    mensaje.setWindowTitle('Error')
                    mensaje.setText('hubo un error en la creación de base de datos')
                    mensaje.exec_()
                
                finally:
                    conexion.close()
                    self.close()
            else:
                self.guardar_datos_en_base(nombre_archivo)
        
    def guardar_datos_en_base(self, nombre_archivo):
        """
        Guarda los datos de los estudiantes en una
        base de datos ya creada.
        
        Parameters:
        nombre_archivo = Nombre de la base de datos
        """
        try: 
                    
            conexion = sqlite3.connect(nombre_archivo)
            cursor = conexion.cursor()
            
            sql_borrar = "DELETE FROM estudiantes"
            cursor.execute(sql_borrar).fetchall()
        
            for e in self.estudiantes.estudiantes:
                id = int(e.id)
                nombre = e.nombre
                notas = e.notas
                puesto = int(e.puesto)
                promedio = float(e.promedio)
                foto = e.foto
                sql_guardar = "INSERT INTO estudiantes VALUES (?, ?, ?, ?, ?, ?)"
                cursor.execute(sql_guardar, (id, nombre, notas, puesto, promedio, foto))
            
            cursor.close()
            conexion.commit()
        
        except sqlite3.Error:
            mensaje = QMessageBox()
            mensaje.setIcon(QMessageBox.Warning)
            mensaje.setWindowTitle('Error')
            mensaje.setText('hubo un error en la creación de base de datos')
            mensaje.exec_()
        
        finally:
            conexion.close()
            self.close()
            
class ExploradorArchivosCargar(QWidget):
    def __init__(self):
        super().__init__()
        self.ruta_seleccionada = None
        self.inicializarGui()
        
    def inicializarGui(self):
        """
        Inicializa la ventana de cargar con base de datos
        """
        self.setWindowTitle('Cargar con...')
        self.setFixedSize(400, 360)
        
        ruta_absoluta = str(os.path.abspath('notas_estudiantes/database'))
        ruta_absoluta = ruta_absoluta.replace("\\", "/")
        
        layout = QVBoxLayout(self)
        
        self.treeview = QTreeView(self)
        self.model = QFileSystemModel()
        self.model.setRootPath(ruta_absoluta)
        self.treeview.setModel(self.model)
        self.treeview.setRootIndex(self.model.index(self.model.rootPath()))
        
        layout.addWidget(self.treeview)
            
class ClickableLabel(QLabel):
    """
    Clase para convertir un label a clickeable
    """
    clicked = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMouseTracking(True)

    def mousePressEvent(self, event):
        self.clicked.emit()
        
    def enterEvent(self, event):
        self.setCursor(QCursor(Qt.PointingHandCursor))

    def leaveEvent(self, event):
        self.unsetCursor()

class Agregar_estudiantes(QWidget):
    def __init__(self, estudiantes):
        super().__init__()
        
        patron = r'^[A-Za-z\s]+$'
        self.regex = re.compile(patron)
        
        self.mensaje = QMessageBox(self)
        self.mensaje.setWindowTitle('mensaje')
        self.mensaje.setIcon(QMessageBox.Warning)
        
        self.estudiantes = estudiantes
        
        self.inicializarGui()
        
    def inicializarGui(self):
        self.ui = Ui_Agregar_estudiante()
        self.ui.setupUi(self)
        
        self.ui.txt_codigo_estudiante.setValidator(QIntValidator(1,1000000,self))
        self.ui.btn_agregar_estudiante.clicked.connect(self.agregar_estudiante)
        
        label = ClickableLabel(self.ui.lbl_foto_agregar)
        label.setFixedSize(223,177)
        label.clicked.connect(self.abrir_foto)
        
        
    def abrir_foto(self):
        """
        Función que permite al usuario elegir una imagen
        de su computadora y agregarla al 'lbl_foto_agregar'
        para luego ser usada para agregarla en base de datos.
        """
        self.archivo, ok = QFileDialog.getOpenFileName(self, 'Seleccionar archivo de imagen...', 'C:\\','Archivos de imágenes (*.jpg *.png)')
        extension = self.archivo.find('.')
        
        if self.archivo[extension:] == '.jpg':
            self.ui.lbl_mensaje.setText('Recomendamos imagenes de tipo .png')
            self.ui.lbl_mensaje_2.setText('para que la consulta sea más rapida')
        
        else:
            self.ui.lbl_mensaje.setText('')
            self.ui.lbl_mensaje_2.setText('')
        if ok:
            self.ui.lbl_foto_agregar.setPixmap(QPixmap(self.archivo))
            
    def agregar_estudiante(self):
        """
        Función que permite agregar un estudiante a 
        una base de datos, insertando su codigo, nombre, notas, puesto, promedio y foto.
        """
        default_image_path = ":/images/mas.png"
        default_pixmap = QPixmap(default_image_path)
        current_pixmap = self.ui.lbl_foto_agregar.pixmap()
        
        codigo = self.ui.txt_codigo_estudiante.text()
        nombre = self.ui.txt_nombre_estudiante.text().strip()
        
        espacios_seguidos_nombre = self.espacios_seguidos(nombre)
        
        
        if len(codigo) == 0:
            self.mensaje.setText('El campo codigo es obligatorio')
            self.mensaje.exec_()
            return
                  
        if len(nombre) == 0:
            self.mensaje.setText('El campo nombre es obligatorio')
            self.mensaje.exec_()
            return
                
        if self.regex.match(nombre) is None:
            self.mensaje.setText('El nombre está mal escrito')
            self.mensaje.exec_()
            return
        
        if espacios_seguidos_nombre != False:
            self.mensaje.setText('No puede haber más dos espacios seguidos en el nombre')
            self.mensaje.exec_()
            return
        
        if current_pixmap.isNull() or current_pixmap.toImage() == default_pixmap.toImage():
            self.mensaje.setText('Agrega una imagen')
            self.mensaje.exec_()
            return
        estudiante = self.estudiantes.buscar_estudiante(codigo)
        
        if estudiante is not None:
            self.mensaje.setText('Ya existe un estudiante con ese codigo')
            self.mensaje.setIcon(QMessageBox.Warning)
            self.mensaje.exec_()
            return
                
        foto_binario = self.convertir_a_binario(self.archivo)
        
        if foto_binario != None:
            new_student = Estudiante(codigo, nombre, '' , 0 , 5.0, foto_binario)
            self.estudiantes.agregar_estudiante(new_student)
            
            self.mensaje.setIcon(QMessageBox.Information)
            self.mensaje.setText('El estudiante se creó de manera satisfactoria')
            self.mensaje.exec_()
         
    def convertir_a_binario(self,foto):
        """
        Función que convierte a binario una imagen.
        
        Parameters:
        foto = ruta de la imagen suministrada por el usuario
        
        Returns:
        blob = Imagen en binario.
        None = Sí hubo un error al convertir a binario.
        """
        try:
            with open(foto, 'rb') as f:
                blob = f.read()
                
            return blob
        except:
            mensaje = QMessageBox(self)
            mensaje.setIcon(QMessageBox.Warning)
            mensaje.setWindowTitle('Error')
            mensaje.setText('hubo un error, intentalo de nuevo')
            mensaje.exec_()
            return None
    
    def espacios_seguidos(self, string):
        """
        Esta función toma un string y pasa por cada uno de sus elementos,
        sí hay dos o más espacios seguidos en el string devuelve True,
        si no hay más de dos espacios seguidos en el string devuelve False.
        
        Parameters:
        string: texto que se quiere buscar espacios seguidos
        
        Returns:
        True: si encuentra dos o más espacios seguidos en el string
        False: si no encuentra dos o más espacios seguidos
        """
        
        lista_texto = []
        for l in string:
            lista_texto.append(l)
        index1 = ''
        index2 = ''
        
        for e in lista_texto:
            index1 = e
            if index1 == index2 and index1 == ' ':
                return True
            index2 = e
        return False
        
class Remover_estudiante(QWidget):
    def __init__(self, estudiantes):
        super().__init__()
        
        self.mensaje = QMessageBox(self)
        self.mensaje.setWindowTitle('mensaje')
        
        self.estudiantes = estudiantes
        self.inicializarGui()
        
    def inicializarGui(self):
        self.ui = Ui_Eliminar_estudiante()
        self.ui.setupUi(self)
        
        self.ui.txt_codigo.setValidator(QIntValidator(1,1000000,self))
        self.ui.btn_eliminar_estudiante.clicked.connect(self.remover_estudiante)
        
    def remover_estudiante(self):
        """
        Función que remueve un estudiante de la lista de estudiantes.
        """
        codigo = self.ui.txt_codigo.text()
        
        if len(codigo) == 0:
            self.mensaje.setText('el campo codigo es obligatorio')
            self.mensaje.setIcon(QMessageBox.Warning)
            self.mensaje.exec_()
            return
        
        estudiante = self.estudiantes.buscar_estudiante(codigo)
        
        if estudiante is None:
            self.mensaje.setText('No existe ningun estudiante con ese codigo')
            self.mensaje.setIcon(QMessageBox.Warning)
            self.mensaje.exec_()
            return
        
        foto_binaria = estudiante.foto
        foto_estudiante = self.estudiantes.convertir_a_normal(foto_binaria)
        
        confirmacion = QMessageBox(self)
        confirmacion.setText(markdown.markdown(f'¿Quiere eliminar al estudiante \n\n**{estudiante.nombre}**\n\nel cual tiene de codigo: **{codigo}**?'))
        confirmacion.setIconPixmap(foto_estudiante.scaled(100, 100))
        confirmacion.setWindowTitle('Remover')
        confirmacion.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        boton_yes = confirmacion.button(QMessageBox.Yes)
        
        confirmacion.exec_()
        
        if confirmacion.clickedButton() == boton_yes:
            self.estudiantes.eliminar_estudiante(estudiante)
        
class Buscar_estudiante(QWidget):
    def __init__(self, estudiantes):
        super().__init__()
        
        self.mensaje = QMessageBox(self)
        self.mensaje.setIcon(QMessageBox.Warning)
        self.mensaje.setWindowTitle('mensaje')
        
        self.estudiantes = estudiantes
        self.inicializarGui()
    
    def inicializarGui(self):
        self.gui = Ui_Buscar_estudiante()
        self.gui.setupUi(self)
        
        self.gui.txt_codigo.setValidator(QIntValidator(1, 1000000, self))
        self.gui.btn_buscar_estudiante.clicked.connect(self.buscar_estudiante)
        
    def buscar_estudiante(self):
        """
        Función que busca a un estudiante por su codigo.
        """
        codigo = self.gui.txt_codigo.text()
        
        if len(codigo) == 0:
            self.mensaje.setText('El campo codigo es obligatorio')
            self.mensaje.exec_()
            return

        estudiante = self.estudiantes.buscar_estudiante(codigo)
        
        if estudiante is None:
            self.mensaje.setText('No existe ningun estudiante con ese codigo')
            self.mensaje.exec_()
            return
        
        nombre = estudiante.nombre
        notas = estudiante.notas
        puesto = estudiante.puesto
        promedio = estudiante.promedio
        foto = self.estudiantes.convertir_a_normal(estudiante.foto)
        
        self.gui.txt_nombre.setText(nombre)
        self.gui.txt_notas.setText(notas)
        self.gui.spb_puesto.setValue(puesto)
        self.gui.spb_promedio.setValue(promedio)
        self.gui.lbl_foto.setPixmap(foto)

class Agregar_notas_estudiantes(QWidget):
    def __init__(self, estudiantes):
        super().__init__()
        
        self.mensaje = QMessageBox(self)
        self.mensaje.setIcon(QMessageBox.Warning)
        self.mensaje.setWindowTitle('mensaje')
        
        self.estudiantes = estudiantes
        self.inicializarGui()
        
    def inicializarGui(self):
        self.ui = Ui_Agregar_notas()
        self.ui.setupUi(self)
        
        self.ui.txt_codigo.setValidator(QIntValidator(1, 1000000, self))
        self.ui.btn_agregar_nota.clicked.connect(self.agregar_nota)
        
    def agregar_nota(self):
        """
        Función que agrega una nota a un estudiante
        """
        codigo = self.ui.txt_codigo.text()
        
        if len(codigo) == 0:
            self.mensaje.setText('el campo codigo es obligatorio')
            self.mensaje.exec_()
            return
        
        estudiante = self.estudiantes.buscar_estudiante(codigo)
        
        if estudiante is None:
            self.mensaje.setText('no existe un estudiante con ese codigo')
            self.mensaje.exec_()
            return
        
        nota = self.ui.spb_nota.value()
        
        if self.estudiantes.agregar_notas_estudiantes(estudiante, nota):
            self.mensaje.setIcon(QMessageBox.Information)
            self.mensaje.setText('Se ha agregado la nota correctamente')
            self.mensaje.exec_()

class Top_5_estudiantes(QWidget):
    def __init__(self, estudiantes):
        super().__init__()
        
        self.estudiantes = estudiantes
        self.inicializarGui()
        
    def inicializarGui(self):
        self.ui = Ui_Top_5_mejores_estudiantes()
        self.ui.setupUi(self)
        
        self.estudiantes.top_5_mejores_estudiantes_promedio(self.ui.tbl_tabla_estudiantes)
        
class Listado_estudiantes(QWidget):
    def __init__(self, estudiantes):
        super().__init__()
        self.estudiantes = estudiantes
        
        self.inicializarGui()
    
    def inicializarGui(self):
        self.ui = Ui_Listado_estudiantes()
        self.ui.setupUi(self)
        
        tabla = self.ui.tbl_tabla_estudiantes
        self.estudiantes.cargar_lista_estudiantes(tabla)

def main():
    app = QApplication(sys.argv)
    ventana = Estudiantes_principal()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()