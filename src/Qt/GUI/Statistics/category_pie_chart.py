import matplotlib

matplotlib.use('Qt4Agg')
matplotlib.rcParams['backend.qt4']='PySide' # May want to cleanup how this is done

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from Qt.Model.Statistics.category_statistics import CategoryStatistics

import matplotlib.pyplot as pyplot

class CategoryPieChart(FigureCanvas):
    """ Represents the Pie Chart of the Category Values """

    def __init__(self, categoryStatistics):
        """ Initialize the Plot """
        self.categoryStatistics = categoryStatistics
        self.addFigure()
        FigureCanvas.__init__(self, self.figure)

    def addFigure(self):
        """  """    
        self.figure = pyplot.figure(1, figsize=(4,4))
        self.figure.add_subplot(111, aspect='equal')

        self.createPlot()

    def createPlot(self):
        """ Create the Pie Chart Plot """
        labels, percentages = self.categoryStatistics.getLabelsAndPercentages()
        pyplot.pie(percentages, labels=labels, autopct='%1.1f%%', shadow=True, colors=['b', 'g', 'r', 'c', 'm', 'y'])

    def updateUI(self):
        self.figure.clear()
        self.addFigure()
        self.figure.canvas.draw()
