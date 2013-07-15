from Qt.GUI.Core.qt_helper import GetCenteredWidgetForTableCell
from Qt.GUI.Category.TableWidgets.delete_button import DeleteButton

class DeleteColumn:
    """ Represents the Delete Column """
    HEADER = ""
    
    def __init__(self, table):
        """ Initialize the Delete Column """
        self.table = table
    
    def getItemForColumn(self, category):
        """  """
        return None
    
    def getWidgetForColumn(self, category):
        """  """
        return GetCenteredWidgetForTableCell(DeleteButton(category, self.table))