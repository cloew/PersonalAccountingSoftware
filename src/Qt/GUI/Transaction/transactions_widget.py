from Qt.GUI.Transaction.Table.transaction_table_widget import TransactionTableWidget
from Qt.GUI.Transaction.Menu.transaction_menu_widget import TransactionMenuWidget

from PySide.QtCore import Qt
from PySide.QtGui import QHBoxLayout, QFrame, QWidget

class TransactionsWidget(QFrame):
    """ Represents the Widget that holds the Transaction table and menu """
    
    def __init__(self, parent):
        """ Initialize the Transactions Widget """
        QFrame.__init__(self)
        
        self.transactionTableWidget = TransactionTableWidget()
        self.transactionMenuWidget = TransactionMenuWidget(self)
        
        self.transactionMenuWidget.setMinimumSize(400, 800)
        self.transactionTableWidget.setMaximumSize(1200, 800)
        
        layout = QHBoxLayout(self)
        layout.addWidget(self.transactionTableWidget)
        layout.addWidget(self.transactionMenuWidget)
        self.setLayout(layout)
        
        
        
    def setToolbar(self, toolbar):
        """ Set the  toolbar for the widget """
        self.toolbar = toolbar
        self.transactionTableWidget.toolbar = toolbar
        
    def tabSelected(self):
        """ Do Nothing when this tab is selected """