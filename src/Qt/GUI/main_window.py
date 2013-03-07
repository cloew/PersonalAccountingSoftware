from db.transactions import Transactions
from ORM.transaction import Transaction
from PyQt4 import QtGui
from Qt.GUI.Category.category_list_view import CategoryListView
from Qt.GUI.Transaction.transaction_list_view import TransactionListView

import datetime
import resources.resource_manager as resource_manager

class MainWindow(QtGui.QMainWindow):
    """ Represents the Main Window of the PAS Application """

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.initUI()

    def initUI(self):
        """ Initialize the User Interface """
        self.tabView = QtGui.QTabWidget()
        self.setCentralWidget(self.tabView)

        self.addTransactionTab()
        self.addCategoriesTab()

        self.statusBar()
        self.prepareToolBar()
        self.setWindowTitle("PAS")
        self.setWindowIcon(QtGui.QIcon(resource_manager.GetResourceFilePath('vault_small.png')))
        self.showMaximized()

    def addTransactionTab(self):
        """ Add the Transaction Tab """
        self.transaction_list_view = TransactionListView()
        self.tabView.addTab(self.transaction_list_view, "Transactions")

    def addCategoriesTab(self):
        """ Add the Categories Tab """
        self.category_list_view = CategoryListView()
        self.tabView.addTab(self.category_list_view, "Categories")

    def prepareToolBar(self):
        """ Prepares the Tool Bar """
        self.addNewTransactionButton()
        self.addExitButton()

    def addNewTransactionButton(self):
        """ Adds the New Transaction Button to the ToolBar """
        newTransactionAction = QtGui.QAction(QtGui.QIcon(resource_manager.GetResourceFilePath('money.png')), 'New Transaction', self)
        newTransactionAction.setShortcut('Ctrl+N')
        newTransactionAction.setStatusTip("Create a New Transaction.")
        newTransactionAction.triggered.connect(self.newTransaction)
        
        self.toolbar = self.addToolBar('New Transaction')
        self.toolbar.addAction(newTransactionAction)

    def addExitButton(self):
        """ Adds the Exit Button to the ToolBar """
        exitAction = QtGui.QAction(QtGui.QIcon(resource_manager.GetResourceFilePath('exit.png')), 'Exit the Application', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip("Exit the Application.")
        exitAction.triggered.connect(QtGui.qApp.quit)
        
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)

    def newTransaction(self): # Want to move this function out of this view class
        """ Creates a New Transaction """
        transaction = Transaction(date=datetime.date.today())
        Transactions.add(transaction)
        self.transaction_list_view.table_model.insertRows(0, 1)