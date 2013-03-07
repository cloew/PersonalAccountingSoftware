from PyQt4.QtCore import QVariant
from Qt.Model.transaction_column import TransactionColumn

class CategoryColumn(TransactionColumn):
    """ Represents the Transaction Category Column """
    header_name = "Category"

    def getDataForTransaction(self, transaction):
        """ Return data for the provided transaction """
        if transaction.category is not None and transaction.category.name is not None:
            return QVariant(transaction.category.name)

    def setDataForTransaction(self, transaction, value):
        """ Set data for the provided transaction """
        #transaction.description = str(value.toString())
        #return True

    def getTip(self, row):
        """ Return the Status/Tool Tip for the given row """
        return "Category the transaction is associated with."