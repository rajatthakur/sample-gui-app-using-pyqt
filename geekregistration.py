import sys
import sqlite3
from PyQt4 import QtCore, QtGui
from PyQt4.QtSql import *

def createConnection(): 
    db=QSqlDatabase.addDatabase("QSQLITE") 
    db.setDatabaseName("acmbkbiet.db")
    db.open()

def createTable(): 
    q=QSqlQuery() 
    q.exec_("create table if not exists GEEKREGISTRATION (NAME TEXT NOT NULL, ID INT PRIMARY KEY NOT NULL, ACMMEMBER TEXT NOT NULL,EVENT1 CHAR(50), EVENT2 CHAR(50), EVENT3 CHAR(50), EVENT4 CHAR(50),AMOUNT REAL)")
    q.exec_("commit") 

class TestWidget(QtGui.QWidget): 
    def __init__(self): 
        QtGui.QWidget.__init__(self)
        
        vbox=QtGui.QVBoxLayout(self) 
        self.view=QtGui.QTableView() 
        vbox.addWidget(self.view)
        self.resize(400,500)
        self.component()

    def component(self):
        NAME = QtGui.QLabel('NAME :', self)
        NAME.move(30, 30)
        
        self.NAMEEdit = QtGui.QLineEdit(self) 
        self.NAMEEdit.move(120, 30)
        self.NAMEEdit.setFocus()
        
        SID = QtGui.QLabel('ID :', self)
        SID.move(30, 70)

        self.SIDEdit = QtGui.QLineEdit(self)
        self.SIDEdit.move(120, 70)
        
        ACM = QtGui.QLabel('ACM MEMBER :', self)
        ACM.move(30, 110)

        self.ACMEdit = QtGui.QLineEdit(self)
        self.ACMEdit.move(120, 110)
        
        EVENT1 = QtGui.QLabel('EVENT 1 :', self)
        EVENT1.move(30, 150)

        self.EVENTEdit1 = QtGui.QLineEdit(self)
        self.EVENTEdit1.move(120, 150)

        EVENT2 = QtGui.QLabel('EVENT 2 :', self)
        EVENT2.move(30, 190)

        self.EVENTEdit2 = QtGui.QLineEdit(self)
        self.EVENTEdit2.move(120, 190)

        EVENT3 = QtGui.QLabel('EVENT 3 :', self)
        EVENT3.move(30, 230)

        self.EVENTEdit3 = QtGui.QLineEdit(self)
        self.EVENTEdit3.move(120, 230)

        EVENT4 = QtGui.QLabel('EVENT 4 :', self)
        EVENT4.move(30, 270)

        self.EVENTEdit4 = QtGui.QLineEdit(self)
        self.EVENTEdit4.move(120, 270)

        AMOUNT = QtGui.QLabel('AMOUNT :', self)
        AMOUNT.move(30, 310)
        self.AMOUNTEdit = QtGui.QLineEdit(self)
        self.AMOUNTEdit.move(120, 310)
           
        button1= QtGui.QPushButton('RESET', self)
        button1.setGeometry(50, 370, 70, 30)
        
        button2= QtGui.QPushButton('SUBMIT', self)
        button2.setGeometry(150, 370, 70, 30)
        
        self.connect(button2, QtCore.SIGNAL('clicked()'),self.button2Clicked)

        self.setWindowTitle('GEEK-16 REGISTRATION')    

    def button2Clicked(self):
        q=QSqlQuery()
        q.exec_("insert into GEEKREGISTRATION (name, \
                              id, \
                              acmmember, \
                              event1, \
                              event2, \
                              event3, \
                              event4, \
                              amount) values ( \
                              '{0}', \
                              '{1}', \
                              '{2}', \
                              '{3}', \
                              '{4}', \
                              '{5}', \
                              '{6}', \
                              '{7}')".format(self.NAMEEdit.text(),
                                             self.SIDEdit.text(),
                                             self.ACMEdit.text(),
                                             self.EVENTEdit1.text(),
                                             self.EVENTEdit2.text(),
                                             self.EVENTEdit3.text(),
                                             self.EVENTEdit4.text(),
                                             self.AMOUNTEdit.text()))
        q.exec_("commit")

if __name__=="__main__": 
    app=QtGui.QApplication(sys.argv) 
    createConnection()
    createTable() 
    w=TestWidget() 
    w.show() 
    sys.exit(app.exec_())
