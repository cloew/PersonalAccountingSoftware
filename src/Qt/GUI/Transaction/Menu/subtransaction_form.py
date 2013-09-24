from db.accounts import Accounts
from db.subtransactions import SubTransactions
from db.transactions import Transactions
from ORM.subtransaction import SubTransaction
from ORM.transaction import Transaction
from Qt.GUI.Utilities.account_combobox_helper import UpdateComboBoxWithAccounts
from Utilities.balance_helper import TheBalanceHelper
from Utilities.dollar_amount_helper import GetCentsFromDollarString

from PySide.QtGui import QComboBox, QFormLayout, QFrame, QLabel, QLineEdit, QPushButton

import datetime

class SubtransactionForm:
    """ Represents the SubTransaction Form """
    
    def __init__(self, parent):
        """ Initialize the Subtransaction Form """
        self.parent = parent
        self.subtransactionLabels = []
    
    def setup(self):
        """ Setup the Subtransactions for the Transaction Details """
        self.subtransactionFrame = QFrame()
        self.formLayout = QFormLayout(self.subtransactionFrame)
        
        label = QLabel()
        label.setText("<b>Subtransactions</b>")
        self.formLayout.addRow(label)
        self.addSubtransactionLabels()
        
        self.accountComboBox = QComboBox()
        UpdateComboBoxWithAccounts(self.accountComboBox)
        self.formLayout.addRow("Account:", self.accountComboBox)
        self.amountEdit = QLineEdit()
        self.formLayout.addRow("Amount:", self.amountEdit)
        self.descriptionEdit = QLineEdit()
        self.formLayout.addRow("Description:", self.descriptionEdit)
        button = QPushButton("Add New Subtransaction")
        button.clicked.connect(self.saveTransaction)
        self.formLayout.addRow(button)
        self.subtransactionFrame.setLayout(self.formLayout)
        self.layout.addWidget(self.subtransactionFrame)
        
    def addSubtransactionLabels(self):
        """ Add Subtransaction Labels """
        if self.transaction is not None and self.transaction.subtransaction_set is not None:
            for transaction in self.transaction.subtransaction_set.transactions:
                if transaction is not self.transaction:
                    label = QLabel("{0}".format(transaction.description))
                    self.subtransactionLabels.append(label)
                    self.formLayout.insertRow(1, label)
        
    def updateOnTransactionChange(self):
        """ Update on a Transaction Change """
        for label in self.subtransactionLabels:
            self.formLayout.removeWidget(label)
        self.addSubtransactionLabels()
        
    def tabSelected(self):
        """ Update the Account Tab when the tab is selected """
        text = self.accountComboBox.currentText()
        UpdateComboBoxWithAccounts(self.accountComboBox)
        index = self.accountComboBox.findText(text)
        if not (index == -1):
            self.accountComboBox.setCurrentIndex(index)
            
    def saveTransaction(self, checked=False):
        """ Save the current Transaction """
        transaction = Transaction(date=datetime.date.today())
        transaction.amount = GetCentsFromDollarString(self.amountEdit.text())
        transaction.description = self.descriptionEdit.text()
        
        if self.transaction is not None:
            subtransaction_set = self.transaction.subtransaction_set
            if subtransaction_set is None:
                subtransaction_set = SubTransaction()
                SubTransactions.save()
                self.transaction.subtransaction_set = subtransaction_set
                Transactions.add(self.transaction)
            
        transaction.subtransaction_set = subtransaction_set
        account = Accounts.all()[self.accountComboBox.currentIndex()]
        transaction.account = account
        Transactions.add(transaction)
        
        TheBalanceHelper.setupBalancesForAccount(transaction.account)
        #self.table_view.insertRow(transaction)
        
    
    @property
    def layout(self):
        return self.parent.layout
        
    @property
    def transaction(self):
        return self.parent.transaction