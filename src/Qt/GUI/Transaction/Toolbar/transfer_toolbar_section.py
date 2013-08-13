from db.accounts import Accounts
from db.transactions import Transactions
from Qt.GUI.Utilities.account_combobox_helper import UpdateComboBoxWithAccounts
from Utilities.balance_helper import TheBalanceHelper

from PySide.QtGui import QAction, QComboBox, QLabel

class TransferToolbarSection:
    """ The Transfer Toolbar section """
    
    def __init__(self, toolbar, table_view):
        """ Initialize the Transfer Toolbar Section """
        self.toolbar = toolbar
        self.table_view = table_view
        
    def addTransfers(self):
        """ Add the transfer widgets """
        if len(self.toolbar.transaction.transferAccounts) == 0:
            self.buildNewTransferSection()
        else:
            self.buildExistingTransferSection()
        
    def buildNewTransferSection(self):
        """ Build a new Transfer Section """
        self.transferLabel = QLabel("Transfer {0}: ".format(self.getTransferDirection()), self.toolbar)
        self.toolbar.addWidget(self.transferLabel)
        self.transferComboBox = QComboBox(self.toolbar)
        UpdateComboBoxWithAccounts(self.transferComboBox, ignoreCurrent=True, table_view=self.table_view)
        self.transferComboBox.activated.connect(self.setTransfer)
        self.toolbar.addWidget(self.transferComboBox)
        
    def buildExistingTransferSection(self):
        """ Build existing Transfer Section """
        if self.toolbar.transaction.account is self.table_view.account:
            self.transferLabel = QLabel("Transferred {0}: {1}".format(self.getTransferDirection(), self.toolbar.transaction.transferAccounts[0].name), self.toolbar)
        else:
            self.transferLabel = QLabel("Transferred {0}: {1}".format(self.getTransferDirection(), self.toolbar.transaction.account.name), self.toolbar)
        self.toolbar.addWidget(self.transferLabel)
        eraseIcon = self.toolbar.getQIcon('erase.png')
        removeTransferAction = QAction(eraseIcon, 'Remove Transfer', self.toolbar)
        removeTransferAction.setStatusTip("Remove Transfer.")
        removeTransferAction.triggered.connect(self.removeTransfer)
        self.toolbar.addAction(removeTransferAction)
            
    def getTransferDirection(self):
        """ Return the Transfer Direction word """
        if self.toolbar.transaction.isIncome(self.table_view.account):
            return "from"
        else:
            return "to"
        
    def setTransfer(self, index):
        """ Set the Transaction Account to view """
        text = self.transferComboBox.itemText(index)
        account = Accounts.accountWithName(text)
        if len(self.toolbar.transaction.transferAccounts) == 0:
            self.toolbar.transaction.transferAccounts.append(account)
            Transactions.save()
            TheBalanceHelper.setupBalancesForAccount(account)
            TheBalanceHelper.setupBalancesForAccount(self.toolbar.transaction.account)
            self.toolbar.buildToolbarWidgets()
            
    def removeTransfer(self):
        """ Remove the Transfer """
        self.toolbar.transaction.transferAccounts = []
        Transactions.save()
        self.toolbar.buildToolbarWidgets()
        self.table_view.updateTransactions()