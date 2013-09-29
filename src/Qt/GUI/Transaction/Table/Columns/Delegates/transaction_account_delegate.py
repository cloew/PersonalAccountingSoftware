from db.accounts import Accounts

from PySide.QtGui import QComboBox, QStyledItemDelegate

class TransactionAccountDelegate(QStyledItemDelegate):
    """ Transaction Account View Delegate """

    def createEditor(self, parent, option, index):
        """ Should return a combo box with Income or Expense """
        self.accounts = Accounts.all()
        self.accountNames = [account.name for account in self.accounts]
        comboBox = QComboBox(parent)
        comboBox.insertItems(0, self.accountNames)
        return comboBox

    def setEditorData (self, editor, index):
        """ Set the current data in the editor """
        data = index.data()
        if data is not None:
            editor.setCurrentIndex(self.accountNames.index(data))

    def setModelData(self, editor, model, index):
        """ Set the appropriate data in the model """
        model.setData(index, editor.currentText())