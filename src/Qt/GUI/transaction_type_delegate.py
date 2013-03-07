from PyQt4.QtCore import QStringList, QVariant
from PyQt4.QtGui import QComboBox, QStyledItemDelegate

class TransactionTypeDelegate(QStyledItemDelegate):
    """ Transaction Type View Delegate """
    __type_strings__ = ["Expense", "Income"]

    def createEditor(self, parent, option, index):
        """ Should return a combo box with Income or Expense """
        comboBox = QComboBox(parent)
        comboBox.insertItems(0, QStringList(self.__type_strings__))
        return comboBox

    def setModelData(self, editor, model, index):
        """ Set the appropriate data in the model """
        model.setData(index, QVariant(editor.currentText()))