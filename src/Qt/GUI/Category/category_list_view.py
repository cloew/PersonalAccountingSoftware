from PyQt4 import QtGui, QtCore

class CategoryListView(QtGui.QTableView): # This will probably really inherit from something else
    """ View that lists all the Categories """

    def __init__(self):
        """ Initialize the Transaction List View """
        QtGui.QWidget.__init__(self)
        # self.table_model = TransactionTableModel()
        # self.setModel(self.table_model)
        # self.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)

        # self.setTransactionTypeDelegate()
        # self.setTransactionCategoryDelegate()