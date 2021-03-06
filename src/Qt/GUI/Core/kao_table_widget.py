from PySide.QtGui import QHeaderView, QTableWidget, QItemSelectionModel 

class KaoTableWidget(QTableWidget):
    """ Base class for Kao Ttessur Qt Table Widgets """
    
    def __init__(self, dataList, columns, parent=None):
        """ Initialize the Kao Ttessur Table Widget """
        self.columns = columns
        QTableWidget.__init__(self, len(dataList), len(self.columns), parent)
        
        self.setHorizontalHeaderLabels([column.HEADER for column in self.columns])
        self.verticalHeader().hide()
        
        self.populateTable(dataList)
        self.delegates = []
        self.setColumnDelegates()
        
        self.horizontalHeader().setResizeMode(QHeaderView.Stretch)
        self.resizeColumnsToContents()
        self.resizeRowsToContents()
        
    def populateTable(self, dataList):
        """ Setup Table Items & Widget with their data """
        for row in range(len(dataList)):
            self.populateRow(row, dataList[row])
        self.resizeRowsToContents()
        
    def populateRow(self, row, data):
        """ Populate the Row """
        for column in range(len(self.columns)):
            columnPopulator = self.columns[column]
            
            widget = columnPopulator.getProcessedWidgetForColumn(data)
            item = columnPopulator.getProcessedItemForColumn(data)
            
            if widget is not None:
                self.setCellWidget(row, column, widget)
            elif item is not None:
                self.setItem(row, column, item)
                    
    def setColumnDelegates(self):
        """ Set Column Delegates """
        for column in self.columns:
            if column.DELEGATE_CLASS is not None:
                delegate = column.DELEGATE_CLASS()
                self.delegates.append(delegate)
                self.setDelegateForColumn(delegate, column.__class__)
        
    def setDelegateForColumn(self, delegate, columnClass):
        """ Set the Custom Delegate for a column """
        index = self.getColumnIndex(columnClass)
        if index is not None:
            self.setItemDelegateForColumn(index, delegate)
            
    def getColumn(self, columnClass):
        """ Returns the column of the type requested or None """
        index = self.getColumnIndex(columnClass)
        if index in range(len(self.columns)):
            return self.columns[index]
            
    def getColumnIndex(self, columnClass):
        """ Return the index for the given column in the table """
        columnClasses = [column.__class__ for column in self.columns]
        return columnClasses.index(columnClass)
        
    def insertRow(self, data, selectRow=True):
        """ Insert a Row into the Kao Table with the given data """
        QTableWidget.insertRow(self, 0)
        self.populateRow(0, data)
        if selectRow:
            self.setCurrentCell(0, 0, QItemSelectionModel.ClearAndSelect)
        self.resizeRowsToContents()
        
    