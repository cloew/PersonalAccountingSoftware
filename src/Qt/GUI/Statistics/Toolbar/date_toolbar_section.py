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
        self.monthComboBox = QComboBox(self.toolbar)
        self.monthComboBox.addItems(["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
        self.monthComboBox.activated.connect(self.setMonth)
        self.monthComboBox.setCurrentIndex(self.getCategoryStatistics().month-1)
        self.toolbar.addWidget(self.monthComboBox)
        
        
        self.yearComboBox = QComboBox(self.toolbar)
        self.yearComboBox.addItems(["2013"])
        self.yearComboBox.activated.connect(self.setYear)
        self.toolbar.addWidget(self.yearComboBox)
    
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