from db.categories import Categories
from ORM.category import Category
from PySide.QtGui import QAction
from Qt.GUI.tab_toolbar import TabToolBar

class CategoryToolBar(TabToolBar):
    """ Represents the Category Tool Bar """

    def addToolBarButtons(self):
        """ Add Tool Bar Buttons """
        self.addNewCategoryButton()

    def addNewCategoryButton(self):
        """ Adds the New Category Button to the ToolBar """
        newIcon = self.getQIcon('money.png')
        newCategoryAction = QAction(newIcon, 'New Category', self)
        newCategoryAction.setShortcut('Ctrl+N')
        newCategoryAction.setStatusTip("Create a New Category.")
        newCategoryAction.triggered.connect(self.newCategory)
        
        self.addAction(newCategoryAction)

    def newCategory(self):
        """ Creates a New Category """
        category = Category()
        Categories.add(category)
        self.addEntryToTable()