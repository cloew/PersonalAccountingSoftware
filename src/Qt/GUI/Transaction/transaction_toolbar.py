from db.transactions import Transactions
from ORM.transaction import Transaction
from PyQt4.QtGui import QAction
from Qt.GUI.tab_toolbar import TabToolBar

import datetime

class TransactionToolBar(TabToolBar):
    """ Represents the Transaction Tool Bar """

    def addToolBarButtons(self):
        """ Add Tool Bar Buttons """
        self.addNewTransactionButton()

    def addNewTransactionButton(self):
        """ Adds the New Transaction Button to the ToolBar """
        newIcon = self.getQIcon('money.png')
        newTransactionAction = QAction(newIcon, 'New Transaction', self)
        newTransactionAction.setShortcut('Ctrl+N')
        newTransactionAction.setStatusTip("Create a New Transaction.")
        newTransactionAction.triggered.connect(self.newTransaction)
        
        self.addAction(newTransactionAction)

    def newTransaction(self):
        """ Creates a New Transaction """
        transaction = Transaction(date=datetime.date.today())
        Transactions.add(transaction)
        self.addEntryToTable()