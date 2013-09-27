from Qt.GUI.Core.kao_table_column import KaoTableColumn
from Qt.GUI.Core.qt_helper import GetCenteredWidgetForTableCell
from Qt.GUI.Transaction.Table.TableWidgets.cleared_checkbox import ClearedCheckbox

class ClearedColumn(KaoTableColumn):
    """ Represents the Cleared Column """
    HEADER = "Cleared"
    
    def getItemForColumn(self, transaction):
        """  """
        return None
    
    def getWidgetForColumn(self, transaction):
        """  """
        return GetCenteredWidgetForTableCell(ClearedCheckbox(transaction))