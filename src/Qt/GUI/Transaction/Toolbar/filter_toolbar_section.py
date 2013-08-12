from ORM.transaction import Transaction
from PySide.QtGui import QComboBox, QLabel

__all__ = "All"
__uncleared__ = "Uncleared"
__unreconciled__ = "Unreconciled"

__filter_order__ = [__all__, 
                    __uncleared__,
                    __unreconciled__]
__transaction_filters__ = {__all__:{},
                           __uncleared__:{Transaction.cleared:[False, None]},
                           __unreconciled__:{Transaction.reconciled:[False, None]}}

class FilterToolbarSection:
    """ The Filter Toolbar section """
    
    def __init__(self, toolbar, table_view):
        """ Initialize the Filter Toolbar Section """
        self.toolbar = toolbar
        self.table_view = table_view
        
    def addFilter(self):
        """ Add Filter Label and Combo Box to the UI """
        label = QLabel("Filter: ", self.toolbar)
        self.toolbar.addWidget(label)
        comboBox = QComboBox(self.toolbar)
        comboBox.addItems(__filter_order__)
        comboBox.activated.connect(self.setTransactionFilter)
        index = [__transaction_filters__[filterText] for filterText in __filter_order__].index(self.table_view.filters)
        comboBox.setCurrentIndex(index)
        self.toolbar.addWidget(comboBox)
        
    def setTransactionFilter(self, index):
        """ Set the Transaction Filter """
        text = __filter_order__[index]
        
        if text in __transaction_filters__:
            self.table_view.updateTransactions(filters=__transaction_filters__[text])