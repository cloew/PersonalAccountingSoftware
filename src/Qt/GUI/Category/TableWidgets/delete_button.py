from db.categories import Categories

from PySide.QtGui import QIcon, QPushButton

import resources.resource_manager as resource_manager

class DeleteButton(QPushButton):
    """ Represents a Delete Button """
    
    def __init__(self, category, table, parentWidget):
        """ Initialize the Delete Button """
        self.category = category
        self.table = table
        self.parentWidget = parentWidget
        QPushButton.__init__(self, QIcon(resource_manager.GetResourceFilePath("erase.png")), "")
        self.clicked.connect(self.deleteCategory)
        
    def deleteCategory(self):
        """ Deletes the category for this button """
        Categories.delete(self.category)
        row = self.table.indexAt(self.parentWidget.pos()).row()
        self.table.removeRow(row)