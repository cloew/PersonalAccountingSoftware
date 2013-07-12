from db.transactions import Transactions

from PySide.QtCore import Qt
from PySide.QtGui import QCheckBox

class ReconciledCheckbox(QCheckBox):
    """ Represents a Checkbox to manage whether a transaction has been reconciled """
    
    def __init__(self, transaction):
        """ Initialize the Checkbox """
        QCheckBox.__init__(self, "")
        self.transaction = transaction
        self.setCheckState(self.getCheckedState())
        self.stateChanged.connect(self.saveReconciledState)
        
    def getCheckedState(self):
        """ Return the Checked State """
        if self.transaction.reconciled is None or not self.transaction.reconciled:
            return Qt.Unchecked
        else:
            return Qt.Checked
            
    def saveReconciledState(self, state):
        """ Save Reconciled State to the database """
        self.transaction.reconciled = state == Qt.Checked
        Transactions.save()