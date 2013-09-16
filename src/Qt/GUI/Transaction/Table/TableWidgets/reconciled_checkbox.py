from db.transactions import Transactions

from PySide.QtCore import Qt

from Qt.GUI.Core.kao_table_checkbox import KaoTableCheckbox

class ReconciledCheckbox(KaoTableCheckbox):
    """ Represents a Checkbox to manage whether a transaction has been reconciled """
    
    def __init__(self, transaction, table):
        """ Initialize the Checkbox """
        self.transaction = transaction
        KaoTableCheckbox.__init__(self, table)
        
    def isChecked(self):
        """ Return whether the checkbox should be checked """
        return self.transaction.reconciled
            
    def onCheckStateChanged(self, state):
        """ Save Reconciled State to the database """
        self.transaction.reconciled = state == Qt.Checked
        Transactions.save()
        self.table.updateTransactions()