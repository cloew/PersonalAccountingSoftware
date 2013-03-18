from Qt.Model.Account.account_table_model import AccountTableModel
from PySide import QtGui, QtCore

class AccountListView(QtGui.QTableView):
    """ View that lists all the Accounts """

    def __init__(self):
        """ Initialize the Account List View """
        QtGui.QTableView.__init__(self)
        self.table_model = AccountTableModel()
        self.setModel(self.table_model)
        self.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)

    def tabSelected(self):
        """ Called when the tab is selected """