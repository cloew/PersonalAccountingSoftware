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
    """ Represnts the Transaction List as a Table """

    def getColumns(self):
        """ Get the Columns for the table """
        return [AmountColumn(),
                DescriptionColumn(),
                TypeColumn(),
                CategoryColumn(),
                DateColumn(),
                ClearedColumn(),
                ReconciledColumn()]

    def rowCount(self, parent):
        """ Returns the number of rows in the table """
        return len(Transactions.all())