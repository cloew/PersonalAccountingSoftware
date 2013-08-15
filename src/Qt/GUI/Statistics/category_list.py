from PySide.QtCore import QCoreApplication 
from PySide.QtGui import QLabel, QWidget, QVBoxLayout

class CategoryList(QWidget):
    """ Represents the List of Categories and their total expenses that are shown """

    def __init__(self, categoryStatistics):
        """ Initialize the Category List """
        QWidget.__init__(self)
        self.categoryStatistics = categoryStatistics
        self.verticalLayout = None
        self.number = 0
        self.initUI()

    def initUI(self):
        """ Initialize the UI """
        self.verticalLayout = QVBoxLayout()
        self.addHeader()

        self.categoryLabels = {}
        self.totalLabel = None

        self.populateList()

        self.verticalLayout.addStretch()
        self.setLayout(self.verticalLayout)
        
    def populateList(self):
        """ Populate the list """
        self.addTotalExpenses()
        self.addCategoryExpenses()

    def addHeader(self):
        """ Add the Header to the Panel """
        label = QLabel("<b>Expenses by Category</b>")
        self.verticalLayout.addWidget(label)

    def addCategoryExpenses(self):
        """ Add Category Expenses """
        for category in self.categoryLabels.keys():
            if category not in self.categoryStatistics.totalForCategory:
                widget = self.categoryLabels[category]
                self.verticalLayout.removeWidget(widget)
                widget.deleteLater()
                self.categoryLabels.pop(category, None)
        
        for category in self.categoryStatistics.totalForCategory:
            if category not in self.categoryLabels:
                self.categoryLabels[category] = self.addHorizontalBar(category.name, self.categoryStatistics.totalForCategory[category])
            else:
                labelText = self.getLabelText(category.name, self.categoryStatistics.totalForCategory[category])
                self.categoryLabels[category].setText(labelText)

    def addTotalExpenses(self):
        """ Add Total Expenses to the Panel """
        if self.totalLabel is None:
            self.totalLabel = self.addHorizontalBar("Total Expenses", self.categoryStatistics.total)
        else:
            labelText = self.getLabelText("Total Expenses", self.categoryStatistics.total)
            self.totalLabel.setText(labelText)

    def addHorizontalBar(self, text, amount):
        """ Add a Horizontal Bar to the UI """
        label = QLabel(self.getLabelText(text, amount), self)
        self.verticalLayout.insertWidget(1, label)
        return label

    def getLabelText(self, text, amount):
        """ Returns the text for the label formatted properly """
        return "<b>{0}: ${1}</b>".format(text, amount/100.0)

    def updateUI(self):
        self.populateList()