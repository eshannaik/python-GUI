from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlTableModel

class ContactsModel:

	def __init__(self):
		self.model = self.createModel()

	@staticmethod
	#Making the Table
	def createModel():
		tableModel = QSqlTableModel()
		tableModel.setTable("contacts")
		tableModel.setEditStrategy(QSqlTableModel.OnFieldChange) #changes get saved immediately
		tableModel.select() #loads table

		headers=("ID","Name","Job","Email")

		for columnIndex, header in enumerate(headers):
			tableModel.setHeaderData(columnIndex,Qt.Horizontal,header)

		return tableModel

	#Adds contacts to the database
	def addContact(self,data):
		rows=self.model.rowCount()
		self.model.insertRows(rows,1)

		for column, field in enumerate(data):
			self.model.setData(self.model.index(rows,column+1),field)
		
		self.model.submitAll()
		self.model.select()

	#Deletes contacts from the database
	def deleteContacts(self,row):
		self.model.removeRow(row)
		self.model.submitAll()
		self.model.select()

	#Clears Contacts from the database
	def clearContacts(self):
		self.model.setEditStrategy(QSqlTableModel.OnManualSubmit) #caches all the rows untill submitAll() comes
		self.model.removeRows(0,self.model.rowCount())
		self.model.submitAll()
		self.model.setEditStrategy(QSqlTableModel.OnFieldChange) #so that we can update directly from the table view
		self.model.select()