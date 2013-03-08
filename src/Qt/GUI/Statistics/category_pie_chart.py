from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from Qt.Model.Statistics.category_statistics import CategoryStatistics

import matplotlib.pyplot as pyplot

class CategoryPieChart(FigureCanvas):
    """ Represents the Pie Chart of the Category Values """

    def __init__(self):
        """ Initialize the Plot """
        self.categoryStatistics = CategoryStatistics()

        self.figure = pyplot.figure(1, figsize=(4,4))
        self.figure.add_subplot(111)

        self.createPlot()
        FigureCanvas.__init__(self, self.figure)

    def createPlot(self):
        """ Create the Pie Chart Plot """
        #explode=(0, 0.05, 0, 0)
        labels, percentages = self.categoryStatistics.getLabelsAndPercentages()
        pyplot.pie(percentages, labels=labels, autopct='%1.1f%%', shadow=True)
