from PySide.QtGui import QHBoxLayout, QFrame

class KaoWidgetWithMenu(QFrame):
    """ Represents a widget with a menu on a single side """
    
    def __init__(self, parent):
        """ Initialize the Kao Widget With Menu """
        QFrame.__init__(self)
        self.parentWidget = parent
        self.__left_widget__, self.__right_widget__ = self.setupWidgets()
        self.setPieceSizes()
        
        layout = QHBoxLayout(self)
        layout.addWidget(self.__left_widget__)
        layout.addWidget(self.__right_widget__)
        self.setLayout(layout)
        
    def setupWidgets(self):
        """ Return the widgets """
        return None, None
    
    def resizeEvent(self, resizeEvent):
        """ Called when window is resized """
        self.setPieceSizes()
        
    def setPieceSizes(self):
        """ Set the Piece Sizes """
        size = self.parentWidget.size()
        height = size.height()-100
        smallWidth = size.width()/3.5
        largeWidth = size.width() - smallWidth
        self.__right_widget__.setMaximumSize(smallWidth, height)
        self.__left_widget__.setMaximumSize(largeWidth, height)