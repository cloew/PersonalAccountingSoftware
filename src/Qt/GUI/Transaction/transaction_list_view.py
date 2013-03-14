from PySide import QtGui, QtCore
from Qt.Model.Transaction.category_column import CategoryColumn
from Qt.Model.Transaction.cleared_column import ClearedColumn
from Qt.Model.Transaction.type_column import TypeColumn
from Qt.Model.Transaction.transaction_table_model import TransactionTableModel

from transaction_category_delegate import TransactionCategoryDelegate
from transaction_cleared_delegate import TransactionClearedDelegate
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

    def setTransactionTypeDelegate(self):
        """ Set the Transaction Type Column View Delegate """
        self.typeDelegate = TransactionTypeDelegate()
        index = self.table_model.indexForColumnClass(TypeColumn)
        self.setItemDelegateForColumn(index, self.typeDelegate)

    def setTransactionCategoryDelegate(self):
        """ Set the Transaction Category Column View Delegate """
        self.categoryDelegate = TransactionCategoryDelegate()
        index = self.table_model.indexForColumnClass(CategoryColumn)
        self.setItemDelegateForColumn(index, self.categoryDelegate)

    def setTransactionClearedDelegate(self):
        """ Set the Transaction Cleared Column View Delegate """
        self.clearedDelegate = TransactionClearedDelegate()
        index = self.table_model.indexForColumnClass(ClearedColumn)
        self.setItemDelegateForColumn(index, self.clearedDelegate)

    def tabSelected(self):
        """ Called when the tab is selected """