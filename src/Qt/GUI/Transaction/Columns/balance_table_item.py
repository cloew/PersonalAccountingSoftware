from db.transactions import Transactions
from ORM.transaction import Transaction
from Utilities.dollar_amount_helper import GetDollarString, GetCentsFromDollarString

from decimal import InvalidOperation

from PySide.QtCore import Qt
from PySide.QtGui import QTableWidgetItem

class BalanceTableItem(QTableWidgetItem):
    """ Represents a Table Widget Item for a Transaction Balance """
    
    def __init__(self, transaction):
        """ Initialize the Amount Item """
        self.transaction = transaction
        QTableWidgetItem.__init__(self, self.getData())
        
    def getData(self):
        """ Return the balance for the current transaction """
        transactions = Transactions.allForAccount(self.transaction.account, order=Transaction.date)
        balance = self.transaction.account.starting_balance
        for loopTransaction in transactions:
            if loopTransaction.amount is not None:
                if loopTransaction.income:
                    balance += loopTransaction.amount
                else:
                    balance -= loopTransaction.amount
            if self.transaction is loopTransaction:
                break
        
        return GetDollarString(balance)