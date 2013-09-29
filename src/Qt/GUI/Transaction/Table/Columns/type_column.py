from Qt.GUI.Core.kao_table_column import KaoTableColumn
from Qt.GUI.Transaction.Table.transaction_type_delegate import TransactionTypeDelegate
from Qt.GUI.Transaction.Table.TableWidgets.type_table_item import TypeTableItem

class TypeColumn(KaoTableColumn):
    """ Represents the Type Column """
    DELEGATE_CLASS = TransactionTypeDelegate
    HEADER = "Type"
    
    def __init__(self, account=None, callbacks=None):
        """ Initialize the type column """
        self.account = account
        KaoTableColumn.__init__(self, callbacks=callbacks)
    
    def getItemForColumn(self, transaction):
        """  """
        return TypeTableItem(transaction, self.account)
    
    def getWidgetForColumn(self, transaction):
        """  """
        return None 