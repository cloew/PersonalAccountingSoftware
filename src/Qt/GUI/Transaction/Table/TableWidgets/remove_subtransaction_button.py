from db.subtransactions import SubTransactions

from PySide.QtGui import QIcon, QPushButton

import resources.resource_manager as resource_manager

class RemoveSubtransactionButton(QPushButton):
    """ Represents a Remove Subtransaction Button """
    
    def __init__(self, transaction, table):
        """ Initialize the Remove Subtransaction Button """
        self.transaction = transaction
        self.table = table
        QPushButton.__init__(self, QIcon(resource_manager.GetResourceFilePath("erase.png")), "")
        self.clicked.connect(self.removeSubtransaction)
        
    def removeSubtransaction(self):
        """ Deletes the subtransaction group for this button's transaction """
        subtransactionSet = self.transaction.subtransaction_set
        if len(subtransactionSet.transactions) == 2:
            SubTransactions.delete(subtransactionSet)
        else:
            subtransactionSet.transactions.remove(self.transaction)
            SubTransactions.save()
        
        row = self.table.indexAt(self.pos()).row()
        self.table.removeRow(row)