from dateutil import parser
from PyQt4.QtCore import QVariant
from Qt.Model.transaction_column import TransactionColumn

class DateColumn(TransactionColumn):
    """ Represents the Transaction Date Column """
    header_name = "Date"

    def getDataForTransaction(self, transaction):
        """ Return data for the provided transaction """
        return QVariant("{0:%m/%d/%Y}".format(transaction.date))

    def setData(self, row, value):
        """ Set data for the provided row """
        transaction = self.getTransactionForRow(row)
        if transaction is not None:
            transaction.date = parser.parse(str(value.toString()))
            return True

    def getTip(self, row):
        """ Return the Status/Tool Tip for the given row """
        return "The Date the Transaction occured."