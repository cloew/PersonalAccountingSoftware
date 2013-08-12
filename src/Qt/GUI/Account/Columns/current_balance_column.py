from Qt.GUI.Account.TableWidgets.current_balance_table_item import CurrentBalanceTableItem

class CurrentBalanceColumn:
    """ Represents the Current Balance Column """
    HEADER = "Current Balance"
    
    def __init__(self, transactionTable):
        """ Initialize the Current Balance Column """
        self.transactionTable = transactionTable
    
    def getItemForColumn(self, account):
        """  """
        return CurrentBalanceTableItem(account, self.transactionTable)
    
    def getWidgetForColumn(self, account):
        """  """
        return None 