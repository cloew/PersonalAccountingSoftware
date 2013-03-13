from Qt.Model.Transaction.transaction_column import TransactionColumn

class TypeColumn(TransactionColumn):
    """ Represents the Transaction Type Column """
    header_name = "Type"

    def getDataForTransaction(self, transaction):
        """ Return data for the provided transaction """
        if transaction.income is True:
            return "Income"
        elif transaction.income is False:
            return "Expense"

    def setDataForTransaction(self, transaction, value):
        """ Set data for the provided transaction """
        if "income".startswith(value.lower()):
            transaction.income = True
            return True
        elif "expense".startswith(value.lower()):
            transaction.income = False
            return True

    def getTip(self, row):
        """ Return the Status/Tool Tip for the given row """
        return "The Transaction type (Income/Expense)."