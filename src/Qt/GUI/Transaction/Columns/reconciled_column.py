from Qt.GUI.Transaction.Columns.reconciled_checkbox import ReconciledCheckbox

class ReconciledColumn:
    """ Represents the Reconciled Column """
    HEADER = "Reconciled"
    
    def getItemForColumn(self, transaction):
        """  """
        return None
    
    def getWidgetForColumn(self, transaction):
        """  """
        return ReconciledCheckbox(transaction) 