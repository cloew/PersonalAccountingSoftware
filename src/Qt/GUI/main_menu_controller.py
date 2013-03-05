from PyQt4 import QtGui

import sys

class MainMenuController:
    """ Controller for the Main PAS Menu """

    def __init__(self):
        """ Initialize the Main Menu """

    def run(self):
        """ Runs the Main Menu """
        app = QtGui.QApplication(sys.argv)

        app.exec_()