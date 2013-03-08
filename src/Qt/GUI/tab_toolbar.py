from PyQt4.QtGui import QAction, qApp, QIcon,QToolBar

import resources.resource_manager as resource_manager   

class TabToolBar(QToolBar):
    """ Represents a Tab Tool Bar """

    def __init__(self, table_view):
        """ Create and populate the Tab Tool Bar """
        QToolBar.__init__(self)
        self.table_view = table_view
        self.addToolBarButtons()
        self.addExitButton()

    def addToolBarButtons(self):
        """ Add Tool Bar Buttons.
            Should be overridden in sub class """

    def addExitButton(self):
        """ Adds the Exit Button to the ToolBar """
        exitAction = QAction(self.getQIcon('exit.png'), 'Exit the Application', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip("Exit the Application.")
        exitAction.triggered.connect(qApp.quit)
        
        self.addAction(exitAction)

    def getQIcon(self, resource_file):
        """ Return QIcon for the resource file given """
        return QIcon(resource_manager.GetResourceFilePath(resource_file ))