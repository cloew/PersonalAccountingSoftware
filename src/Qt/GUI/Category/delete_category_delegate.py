from PySide.QtCore import QEvent, Qt
from PySide.QtGui import QApplication, QPushButton, QStyle, QStyledItemDelegate, QStyleOptionButton

import resources.resource_manager as resource_manager

class DeleteCategoryDelegate(QStyledItemDelegate):
    """ Delete Category Delegate """

    def paint(self, painter, option, index):
        """ Paint the Item """
        buttonOptions = QStyleOptionButton()
        buttonOptions.rect = option.rect
        
        button = QPushButton()
        buttonOptions.rect = QStyle.alignedRect(Qt.LeftToRight, Qt.AlignHCenter | Qt.AlignVCenter, button.sizeHint(), option.rect)
        buttonOptions.state = QStyle.State_Enabled
        
        QApplication.style().drawControl(QStyle.CE_PushButton, buttonOptions, painter)