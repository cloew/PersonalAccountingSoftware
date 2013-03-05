from PyQt4 import QtGui
from Qt.GUI.transaction_list_view import TransactionListView

class MainWindow(QtGui.QMainWindow):
    """ Represents the Main Window of the PAS Application """

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.initUI()

    def initUI(self):
        """ Initialize the User Interface """
        list_view = TransactionListView()
        self.setCentralWidget(list_view)

        self.setWindowTitle("PAS")
        self.showMaximized()