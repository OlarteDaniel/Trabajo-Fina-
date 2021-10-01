import os
from PyQt5.QtWidgets import *
from PyQt5.QtPrintSupport import * 
import sys

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.cadena = 0
        self.path=None
        self.ancho = 800
        self.alto = 500
        self.Coor_y = 100
        self.Coor_x= 100 

        self.texto = QPlainTextEdit() #Lo coloque acá momentaneamente si encuento una solucion
        
        self.acciones()
        self.CuadroTexto()
        self.BarraMenu()
        self.InitUI()


    def acciones(self):
        
#---------------------------SECCION ARCHIVO ----------------------------------

        self.accion_archivo_abrir = QAction("&Abrir...", self)
        self.accion_archivo_abrir.setStatusTip("Abrir un archivo nuevo")
        self.accion_archivo_abrir.triggered.connect(self.MenuArchivoAbrir) #Lanzador

        self.accion_archivo_guardar = QAction("&Guardar", self)
        self.accion_archivo_guardar.setStatusTip("Guardar archivo")
        self.accion_archivo_guardar.triggered.connect(self.MenuArchivoGuardar) #Lanzador
        
        self.accion_archivo_guardar_como = QAction("&Guardar como...", self)
        self.accion_archivo_guardar_como.setStatusTip("Guardar archivo como...")
        self.accion_archivo_guardar_como.triggered.connect(self.MenuArchivoGuardarComo) #Lanzador

        self.accion_archivo_imprimir = QAction("&Imprimir", self)   
        self.accion_archivo_imprimir.setStatusTip("Imprimir archivo")
        self.accion_archivo_imprimir.triggered.connect(self.MenuArchivoImprimir) 

        self.accion_archivo_salir = QAction("Salir", self)
        self.accion_archivo_salir.setShortcut("Ctrl+Q")
        self.accion_archivo_salir.setStatusTip("Salir de la aplicacion")
        self.accion_archivo_salir.triggered.connect(qApp.quit)
  
  #---------------------------SECCION EDICION ----------------------------------
        self.accion_edicion_deshacer = QAction("&Deshacer", self)    
        self.accion_edicion_deshacer.setStatusTip("Deshacer el último cambio")
        self.accion_edicion_deshacer.triggered.connect(self.texto.undo)
        
        self.accion_edicion_rehacer = QAction("&Rehacer", self)     
        self.accion_edicion_rehacer.setStatusTip("Rehacer el último cambio")
        self.accion_edicion_rehacer.triggered.connect(self.texto.redo)

        self.accion_edicion_cortar = QAction("&Cortar", self)    
        self.accion_edicion_cortar.setStatusTip("Cortar texto seleccionado")
        self.accion_edicion_cortar.triggered.connect(self.texto.cut)
        
        self.accion_edicion_copiar = QAction("&Copiar", self)     
        self.accion_edicion_copiar.setStatusTip("Copiar texto seleccionado")
        self.accion_edicion_copiar.triggered.connect(self.texto.copy)
        
        self.accion_edicion_pegar = QAction("Pegar", self)     
        self.accion_edicion_pegar.setStatusTip("Pegar texto seleccionado")
        self.accion_edicion_pegar.triggered.connect(self.texto.paste)
        
        self.accion_edicion_seleccionar_todo = QAction("&Seleccionar todo", self)    
        self.accion_edicion_seleccionar_todo.setStatusTip("Seleccionar todo ")
        self.accion_edicion_seleccionar_todo.triggered.connect(self.texto.selectAll)   

    #---------------------------SECCION FORMATO ----------------------------------    

        self.accion_formato_ajustar = QAction("Ajustar texto de la ventana", self) 
        self.accion_formato_ajustar.setStatusTip("Marque para ajustar el texto a la ventana") 
        self.accion_formato_ajustar.setCheckable(True) 
        self.accion_formato_ajustar.setChecked(True) 
        self.accion_formato_ajustar.triggered.connect(self.MenuVerAccionAjustar)  


    def BarraMenu(self):
        self.texto.textChanged.connect(self.contador)
        self.barra_de_estado = QStatusBar()  
        self.setStatusBar(self.barra_de_estado)
        self.statusBar().showMessage("Bienvenido al Bloc de nota")
        self.menu = self.menuBar() #Menu
        
        #Elementos del Menu
        self.menu_archivo=self.menu.addMenu("&Archivo")
        self.menu_edicion=self.menu.addMenu("&Edicion")
        self.menu_formato=self.menu.addMenu("&Formato")

        
        #Acciones que realiza el menu seccion archivo
        self.menu_archivo.addAction(self.accion_archivo_abrir)
        self.menu_archivo.addAction(self.accion_archivo_guardar)
        self.menu_archivo.addAction(self.accion_archivo_guardar_como)   
        self.menu_archivo.addAction(self.accion_archivo_imprimir) 
        self.menu_archivo.addAction(self.accion_archivo_salir)
         
        #Acciones que realiza el menu seccion edicion
        self.menu_edicion.addAction(self.accion_edicion_deshacer) 
        self.menu_edicion.addAction(self.accion_edicion_rehacer)
        self.menu_edicion.addAction(self.accion_edicion_cortar)
        self.menu_edicion.addAction(self.accion_edicion_copiar)
        self.menu_edicion.addAction(self.accion_edicion_pegar)  

        #Acciones que realiza el menu seccion Ver
        self.menu_formato.addAction(self.accion_formato_ajustar)

        #Actualizar Titulo 
        self.actualizar_titulo() 

    def contador(self):
        self.cantidad_letra=self.texto.toPlainText()
        self.caracteres=str(self.cantidad_letra)
        self.cadena=len(self.caracteres)
        self.statusBar().showMessage("Caracteres con espacio: "+str(self.cadena), 0)
    
    #Creacion del contenedor para almacenar el cuadro de texto
    def CuadroTexto(self):
        self.contenedorVertical = QVBoxLayout()
        self.contenedorVertical.addWidget(self.texto)
        self.WidgetPrincipal = QWidget()
        self.WidgetPrincipal.setLayout(self.contenedorVertical)
        self.setCentralWidget(self.WidgetPrincipal)


    def dialog_critical(self, s): 
        
        dlg = QMessageBox(self) 
  
        dlg.setText(s) 
        
        dlg.setIcon(QMessageBox.Critical) 
        
        dlg.show() 

    
    def MenuArchivoAbrir(self):         
        path, _ = QFileDialog.getOpenFileName(self, "Open file", "", "Documento de Texto(*.txt)") 
  
        if path: 
            try: 
                with open(path, 'rU') as f: 
                    text = f.read() 

            except Exception as e:     
                self.dialog_critical(str(e)) 
            
            else:  
                self.path = path 
        
                self.texto.setPlainText(text) 
                
                self.actualizar_titulo()
        

    def MenuArchivoGuardar(self): 
        if self.path is None: 

            return self.MenuArchivoGuardarComo()
         
        self._guardar_en_path(self.path) 


    def actualizar_titulo(self): 
        self.setWindowTitle("%s - PyQt5 Bloc de Notas" %(os.path.basename(self.path)  if self.path else "Untitled"))  
    

    def MenuArchivoGuardarComo(self): 
        path, _ = QFileDialog.getSaveFileName(self, "Guardar archivo...", "","Documento de Texto(*.txt)") 
        
        if not path: 
        
            return
        
        self._guardar_en_path(path) 


    def _guardar_en_path(self, path): 
        
        text = self.texto.toPlainText() 
        
        try: 
            
            with open(path, 'w') as f: 
                
                f.write(text) 
        
        except Exception as e: 
            
            self.dialog_critical(str(e)) 
       
        else: 
            
            self.path = path 
            
            self.actualizar_titulo() 


    def MenuArchivoImprimir(self):         
        dlg = QPrintDialog() 
        
        if dlg.exec_(): 
            
            self.texto.print_(dlg.printer()) 
    

    def MenuVerAccionAjustar(self): 
        self.texto.setLineWrapMode(1 if self.texto.lineWrapMode() == 0 else 0 )


    def InitUI(self):
        self.setGeometry(self.Coor_x, self.Coor_y, self.ancho, self.alto)
        self.setWindowTitle("Bloc de nota")

if __name__ == '__main__': 
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    codigoDeFinalizacion = app.exec_()
    sys.exit(codigoDeFinalizacion)