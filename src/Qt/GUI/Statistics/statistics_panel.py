from PySide.QtGui import QApplication, QHBoxLayout, QPushButton, QWidget
from Qt.Model.Statistics.category_statistics import CategoryStatistics

from category_list import CategoryList
from category_pie_chart import CategoryPieChart

class StatisticsPanel(QWidget):
    """ Represents the Statistics Panel """

    def __init__(self):
        """  """
        QWidget.__init__(self)
        self.categoryStatistics = CategoryStatistics()

        self.pieChart = None
        self.categoryList = None
        self.setupLayout()

    def setupLayout(self):
        """ Setup the Layout on the Statistics Panel """
        layout = QHBoxLayout()
        self.pieChart = CategoryPieChart(self.categoryStatistics)
        self.categoryList = CategoryList(self.categoryStatistics)

        layout.addWidget(self.pieChart)
        layout.addWidget(self.categoryList)
        self.setLayout(layout)

    def tabSelected(self):
        """ Called when the tab is selected """
        self.categoryStatistics.prepareStatistics()
        self.categoryList.updateUI()