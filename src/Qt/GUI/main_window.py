from db.transactions import Transactions
from ORM.transaction import Transaction
from PyQt4 import QtGui
from Qt.GUI.transaction_list_view import TransactionListView

import datetime

class MainWindow(QtGui.QMainWindow):
    """ Represents the Main Window of the PAS Application """

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.initUI()

    def initUI(self):
        """ Initialize the User Interface """
        self.list_view = TransactionListView()
        self.setCentralWidget(self.list_view)

        self.statusBar()
        self.prepareToolBar()
        self.setWindowTitle("PAS")
        self.setWindowIcon(QtGui.QIcon('resources/vault_small.png'))
        self.showMaximized()

    def prepareToolBar(self):
        """ Prepares the Tool Bar """
        self.addNewTransactionButton()
        self.addExitButton()

    def addNewTransactionButton(self):
        """ Adds the New Transaction Button to the ToolBar """
        newTransactionAction = QtGui.QAction(QtGui.QIcon('resources/money.png'), 'New Transaction', self)
        newTransactionAction.setShortcut('Ctrl+N')
        newTransactionAction.triggered.connect(self.newTransaction)
        
        self.toolbar = self.addToolBar('New Transaction')
        self.toolbar.addAction(newTransactionAction)

    def addExitButton(self):
        """ Adds the Exit Button to the ToolBar """
        exitAction = QtGui.QAction(QtGui.QIcon('resources/exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(QtGui.qApp.quit)
        
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)

    def newTransaction(self): # Want to move this function out of this view class
        """ Creates a New Transaction """
        transaction = Transaction(date=datetime.date.today())
        Transactions.add(transaction)
        self.list_view.model.insertRows(0, 1)