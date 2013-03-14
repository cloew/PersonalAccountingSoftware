from PySide.QtCore import Qt
from Qt.Model.Transaction.transaction_column import TransactionColumn

class ReconciledColumn(TransactionColumn):
    """ Represents the Transaction Reconciled Column """
    header_name = "Reconciled"

    def flags(self, row):
        """ Return flags for the Column's Row """
        return Qt.ItemIsEnabled

    def getDataForTransaction(self, transaction):
        """ Return data for the provided transaction """
        if transaction.reconciled is not None:
            return transaction.reconciled

    def setDataForTransaction(self, transaction, value):
        """ Set data for the provided transaction """
        if value:
            transaction.reconciled = True
        else:
            transaction.reconciled = False
        return True

    def getTip(self, row):
        """ Return the Status/Tool Tip for the given row """
        return "Whether the transaction has been reconciled with a bank statement."