from PySide import QtGui, QtCore
from Qt.Model.Transaction.category_column import CategoryColumn
from Qt.Model.Transaction.cleared_column import ClearedColumn
from Qt.Model.Transaction.reconciled_column import ReconciledColumn
from Qt.Model.Transaction.type_column import TypeColumn
from Qt.Model.Transaction.transaction_table_model import TransactionTableModel

from transaction_category_delegate import TransactionCategoryDelegate
from checkbox_delegate import CheckBoxDelegate
from transaction_type_delegate import TransactionTypeDelegate

class TransactionListView(QtGui.QTableView):
    """ View that lists all the Transactions """

    def __init__(self):
        """ Initialize the Transaction List View """
        QtGui.QTableView.__init__(self)
        self.table_model = TransactionTableModel()
        self.setModel(self.table_model)
        self.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)

        self.setTransactionTypeDelegate()
        self.setTransactionCategoryDelegate()
        self.setTransactionClearedDelegate()
        self.setTransactionReconciledDelegate()

    def setTransactionTypeDelegate(self):
        """ Set the Transaction Type Column View Delegate """
        self.typeDelegate = TransactionTypeDelegate()
        self.setDelegateForColumn(self.typeDelegate, TypeColumn)

    def setTransactionCategoryDelegate(self):
        """ Set the Transaction Category Column View Delegate """
        self.categoryDelegate = TransactionCategoryDelegate()
        self.setDelegateForColumn(self.categoryDelegate, CategoryColumn)

    def setTransactionClearedDelegate(self):
        """ Set the Transaction Cleared Column View Delegate """
        self.clearedDelegate = CheckBoxDelegate()
        self.setDelegateForColumn(self.clearedDelegate, ClearedColumn)
        
    def setTransactionReconciledDelegate(self):
        """ Set the Transaction Cleared Column View Delegate """
        self.reconciledDelegate = CheckBoxDelegate()
        self.setDelegateForColumn(self.reconciledDelegate, ReconciledColumn)
        
    def setDelegateForColumn(self, delegate, columnClass):
        """ Set the delegate for the column """
        index = self.table_model.indexForColumnClass(columnClass)
        self.setItemDelegateForColumn(index, delegate)

    def tabSelected(self):
        """ Called when the tab is selected """