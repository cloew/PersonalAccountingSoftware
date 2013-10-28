from PySide.QtCore import Qt
from PySide.QtGui import QCheckBox

class KaoTableCheckbox(QCheckBox):
    """ Represents a Checkbox in a Table """
    
    def __init__(self):
        """ Initialize the Checkbox """
        callbacks = []
        QCheckBox.__init__(self, "")
        self.setCheckState(self.getCheckedState())
        self.stateChanged.connect(self.__on_check_state_changed__)
        
    def getCheckedState(self):
        """ Return the Checked State """
        if self.isChecked():
            return Qt.Checked
        else:
            return Qt.Unchecked
            
    def isChecked(self):
        """ Return if the box should be checked """
        return False
        
    def __on_check_state_changed__(self, state):
        self.onCheckStateChanged(state)
            
    def onCheckStateChanged(self, state):
        """ Event called when the Checkbox state is changed """