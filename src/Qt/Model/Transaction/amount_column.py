from decimal import InvalidOperation
from Qt.Model.Transaction.transaction_column import TransactionColumn
from Utilities.dollar_amount_helper import GetDollarString, GetCentsFromDollarString

class AmountColumn(TransactionColumn):
    """ Represents the Transaction Amount Column """
    header_name = "Amount"

    def getDataForTransaction(self, transaction):
        """ Return data for the provided transaction """
        if transaction.amount is not None:
            amount = transaction.amount
            return GetDollarString(transaction.amount)

    def setDataForTransaction(self, transaction, value):
        """ Set data for the provided transaction """
        try:
            transaction.amount = GetCentsFromDollarString(value)
            return True
        except InvalidOperation:
            pass # The cast from the string to a Decimal

    def getTip(self, row):
        """ Return the Status/Tool Tip for the given row """
        return "The amount of money in the transaction."