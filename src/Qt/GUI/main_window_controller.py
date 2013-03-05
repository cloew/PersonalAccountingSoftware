from PyQt4 import QtGui
from Qt.GUI.main_window import MainWindow

import sys

class MainWindowController:
    """ Controller for the Main PAS Window """

    def __init__(self):
        """ Initialize the Main Window Controller """

    def run(self):
        """ Runs the Main Window """
        app = QtGui.QApplication(sys.argv)
        window = MainWindow()
        app.exec_()