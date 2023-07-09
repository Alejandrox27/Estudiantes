from PIL import Image
import io
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtCore import Qt

class Estudiantes():
    def __init__(self):
        self.estudiantes = []
        self.promedios_id = {}
    
    def agregar_estudiante(self, nuevo_estudiante):
        """
        Función que agrega un estudiante a la lista de estudiantes
        
        Parameters:
        nuevo_estudiante = Estudiante
        """
        self.estudiantes.append(nuevo_estudiante)
        
    def agregar_promedios(self):
        """
        Función que agrega los promedios de los estudiantes por su id
        en el diccionario promedios_id.
        """
        
        for e in self.estudiantes:
            self.promedios_id[e.id] = e.promedio
        
    def buscar_estudiante(self, id):
        """
        Busca a un estudiante por su id
        
        Parameters:
        id: id del estudiante
        
        Returns:
        e: información del estudiante sí se encuentra
        None: si no se encuentra el estudiante
        """
        for e in self.estudiantes:
            if e.id == id:
                return e
        return None
    
    def agregar_notas_estudiantes(self, estudiante, nota):
        """
        Agrega una nota a un estudiante, además de agregar el promedio y el puesto.
        
        Parameters:
        estudiante: Estudiante que se le debe agregar la nota
        nota: nota que se le va a agregar al estudiante
        """
        nota = str(nota)
        
        if len(estudiante.notas) == 0:
            estudiante.notas = nota
            estudiante.promedio = float(nota)
            
            self.promedios_id[estudiante.id] = estudiante.promedio
            
            prom = sorted([(v,k) for k,v in self.promedios_id.items()],reverse = True)
            
            puesto = 0
            nota = None
            for e in prom:
                estudiante = self.buscar_estudiante(e[1])
                
                notas = estudiante.notas
                
                if len(notas) != 0:
            
                    notas = notas.replace(" ", "")
                    notas_list = [float(nota) for nota in notas.split(",")]
                
                    if estudiante.promedio == nota:
                        estudiante.puesto = puesto
                        continue
                        
                    puesto += 1
                    nota = estudiante.promedio
                    estudiante.puesto = puesto
                
                else:
                    estudiante.puesto = 0
            
        else:
            notas = estudiante.notas + ' , ' + nota
            estudiante.notas = notas
            
            notas = notas.replace(" ", "")
            notas_list = [float(nota) for nota in notas.split(",")]
            
            promedio = sum(notas_list) / (len(notas_list))
            
            estudiante.promedio = round(float(promedio), 2)
            
            self.promedios_id[estudiante.id] = estudiante.promedio
            
            prom = sorted([(v,k) for k,v in self.promedios_id.items()],reverse = True)
            
            puesto = 0
            nota = None
            for e in prom:
                estudiante = self.buscar_estudiante(e[1])
                
                notas = estudiante.notas
                
                if len(notas) != 0:
            
                    notas = notas.replace(" ", "")
                    notas_list = [float(nota) for nota in notas.split(",")]
                
                    if estudiante.promedio == nota:
                        estudiante.puesto = puesto
                        continue
                        
                    puesto += 1
                    nota = estudiante.promedio
                    estudiante.puesto = puesto
                
                else:
                    estudiante.puesto = 0
                
            
        return True
        
    def top_5_mejores_estudiantes_promedio(self, tabla):
        """
        Función que agrega los 5 mejores estudiantes según su promedio
        en un QTableWidget.
        
        Parameters:
        tabla: QTableWidget donde se agregarán los estudiantes
        """
        prom = {k:v for k,v in sorted(self.promedios_id.items(), key = lambda item: item[1], reverse = True)}
        keys_to_remove = []
        estudiantes = []

        for id, value in prom.items():
            estudiante = self.buscar_estudiante(id)
            if estudiante.puesto == 0:
                keys_to_remove.append(estudiante.id)

        for key in keys_to_remove:
            prom.pop(key)
        
        for i,e in prom.items():
            estudiante = self.buscar_estudiante(i)
            
            if estudiante.puesto == 5:
                estud = (i,e)
                estudiantes.append(estud)
                continue
            
            if estudiante.puesto > 5:
                break
            
            estud = (i,e)
            estudiantes.append(estud)
        
        tabla.setRowCount(0)
        
        for e in estudiantes:
            estudiante = self.buscar_estudiante(e[0])
            codigo = estudiante.id
            nombre = estudiante.nombre
            puesto = estudiante.puesto
            promedio = estudiante.promedio
            foto = self.convertir_a_normal(estudiante.foto)
            pixmap = foto.scaled(80, 80)

            foto_1 = QTableWidgetItem()
            foto_1.setIcon(QIcon(pixmap))
            tabla.setIconSize(pixmap.size()) 
            
            numeroFila = tabla.rowCount()
            tabla.insertRow(numeroFila)
            
            tabla.setItem(numeroFila, 0, QTableWidgetItem(str(codigo)))
            tabla.setItem(numeroFila, 1, QTableWidgetItem(str(nombre)))
            tabla.setItem(numeroFila, 2, QTableWidgetItem(str(puesto)))
            tabla.setItem(numeroFila, 3, QTableWidgetItem(str(promedio)))
            tabla.setItem(numeroFila, 4, foto_1)
            
            tabla.item(numeroFila, 0).setTextAlignment(Qt.AlignCenter)
            tabla.item(numeroFila, 1).setTextAlignment(Qt.AlignCenter)
            tabla.item(numeroFila, 2).setTextAlignment(Qt.AlignCenter)
            tabla.item(numeroFila, 3).setTextAlignment(Qt.AlignCenter)
        
        tabla.resizeRowsToContents()
        
        tabla.setColumnWidth(0, 70)  
        tabla.setColumnWidth(1, 150)  
        tabla.setColumnWidth(2, 70)  
        tabla.setColumnWidth(3, 100)
        
    def eliminar_estudiante(self, estudiante):
        """
        Elimina un estudiate
        
        Parameters:
        estudiante: estudiante a eliminar
        """
        
        self.estudiantes.remove(estudiante)
        if estudiante.id in self.promedios_id:
            self.promedios_id.pop(estudiante.id)
        
    def convertir_a_normal(self, imagen_binaria):
        """
        Función que convierte una imagen binaria
        y la convierte en un QPixmap.
        
        Parameters:
        imagen_binaria: imagen binaria.

        Returns:
        imagen_normal: QPixmap de la imagen.
        """
        imagen_io = io.BytesIO(imagen_binaria)

        imagen_pil = Image.open(imagen_io)
        
        if imagen_pil.mode == 'P' and 'transparency' in imagen_pil.info:
            imagen_pil = imagen_pil.convert('RGBA')

        imagen_pil.save('notas_estudiantes/images/imagen_temp.png', 'PNG')

        ruta_imagen = 'notas_estudiantes/images/imagen_temp.png' 
        imagen_normal = QPixmap(ruta_imagen)
        return imagen_normal
            
    def cargar_lista_estudiantes(self, tabla):
        """
        Función que agrega a todos los estudiantes en
        orden de puetos de mejor a peor en un QTableWidget.
        
        Parameters:
        tabla = QTableWidget donde se agregarán los estudiantes.
        """
        prom = sorted([(v,k) for k,v in self.promedios_id.items()],reverse = True)
        sin_nota = {}
        
        tabla.setRowCount(0)
        
        for e in prom:
            estudiante = self.buscar_estudiante(e[1])
            
            if estudiante.puesto == 0:
                sin_nota[e[1]] = e[0]
                continue
            codigo = estudiante.id
            nombre = estudiante.nombre
            puesto = estudiante.puesto
            promedio = estudiante.promedio
            foto = self.convertir_a_normal(estudiante.foto)
            pixmap = foto.scaled(80, 80)

            foto_1 = QTableWidgetItem()
            foto_1.setIcon(QIcon(pixmap))
            tabla.setIconSize(pixmap.size()) 
            
            numeroFila = tabla.rowCount()
            tabla.insertRow(numeroFila)
            
            tabla.setItem(numeroFila, 0, QTableWidgetItem(str(codigo)))
            tabla.setItem(numeroFila, 1, QTableWidgetItem(str(nombre)))
            tabla.setItem(numeroFila, 2, QTableWidgetItem(str(puesto)))
            tabla.setItem(numeroFila, 3, QTableWidgetItem(str(promedio)))
            tabla.setItem(numeroFila, 4, foto_1)
            
            tabla.item(numeroFila, 0).setTextAlignment(Qt.AlignCenter)
            tabla.item(numeroFila, 1).setTextAlignment(Qt.AlignCenter)
            tabla.item(numeroFila, 2).setTextAlignment(Qt.AlignCenter)
            tabla.item(numeroFila, 3).setTextAlignment(Qt.AlignCenter)
        
        if len(sin_nota) != 0:
            for key, value in sin_nota.items():
                estudiante = self.buscar_estudiante(key)
                codigo = estudiante.id
                nombre = estudiante.nombre
                puesto = estudiante.puesto
                promedio = estudiante.promedio
                foto = self.convertir_a_normal(estudiante.foto)
                pixmap = foto.scaled(80, 80)

                foto_1 = QTableWidgetItem()
                foto_1.setIcon(QIcon(pixmap))
                tabla.setIconSize(pixmap.size()) 
                
                numeroFila = tabla.rowCount()
                tabla.insertRow(numeroFila)
                
                tabla.setItem(numeroFila, 0, QTableWidgetItem(str(codigo)))
                tabla.setItem(numeroFila, 1, QTableWidgetItem(str(nombre)))
                tabla.setItem(numeroFila, 2, QTableWidgetItem(str(puesto)))
                tabla.setItem(numeroFila, 3, QTableWidgetItem(str(promedio)))
                tabla.setItem(numeroFila, 4, foto_1)
                
                tabla.item(numeroFila, 0).setTextAlignment(Qt.AlignCenter)
                tabla.item(numeroFila, 1).setTextAlignment(Qt.AlignCenter)
                tabla.item(numeroFila, 2).setTextAlignment(Qt.AlignCenter)
                tabla.item(numeroFila, 3).setTextAlignment(Qt.AlignCenter)
        
        tabla.resizeRowsToContents()
        
        tabla.setColumnWidth(0, 70)  
        tabla.setColumnWidth(1, 150)  
        tabla.setColumnWidth(2, 70)  
        tabla.setColumnWidth(3, 100)