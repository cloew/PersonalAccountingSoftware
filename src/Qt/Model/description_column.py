from PyQt4.QtCore import QVariant
from Qt.Model.transaction_column import TransactionColumn

class DescriptionColumn(TransactionColumn):
    """ Represents the Transaction Description Column """
    header_name = "Description"

    def getDataForTransaction(self, transaction):
        """ Return data for the provided transaction """
        return QVariant(transaction.description)

    def setDataForTransaction(self, transaction, value):
        """ Set data for the provided transaction """
        transaction.description = str(value.toString())
        return True

    def getTip(self, row):
        """ Return the Status/Tool Tip for the given row """
        return "Description of the transaction."