import sys
from PyQt4 import QtCore, QtGui, QtSql

def initializeModel(model):
   model.setTable('acmmembers')
   model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
   model.select()
   model.setHeaderData(0, QtCore.Qt.Horizontal, "NAME")
   model.setHeaderData(1, QtCore.Qt.Horizontal, "STUDENT ID")
   model.setHeaderData(2, QtCore.Qt.Horizontal, "EMAIL ID")
   model.setHeaderData(3, QtCore.Qt.Horizontal, "MOBILE NO")
	
def createView(title, model):
   view = QtGui.QTableView()
   view.setModel(model)
   view.setWindowTitle(title)
   return view
	
def addrow():
   print model.rowCount()
   ret = model.insertRows(model.rowCount(), 1)
   print ret
	
def findrow(i):
   delrow = i.row()
	
if __name__ == '__main__':

   app = QtGui.QApplication(sys.argv)
   db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
   db.setDatabaseName('acmbkbiet.db')
   model = QtSql.QSqlTableModel()
   delrow = -1
   initializeModel(model)
	
   view1 = createView("Table Model (View 1)", model)
   view1.clicked.connect(findrow)
	
   dlg = QtGui.QDialog()
   layout = QtGui.QVBoxLayout()
   layout.addWidget(view1)
	
   button = QtGui.QPushButton("Add a row")
   button.clicked.connect(addrow)
   layout.addWidget(button)
	
   btn1 = QtGui.QPushButton("del a row")
   btn1.clicked.connect(lambda: model.removeRow(view1.currentIndex().row()))
   layout.addWidget(btn1)
	
   dlg.setLayout(layout)
   dlg.setWindowTitle("Database Demo")
   dlg.show()
   sys.exit(app.exec_())
