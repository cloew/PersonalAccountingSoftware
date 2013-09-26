from Qt.GUI.Transaction.Menu.subtransaction_form import SubtransactionForm

from PySide.QtGui import QFrame, QLabel, QVBoxLayout

class TransactionMenuWidget(QFrame):
    """ Represents Transaction Menu Widget """
    
    def __init__(self, parent=None):
        """ Initialize the Transaction Menu Widget """
        QFrame.__init__(self, parent=parent)
        self.setFrameShape(QFrame.Panel)
        self.layout = QVBoxLayout(self)
        
        self.transaction = None
        self.forms = [SubtransactionForm(self)]
        
        self.setupHeader()
        for form in self.forms:
            form.setup()
        self.layout.addStretch()
        
    def setupHeader(self):
        header = QLabel()
        header.setText("<b>Transaction Details</b>")
        font = header.font()
        font.setPointSize(16)
        header.setFont(font)
        self.layout.addWidget(header)
        
        self.transactionLabel = QLabel()
        self.setTransactionLabelText()
        self.layout.addWidget(self.transactionLabel)
        
    def updateOnTransactionChange(self, currentTransaction):
        """ Update menu contents when the current transaction changes Transaction Change """
        self.transaction = currentTransaction
        self.setTransactionLabelText()
        for form in self.forms:
            form.updateOnTransactionChange()
        
    def setTransactionLabelText(self):
        """ Set the Transaction label Text """
        if self.transaction is not None:
            self.transactionLabel.setText("<b>{0}</b>".format(self.transaction.description))
            
    def tabSelected(self):
        """ Update the Account Tab when the tab is selected """
        for form in self.forms:
            form.tabSelected()
        