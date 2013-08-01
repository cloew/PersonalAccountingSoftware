from PySide.QtCore import Qt
from PySide.QtGui import QCheckBox

class KaoTableCheckbox(QCheckBox):
    """ Represents a Checkbox to manage whether a transaction has been cleared """
    
    def __init__(self, table):
        """ Initialize the Checkbox """
        QCheckBox.__init__(self, "")
        self.table = table
        self.setCheckState(self.getCheckedState())
        self.stateChanged.connect(self.onCheckStateChanged)
        
    def getCheckedState(self):
        """ Return the Checked State """
        if self.isChecked():
            return Qt.Checked
        else:
            return Qt.Unchecked
            
    def isChecked(self):
        """ Return if the box should be checked """
        return False
            
    def onCheckStateChanged(self, state):
        """ Event called when the Checkbox state is changed """