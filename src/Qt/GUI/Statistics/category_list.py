from PySide.QtGui import QWidget, QPushButton

class CategoryList(QWidget):
    """ Represents the List of Categories and their total expenses that are shown """

    def __init__(self):
        """ Initialize the Category List """
        QWidget.__init__(self)
        self.initUI()

    def initUI(self):
        """ Initialize the UI """
        self.button = QPushButton("Some Button", self)
        self.show()
