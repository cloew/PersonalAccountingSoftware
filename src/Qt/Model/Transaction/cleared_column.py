from Qt.Model.Transaction.transaction_column import TransactionColumn

class ClearedColumn(TransactionColumn):
    """ Represents the Transaction Cleared Column """
    header_name = "Cleared"

    def getDataForTransaction(self, transaction):
        """ Return data for the provided transaction """
        if transaction.cleared is not None:
            return str(transaction.cleared)

    def setDataForTransaction(self, transaction, value):
        """ Set data for the provided transaction """
        if value:
            transaction.cleared = True
        else:
            transaction.cleared = False
        return True

    def getTip(self, row):
        """ Return the Status/Tool Tip for the given row """
        return "Whether the transaction has cleared the bank."