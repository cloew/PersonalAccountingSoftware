from Qt.GUI.Core.kao_table_column import KaoTableColumn
from Qt.GUI.Transaction.Table.transaction_category_delegate import TransactionCategoryDelegate
from Qt.GUI.Transaction.Table.TableWidgets.category_table_item import CategoryTableItem

class CategoryColumn(KaoTableColumn):
    """ Represents the Category Column """
    DELEGATE_CLASS = TransactionCategoryDelegate
    HEADER = "Category"
    
    def getItemForColumn(self, transaction):
        """  """
        return CategoryTableItem(transaction)
    
    def getWidgetForColumn(self, transaction):
        """  """
        return None 