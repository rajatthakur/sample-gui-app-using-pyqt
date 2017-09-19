import sys
from PyQt4 import QtGui,QtCore

class Register(QtGui.QWidget):    

    
    def __init__(self):
        super(Register, self).__init__()
        self.setGeometry(50,50,500,300)


       # extractAction = QtGui.QAction("Close", self)
       # extractAction.triggered.connect(self.close_application)

        
        self.initUI()
        
    def initUI(self):
        
        sname = QtGui.QLabel('NAME')
        sid = QtGui.QLabel('ID')
        smobile = QtGui.QLabel('MOBILE NO.')
        sEmail = QtGui.QLabel('Email')
        sevent = QtGui.QLabel('RENEW STATUS')
        samount = QtGui.QLabel('Final Amount')

        snameEdit = QtGui.QLineEdit()
        sname.setGeometry(QtCore.QRect(300,300,640,480))
        sidEdit = QtGui.QLineEdit()
        smobileEdit = QtGui.QLineEdit()
        semailEdit = QtGui.QLineEdit()
        samountEdit = QtGui.QLineEdit()
        
      

        
        #sprice = int(self.price_box.toPlainText())

        selectEvent1 = QtGui.QComboBox(self)
        selectEvent1.addItem("New Member")
        selectEvent1.addItem("Renew")
        
        
        selectEvent1Edit = QtGui.QLineEdit
        

        btn = QtGui.QPushButton("OK", self)
        #btn.clicked.connect(self.close_application)
        
        grid = QtGui.QGridLayout()
        grid.setSpacing(10)
        
        grid.addWidget(sname, 1, 0)
        grid.addWidget(snameEdit, 1, 1, 1, 1)

        grid.addWidget(sid, 2, 0)
        grid.addWidget(sidEdit, 2, 1, 1, 1)

        grid.addWidget(smobile, 3, 0)
        grid.addWidget(smobileEdit, 3, 1, 1, 1)

        grid.addWidget(sEmail, 4, 0)
        grid.addWidget(semailEdit, 4, 1, 1, 1)

        grid.addWidget(sevent, 5, 0)
        grid.addWidget(selectEvent1, 5,1)
        grid.addWidget(btn, 6, 6, 8, 1)
        self.setLayout(grid)

        grid.addWidget(samount, 8, 0)
        grid.addWidget(samountEdit, 8, 1, 1, 1)
        
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Sign Up')    
        self.show()
        
 
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Register()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
