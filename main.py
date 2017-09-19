import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import os
import subprocess

class Window(QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setWindowState(Qt.WindowMaximized)
        #self.setGeometry(10, 30, 1350, 740)
        #self.move(300,200)
        self.setWindowTitle("ACM BKBIET - Event Handler")
        self.setWindowIcon(QIcon('acm1.png'))
         #self.image = QImage()
    
        
        extractAction = QAction("&Exit", self)
        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip('Leave The App')#status at below the window
        extractAction.triggered.connect(self.close_application)
        extractAction = QAction("&Exit", self)
        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip('Leave The App')#status at below the window
        extractAction.triggered.connect(self.close_application)

        self.statusBar()

 
       

        

        self.home()
        
        #self.home()

        
        
    def home(self):
        
       
        #self.palette = QPalette()
        #self.palette.setColor(QPalette.Background,Qt.red)

        self.quit = QPushButton("QUIT",self)
        self.quit.clicked.connect(self.close_application)

        self.quit.move(600,600)
        self.quit.resize(150,60)

        self.btn1 = QPushButton("GEEK REGISTRATION",self)
        self.btn1.move(150,200)
        self.btn1.resize(150,60)

        self.btn1.clicked.connect(lambda:self.run('geekregistration.py'))

    

        #self.btn1.clicked.connect(self)
        #os.startfile("form.py")
        self.btn2 = QPushButton("MEMBER SIGN-UP",self)
        self.btn2.move(600,200)
        self.btn2.resize(150,60)

        self.btn2.clicked.connect(lambda:self.run('signup.py'))

        #ex = QWidget()
        #ex.show()
        
        #self.btn2.clicked.connect(self)
        #os.startfile("signup.py")
        self.btn3 = QPushButton("MEMBER VERIFICATION",self)
        self.btn3.move(1050,200)
        self.btn3.resize(150,60)
        self.btn4 = QPushButton("EVENT REGISTRATION",self)
        self.btn4.move(150,400)
        self.btn4.resize(150,60)

        self.btn4.clicked.connect(lambda:self.run('eventregistration.py'))

        #ex2 = QWidget()
        #ex2.show()


        self.snameEdit = QLabel()

        self.btn = QPushButton("ACCESS DATABASE",self)
        self.btn.move(600,400)
        self.btn.resize(150,60)
        self.btn.clicked.connect(self.download)

        self.btn = QPushButton("REGISTER",self)
        self.btn.move(1050,400)
        self.btn.resize(150,60)
        self.btn.clicked.connect(self.download)

        #pic = QLabel()
        #pic.setGeometry(100, 30, 400, 100)
        #use full ABSOLUTE path to the image, not relative
        #pic.setPixmap(QPixmap(os.getcwd() + "acm1.png"))

       
       
        self.show()

    def main():
        app = QtGui.QApplication(sys.argv)
        ex = QtGui.QWidget()
        ex.show()
        ex2 = QtGui.QWidget()
        ex2.show()

           



    def run(self, path):
        subprocess.call(['pythonw',path])    

           
    def showDate(self, date):     
    
        self.lbl.setText(date.toString())
    
    
        
        self.show()   
   

    def style_choice(self):
        #self.styleChoice.setText()
        QApplication.setStyle(QStyleFactory.create())
        
    def download(self):
        self.completed = 0

        while self.completed < 100:
            self.completed += 0.0001
            self.progress.setValue(self.completed)
        
            

    def close_application(self):
        #popup message

        choice = QMessageBox.question(self, 'Close',
                                           "Do You Want To Close ?",
                                           QMessageBox.Yes | QMessageBox.No)
        if choice == QMessageBox.Yes:
            print("Doing")
            sys.exit()
        else:
            pass
        
    
def run():
        app = QApplication(sys.argv)
        app.setStyleSheet('QMainWindow{background-color:#008069;border: 1px solid black}')
        GUI = Window()
        sys.exit(app.exec_())

run()
