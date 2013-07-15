from db.transactions import Transactions
from ORM.transaction import Transaction
from PySide import QtGui

from Qt.GUI.tab_toolbar import TabToolBar

from Qt.GUI.Account.account_table_widget import AccountTableWidget
from Qt.GUI.Account.account_toolbar import AccountToolBar

from Qt.GUI.Category.category_table_widget import CategoryTableWidget
from Qt.GUI.Category.category_toolbar import CategoryToolBar

from Qt.GUI.Statistics.statistics_panel import StatisticsPanel

from Qt.GUI.Transaction.transaction_table_widget import TransactionTableWidget
from Qt.GUI.Transaction.transaction_toolbar import TransactionToolBar

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
        self.addAccountsTab()
        self.addStatisticsTab()

        self.statusBar()
        self.setWindowTitle("PAS")
        self.setWindowIcon(QtGui.QIcon(resource_manager.GetResourceFilePath('vault_small.png')))
        self.showMaximized()

    def addTransactionTab(self):
        """ Add the Transaction Tab """
        self.transaction_table_widget = TransactionTableWidget()
        self.transaction_table_widget.toolbar = TransactionToolBar
        self.tabView.addTab(self.transaction_table_widget, "Transactions")

    def addCategoriesTab(self):
        """ Add the Categories Tab """
        self.category_table_widget = CategoryTableWidget()
        self.category_table_widget.toolbar = CategoryToolBar
        self.tabView.addTab(self.category_table_widget, "Categories")

    def addAccountsTab(self):
        """ Add the Accounts Tab """
        self.account_table_widget = AccountTableWidget(self.transaction_table_widget)
        self.account_table_widget.toolbar = AccountToolBar
        self.tabView.addTab(self.account_table_widget, "Accounts")

    def addStatisticsTab(self):
        """ Add the Statistics Tab """
        self.statistics_view = StatisticsPanel()
        self.statistics_view.toolbar = TabToolBar
        self.tabView.addTab(self.statistics_view, "Statistics")

    def setToolBar(self, index):
        """ Set the Tool Bar to be the tool bar for the tab's widget """
        if self.toolbar is not None:
            self.removeToolBar(self.toolbar)

        widget = self.tabView.widget(index)
        self.toolbar = widget.toolbar(widget)
        self.addToolBar(self.toolbar)
        widget.tabSelected()