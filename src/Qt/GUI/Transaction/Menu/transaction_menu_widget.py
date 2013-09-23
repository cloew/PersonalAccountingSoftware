from db.accounts import Accounts
from db.transactions import Transactions
from ORM.transaction import Transaction
from Qt.GUI.Utilities.account_combobox_helper import UpdateComboBoxWithAccounts
from Utilities.balance_helper import TheBalanceHelper

from PySide.QtGui import QComboBox, QFormLayout, QFrame, QLabel, QLineEdit, QPushButton, QVBoxLayout

import datetime

class TransactionMenuWidget(QFrame):
    """ Represents Transaction Menu Widget """
    
    def __init__(self, parent=None):
        """ Initialize the Transaction Menu Widget """
        QFrame.__init__(self, parent=parent)
        
        self.transaction = None
        
        self.setFrameShape(QFrame.Panel)
        self.layout = QVBoxLayout(self)
        self.setupHeader()
        self.setupMenuBody()
        self.layout.addStretch()
        
    def setupHeader(self):
        header = QLabel()
        header.setText("<b>Transaction Details</b>")
        font = header.font()
        font.setPointSize(16)
        header.setFont(font)
        self.layout.addWidget(header)
        
        self.transactionLabel = QLabel()
        self.setTransactionLabelText()
        self.layout.addWidget(self.transactionLabel)
    
    def setupMenuBody(self):
        """ Setup the Body of the Menu """
        self.setupSubtransactions()
        
    def setupSubtransactions(self):
        """ Setup the Subtransactions for the Transaction Details """
        self.subtransactionFrame = QFrame()
        formLayout = QFormLayout(self.subtransactionFrame)
        
        label = QLabel()
        label.setText("<b>Subtransactions</b>")
        formLayout.addRow(label)
        self.accountComboBox = QComboBox()
        UpdateComboBoxWithAccounts(self.accountComboBox)
        formLayout.addRow("Account:", self.accountComboBox)
        formLayout.addRow("Amount:", QLineEdit())
        button = QPushButton()
        button.clicked.connect(self.saveTransaction)
        formLayout.addRow(button)
        self.subtransactionFrame.setLayout(formLayout)
        self.layout.addWidget(self.subtransactionFrame)
        
    def updateOnTransactionChange(self, currentTransaction):
        """ Update menu contents when the current transaction changes Transaction Change """
        self.transaction = currentTransaction
        self.setTransactionLabelText()
        
    def setTransactionLabelText(self):
        """ Set the Transaction label Text """
        if self.transaction is not None:
            self.transactionLabel.setText("<b>{0}</b>".format(self.transaction.description))
            
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
        account = Accounts.all()[self.accountComboBox.currentIndex()]
        transaction.account = account
        Transactions.add(transaction)
        TheBalanceHelper.setupBalancesForAccount(transaction.account)
        #self.table_view.insertRow(transaction)
        