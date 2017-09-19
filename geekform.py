import sys,os
from PyQt4 import QtGui,QtCore
import sqlite3
from PyQt4.QtSql import *

def createConnection(): 
    db=QSqlDatabase.addDatabase("QSQLITE") 
    db.setDatabaseName("acmbkbiet.db")
    db.open()

def createTable(): 
    q=QSqlQuery() 
    q.exec_("create table if not exists geekevents(sname TEXT NOT NULL, sid INT PRIMARY KEY NOT NULL, smember TEXT, event1 TEXT, event2 TEXT, event3 TEXT, event4 TEXT)") 
    q.exec_("commit") 

class Model(QSqlTableModel): 
    def __init__(self,parent): 
        QSqlTableModel.__init__(self,parent)                     
        self.setTable("geekevents") 
        self.select()                                         
        self.setEditStrategy(QSqlTableModel.OnManualSubmit) 

class Register(QtGui.QWidget):

    def __init__(self):
        super(Register, self).__init__()
        self.setGeometry(50,50,500,300)


       # extractAction = QtGui.QAction("Close", self)
       # extractAction.triggered.connect(self.close_application)
       
        self.initUI()
        
    def initUI(self):
        
        sname = QtGui.QLabel('NAME')
        snameEdit = QtGui.QLineEdit()
        sname.setGeometry(QtCore.QRect(300,300,640,480))
        snameEdit = QtGui.QLineEdit()
        sname.setGeometry(QtCore.QRect(300,300,640,480))                    
        
        sid = QtGui.QLabel('ID')
        smember = QtGui.QLabel('ACM MEMBER')
        sevent = QtGui.QLabel('EVENT')

    
        sidEdit = QtGui.QLineEdit()
        smemberCheck_1 = QtGui.QRadioButton("Yes")
        smemberCheck_2 = QtGui.QRadioButton("No")
        selectEvent1 = QtGui.QComboBox()
        #sprice = int(self.price_box.toPlainText())

        selectEvent1 = QtGui.QComboBox(self)
        selectEvent1.addItem("Select...")
        selectEvent1.addItem("Android Workshop")
        selectEvent1.addItem("Maya 3d Workshop")
        selectEvent1.addItem("Live CS")
        selectEvent1.addItem("ACM Night")
        selectEvent1.addItem("Non Technical")
        
        selectEvent2 = QtGui.QComboBox()
        
        selectEvent2 = QtGui.QComboBox(self)
        selectEvent2.addItem("Select...")
        selectEvent2.addItem("Android Workshop")
        selectEvent2.addItem("Maya 3d Workshop")
        selectEvent2.addItem("Live CS")
        selectEvent2.addItem("ACM Night")
        selectEvent2.addItem("Non Technical")
        
        selectEvent3 = QtGui.QComboBox()
    
        selectEvent3 = QtGui.QComboBox(self)
        selectEvent3.addItem("Select...")
        selectEvent3.addItem("Android Workshop")
        selectEvent3.addItem("Maya 3d Workshop")
        selectEvent3.addItem("Live CS")
        selectEvent3.addItem("ACM Night")
        selectEvent3.addItem("Non Technical")
        
        selectEvent4 = QtGui.QComboBox()

        selectEvent4 = QtGui.QComboBox(self)
        selectEvent4.addItem("Select...")
        selectEvent4.addItem("Android Workshop")
        selectEvent4.addItem("Maya 3d Workshop")
        selectEvent4.addItem("Live CS")
        selectEvent4.addItem("ACM Night")
        selectEvent4.addItem("Non Technical")
    
        btn = QtGui.QPushButton("OK", self)
        #btn.clicked.connect(self.close_application)
        self.connect(btn, QtCore.SIGNAL('clicked()'),self.button1Clicked)

        grid = QtGui.QGridLayout()
        grid.setSpacing(10)
        
        grid.addWidget(sname, 1, 0)
        grid.addWidget(snameEdit, 1, 1, 1, 1)
        
        grid.addWidget(sid, 2, 0)
        grid.addWidget(sidEdit, 2, 1, 1, 1)

        grid.addWidget(smember, 3, 0)
        grid.addWidget(smemberCheck_1, 3, 1, 1, 1)
        grid.addWidget(smemberCheck_2, 3, 2, 1, 1)

        grid.addWidget(sevent, 4, 0)
        grid.addWidget(selectEvent1, 4,1)
        grid.addWidget(selectEvent2, 5,1)
        grid.addWidget(selectEvent3, 6,1)
        grid.addWidget(selectEvent4, 7,1)
        grid.addWidget(btn, 5, 6, 7, 1)
        self.setLayout(grid) 
        
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('THE GEEK-16 REGISTRATION')    
        self.show()
        
 
    def button1Clicked(self):
        q=QSqlQuery()
        q.exec_("insert into geekevents(\ sname, \ sid, \ acmmember, \ event1, \ event2, \ event3, \ event4) values( \
                              '{0}', \
                              '{1}', \
                              '{2}', \
                              '{3}', \
                              '{4}', \
                              '{5}', \
                              '{6}', \
                              '{7}')"
                              .format(self.snameEdit.text(),
                                      self.sidEdit.text(),
                                             self.smemberCheck_1.text(),
                                             self.selectEvent1.text(),
                                             self.selectEvent2.text(),
                                             self.selectEvent3.text(),
                                             self.selectEvent4.text()))
 
        q.exec_("commit")

if __name__=="__main__": 
    app=QtGui.QApplication(sys.argv) 
    createConnection()
    createTable() 
    w=Register() 
    w.show() 
    sys.exit(app.exec_())
