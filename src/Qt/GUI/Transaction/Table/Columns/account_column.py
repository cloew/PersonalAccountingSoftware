from Qt.GUI.Core.kao_table_column import KaoTableColumn
from Qt.GUI.Transaction.Table.Columns.Delegates.transaction_account_delegate import TransactionAccountDelegate
from Qt.GUI.Transaction.Table.TableWidgets.account_table_item import AccountTableItem

class AccountColumn(KaoTableColumn):
    """ Represents the Account Column """
    DELEGATE_CLASS = TransactionAccountDelegate
    HEADER = "Account"
    
    def __init__(self, callbacks=None):
        """ Initialize the account column """
        KaoTableColumn.__init__(self, callbacks=callbacks)
    
    def getItemForColumn(self, transaction):
        """  """
        return AccountTableItem(transaction)
    
    def getWidgetForColumn(self, transaction):
        """  """
        return None 