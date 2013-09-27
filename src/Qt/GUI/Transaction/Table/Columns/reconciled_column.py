from Qt.GUI.Core.kao_table_column import KaoTableColumn
from Qt.GUI.Core.qt_helper import GetCenteredWidgetForTableCell
from Qt.GUI.Transaction.Table.TableWidgets.reconciled_checkbox import ReconciledCheckbox

class ReconciledColumn(KaoTableColumn):
    """ Represents the Reconciled Column """
    HEADER = "Reconciled"
    
    def getItemForColumn(self, transaction):
        """  """
        return None
    
    def getWidgetForColumn(self, transaction):
        """  """
        return GetCenteredWidgetForTableCell(ReconciledCheckbox(transaction))