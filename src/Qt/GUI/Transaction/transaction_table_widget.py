from db.accounts import Accounts
from db.transactions import Transactions

from PySide.QtGui import QTableWidget, QTableWidgetItem

class TransactionTableWidget(QTableWidget):
    """ The Transaction Tabel Widget View """
    
    def __init__(self):
        """ Initialize the Transaction Table Widget """
        self.account = Accounts.all()[0]
        self.columns = ["Amount", "Description", "Type", "Category", "Date", "Balance", "Cleared", "Reconciled"]
        transactions = Transactions.allForAccount(self.account)
        QTableWidget.__init__(self, len(transactions), len(self.columns))
        
        self.setHorizontalHeaderLabels(self.columns)
        self.verticalHeader().hide()
        
        self.populateTable(transactions)
        
    def populateTable(self, transactions):
        """ Load Transactions from the Database """
        for row in range(len(transactions)):
            for column in range(len(self.columns)):
                item = QTableWidgetItem(str(row*len(self.columns)+column))
                self.setItem(row, column, item)
        
        
    def tabSelected(self):
        """ Do Nothing when this tab is selected """