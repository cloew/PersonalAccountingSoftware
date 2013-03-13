from ORM.transaction import Transaction
from Qt.Model.Transaction.description_column import DescriptionColumn

import unittest

class getDataForTransaction(unittest.TestCase):
    """ Test cases of getDataForTransaction """
    
    def  setUp(self):
        """ Build the Transaction and Column for the test """
        self.transaction = Transaction()
        self.descriptionColumn = DescriptionColumn()
        
    def noDescription(self):
        """ Test that getDataForTransaction properly handles when there is no description """
        self.transaction.description = None
        data = self.descriptionColumn.getDataForTransaction(self.transaction)
        assert data is None, "Should get no data when the transaction description is None"

    def aDescription(self):
        """ Test that getDataForTransaction properly handles when there is a description """
        description = "Some Description"
        self.transaction.description = description
        data = self.descriptionColumn.getDataForTransaction(self.transaction)
        assert data == description, "Should get the same description as a string"

# Collect all test cases in this class
testcasesGetDataForTransaction = ["noDescription", "aDescription"]
suiteGetDataForTransaction = unittest.TestSuite(map(getDataForTransaction, testcasesGetDataForTransaction))

##########################################################

class setDataForTransaction(unittest.TestCase):
    """ Test cases of setDataForTransaction """
    
    def  setUp(self):
        """ Build the *** for the test """
        self.transaction = Transaction()
        self.transaction.description = None
        self.descriptionColumn = DescriptionColumn()

    def descriptionString(self):
        """ Test that setDataForTransaction properly handles when there is a description """
        value = "Some Description"
        dataSet = self.descriptionColumn.setDataForTransaction(self.transaction, value)
        assert dataSet, "Should have data set"
        assert self.transaction.description == value, "Should have the Transaction Description"

# Collect all test cases in this class
testcasesSetDataForTransaction = ["descriptionString"]
suiteSetDataForTransaction = unittest.TestSuite(map(setDataForTransaction, testcasesSetDataForTransaction))

##########################################################

# Collect all test cases in this file
suites = [suiteGetDataForTransaction, suiteSetDataForTransaction]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()