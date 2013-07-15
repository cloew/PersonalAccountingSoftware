from PySide.QtGui import QHBoxLayout, QWidget

def GetCenteredWidgetForTableCell(centeredWidget):
    """ Returns a Widget centered in another widget so it appears centered in a table cell """
    widget = QWidget()
    layout = QHBoxLayout(widget)
    layout.addStretch()
    layout.addWidget(centeredWidget)
    layout.addStretch()
    widget.setLayout(layout)
    return widget