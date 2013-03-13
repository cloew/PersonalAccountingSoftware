from db.categories import Categories

#from PySide.QtCore import QStringList, QVariant
from PySide.QtGui import QComboBox, QCompleter, QLineEdit, QStringListModel, QStyledItemDelegate

class TransactionCategoryDelegate(QStyledItemDelegate):
    """ Transaction Category View Delegate """

    def createEditor(self, parent, option, index):
        """ Should return a LineEdit with all the Category Names as AutoComplete values """
        edit = QLineEdit(parent)
        completer = QCompleter()
        edit.setCompleter(completer) 
        model = QStringListModel()
        completer.setModel(model)
        self.setCompleterData(model)
        return edit

    def setCompleterData(self, model):
        """ Set Completer Data to use Category data """
        categoryNames = []
        for category in Categories.all():
            if category.name is not None:
                categoryNames.append(category.name)
        model.setStringList(categoryNames)