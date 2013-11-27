from Qt.GUI.Core.kao_table_column import KaoTableColumn
from Qt.GUI.Core.qt_helper import GetCenteredWidgetForTableCell
from Qt.GUI.Transaction.Table.TableWidgets.remove_subtransaction_button import RemoveSubtransactionButton

class RemoveSubtransactionColumn(KaoTableColumn):
    """ Represents the Remove Subtransaction Column """
    HEADER = ""
    
    def __init__(self, table):
        """ Initialize the Remove Subtransaction Column """
        self.table = table
        KaoTableColumn.__init__(self)
    
    def getItemForColumn(self, transaction):
        """  """
        return None
    
    def getWidgetForColumn(self, transaction):
        """  """
        return GetCenteredWidgetForTableCell(RemoveSubtransactionButton(transaction, self.table))