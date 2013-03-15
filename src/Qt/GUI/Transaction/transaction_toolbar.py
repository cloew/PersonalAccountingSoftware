from db.transactions import Transactions
from ORM.transaction import Transaction
from PySide.QtGui import QAction, QComboBox, QLabel
from Qt.GUI.tab_toolbar import TabToolBar

import datetime

class TransactionToolBar(TabToolBar):
    """ Represents the Transaction Tool Bar """

    def addToolBarButtons(self):
        """ Add Tool Bar Buttons """
        self.addNewTransactionButton()
        self.addSeparator()
        self.addFilter()
        self.addSeparator()

    def addNewTransactionButton(self):
        """ Adds the New Transaction Button to the ToolBar """
        newIcon = self.getQIcon('money.png')
        newTransactionAction = QAction(newIcon, 'New Transaction', self)
        newTransactionAction.setShortcut('Ctrl+N')
        newTransactionAction.setStatusTip("Create a New Transaction.")
        newTransactionAction.triggered.connect(self.newTransaction)
        
        self.addAction(newTransactionAction)

    def addFilter(self):
        """ Add Filter Label and Combo Box to the UI """
        label = QLabel("Filter", self)
        self.addWidget(label)
        comboBox = QComboBox(self)
        comboBox.addItems(["All", "Uncleared", "Unreconciled"])
        self.addWidget(comboBox)

    def newTransaction(self):
        """ Creates a New Transaction """
        transaction = Transaction(date=datetime.date.today())
        Transactions.add(transaction)
        self.addEntryToTable()