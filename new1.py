import sys
from PyQt4 import QtGui,QtCore
import os
class Window(QtGui.QMainWindow):
    def __init__(self):
         super(Window,self).__init__()
         self.setGeometry(10,30,1200,400)
         self.setWindowTitle('Love')
         self.setWindowIcon(QtGui.QIcon('acm1.png'))


         extractAction = QtGui.QAction("&New",self)
         extractAction.setShortcut("Ctrl+N")
         extractAction.setStatusTip('leave the app')
         extractAction.triggered.connect(self.close_application)
        
         self.statusBar()

         
         mainMenu = self.menuBar()
         fileMenu = mainMenu.addMenu('&File')
         fileMenu.addAction(extractAction)
         fileMenu = mainMenu.addMenu('&Edit')
         fileMenu = mainMenu.addMenu('&View')
         fileMenu = mainMenu.addMenu('&Help')
         
         fileMenu.addAction(extractAction)
         
         self.home()

    def home(self):
        btn = QtGui.QPushButton("Quit",self)
        btn.clicked.connect(self.close_application)
        btn.resize(btn.minimumSizeHint())
        btn.move(0,100)

        
        self.progress = QtGui.QProgressBar(self)
        self.progress.setGeometry(200,80,250,20)

        self.btn = QtGui.QPushButton('Download',self)
        self.btn.move(200,120)
        self.btn.clicked.connect(self.download)

        print(self.style().objectName())
        self.styleChoice = QLabel("Windows7",self)

        comboBox=QtGui.QComboBox(self)
        comboBox.addItem("A")
        comboBox.addItem("B")
        comboBox.addItem("C")
        comboBox.addItem("D")
        comboBox.addItem("E")

        comboBox.move(50,250)
        self.styleChoice.move(50,250)
        comboBox.activated[str].connect(self.style_choice)
        
        self.show()

    def style_choice(self,tax):
        self.styleChoice.setTax(text)
        QApplication.setStyle(QStyleFactory.create(tax))
        

    def download(self):
        self.completed = 0
        
        while(self.completed<100):
            self.completed += 0.0001
            self.progress.setValue(self.completed)


    def close_application(self):
        choice = QMessageBox.question(self,'Extract!',
                                      "Go to Acm... ",
                                      QMessageBox.Yes | QMessageBox.No)
        if(choice == QMessageBox.Yes):
            print("Extracting")
            sys.exit()
        else:
            pass
       
        
def main():
    app = QtGuiQApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

main()

            
        
        
