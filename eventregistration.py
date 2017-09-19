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
    q.exec_("create table if not exists EVENTREGISTRATION (NAME TEXT NOT NULL, ID TEXT PRIMARY KEY NOT NULL, DATE TEXT NOT NULL, EVENT CHAR(50), MOBILE INT, AMOUNT REAL)")
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
        
        DATE = QtGui.QLabel('DATE :', self)
        DATE.move(30, 110)

        self.DATEEdit = QtGui.QLineEdit(self)
        self.DATEEdit.move(120, 110)
        
        EVENT = QtGui.QLabel('EVENT NAME :', self)
        EVENT.move(30, 150)

        self.EVENTEdit = QtGui.QLineEdit(self)
        self.EVENTEdit.move(120, 150)

        MOBILENO = QtGui.QLabel('MOBILE NO :', self)
        MOBILENO.move(30, 190)

        self.MOBILENOEdit = QtGui.QLineEdit(self)
        self.MOBILENOEdit.move(120, 190)

        AMOUNT = QtGui.QLabel('AMOUNT :', self)
        AMOUNT.move(30, 310)
        self.AMOUNTEdit = QtGui.QLineEdit(self)
        self.AMOUNTEdit.move(120, 310)
           
        button1= QtGui.QPushButton('RESET', self)
        button1.setGeometry(50, 370, 70, 30)
        
        button2= QtGui.QPushButton('SUBMIT', self)
        button2.setGeometry(150, 370, 70, 30)
        
        self.connect(button2, QtCore.SIGNAL('clicked()'),self.button2Clicked)

        self.setWindowTitle('EVENT/WORKSHOP REGISTRATION')    

    def button2Clicked(self):
        q=QSqlQuery()
        q.exec_("insert into EVENTREGISTRATION (name, \
                                                id, \
                                                date, \
                                                event, \
                                                mobile, \
                                                amount) values ( \
                              '{0}', \
                              '{1}', \
                              '{2}', \
                              '{3}', \
                              '{4}', \
                              '{5}')".format(self.NAMEEdit.text(),
                                             self.SIDEdit.text(),
                                             self.DATEEdit.text(),
                                             self.EVENTEdit.text(),
                                             self.MOBILENOEdit.text(),
                                             self.AMOUNTEdit.text()))
        q.exec_("commit")
        
if __name__=="__main__": 
    app=QtGui.QApplication(sys.argv) 
    createConnection()
    createTable() 
    w=TestWidget() 
    w.show()
    sys.exit(app.exec_())
