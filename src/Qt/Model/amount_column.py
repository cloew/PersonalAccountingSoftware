from decimal import Decimal, InvalidOperation
from PyQt4.QtCore import QVariant
from Qt.Model.transaction_column import TransactionColumn

class AmountColumn(TransactionColumn):
    """ Represents the Transaction Amount Column """
    header_name = "Amount"

    def getData(self, row):
        """ Return data for the provided row """
        transaction = self.getTransactionForRow(row)
        if transaction is not None and transaction.amount is not None:
            amount = transaction.amount
            cents = amount%100
            dollars = amount/100
            return QVariant("${0}.{1:{fill}2}".format(dollars, cents, fill=0))

    def setData(self, row, value):
        """ Set data for the provided row """
        transaction = self.getTransactionForRow(row)
        if transaction is not None:
            try:
                cleanedValue = str(value.toString())
                if cleanedValue.startswith('$'):
                    cleanedValue = cleanedValue[1:]
                newAmount = Decimal(cleanedValue)
                transaction.amount = int(newAmount*100)
                return True
            except InvalidOperation:
                pass # The cast from the string to a Decimal

    def getTip(self, row):
        """ Return the Status/Tool Tip for the given row """
        return "The amount of money in the transaction."