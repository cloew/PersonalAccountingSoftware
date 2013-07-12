from PySide.QtCore import Qt
from PySide.QtGui import QTableWidgetItem

class KaoTableItem(QTableWidgetItem):
    """ Base class for Kao Ttessur Qt Table Items """
    
    def __init__(self):
        """ Initialize the Kao Table Item """
        QTableWidgetItem.__init__(self, self.getData())
        
    def getData(self):
        """ Return the item's data as a string """
        return ""
        
    def setData(self, role, value):
        """ Set Data in Item """
        if role == Qt.EditRole:
            self.saveData(value)
        return QTableWidgetItem.setData(self, role, self.getData())
        
    def updateData(self):
        """ Update the Table Item's text and data """
        self.setText(self.getData())
        
    def saveData(self, value):
        """ Save the table items data change """