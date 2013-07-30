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

    def addToolBarButtons(self):
        """ Add Tool Bar Buttons """
        self.addNewTransactionButton()
        self.addSeparator()
        print "In constructor before adding filter"
        self.addFilter()
        print "In constructor after adding filter"
        self.addSeparator()
        self.addAccount()
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
        print "Adding Fitler Combo Box"
        
        label = QLabel("Filter", self)
        self.addWidget(label)
        comboBox = QComboBox(self)
        comboBox.addItems(__filter_order__)
        comboBox.currentIndexChanged.connect(self.setTransactionFilter)
        self.addWidget(comboBox)
        
    def addAccount(self):
        """ Add Account Label and Combo Box to the UI """
        label = QLabel("Account", self)
        self.addWidget(label)
        comboBox = QComboBox(self)
        
        names = self.getAccountNames()
        comboBox.addItems(names)
        comboBox.currentIndexChanged.connect(self.setAccount)
        self.addWidget(comboBox)

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
        
        print "Trying to set the Transaction Filter", __transaction_filters__[text]
        
        if text in __transaction_filters__:
            print "Setting Transaction Filter", __transaction_filters__[text]
            self.table_view.updateTransactions(filters=__transaction_filters__[text])
            
    def setAccount(self, index):
        """ Set the Transaction Account to view """
        account = Accounts.all()[index]
        self.table_view.updateTransactions(account=account)
            
    def getAccountNames(self):
        """ Return Account Names """
        names = []
        for account in Accounts.all():
            if account.name is not None:
                names.append(account.name)
        return names