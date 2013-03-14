from PySide.QtCore import QEvent
from PySide.QtGui import QApplication, QStyle, QStyledItemDelegate, QStyleOptionButton

class CheckBoxDelegate(QStyledItemDelegate):
    """ Check Box View Delegate """

    def editorEvent(self, event, model, option, index):
        """ Handle Editor Events """
        if event.type() == QEvent.MouseButtonRelease:
            value = not index.data()
            index.model().setData(index, value)
            return True
        return False

    def paint(self, painter, option, index):
        """ Paint the Item """
        buttonOptions = QStyleOptionButton()
        buttonOptions.rect = option.rect

        if index.data():
            buttonOptions.state = QStyle.State_Enabled | QStyle.State_On
        else:
            buttonOptions.state = QStyle.State_Enabled | QStyle.State_Off
        

        QApplication.style().drawControl(QStyle.CE_CheckBox, buttonOptions, painter)