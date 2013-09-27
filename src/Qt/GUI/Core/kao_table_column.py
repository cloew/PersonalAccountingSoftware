
class KaoTableColumn:
    """ Represents a column in a Kao Table Widget """
    DELEGATE_CLASS = None
    HEADER = ""
    
    def __init__(self, callbacks=None):
        """ Initialize the Kao Table Column """
        self.callbacks = callbacks
        if callbacks is None:
            self.callbacks = []

    def getProcessedItemForColumn(self, rowModel):
        """ Return the Table Item for this column """
        item = self.getItemForColumn(rowModel)
        self.populateWithCallbacks(item)
        return item
    
    def getProcessedWidgetForColumn(self, rowModel):
        """ Return Widget for this column """
        widget = self.getWidgetForColumn(rowModel)
        self.populateWithCallbacks(widget)
        return widget
            
    def getItemForColumn(self, rowModel):
        """ Return the Table Item for this column """
        return None
    
    def getWidgetForColumn(self, rowModel):
        """ Return Widget for this column """
        return None 
        
    def populateWithCallbacks(self, itemOrWidget):
        """ Populate the given item with the info needed to perform callbacks """
        if itemOrWidget is not None:
            itemOrWidget.callbacks = self.callbacks