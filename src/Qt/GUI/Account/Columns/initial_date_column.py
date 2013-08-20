from Qt.GUI.Account.TableWidgets.initial_date_table_item import InitialDateTableItem

class InitialDateColumn:
    """ Represents the Initial Date Column """
    HEADER = "as of"
    
    def __init__(self, transactionTable):
        """ Initialize the Starting Balance Column """
        self.transactionTable = transactionTable
    
    def getItemForColumn(self, account):
        """  """
        return InitialDateTableItem(account, self.transactionTable)
    
    def getWidgetForColumn(self, account):
        """  """
        return None 