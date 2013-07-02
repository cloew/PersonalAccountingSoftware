from PySide.QtCore import Qt
from PySide.QtGui import QCheckBox

class ClearedCheckbox(QCheckBox):
    """ Represents a Checkbox to manage whether a transaction has been cleared """
    
    def __init__(self, transaction):
        """ Initialize the Checkbox """
        QCheckBox.__init__(self, "")
        self.transaction = transaction
        self.setCheckState(self.getCheckedState())
        
    def getCheckedState(self):
        """ Return the Checked State """
        if self.transaction.cleared is None or not self.transaction.cleared:
            return Qt.Unchecked
        else:
            return Qt.Checked