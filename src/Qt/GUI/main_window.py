from db.transactions import Transactions
from ORM.transaction import Transaction
from PyQt4 import QtGui

from Qt.GUI.Category.category_list_view import CategoryListView
from Qt.GUI.Category.category_toolbar import CategoryToolBar

from Qt.GUI.Transaction.transaction_list_view import TransactionListView
from Qt.GUI.Transaction.transaction_toolbar import TransactionToolBar

import datetime
import resources.resource_manager as resource_manager

class MainWindow(QtGui.QMainWindow):
    """ Represents the Main Window of the PAS Application """

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.toolbar = None
        self.initUI()

    def initUI(self):
        """ Initialize the User Interface """
        self.tabView = QtGui.QTabWidget()
        self.tabView.currentChanged.connect(self.setToolBar)
        self.setCentralWidget(self.tabView)

        self.addTransactionTab()
        self.addCategoriesTab()

        self.statusBar()
        self.setWindowTitle("PAS")
        self.setWindowIcon(QtGui.QIcon(resource_manager.GetResourceFilePath('vault_small.png')))
        self.showMaximized()

    def addTransactionTab(self):
        """ Add the Transaction Tab """
        self.transaction_list_view = TransactionListView()
        self.transaction_list_view.toolbar = TransactionToolBar
        self.tabView.addTab(self.transaction_list_view, "Transactions")

    def addCategoriesTab(self):
        """ Add the Categories Tab """
        self.category_list_view = CategoryListView()
        self.category_list_view.toolbar = CategoryToolBar
        self.tabView.addTab(self.category_list_view, "Categories")

    def setToolBar(self, index):
        """ Set the Tool Bar to be the tool bar for the tab's widget """
        if self.toolbar is not None:
            self.removeToolBar(self.toolbar)

        widget = self.tabView.widget(index)
        self.toolbar = widget.toolbar(widget)
        self.addToolBar(self.toolbar)