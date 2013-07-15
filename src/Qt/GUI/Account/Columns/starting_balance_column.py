from Qt.GUI.Account.TableWidgets.starting_balance_table_item import StartingBalanceTableItem

class StartingBalanceColumn:
    """ Represents the Starting Balance Column """
    HEADER = "Starting Balance"
    
    def __init__(self, transactionTable):
        """ Initialize the Starting Balance Column """
        self.transactionTable = transactionTable
    
    def getItemForColumn(self, account):
        """  """
        return StartingBalanceTableItem(account, self.transactionTable)
    
    def getWidgetForColumn(self, account):
        """  """
        return None 