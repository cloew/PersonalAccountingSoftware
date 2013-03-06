from Qt.Model.transaction_column import TransactionColumn

class TypeColumn(TransactionColumn):
    """ Represents the Transaction Type Column """
    header_name = "Type"

    def getData(self, row):
        """ Return data for the provided row """
        transaction = self.getTransactionForRow(index)
        if transaction is not None:
            if transaction.income is True:
                return QVariant("Income")
            elif transaction.income is False:
                return QVariant("Expense")

    def setData(self, row, value):
        """ Set data for the provided row """
        transaction = self.getTransactionForRow(index)
        if transaction is not None:
            newIncomeValue = str(value.toString())
            if "income".startswith(newIncomeValue.lower()):
                transaction.income = True
                return True
            elif "expense".startswith(newIncomeValue.lower()):
                transaction.income = False
                return True

    def getTip(self, row):
        """ Return the Status/Tool Tip for the given row """
        return "The Transaction type (Income/Expense)."