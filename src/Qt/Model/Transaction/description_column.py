from Qt.Model.Transaction.transaction_column import TransactionColumn

class DescriptionColumn(TransactionColumn):
    """ Represents the Transaction Description Column """
    header_name = "Description"

    def getDataForTransaction(self, transaction):
        """ Return data for the provided transaction """
        if transaction.description is not None:
            return transaction.description

    def setDataForTransaction(self, transaction, value):
        """ Set data for the provided transaction """
        transaction.description = value
        return True

    def getTip(self, row):
        """ Return the Status/Tool Tip for the given row """
        return "Description of the transaction."