from db.accounts import Accounts
from Qt.GUI.Utilities.account_combobox_helper import UpdateComboBoxWithAccounts

from PySide.QtGui import QComboBox, QLabel

class AccountToolbarSection:
    """ The Account Toolbar section """
    
    def __init__(self, toolbar, table_view):
        """ Initialize the Account Toolbar Section """
        self.toolbar = toolbar
        self.table_view = table_view
        
    def addAccount(self):
        """ Add Account Label and Combo Box to the UI """
        label = QLabel("Account: ", self.toolbar)
        self.toolbar.addWidget(label)
        
        self.accountComboBox = QComboBox(self.toolbar)
        UpdateComboBoxWithAccounts(self.accountComboBox)
        self.accountComboBox.activated.connect(self.setAccount)
        index = self.accountComboBox.findText(self.table_view.account.name)
        if not index == -1:
            self.accountComboBox.setCurrentIndex(index)
        self.toolbar.addWidget(self.accountComboBox)
        
    def setAccount(self, index):
        """ Set the Transaction Account to view """
        account = Accounts.all()[index]
        self.table_view.updateTransactions(account=account)
        self.toolbar.buildToolbarWidgets()
        
    def tabSelected(self):
        """ Update the Account Tab when the tab is selected """
        text = self.accountComboBox.currentText()
        UpdateComboBoxWithAccounts(self.accountComboBox)
        index = self.accountComboBox.findText(text)
        if not (index == -1):
            self.accountComboBox.setCurrentIndex(index)