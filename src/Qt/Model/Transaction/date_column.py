from dateutil import parser
from Qt.Model.Transaction.transaction_column import TransactionColumn

class DateColumn(TransactionColumn):
    """ Represents the Transaction Date Column """
    header_name = "Date"

    def getDataForTransaction(self, transaction):
        """ Return data for the provided transaction """
        if transaction.date is not None:
            return "{0:%m/%d/%Y}".format(transaction.date)

    def setDataForTransaction(self, transaction, value):
        """ Set data for the provided transaction """
        try:
            transaction.date = parser.parse(str(value.toString()))
            return True
        except ValueError:
            pass # Expect it to happen if user enters a bad String for the date

    def getTip(self, row):
        """ Return the Status/Tool Tip for the given row """
        return "The Date the Transaction occured."