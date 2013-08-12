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
        
    def addTransfers(self):
        """ Add the transfer widgets """
        if len(self.transaction.transferAccounts) == 0:
            self.transferLabel = QLabel("Transfer {0}: ".format(self.getTransferDirection()), self)
            self.addWidget(self.transferLabel)
            self.transferComboBox = QComboBox(self)
            self.updateComboBoxWithAccounts(self.transferComboBox, ignoreCurrent=True)
            self.transferComboBox.activated.connect(self.setTransfer)
            self.addWidget(self.transferComboBox)
        else:
            if self.transaction.account is self.table_view.account:
                self.transferLabel = QLabel("Transferred {0}: {1}".format(self.getTransferDirection(), self.transaction.transferAccounts[0].name), self)
            else:
                self.transferLabel = QLabel("Transferred {0}: {1}".format(self.getTransferDirection(), self.transaction.account.name), self)
            self.addWidget(self.transferLabel)
            eraseIcon = self.getQIcon('erase.png')
            removeTransferAction = QAction(eraseIcon, 'Remove Transfer', self)
            removeTransferAction.setStatusTip("Remove Transfer.")
            removeTransferAction.triggered.connect(self.removeTransfer)
            self.addAction(removeTransferAction)
            
    def getTransferDirection(self):
        """ Return the Transfer Direction word """
        if self.transaction.isIncome(self.table_view.account):
            return "from"
        else:
            return "to"
        
    def updateComboBoxWithAccounts(self, comboBox, ignoreCurrent=False):
        """ Update Combo Box """
        names = self.getAccountNames()
        if ignoreCurrent:
            names.remove(self.table_view.account.name)
        comboBox.clear()
        comboBox.addItems(names)
        
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