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
        self.addHorizontalBar("Total Expenses", 1234.56)

    def addHorizontalBar(self, label, amount):
        """ Add a Horizontal Bar to the UI """
        horizontalLayout = QHBoxLayout()
        textLabel = QLabel("<b>{0}</b>:".format(label))
        amountLabel = QLabel("<b>{0}</b>".format(amount))
        horizontalLayout.addWidget(textLabel)
        horizontalLayout.addWidget(amountLabel)
        horizontalLayout.addStretch()
        self.verticalLayout.addLayout(horizontalLayout)