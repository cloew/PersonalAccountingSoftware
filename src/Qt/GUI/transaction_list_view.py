from PyQt4 import QtGui
from Qt.Model.transaction_table_model import TransactionTableModel

class TransactionListView(QtGui.QTableView): # This will probably really inherit from something else
    """ View that lists all the Transactions """

    def __init__(self):
        """ Initialize the Transaction List View """
        QtGui.QWidget.__init__(self)
        self.model = TransactionTableModel()
        self.setModel(self.model)
        self.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)