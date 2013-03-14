from PySide.QtCore import QEvent, QSize, Qt
from PySide.QtGui import QApplication, QIcon, QPushButton, QStyle, QStyledItemDelegate, QStyleOptionButton

import resources.resource_manager as resource_manager

class DeleteCategoryDelegate(QStyledItemDelegate):
    """ Delete Category Delegate """

    def editorEvent(self, event, model, option, index):
        """ Handle Editor Events """
        if event.type() == QEvent.MouseButtonRelease:
            index.model().setData(index, True)
            index.model().removeRow(index.row())
            return True
        return False

    def paint(self, painter, option, index):
        """ Paint the Item """
        buttonOptions = QStyleOptionButton()
        buttonOptions.rect = option.rect
        
        button = QPushButton()
        buttonOptions.rect = QStyle.alignedRect(Qt.LeftToRight, Qt.AlignHCenter | Qt.AlignVCenter, button.sizeHint(), option.rect)
        buttonOptions.state = QStyle.State_Enabled
        buttonOptions.icon = QIcon(resource_manager.GetResourceFilePath("erase.png"))
        buttonOptions.iconSize = QSize(24, 24)
        
        QApplication.style().drawControl(QStyle.CE_PushButton, buttonOptions, painter)