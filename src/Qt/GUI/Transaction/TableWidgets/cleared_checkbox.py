from db.transactions import Transactions

from PySide.QtCore import Qt

from Qt.GUI.Core.kao_table_checkbox import KaoTableCheckbox

class ClearedCheckbox(KaoTableCheckbox):
    """ Represents a Checkbox to manage whether a transaction has been cleared """
    
    def __init__(self, transaction, table):
        """ Initialize the Checkbox """
        self.transaction = transaction
        KaoTableCheckbox.__init__(self, table)
        
    def isChecked(self):
        """ Return if the box should be checked """
        return self.transaction.cleared
            
    def onCheckStateChanged(self, state):
        """ Save Cleared State to the database """
        self.transaction.cleared = state == Qt.Checked
        Transactions.save()
        self.table.updateTransactions()