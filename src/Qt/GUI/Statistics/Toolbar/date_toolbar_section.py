from db.transactions import Transactions

from PySide.QtGui import QComboBox, QLabel

class DateToolbarSection:
    """ Represents the Date Toolbar Section """
    
    def __init__(self, toolbar, panel):
        """ Initialize the Date Toolbar Section """
        self.toolbar = toolbar
        self.panel = panel
        
    def addDateSection(self):
        """ Add Date Section """
        self.dateLabel = QLabel("Month: ", self.toolbar)
        self.toolbar.addWidget(self.dateLabel)
        self.setupMonthComboBox()
        self.setupYearComboBox()
        
    def setupMonthComboBox(self):
        """ Setup the month combo box """
        self.monthComboBox = QComboBox(self.toolbar)
        self.monthComboBox.addItems(["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
        self.monthComboBox.activated.connect(self.setMonth)
        self.monthComboBox.setCurrentIndex(self.getCategoryStatistics().month-1)
        self.toolbar.addWidget(self.monthComboBox)
        
    def setupYearComboBox(self):
        """ Setup the year combo box """
        self.yearComboBox = QComboBox(self.toolbar)
        self.getTransactionYears()
        self.yearComboBox.addItems([str(year) for year in self.transactionYears])
        self.yearComboBox.activated.connect(self.setYear)
        self.yearComboBox.setCurrentIndex(self.transactionYears.index(self.getCategoryStatistics().year))
        self.toolbar.addWidget(self.yearComboBox)
    
    def getTransactionYears(self):
        """ Get the possible transacttion years """
        self.transactionYears = list(Transactions.getAllYears())
        self.transactionYears.sort()
    
    def setMonth(self, index):
        """ Set the month """
        categoryStatistics = self.getCategoryStatistics()
        categoryStatistics.month = index+1
        self.panel.updatePanel()
    
    def setYear(self, index):
        """ Set the year """
        categoryStatistics = self.getCategoryStatistics()
        categoryStatistics.year = int(self.yearComboBox.currentText())
        self.panel.updatePanel()
        
    def getCategoryStatistics(self):
        """ Returns the Category Statistics """
        return self.panel.categoryStatistics