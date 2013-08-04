from db.transactions import Transactions

from PySide.QtGui import QAction

class NewTransferAction(QAction):
    """ Represents an action to switch a Transaction to a Transfer """
    
    def __init__(self, transaction, account,  widget):
        """ Initialize the New Transfer Action """
        QAction.__init__("Transfer to {0}".format(account.name), widget)
        self.account = account
        self.transaction = transaction
        
    def transfer(self):
        """ Mark the transaction as a transfer """
        if len(self.transaction.transferAccounts) == 0:
            self.transaction.transferAccounts.append(self.account)
            Transactions.save()