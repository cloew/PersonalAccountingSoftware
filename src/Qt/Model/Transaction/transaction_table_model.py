from amount_column import AmountColumn
from category_column import CategoryColumn
from cleared_column import ClearedColumn
from date_column import DateColumn
from description_column import DescriptionColumn
from reconciled_column import ReconciledColumn
from type_column import TypeColumn

from db.transactions import Transactions
from Qt.Model.table_model import TableModel

class TransactionTableModel(TableModel):
    """ Reprsents the Transaction List as a Table """
    transaction_retrievers = {"All":Transactions.all}
    default_retriever = transaction_retrievers["All"]

    def __init__(self):
        """ Initialize the Table Model """
        self.retriever = self.default_retriever
        TableModel.__init__(self)

    def getColumns(self):
        """ Get the Columns for the table """
        return [AmountColumn(self.retriever),
                DescriptionColumn(self.retriever),
                TypeColumn(self.retriever),
                CategoryColumn(self.retriever),
                DateColumn(self.retriever),
                ClearedColumn(self.retriever),
                ReconciledColumn(self.retriever)]

    def rowCount(self, parent):
        """ Returns the number of rows in the table """
        return len(self.retriever())

    def setTransactionRetriever(self, transactionFilter):
        """ Set the Transaction Retriever """
        if transactionFilter in self.transaction_retrievers:
            self.retriever = self.transaction_retrievers[transactionFilter]

            for column in self.columns:
                column.transactionRetriever = self.retriever