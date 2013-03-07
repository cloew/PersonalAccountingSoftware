from ORM.transaction import Transaction
from PyQt4.QtCore import QVariant
from Qt.Model.Transaction.type_column import TypeColumn

import unittest

class getDataForTransaction(unittest.TestCase):
    """ Test cases of getDataForTransaction """
    
    def  setUp(self):
        """ Build the *** for the test """
        self.transaction = Transaction()
        self.typeColumn = TypeColumn()
        
    def noType(self):
        """ Test that getDataForTransaction properly handles when there is no type """
        self.transaction.type = None
        data = self.typeColumn.getDataForTransaction(self.transaction)
        assert data is None, "Should get no data when the transaction type is None"

    def income(self):
        """ Test that getDataForTransaction properly handles when there is an income type """
        income = True
        self.transaction.income = income
        data = self.typeColumn.getDataForTransaction(self.transaction)
        assert str(data.toString()) == "Income", "Should get the Income string"

    def expense(self):
        """ Test that getDataForTransaction properly handles when there is an expense type """
        income = False
        self.transaction.income = income
        data = self.typeColumn.getDataForTransaction(self.transaction)
        assert str(data.toString()) == "Expense", "Should get the Expense string"

# Collect all test cases in this class
testcasesGetDataForTransaction = ["noType", "income", "expense"]
suiteGetDataForTransaction = unittest.TestSuite(map(getDataForTransaction, testcasesGetDataForTransaction))

##########################################################

class setDataForTransaction(unittest.TestCase):
    """ Test cases of setDataForTransaction """
    
    def  setUp(self):
        """ Build the *** for the test """
        self.transaction = Transaction()
        self.transaction.type = None
        self.typeColumn = TypeColumn()

    def badString(self):
        """ Test that setDataForTransaction properly handles when there is a bad String """
        typeString = "q2w3e4r5ty"
        value = QVariant(typeString)
        dataSet = self.typeColumn.setDataForTransaction(self.transaction, value)
        assert not dataSet, "Should have data set"
        assert self.transaction.income == None, "Should have no type"

    def fullIncomeString(self):
        """ Test that setDataForTransaction properly handles when there is a full Income String """
        typeString = "Income"
        value = QVariant(typeString)
        dataSet = self.typeColumn.setDataForTransaction(self.transaction, value)
        assert dataSet, "Should have data set"
        assert self.transaction.income == True, "Should be Income"

    def partialIncomeString(self):
        """ Test that setDataForTransaction properly handles when there is a partial Income String """
        typeString = "I"
        value = QVariant(typeString)
        dataSet = self.typeColumn.setDataForTransaction(self.transaction, value)
        assert dataSet, "Should have data set"
        assert self.transaction.income == True, "Should be Income"

    def lowerIncomeString(self):
        """ Test that setDataForTransaction properly handles when there is a partial Income String """
        typeString = "i"
        value = QVariant(typeString)
        dataSet = self.typeColumn.setDataForTransaction(self.transaction, value)
        assert dataSet, "Should have data set"
        assert self.transaction.income == True, "Should be Income"

    def fullExpenseString(self):
        """ Test that setDataForTransaction properly handles when there is a full Expense String """
        typeString = "Expense"
        value = QVariant(typeString)
        dataSet = self.typeColumn.setDataForTransaction(self.transaction, value)
        assert dataSet, "Should have data set"
        assert self.transaction.income == False, "Should be Expense"

    def partialExpenseString(self):
        """ Test that setDataForTransaction properly handles when there is a partial Expense String """
        typeString = "E"
        value = QVariant(typeString)
        dataSet = self.typeColumn.setDataForTransaction(self.transaction, value)
        assert dataSet, "Should have data set"
        assert self.transaction.income == False, "Should be Expense"

    def lowerExpenseString(self):
        """ Test that setDataForTransaction properly handles when there is a partial Expense String """
        typeString = "e"
        value = QVariant(typeString)
        dataSet = self.typeColumn.setDataForTransaction(self.transaction, value)
        assert dataSet, "Should have data set"
        assert self.transaction.income == False, "Should be Expense"

# Collect all test cases in this class
testcasesSetDataForTransaction = ["badString", "fullIncomeString", "partialIncomeString", "lowerIncomeString",
                                  "fullExpenseString", "partialExpenseString", "lowerExpenseString"]
suiteSetDataForTransaction = unittest.TestSuite(map(setDataForTransaction, testcasesSetDataForTransaction))

##########################################################

# Collect all test cases in this file
suites = [suiteGetDataForTransaction, suiteSetDataForTransaction]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()