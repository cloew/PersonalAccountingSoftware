from PySide.QtGui import QComboBox, QStyledItemDelegate

class TransactionTypeDelegate(QStyledItemDelegate):
    """ Transaction Type View Delegate """
    __type_strings__ = ["Expense", "Income"]

    def createEditor(self, parent, option, index):
        """ Should return a combo box with Income or Expense """
        comboBox = QComboBox(parent)
        comboBox.insertItems(0, self.__type_strings__)
        return comboBox

    def setEditorData (self, editor, index):
        """ Set the current data in the editor """
        data = index.model().data(index)
        if data is not None:
            editor.setCurrentIndex(self.__type_strings__.index(str(data.toString())))

    def setModelData(self, editor, model, index):
        """ Set the appropriate data in the model """
        model.setData(index, editor.currentText())