from decimal import Decimal, InvalidOperation
#from PySide.QtCore import QVariant
from Qt.Model.Transaction.transaction_column import TransactionColumn

class AmountColumn(TransactionColumn):
    """ Represents the Transaction Amount Column """
    header_name = "Amount"

    def getDataForTransaction(self, transaction):
        """ Return data for the provided transaction """
        if transaction.amount is not None:
            amount = transaction.amount
            cents = amount%100
            dollars = amount/100
            #return QVariant("${0}.{1:{fill}2}".format(dollars, cents, fill=0))
            return "${0}.{1:{fill}2}".format(dollars, cents, fill=0)

    def setDataForTransaction(self, transaction, value):
        """ Set data for the provided transaction """
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