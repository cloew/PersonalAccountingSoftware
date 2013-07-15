from db.accounts import Accounts
from Qt.GUI.Core.kao_table_item import KaoTableItem

class NameTableItem(KaoTableItem):
    """ Represents a Table Widget Item for an Account Name """
    
    def __init__(self, account):
        """ Initialize the Amount Item """
        self.account = account
        KaoTableItem.__init__(self)
        
    def getData(self):
        """ Return the item's data as a string """
        return self.account.name
        
    def saveData(self, value):
        """ Save Data """
        self.account.name = value
        Accounts.save()