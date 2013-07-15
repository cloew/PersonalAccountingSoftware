from db.categories import Categories

from PySide.QtGui import QIcon, QPushButton

import resources.resource_manager as resource_manager

class DeleteButton(QPushButton):
    """ Represents a Delete Button """
    
    def __init__(self, category, table):
        """ Initialize the Delete Button """
        self.category = category
        self.table = table
        QPushButton.__init__(self, QIcon(resource_manager.GetResourceFilePath("erase.png")), "")
        self.clicked.connect(self.deleteCategory)
        
    def deleteCategory(self):
        """ Deletes the category for this button """
        Categories.delete(self.category)
        row = self.table.indexAt(self.pos()).row()
        self.table.removeRow(row)