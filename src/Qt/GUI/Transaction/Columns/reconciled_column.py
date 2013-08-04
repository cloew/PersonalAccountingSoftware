from Qt.GUI.Core.qt_helper import GetCenteredWidgetForTableCell
from Qt.GUI.Transaction.TableWidgets.reconciled_checkbox import ReconciledCheckbox

class ReconciledColumn:
    """ Represents the Reconciled Column """
    HEADER = "Reconciled"
    
    def __init__(self, table):
        """ Initialize the Reconciled Column """
        self.table = table
    
    def getItemForColumn(self, transaction):
        """  """
        return None
    
    def getWidgetForColumn(self, transaction):
        """  """
        return GetCenteredWidgetForTableCell(ReconciledCheckbox(transaction, self.table))