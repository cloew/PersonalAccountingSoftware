from PySide.QtGui import QTableWidgetItem

class DescriptionTableItem(QTableWidgetItem):
    """ Represents a Table Widget Item for a Transaction Description """
    
    def __init__(self, transaction):
        """ Initialize the Description Item """
        QTableWidgetItem.__init__(self, transaction.description)
        self.transaction = transaction