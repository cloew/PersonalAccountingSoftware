from PySide.QtGui import QFrame, QLabel

class TransactionMenuWidget(QFrame):
    """ Represents Transaction Menu Widget """
    
    def __init__(self, parent=None):
        """ Initialize the Transaction Menu Widget """
        QFrame.__init__(self, parent=parent)
        
        self.setFrameShape(QFrame.Panel)
        self.label = QLabel(self)
        self.label.setText("Something")