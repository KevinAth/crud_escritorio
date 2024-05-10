import sys
from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtCore import QTimer
from script import dbagredatos,dbeditdatos,Datos,delete
#####--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------->>>>>
class Ui_CRUD:                   
    def __init__(self, CRUD):
        CRUD.setObjectName("CRUD")
        CRUD.resize(900, 590)
        CRUD.setMinimumSize(QtCore.QSize(900, 590))
        CRUD.setMaximumSize(QtCore.QSize(900, 590))
        
        self.centralwidget = QtWidgets.QWidget(parent=CRUD)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMaximumSize)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setStyleSheet("background-color: rgb(125, 125, 125);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widgetiz = QtWidgets.QWidget(parent=self.frame)
        self.widgetiz.setStyleSheet("#widgetiz{border-right: 5px solid #BD0B00;} ")
        self.widgetiz.setObjectName("widgetiz")
        self.pushButton = QtWidgets.QPushButton(parent=self.widgetiz)
        self.pushButton.setGeometry(QtCore.QRect(580, 10, 75, 21))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton.clicked.connect(lambda: self.animate_button(self.pushButton))
        self.pushButton.clicked.connect(lambda: self.tableDatos())
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.widgetiz)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 561, 22))
        self.lineEdit.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.IBeamCursor))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);border-radius: 7px;")
        self.lineEdit.setCursorMoveStyle(QtCore.Qt.CursorMoveStyle.LogicalMoveStyle)
        self.lineEdit.textChanged.connect(self.Buscartabla)
        self.lineEdit.setObjectName("lineEdit")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.widgetiz)
        header = ["id","Nombre","Categoria","Descripcion","Precio"]
        self.tableWidget.setGeometry(QtCore.QRect(10, 40, 651, 541))
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);border-radius: 10px;")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(header)
        self.tableDatos()
        self.tableWidget.setColumnWidth(0, 50)
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.itemSelectionChanged.connect(self.Selection)

        self.horizontalLayout_2.addWidget(self.widgetiz)
        self.widget_2 = QtWidgets.QWidget(parent=self.frame)
        self.widget_2.setStyleSheet("background-color: rgb(61, 61, 61);")
        self.widget_2.setObjectName("widget_2")
        self.botonAgregar = QtWidgets.QPushButton(parent=self.widget_2)
        self.botonAgregar.setGeometry(QtCore.QRect(10, 80, 201, 41))
        font = QtGui.QFont()
        font.setFamily("PMingLiU-ExtB")
        font.setPointSize(15)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.botonAgregar.setFont(font)
        self.botonAgregar.setStyleSheet("background-color: rgb(255, 255, 255);border-radius: 20px;")
        self.botonAgregar.clicked.connect(lambda:self.animate_button(self.botonAgregar))
        self.botonAgregar.clicked.connect(lambda: self.añadirPro())
        self.botonAgregar.setObjectName("botonAgregar")
        self.BotonEditar = QtWidgets.QPushButton(parent=self.widget_2)
        self.BotonEditar.setGeometry(QtCore.QRect(10, 130, 201, 41))
        font = QtGui.QFont()
        font.setFamily("PMingLiU-ExtB")
        font.setPointSize(15)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.BotonEditar.setFont(font)
        self.BotonEditar.setStyleSheet("background-color: rgb(255, 255, 255);border-radius: 20px;")
        self.BotonEditar.clicked.connect(lambda:self.animate_button(self.BotonEditar))
        self.BotonEditar.clicked.connect(lambda: self.ModiPro())
        self.BotonEditar.setObjectName("BotonEditar")
        self.BotonEliminar = QtWidgets.QPushButton(parent=self.widget_2)
        self.BotonEliminar.setGeometry(QtCore.QRect(10, 180, 201, 41))
        font = QtGui.QFont()
        font.setFamily("PMingLiU-ExtB")
        font.setPointSize(15)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.BotonEliminar.setFont(font)
        self.BotonEliminar.setStyleSheet("background-color: rgb(255, 255, 255);border-radius: 20px;")
        self.BotonEliminar.clicked.connect(lambda: self.animate_button(self.BotonEliminar))
        self.BotonEliminar.clicked.connect(self.Del)
        self.BotonEliminar.setObjectName("BotonEliminar")
        self.label = QtWidgets.QLabel(parent=self.widget_2)
        self.label.setGeometry(QtCore.QRect(10, 20, 201, 41))
        font = QtGui.QFont()
        font.setFamily("MingLiU_HKSCS-ExtB")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.widget_2)
        self.horizontalLayout_2.setStretch(0, 9)
        self.horizontalLayout_2.setStretch(1, 3)
        self.horizontalLayout.addWidget(self.frame)
        CRUD.setCentralWidget(self.centralwidget)

        self.retranslateUi(CRUD)
        QtCore.QMetaObject.connectSlotsByName(CRUD)

    def retranslateUi(self, CRUD):
        _translate = QtCore.QCoreApplication.translate
        CRUD.setWindowTitle(_translate("CRUD", "CRUD: Gestor de productos"))
        self.pushButton.setText(_translate("CRUD", "Actualizar"))
        self.lineEdit.setPlaceholderText(_translate("CRUD", " Buscar..."))
        self.botonAgregar.setText(_translate("CRUD", "Agregar Producto"))
        self.BotonEditar.setText(_translate("CRUD", "Editar Producto"))
        self.BotonEliminar.setText(_translate("CRUD", "Eliminar Producto"))
        self.label.setText(_translate("CRUD", "Gestion de productos"))
        
    def animate_button(self, boton):
        boton.setStyleSheet("background-color: #AAAAAA; color: black; border-radius: 20px; border: 3px solid black;")
        QTimer.singleShot(175, lambda: boton.setStyleSheet("background-color: White; color: black; border-radius: 20px;"))

    def tableDatos(self):
        datos = Datos()
        self.tableWidget.setRowCount(len(datos))
        for i , y in enumerate(datos):
            for col , val in enumerate(y):
                item = QtWidgets.QTableWidgetItem(str(val))
                self.tableWidget.setItem(i,col,item)
    def Selection(self):
        selec = None
        selec = self.tableWidget.selectedItems()
        if selec != None and len(selec) != 0:
            idd = selec[0].text()
            return idd

    def añadirPro(self):
        self.aña = uic.loadUi("ui/añadir.ui")
        self.aña.show()
        self.aña.confirmarA.clicked.connect(self.ConAgre)
        
    def ConAgre(self):
        print("funciona")
        nombre = self.aña.nombreA.text()
        cat = self.aña.categoriaA.text()
        des = self.aña.descripcionA.text()
        pre = self.aña.precioA.text()
        dbagredatos(nombre,cat,des,pre)
        self.tableDatos()
        self.aña.close()
        
    def ModiPro(self):
        self.mod = uic.loadUi("ui/editar.ui")
        self.mod.show()
        self.mod.modificarE.clicked.connect(self.modedit)
        self.mod.cancelarE.clicked.connect(self.cancelarmod)
        
    def modedit(self):
        nombre = self.mod.nombreE.text()
        cat = self.mod.categoriaE.text()
        des = self.mod.descripcionE.text()
        pre = self.mod.precioE.text()
        idd = self.Selection()
        print(idd)
        dbeditdatos(idd,nombre,cat,des,pre)
        self.tableDatos()
        self.mod.close()  
    
    def cancelarmod(self):
        self.mod.close()
    
    def Del(self):
        idd = self.Selection()
        delete(idd)
        self.tableDatos()
    def Buscartabla(self):
        filtext = self.lineEdit.text().lower()
        for fila in range(self.tableWidget.rowCount()):
            textofila = " ".join([self.tableWidget.item(fila, col).text().lower() for col in range(self.tableWidget.columnCount())])
            if filtext in textofila:
                self.tableWidget.setRowHidden(fila, False)
            else:
                self.tableWidget.setRowHidden(fila, True)    
        
###---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------->>>>        
    
def app():
    app = QtWidgets.QApplication(sys.argv)
    CRUD = QtWidgets.QMainWindow()
    ui = Ui_CRUD(CRUD)
    CRUD.show()
    sys.exit(app.exec())
    
app()
