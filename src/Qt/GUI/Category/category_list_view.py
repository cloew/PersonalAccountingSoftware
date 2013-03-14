from delete_category_delegate import DeleteCategoryDelegate

from PySide import QtGui, QtCore
from Qt.Model.Category.category_table_model import CategoryTableModel
from Qt.Model.Category.delete_column import DeleteColumn

class CategoryListView(QtGui.QTableView): # This will probably really inherit from something else
    """ View that lists all the Categories """

    def __init__(self):
        """ Initialize the Transaction List View """
        QtGui.QTableView.__init__(self)
        self.table_model = CategoryTableModel()
        self.setModel(self.table_model)
        self.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)

        self.setDeleteDelegate()

    def setDeleteDelegate(self):
        """ Set Delegate for the delete column """
        self.deleteDelegate = DeleteCategoryDelegate()
        self.setDelegateForColumn(self.deleteDelegate, DeleteColumn)

    def setDelegateForColumn(self, delegate, columnClass):
        """ Set the delegate for the column """
        index = self.table_model.indexForColumnClass(columnClass)
        self.setItemDelegateForColumn(index, delegate)

    def tabSelected(self):
        """ Called when the tab is selected """