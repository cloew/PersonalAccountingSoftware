from db.accounts import Accounts
from db.transactions import Transactions
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
    
    def setup(self):
        """ Setup the Subtransactions for the Transaction Details """
        self.subtransactionFrame = QFrame()
        formLayout = QFormLayout(self.subtransactionFrame)
        
        label = QLabel()
        label.setText("<b>Subtransactions</b>")
        formLayout.addRow(label)
        self.accountComboBox = QComboBox()
        UpdateComboBoxWithAccounts(self.accountComboBox)
        formLayout.addRow("Account:", self.accountComboBox)
        self.amountEdit = QLineEdit()
        formLayout.addRow("Amount:", self.amountEdit)
        self.descriptionEdit = QLineEdit()
        formLayout.addRow("Description:", self.descriptionEdit)
        button = QPushButton("Add New Subtransaction")
        button.clicked.connect(self.saveTransaction)
        formLayout.addRow(button)
        self.subtransactionFrame.setLayout(formLayout)
        self.layout.addWidget(self.subtransactionFrame)
        
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