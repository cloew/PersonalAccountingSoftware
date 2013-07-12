from Qt.GUI.Category.TableWidgets.delete_button import DeleteButton

from PySide.QtGui import QHBoxLayout, QWidget

class DeleteColumn:
    """ Represents the Delete Column """
    HEADER = ""
    
    def __init__(self, table):
        """ Initialize the Delete Column """
        self.table = table
    
    def getItemForColumn(self, category):
        """  """
        return None
    
    def getWidgetForColumn(self, category):
        """  """
        widget = QWidget()
        layout = QHBoxLayout(widget)
        layout.addStretch()
        layout.addWidget(DeleteButton(category, self.table, widget))
        layout.addStretch()
        widget.setLayout(layout)
        return widget