from db.accounts import Accounts
from db.transactions import Transactions

from Qt.GUI.Transaction.transaction_category_delegate import TransactionCategoryDelegate

from Qt.GUI.Transaction.Columns.amount_column import AmountColumn
from Qt.GUI.Transaction.Columns.category_column import CategoryColumn
from Qt.GUI.Transaction.Columns.cleared_column import ClearedColumn
from Qt.GUI.Transaction.Columns.date_column import DateColumn
from Qt.GUI.Transaction.Columns.description_column import DescriptionColumn

from PySide.QtGui import QTableWidget, QTableWidgetItem

class TransactionTableWidget(QTableWidget):
    """ The Transaction Tabel Widget View """
    
    def __init__(self):
        """ Initialize the Transaction Table Widget """
        self.account = Accounts.all()[0]
        self.columns = [AmountColumn(), DescriptionColumn(), CategoryColumn(), DateColumn(), ClearedColumn()] #"Amount", "Description", "Type", "Category", "Date", "Balance", "Cleared", "Reconciled"]
        transactions = Transactions.allForAccount(self.account)
        QTableWidget.__init__(self, len(transactions), len(self.columns))
        
        self.setHorizontalHeaderLabels([column.HEADER for column in self.columns])
        self.verticalHeader().hide()
        
        self.populateTable(transactions)
        self.setDelegateForColumn()
        
    def populateTable(self, transactions):
        """ Load Transactions from the Database """
        for row in range(len(transactions)):
            for column in range(len(self.columns)):
                transaction = transactions[row]
                columnPopulator = self.columns[column]
                
                widget = columnPopulator.getWidgetForColumn(transaction)
                item = columnPopulator.getItemForColumn(transaction)
                
                if widget is not None:
                    self.setCellWidget(row, column, widget)
                elif item is not None:
                    self.setItem(row, column, item)
                    
    def setDelegateForColumn(self):
        """  """
        self.categoryDelegate = TransactionCategoryDelegate()
        self.setItemDelegateForColumn(2, self.categoryDelegate)
        
    def tabSelected(self):
        """ Do Nothing when this tab is selected """