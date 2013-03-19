from decimal import Decimal, InvalidOperation
from db.transactions import Transactions
from ORM.transaction import Transaction
from PySide.QtCore import Qt
from Qt.Model.Transaction.transaction_column import TransactionColumn

class BalanceColumn(TransactionColumn):
    """ Represents the Transaction Balance Column """
    header_name = "Current Blanace"
    
    def flags(self, row):
        """ Return flags for the Column's Row """
        return Qt.ItemIsEnabled

    def getDataForTransaction(self, transaction):
        """ Return data for the provided transaction """
        transactions = Transactions.all(order=Transaction.date)
        balance = transaction.account.starting_balance
        for loopTransaction in transactions:
            if loopTransaction.amount is not None:
                if loopTransaction.income:
                    balance += loopTransaction.amount
                else:
                    balance -= loopTransaction.amount
            if transaction is loopTransaction:
                break
        
        cents = balance%100
        dollars = balance/100
        return "${0}.{1:{fill}2}".format(dollars, cents, fill=0)

    def setDataForTransaction(self, transaction, value):
        """ Set data for the provided transaction """
        return False # Cannot set data in this column

    def getTip(self, row):
        """ Return the Status/Tool Tip for the given row """
        return "The Current Bank Account Balance after this Transaction."