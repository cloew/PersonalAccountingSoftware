from Qt.GUI.Transaction.transaction_table_widget import TransactionTableWidget

from PySide.QtGui import QHBoxLayout, QWidget

class TransactionsWidget(QWidget):
    """ Represents the Widget that holds the Transaction table and menu """
    
    def __init__(self):
        """ Initialize the Transactions Widget """
        QWidget.__init__(self)
        self.transactionTableWidget = TransactionTableWidget()
        layout = QHBoxLayout()
        layout.addWidget(self.transactionTableWidget)
        self.setLayout(layout)
        
    def setToolbar(self, toolbar):
        """ Set the  toolbar for the widget """
        self.toolbar = toolbar
        self.transactionTableWidget.toolbar = toolbar
        
    def tabSelected(self):
        """ Do Nothing when this tab is selected """