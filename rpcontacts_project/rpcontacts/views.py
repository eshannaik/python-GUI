# GUI Part
# The design of the Contact Book

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
	QHBoxLayout,
	QWidget,
	QMainWindow,
	QAbstractItemView,
	QPushButton,
	QTableView,
	QVBoxLayout,
	QDialog,
	QDialogButtonBox,
	QFormLayout,
	QLineEdit,
	QMessageBox,
	)

from .model import ContactsModel

class Window(QMainWindow):

	def __init__(self,parent=None): 
		super().__init__(parent)
		self.setWindowTitle("RP Contacts")
		self.resize(625, 250)
		self.centralWidget = QWidget()
		self.setCentralWidget(self.centralWidget)
		self.layout = QHBoxLayout()
		self.centralWidget.setLayout(self.layout)
		self.contactModel = ContactsModel()
		self.setupUI()
		
	def setupUI(self):
		self.table =QTableView()
		self.table.setModel(self.contactModel.model)
		self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
		self.table.resizeColumnsToContents()

		self.addButton = QPushButton("Add")
		self.addButton.clicked.connect(self.openAddDialog)
		self.deleteButton = QPushButton("Delete")
		self.deleteButton.clicked.connect(self.deleteContact)
		self.clearButton = QPushButton("Clear All")
		self.clearButton.clicked.connect(self.clearContacts)

		layout = QVBoxLayout()
		layout.addWidget(self.addButton)
		layout.addWidget(self.deleteButton)
		layout.addStretch()
		layout.addWidget(self.clearButton)

		self.layout.addWidget(self.table)
		self.layout.addLayout(layout)

	def openAddDialog(self):
		dialog = AddDialog(self)

		if dialog.exec() == QDialog.Accepted:
			self.contactModel.addContact(dialog.data)
			self.table.resizeColumnsToContents()

	def deleteContact(self):
		row=self.table.currentIndex().row()

		if row<0:
			return

		messageBox=QMessageBox.warning(
			self,
			"Warning!",
			"Do you want to delete this contact?",
			QMessageBox.Ok | QMessageBox.Cancel,
		)

		if messageBox == QMessageBox.Ok:
			self.contactModel.deleteContacts(row)

	def clearContacts(self):
		messageBox = QMessageBox.warning(
			self,
			"Warning",
			"Are you sure you want to clear the entire table",
			QMessageBox.Ok | QMessageBox.Cancel,
		)

		if messageBox == QMessageBox.Ok:
			self.contactModel.clearContacts()


class AddDialog(QDialog):

	def __init__(self,parent=None):
		super().__init__(parent=parent)
		self.setWindowTitle("Add Contact")
		self.layout=QVBoxLayout()
		self.setLayout(self.layout)
		self.data=None

		self.setupUI()

	def setupUI(self):
		self.nameField=QLineEdit()
		self.nameField.setObjectName("Name")
		self.jobField=QLineEdit()
		self.jobField.setObjectName("Job")
		self.emailField=QLineEdit()
		self.emailField.setObjectName("Email")

		layout=QFormLayout()
		layout.addRow("Name:",self.nameField)
		layout.addRow("Job:",self.jobField)
		layout.addRow("Email:",self.emailField)
		self.layout.addLayout(layout)

		self.buttonsBox = QDialogButtonBox(self)
		self.buttonsBox.setOrientation(Qt.Horizontal)
		self.buttonsBox.setStandardButtons(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
		self.buttonsBox.accepted.connect(self.accept)
		self.buttonsBox.rejected.connect(self.reject)
		self.layout.addWidget(self.buttonsBox)

	def accept(self):
		self.data=[]

		for field in (self.nameField,self.jobField,self.emailField):
			if not field.text():
				QMessageBox.critical(
					self,
					"Error!",
					f"You must provide contact's {field.objectName()}"
					)

				self.data = None
				return
			self.data.append(field.text())

		if not self.data:
			return

		super().accept()