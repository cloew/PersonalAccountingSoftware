from PySide import QtGui, QtCore
from Qt.Model.Category.category_table_model import CategoryTableModel

class CategoryListView(QtGui.QTableView): # This will probably really inherit from something else
    """ View that lists all the Categories """

    def __init__(self):
        """ Initialize the Transaction List View """
        QtGui.QTableView.__init__(self)
        self.table_model = CategoryTableModel()
        self.setModel(self.table_model)
        self.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)

    def tabSelected(self):
        """ Called when the tab is selected """