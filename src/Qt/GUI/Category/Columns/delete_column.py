from Qt.GUI.Core.kao_table_column import KaoTableColumn
from Qt.GUI.Core.qt_helper import GetCenteredWidgetForTableCell
from Qt.GUI.Category.TableWidgets.delete_button import DeleteButton

class DeleteColumn(KaoTableColumn):
    """ Represents the Delete Column """
    HEADER = ""
    
    def __init__(self, table):
        """ Initialize the Delete Column """
        self.table = table
        KaoTableColumn.__init__(self)
    
    def getItemForColumn(self, category):
        """  """
        return None
    
    def getWidgetForColumn(self, category):
        """  """
        return GetCenteredWidgetForTableCell(DeleteButton(category, self.table))