from db.transactions import Transactions
from ORM.transaction import Transaction
from PyQt4.QtGui import QAction, qApp, QIcon,QToolBar

import datetime
import resources.resource_manager as resource_manager   

class TransactionToolBar(QToolBar):
    """ Represents the Transaction Tool Bar """

    def __init__(self, table_view):
        """ Create and populate the Transaction Tool Bar """
        QToolBar.__init__(self)
        self.table_view = table_view
        self.addNewTransactionButton()
        self.addExitButton()

    def addNewTransactionButton(self):
        """ Adds the New Transaction Button to the ToolBar """
        newIcon = QIcon(resource_manager.GetResourceFilePath('money.png'))
        newTransactionAction = QAction(newIcon, 'New Transaction', self)
        newTransactionAction.setShortcut('Ctrl+N')
        newTransactionAction.setStatusTip("Create a New Transaction.")
        newTransactionAction.triggered.connect(self.newTransaction)
        
        self.addAction(newTransactionAction)

    def addExitButton(self):
        """ Adds the Exit Button to the ToolBar """
        exitAction = QAction(QIcon(resource_manager.GetResourceFilePath('exit.png')), 'Exit the Application', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip("Exit the Application.")
        exitAction.triggered.connect(qApp.quit)
        
        self.addAction(exitAction)

    def newTransaction(self): # Want to move this function out of this view class
        """ Creates a New Transaction """
        transaction = Transaction(date=datetime.date.today())
        Transactions.add(transaction)
        self.table_view.table_model.insertRows(0, 1)