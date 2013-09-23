from Qt.GUI.Transaction.Table.transaction_table_widget import TransactionTableWidget
from Qt.GUI.Transaction.Menu.transaction_menu_widget import TransactionMenuWidget

from PySide.QtCore import Qt
from PySide.QtGui import QHBoxLayout, QFrame, QWidget

class TransactionsWidget(QFrame):
    """ Represents the Widget that holds the Transaction table and menu """
    
    def __init__(self, parent):
        """ Initialize the Transactions Widget """
        QFrame.__init__(self)
        self.parentWidget = parent
        self.transactionMenuWidget = TransactionMenuWidget(self)
        self.transactionTableWidget = TransactionTableWidget(self.transactionMenuWidget)
            
        self.setPieceSizes()
        
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
    
    def resizeEvent(self, resizeEvent):
        """ Called when window is resized """
        self.setPieceSizes()
        
    def setPieceSizes(self):
        """ Set the Piece Sizes """
        size = self.parentWidget.size()
        height = size.height()-100
        smallWidth = size.width()/4
        largeWidth = size.width() - smallWidth
        self.transactionMenuWidget.setMaximumSize(smallWidth, height)
        self.transactionTableWidget.setMaximumSize(largeWidth, height)