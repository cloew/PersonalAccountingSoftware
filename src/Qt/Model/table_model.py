from PyQt4.QtCore import QAbstractTableModel, QModelIndex, QVariant, Qt

class TableModel(QAbstractTableModel):
    """ Represnts the a Table Model """

    def __init__(self):
        """ Build the Transactions Table """
        QAbstractTableModel.__init__(self)
        self.columns = self.getColumns()

        self.roleResponses = {Qt.DisplayRole:self.getData,
                              Qt.EditRole:self.getData,
                              Qt.ToolTipRole:self.getTip,
                              Qt.StatusTipRole:self.getTip,
                              Qt.TextAlignmentRole:self.getTextAlignment}

    def getColumns(self):
        """ Get the Columns for the table.
            Should be overridden in the sub classes """

    def indexForColumnClass(self, column_class):
        """ Returns the index that has a column of the given class """
        for column in self.columns:
            if isinstance(column, column_class):
                return self.columns.index(column)

    def rowCount(self, parent):
        """ Returns the number of rows in the table.
            Should be overridden in sub classes """

    def columnCount(self, parent):
        """ Returns the number of columns in the table """
        return len(self.columns)

    def insertRows(self, row, count, parent=QModelIndex()):
        """ Insert Rows """
        self.beginInsertRows(parent, row, row+count-1)
        self.endInsertRows()
        return True

    def data(self, index, role = Qt.DisplayRole):
        """ Return the data at the given index """
        if not index.isValid():
            return self.getDisplayRoleData(index)
        else:
            return self.getDataBasedOnRole(index, role)

    def flags(self, index):
        """ Return flags for the Transaction Table """
        return Qt.ItemIsEditable | Qt.ItemIsEnabled # | Qt.ItemIsSelectable

    def setData(self, index, value, role = Qt.EditRole):
        """ Set Data in the Transaction Table """
        column = index.column()
        if column < len(self.columns):
            changed = self.columns[column].setData(index.row(), value)
            return changed
        return False

    def getDataBasedOnRole(self, index, role):
        """ Get Data based on the role given """
        if role in self.roleResponses:
            return self.roleResponses[role](index)

    def getData(self, index):
        """ Return the actual Data """
        column = index.column()
        if column < len(self.columns):
            return self.columns[column].getData(index.row())

    def getTip(self, index):
        """ Return Data for a Status or Tool Tip """
        column = index.column()
        if column < len(self.columns):
            return self.columns[column].getTip(index.row())

    def getTextAlignment(self, index):
        """ Return Text Alignment for the given cell """
        return int(Qt.AlignLeft|Qt.AlignVCenter)

    def headerData(self, section, orientation, role = Qt.DisplayRole):
        """ Return Header Data """
        if role != Qt.DisplayRole:
            return None
        if Qt.Horizontal == orientation:
            if section < len(self.columns):
                return QVariant(self.columns[section].getHorizontalHeader())    
            return QVariant("Horizontal Header")