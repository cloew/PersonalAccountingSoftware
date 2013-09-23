from PySide.QtGui import QFormLayout, QFrame, QLabel, QLineEdit, QVBoxLayout

class TransactionMenuWidget(QFrame):
    """ Represents Transaction Menu Widget """
    
    def __init__(self, parent=None):
        """ Initialize the Transaction Menu Widget """
        QFrame.__init__(self, parent=parent)
        
        self.setFrameShape(QFrame.Panel)
        self.layout = QVBoxLayout(self)
        self.setupHeader()
        self.setupMenuBody()
        self.layout.addStretch()
        
    def setupHeader(self):
        header = QLabel()
        header.setText("<b>Transaction Details</b>")
        font = header.font()
        font.setPointSize(16)
        header.setFont(font)
        self.layout.addWidget(header)
    
    def setupMenuBody(self):
        """ Setup the Body of the Menu """
        self.setupSubtransactions()
        
    def setupSubtransactions(self):
        """ Setup the Subtransactions for the Transaction Details """
        self.subtransactionFrame = QFrame()
        formLayout = QFormLayout(self.subtransactionFrame)
        
        label = QLabel()
        label.setText("<b>Subtransactions</b>")
        formLayout.addRow(label)
        formLayout.addRow("Amount", QLineEdit())
        self.subtransactionFrame.setLayout(formLayout)
        self.layout.addWidget(self.subtransactionFrame)