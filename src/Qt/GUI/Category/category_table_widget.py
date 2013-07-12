from db.categories import Categories

from Qt.GUI.Core.kao_table_widget import KaoTableWidget
from Qt.GUI.Category.Columns.name_column import NameColumn

class CategoryTableWidget(KaoTableWidget):
    """ The Category Table Widget View """
    
    def __init__(self):
        """ Initalize the Category Table """
        categories = Categories.all()
        columns = [NameColumn()]
        KaoTableWidget.__init__(self, categories, columns)
        
    def tabSelected(self):
        """ Do Nothing when this tab is selected """