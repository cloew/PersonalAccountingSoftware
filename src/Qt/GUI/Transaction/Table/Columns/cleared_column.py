from Qt.GUI.Core.qt_helper import GetCenteredWidgetForTableCell
from Qt.GUI.Transaction.Table.TableWidgets.cleared_checkbox import ClearedCheckbox

class ClearedColumn:
    """ Represents the Cleared Column """
    HEADER = "Cleared"
    
    def __init__(self, table):
        """ Initialize the Cleared Column """
        self.table = table
    
    def getItemForColumn(self, transaction):
        """  """
        return None
    
    def getWidgetForColumn(self, transaction):
        """  """
        return GetCenteredWidgetForTableCell(ClearedCheckbox(transaction, self.table))