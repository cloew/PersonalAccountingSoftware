from Qt.GUI.Core.kao_table_item import KaoTableItem

class TransactionTableItem(KaoTableItem):
    """ Represents a Transaction Table Item """
    
    def __init__(self, transaction):
        """ Initialize the Transaction Table Item """
        self.transaction = transaction
        KaoTableItem.__init__(self)