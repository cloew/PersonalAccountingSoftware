from db.accounts import Accounts
from db.transactions import Transactions

from PySide.QtGui import QTableWidget, QTableWidgetItem

class TransactionTableWidget(QTableWidget):
    """ The Transaction Tabel Widget View """
    
    def __init__(self):
        """ Initialize the Transaction Table Widget """
        self.account = Accounts.all()[0]
        transactions = Transactions.all()
        columns = ["Amount", "Description", "Type", "Category", "Date", "Balance", "Cleared", "Reconciled"]
        QTableWidget.__init__(self, len(transactions), len(columns))
        
        self.setHorizontalHeaderLabels(columns)
        self.verticalHeader().hide()
        
        for row in range(len(transactions)):
            for column in range(len(columns)):
                item = QTableWidgetItem(str(row*len(columns)+column))
                self.setItem(row, column, item)
        