from PyQt4 import QtGui, QtCore
from Qt.Model.category_column import CategoryColumn
from Qt.Model.type_column import TypeColumn
from Qt.Model.transaction_table_model import TransactionTableModel

from transaction_category_delegate import TransactionCategoryDelegate
from transaction_type_delegate import TransactionTypeDelegate

class TransactionListView(QtGui.QTableView): # This will probably really inherit from something else
    """ View that lists all the Transactions """

    def __init__(self):
        """ Initialize the Transaction List View """
        QtGui.QWidget.__init__(self)
        self.table_model = TransactionTableModel()
        self.setModel(self.table_model)
        self.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)

        self.setTransactionTypeDelegate()
        self.setTransactionCategoryDelegate()

    def setTransactionTypeDelegate(self):
        """ Set the Transaction Type Column View Delegate """
        index = self.table_model.indexForColumnClass(TypeColumn)
        self.setItemDelegateForColumn(index, TransactionTypeDelegate())

    def setTransactionCategoryDelegate(self):
        """ Set the Transaction Category Column View Delegate """
        index = self.table_model.indexForColumnClass(CategoryColumn)
        self.setItemDelegateForColumn(index, TransactionCategoryDelegate())
        print self.itemDelegateForColumn(index)