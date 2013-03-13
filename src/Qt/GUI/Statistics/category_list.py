from PySide.QtGui import QHBoxLayout, QLabel, QWidget, QVBoxLayout

class CategoryList(QWidget):
    """ Represents the List of Categories and their total expenses that are shown """

    def __init__(self):
        """ Initialize the Category List """
        QWidget.__init__(self)
        self.initUI()

    def initUI(self):
        """ Initialize the UI """
        self.verticalLayout = QVBoxLayout()
        
        self.addHeader()
        self.addTotalExpenses()

        self.verticalLayout.addStretch()

        self.setLayout(self.verticalLayout)

    def addHeader(self):
        """ Add the Header to the Panel """
        label = QLabel("<b>Expenses by Category</b>")
        self.verticalLayout.addWidget(label)

    def addTotalExpenses(self):
        """ Add Total Expenses to the Panel """
        totalLabel = QLabel("<b>Total Expenses</b>")
        self.verticalLayout.addWidget(totalLabel)