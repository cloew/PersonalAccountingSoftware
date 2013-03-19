from db.transactions import Transactions
from ORM.transaction import Transaction
from PySide.QtGui import QAction, QComboBox, QLabel
from Qt.GUI.tab_toolbar import TabToolBar

import datetime
import db.transaction_filters as TransactionFilters

__all__ = "All"
__uncleared__ = "Uncleared"
__unreconciled__ = "Unreconciled"

__filter_order__ = [__all__, 
                    __uncleared__,
                    __unreconciled__]
__transaction_filters__ = {__all__: TransactionFilters.All,
                           __uncleared__: TransactionFilters.Uncleared,
                           __unreconciled__: TransactionFilters.Unreconciled}

class TransactionToolBar(TabToolBar):
    """ Represents the Transaction Tool Bar """

    def addToolBarButtons(self):
        """ Add Tool Bar Buttons """
        self.addNewTransactionButton()
        self.addSeparator()
        self.addFilter()
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
        label = QLabel("Filter", self)
        self.addWidget(label)
        comboBox = QComboBox(self)
        comboBox.addItems(__filter_order__)
        comboBox.currentIndexChanged.connect(self.setTransactionFilter)
        self.addWidget(comboBox)

    def newTransaction(self):
        """ Creates a New Transaction """
        transaction = Transaction(date=datetime.date.today())
        transaction.account = self.table_view.table_model.account
        Transactions.add(transaction)
        self.table_view.table_model.checkCount()

    def setTransactionFilter(self, index):
        """ Set the Transaction Filter """
        text = __filter_order__[index]
        
        if text in __transaction_filters__:
            self.table_view.table_model.setTransactionRetriever(__transaction_filters__[text])