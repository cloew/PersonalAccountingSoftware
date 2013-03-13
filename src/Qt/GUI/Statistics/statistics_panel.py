from PySide.QtGui import QHBoxLayout, QPushButton, QWidget

from category_list import CategoryList
from category_pie_chart import CategoryPieChart

class StatisticsPanel(QWidget):
    """ Represents the Statistics Panel """

    def __init__(self):
        """  """
        QWidget.__init__(self)
        self.setupLayout()

    def setupLayout(self):
        """ Setup the Layout on the Statistics Panel """
        layout = QHBoxLayout()
        pieChart = CategoryPieChart()
        categoryList = CategoryList()
        
        layout.addWidget(pieChart)
        layout.addWidget(categoryList)
        self.setLayout(layout)