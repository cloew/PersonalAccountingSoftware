from Qt.GUI.Core.qt_helper import GetCenteredWidgetForTableCell
from Qt.GUI.Transaction.TableWidgets.cleared_checkbox import ClearedCheckbox

class ClearedColumn:
    """ Represents the Cleared Column """
    HEADER = "Cleared"
    
    def getItemForColumn(self, transaction):
        """  """
        return None
    
    def getWidgetForColumn(self, transaction):
        """  """
        return GetCenteredWidgetForTableCell(ClearedCheckbox(transaction))