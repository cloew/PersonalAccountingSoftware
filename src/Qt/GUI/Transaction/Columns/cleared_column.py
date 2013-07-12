from Qt.GUI.Transaction.TableWidgets.cleared_checkbox import ClearedCheckbox

from PySide.QtGui import QHBoxLayout, QWidget

class ClearedColumn:
    """ Represents the Cleared Column """
    HEADER = "Cleared"
    
    def getItemForColumn(self, transaction):
        """  """
        return None
    
    def getWidgetForColumn(self, transaction):
        """  """
        widget = QWidget()
        layout = QHBoxLayout(widget)
        layout.addStretch()
        layout.addWidget(ClearedCheckbox(transaction))
        layout.addStretch()
        widget.setLayout(layout)
        return widget