from PyQt4 import QtGui

class MainWindow(QtGui.QMainWindow):
    """ Represents the Main Window of the PAS Application """

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.initUI()

    def initUI(self):
        """ Initialize the User Interface """
        self.resize(250, 150)
        #self.center()

        self.setWindowTitle("PAS")
        self.show()

    #def center(self):
