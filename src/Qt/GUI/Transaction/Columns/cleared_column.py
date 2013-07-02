from Qt.GUI.Transaction.Columns.cleared_checkbox import ClearedCheckbox

class ClearedColumn:
    """ Represents the Cleared Column """
    HEADER = "Cleared"
    
    def getItemForColumn(self, transaction):
        """  """
        return None
    
    def getWidgetForColumn(self, transaction):
        """  """
        return ClearedCheckbox(transaction) 