from db.accounts import Accounts
from db.transactions import Transactions
from Utilities.balance_helper import TheBalanceHelper
from ORM.transaction import Transaction
from Qt.GUI.tab_toolbar import TabToolBar

from PySide.QtGui import QAction, QComboBox, QLabel

import datetime
import db.transaction_filters as TransactionFilters

__all__ = "All"
__uncleared__ = "Uncleared"
__unreconciled__ = "Unreconciled"

__filter_order__ = [__all__, 
                    __uncleared__,
                    __unreconciled__]
__transaction_filters__ = {__all__:{},
                           __uncleared__:{Transaction.cleared:[False, None]},
                           __unreconciled__:{Transaction.reconciled:[False, None]}}

class TransactionToolBar(TabToolBar):
    """ Represents the Transaction Tool Bar """
    
    def __init__(self, table_view):
        """ Create and populate the Tab Tool Bar """
        self.transaction = None
        TabToolBar.__init__(self, table_view)

    def addToolBarButtons(self):
        """ Add Tool Bar Buttons """
        self.addNewTransactionButton()
        self.addSeparator()
        self.addFilter()
        self.addSeparator()
        self.addAccount()
        self.addSeparator()
        if self.transaction is not None:
            self.addTransfers()
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
        label = QLabel("Filter: ", self)
        self.addWidget(label)
        comboBox = QComboBox(self)
        comboBox.addItems(__filter_order__)
        comboBox.currentIndexChanged.connect(self.setTransactionFilter)
        self.addWidget(comboBox)
        
    def addAccount(self):
        """ Add Account Label and Combo Box to the UI """
        label = QLabel("Account: ", self)
        self.addWidget(label)
        
        self.accountComboBox = QComboBox(self)
        self.updateComboBoxWithAccounts(self.accountComboBox)
        self.accountComboBox.currentIndexChanged.connect(self.setAccount)
        self.addWidget(self.accountComboBox)
        
    def addTransfers(self):
        """ Add the transfer widgets """
        if len(self.transaction.transferAccounts) == 0:
            self.transferLabel = QLabel("Transfer to: ", self)
            self.addWidget(self.transferLabel)
            self.transferComboBox = QComboBox(self)
            self.updateComboBoxWithAccounts(self.transferComboBox)
            self.transferComboBox.currentIndexChanged.connect(self.setTransfer)
            self.addWidget(self.transferComboBox)
        else:
            if self.transaction.account is self.table_view.account:
                self.transferLabel = QLabel("Transferred to: {0}".format(self.transaction.transferAccounts[0].name), self)
            else:
                self.transferLabel = QLabel("Transferred to: {0}".format(self.transaction.account.name), self)
            self.addWidget(self.transferLabel)
            eraseIcon = self.getQIcon('erase.png')
            removeTransferAction = QAction(eraseIcon, 'Remove Transfer', self)
            removeTransferAction.setStatusTip("Remove Transfer.")
            removeTransferAction.triggered.connect(self.removeTransfer)
            self.addAction(removeTransferAction)
        
    def updateAccountComboBox(self):
        """ Update the Account Combo Box """
        names = self.getAccountNames()
        self.accountComboBox.clear()
        self.accountComboBox.addItems(names)
        
    def updateComboBoxWithAccounts(self, comboBox):
        """ Update Combo Box """
        names = self.getAccountNames()
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

    def setTransactionFilter(self, index):
        """ Set the Transaction Filter """
        text = __filter_order__[index]
        
        if text in __transaction_filters__:
            self.table_view.updateTransactions(filters=__transaction_filters__[text])
            
    def setAccount(self, index):
        """ Set the Transaction Account to view """
        account = Accounts.all()[index]
        self.table_view.updateTransactions(account=account)
        
    def setTransfer(self, index):
        """ Set the Transaction Account to view """
        account = Accounts.all()[index]
        if len(self.transaction.transferAccounts) == 0:
            self.transaction.transferAccounts.append(account)
            Transactions.save()
            self.buildToolbarWidgets()
            
    def removeTransfer(self):
        """ Remove the Transfer """
        self.transaction.transferAccounts = []
        Transactions.save()
        self.buildToolbarWidgets()
            
    def getAccountNames(self):
        """ Return Account Names """
        names = []
        for account in Accounts.all():
            if account.name is not None:
                names.append(account.name)
        return names
        
    def tabSelected(self):
        """ Update the Account Tab when the tab is selected """
        text = self.accountComboBox.currentText()
        self.updateAccountComboBox()
        index = self.accountComboBox.findText(text)
        if not (index == -1):
            self.accountComboBox.setCurrentIndex(index)