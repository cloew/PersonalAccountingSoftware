from PySide.QtCore import Qt
from PySide.QtGui import QTableWidgetItem

class KaoTableItem(QTableWidgetItem):
    """ Base class for Kao Ttessur Qt Table Items """
    
    def __init__(self):
        """ Initialize the Kao Table Item """
        callbacks = []
        QTableWidgetItem.__init__(self, self.getData())
        
    def getData(self):
        """ Return the item's data as a string """
        return ""
        
    def setData(self, role, value):
        """ Set Data in Item """
        if role == Qt.EditRole:
            dataSaved = self.saveData(value)
            if dataSaved:
                for callback in self.callbacks:
                    callback()
        if self.shouldSetData(role):
            try:
                return QTableWidgetItem.setData(self, role, self.getData())
            except RuntimeError:
                pass
        
    def updateData(self):
        """ Update the Table Item's text and data """
        self.setText(self.getData())
        
    def saveData(self, value):
        """ Save the table items data change """
        
    def shouldSetData(self, role):
        """ Returns if the Table Item should call the base classes set Data """
        return True 