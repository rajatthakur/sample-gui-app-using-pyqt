from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
import os
class Login(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        
        self.setGeometry(50, 50, 300, 250)
        self.setWindowTitle("ACM BKBIET-Login Page")
        self.setWindowIcon(QIcon('acm1.png'))

        self.Login = QLabel('USERNAME :',self)
        self.Login.move(14,24)
        
        self.textName = QLineEdit(self)
        #self.textName.setGeometry(22,33,44,55)

        self.Pass = QLabel('PASSWORD :',self)
        self.Pass.move(14,88)

        self.textPass = QLineEdit(self)
        self.textPass.setEchoMode(QLineEdit.Password)     #For bullet password

        self.buttonLogin = QPushButton('LOGIN', self)
        #self.buttonLogin.setGeometry(50, 120, 70, 30)
        
       # self.buttonLogin1 = QPushButton('CANCEL', self)
        #self.buttonLogin1.setGeometry(50, 170, 70, 30)
        
      #  self.buttonLogin1.clicked.connect(close_application)
        
        self.buttonLogin.clicked.connect(self.handleLogin)
        
        layout = QVBoxLayout(self)
        layout.addWidget(self.textName)
        layout.addWidget(self.textPass)
        layout.addWidget(self.buttonLogin)
        #layout.addWidget(self.buttonLogin1)
        
    def handleLogin(self):
        if (self.textName.text() == 'admin' and
            self.textPass.text() == 'acmbkbiet'):
            #open main ui file
            os.startfile("main.py")
            self.accept()
        else:
            QMessageBox.warning(self, 'Error', 'Bad username or password')
"""
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
   """         
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
         
    if Login().exec_() == QDialog.Accepted:
        window = Login()
        window.setBackgroundRole(QPalette.Base)
        window.show()
        sys.exit(app.exec_())
