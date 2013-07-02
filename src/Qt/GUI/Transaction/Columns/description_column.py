from PySide.QtGui import QTableWidgetItem 

class DescriptionColumn:
    """ Represents the Description Column """
    HEADER = "Description"
    
    def getItemForColumn(self, transaction):
        """  """
        return QTableWidgetItem(transaction.description)
    
    def getWidgetForColumn(self, transaction):
        """  """
        return None 