from Qt.GUI.tab_toolbar import TabToolBar
from Qt.GUI.Statistics.Toolbar.date_toolbar_section import DateToolbarSection

class StatisticsToolbar(TabToolBar):
    """ Represents the Statistics Toolbar """
    
    def __init__(self, panel):
        """ Initialize the Toolbar """
        self.dateSection = DateToolbarSection(self, panel)
        TabToolBar.__init__(self, panel)
    
    def addToolBarButtons(self):
        """ Add Tool Bar Buttons """
        self.dateSection.addDateSection()
        self.addSeparator()