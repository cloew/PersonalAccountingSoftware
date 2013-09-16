from Qt.GUI.Account.TableWidgets.initial_balance_table_item import InitialBalanceTableItem

class InitialBalanceColumn:
    """ Represents the Initial Balance Column """
    HEADER = "Initial Balance"
    
    def __init__(self, transactionTable):
        """ Initialize the Starting Balance Column """
        self.transactionTable = transactionTable
    
    def getItemForColumn(self, account):
        """  """
        return InitialBalanceTableItem(account, self.transactionTable)
    
    def getWidgetForColumn(self, account):
        """  """
        return None 