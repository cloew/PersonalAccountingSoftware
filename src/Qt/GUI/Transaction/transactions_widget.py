from Qt.GUI.Core.kao_widget_with_menu import KaoWidgetWithMenu
from Qt.GUI.Transaction.Table.transaction_account_table_widget import TransactionAccountTableWidget
from Qt.GUI.Transaction.Menu.transaction_menu_widget import TransactionMenuWidget

from PySide.QtGui import QHBoxLayout, QFrame, QWidget

class TransactionsWidget(KaoWidgetWithMenu):
    """ Represents the Widget that holds the Transaction table and menu """
    
    def setupWidgets(self):
        """ Setup the Transactions Widget """
        self.transactionMenuWidget = TransactionMenuWidget(self)
        self.transactionTableWidget = TransactionAccountTableWidget(self.transactionMenuWidget)
        self.transactionMenuWidget.table = self.transactionTableWidget
        return self.transactionTableWidget, self.transactionMenuWidget
        
    def setToolbar(self, toolbar):
        """ Set the  toolbar for the widget """
        self.toolbar = toolbar
        self.transactionTableWidget.toolbar = toolbar
        
    def tabSelected(self):
        """ Do Nothing when this tab is selected """
        self.transactionMenuWidget.tabSelected()