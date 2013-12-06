from db.accounts import Accounts
from db.transactions import Transactions
from ORM.transaction import Transaction
from ORM.transaction_helper import GetOrCreateSubtransactionSet
from Qt.GUI.Transaction.Table.subtransaction_table_widget import SubTransactionTableWidget
from Qt.GUI.Utilities.account_combobox_helper import UpdateComboBoxWithAccounts
from Utilities.balance_helper import TheBalanceHelper
from Utilities.dollar_amount_helper import GetCentsFromDollarString

from PySide.QtGui import QComboBox, QFormLayout, QFrame, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout

import datetime

class SubtransactionForm:
    """ Represents the SubTransaction Form """
    
    def __init__(self, parent):
        """ Initialize the Subtransaction Form """
        self.parent = parent
        self.subtransactionTable = SubTransactionTableWidget(self.transaction, self)
        self.subtransactionLabels = []
    
    def setup(self):
        """ Setup the Subtransactions for the Transaction Details """
        self.subtransactionFrame = QFrame()
        
        self.verticalLayout = QVBoxLayout(self.subtransactionFrame)
        self.horizontalLayout = QHBoxLayout()
        
        label = QLabel("<b>Subtransactions</b>")
        self.horizontalLayout.addWidget(label)
        
        button = QPushButton("Add New Subtransaction")
        button.clicked.connect(self.saveTransaction)
        self.horizontalLayout.addWidget(button)
        
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.addWidget(self.subtransactionTable)
        self.verticalLayout.addStretch()
        
        self.subtransactionFrame.setLayout(self.verticalLayout)
        self.layout.addWidget(self.subtransactionFrame)
        
    def addSubtransactionLabels(self):
        """ Add Subtransaction Labels """
        self.subtransactionLabels = []
        if self.transaction is not None and self.transaction.subtransaction_set is not None:
            for transaction in self.transaction.subtransaction_set.transactions:
                if transaction is not self.transaction:
                    label = QLabel("{0}".format(transaction.description))
                    self.subtransactionLabels.append(label)
                    self.formLayout.insertRow(1, label)
        
    def updateOnTransactionChange(self):
        """ Update on a Transaction Change """
        self.subtransactionTable.parent_transaction = self.transaction
        self.subtransactionTable.updateTransactions()
        
    def tabSelected(self):
        """ Do nothing when selected """
            
    def saveTransaction(self, checked=False):
        """ Save the current Transaction """
        if self.transaction is not None:
            transaction = self.createSubtransaction(self.transaction)
            
            TheBalanceHelper.setupBalancesForAccount(transaction.account)
            self.subtransactionTable.updateTransactions()
            if transaction.account is self.table.account:
                self.table.insertRow(transaction)
                
    def createSubtransaction(self, relative):
        """ Create a Subtransaction from its relative """
        transaction = Transaction(date=datetime.date.today())
        transaction.subtransaction_set = GetOrCreateSubtransactionSet(relative)
        transaction.account = relative.account
        
        Transactions.add(transaction)
        Transactions.save()
        return transaction
    
    @property
    def layout(self):
        return self.parent.layout
        
    @property
    def table(self):
        return self.parent.table
        
    @property
    def transaction(self):
        return self.parent.transaction