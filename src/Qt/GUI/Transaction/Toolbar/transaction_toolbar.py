from db.accounts import Accounts
from db.transactions import Transactions
from ORM.transaction import Transaction
from Qt.GUI.tab_toolbar import TabToolBar
from Qt.GUI.Transaction.Toolbar.account_toolbar_section import AccountToolbarSection
from Qt.GUI.Transaction.Toolbar.filter_toolbar_section import FilterToolbarSection
from Qt.GUI.Transaction.Toolbar.transfer_toolbar_section import TransferToolbarSection
from Utilities.balance_helper import TheBalanceHelper

from PySide.QtGui import QAction, QComboBox, QLabel

import datetime

class TransactionToolBar(TabToolBar):
    """ Represents the Transaction Tool Bar """
    
    def __init__(self, table_view):
        """ Create and populate the Tab Tool Bar """
        self.transaction = None
        self.accountSection = AccountToolbarSection(self, table_view)
        self.filterSection = FilterToolbarSection(self, table_view)
        self.transferSection = TransferToolbarSection(self, table_view)
        TabToolBar.__init__(self, table_view)

    def addToolBarButtons(self):
        """ Add Tool Bar Buttons """
        self.addNewTransactionButton()
        self.addSeparator()
        self.filterSection.addFilter()
        self.addSeparator()
        self.accountSection.addAccount()
        self.addSeparator()
        if self.transaction is not None:
            self.transferSection.addTransfers()
            self.addSeparator()
        
    def addNewTransactionButton(self):
        """ Adds the New Transaction Button to the ToolBar """
        newIcon = self.getQIcon('money.png')
        newTransactionAction = QAction(newIcon, 'New Transaction', self)
        newTransactionAction.setShortcut('Ctrl+N')
        newTransactionAction.setStatusTip("Create a New Transaction.")
        newTransactionAction.triggered.connect(self.newTransaction)
        
        self.addAction(newTransactionAction)
        
    def updateTransfers(self, transaction):
        """ Update the Transfer Selection """
        self.transaction = transaction
        self.buildToolbarWidgets()

    def newTransaction(self):
        """ Creates a New Transaction """
        transaction = Transaction(date=datetime.date.today())
        transaction.account = self.table_view.account
        Transactions.add(transaction)
        TheBalanceHelper.setupBalancesForAccount(transaction.account)
        self.table_view.insertRow(transaction)
        
    def tabSelected(self):
        """ Update the Account Tab when the tab is selected """
        self.accountSection.tabSelected()