from ORM.transaction import Transaction
from Qt.Model.Transaction.cleared_column import ClearedColumn

import unittest

class getDataForTransaction(unittest.TestCase):
    """ Test cases of getDataForTransaction """
    
    def  setUp(self):
        """ Build the Transaction and Column for the test """
        self.transaction = Transaction()
        self.clearedColumn = ClearedColumn()
        
    def noClearedValue(self):
        """ Test that getDataForTransaction properly handles when there is no cleared """
        self.transaction.cleared = None
        data = self.clearedColumn.getDataForTransaction(self.transaction)
        assert data is None, "Should get no data when the transaction cleared is None"

    def aClearedValue(self):
        """ Test that getDataForTransaction properly handles when there is a cleared """
        cleared = True
        self.transaction.cleared = cleared
        data = self.clearedColumn.getDataForTransaction(self.transaction)
        assert data == str(cleared), "Should get the same cleared as a string"

# Collect all test cases in this class
testcasesGetDataForTransaction = ["noClearedValue", "aClearedValue"]
suiteGetDataForTransaction = unittest.TestSuite(map(getDataForTransaction, testcasesGetDataForTransaction))

##########################################################

class setDataForTransaction(unittest.TestCase):
    """ Test cases of setDataForTransaction """
    
    def  setUp(self):
        """ Build the *** for the test """
        self.transaction = Transaction()
        self.transaction.cleared = None
        self.clearedColumn = ClearedColumn()

    def cleared(self):
        """ Test that setDataForTransaction properly handles when there is a cleared """
        value = True
        dataSet = self.clearedColumn.setDataForTransaction(self.transaction, value)
        assert dataSet, "Should have data set"
        assert self.transaction.cleared, "Should have the Transaction Cleared"

    def uncleared(self):
        """ Test that setDataForTransaction properly handles when there is a cleared """
        value = False
        dataSet = self.clearedColumn.setDataForTransaction(self.transaction, value)
        assert dataSet, "Should have data set"
        assert not self.transaction.cleared, "Should have the Transaction Uncleared"

# Collect all test cases in this class
testcasesSetDataForTransaction = ["cleared", "uncleared"]
suiteSetDataForTransaction = unittest.TestSuite(map(setDataForTransaction, testcasesSetDataForTransaction))

##########################################################

# Collect all test cases in this file
suites = [suiteGetDataForTransaction, suiteSetDataForTransaction]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()