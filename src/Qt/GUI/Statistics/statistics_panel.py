from PySide.QtGui import QHBoxLayout, QPushButton, QWidget

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
        
        layout.addWidget(pieChart)
        layout.addWidget(QPushButton("Some Button"))
        self.setLayout(layout)