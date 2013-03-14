from ORM.transaction import Transaction
from Qt.Model.Transaction.reconciled_column import ReconciledColumn

import unittest

class getDataForTransaction(unittest.TestCase):
    """ Test cases of getDataForTransaction """
    
    def  setUp(self):
        """ Build the Transaction and Column for the test """
        self.transaction = Transaction()
        self.reconciledColumn = ReconciledColumn()
        
    def noReconciledValue(self):
        """ Test that getDataForTransaction properly handles when there is no reconciled """
        self.transaction.reconciled = None
        data = self.reconciledColumn.getDataForTransaction(self.transaction)
        assert data is None, "Should get no data when the transaction reconciled is None"

    def aReconciledValue(self):
        """ Test that getDataForTransaction properly handles when there is a reconciled """
        reconciled = True
        self.transaction.reconciled = reconciled
        data = self.reconciledColumn.getDataForTransaction(self.transaction)
        assert data == reconciled, "Should get the same reconciled as a string"

# Collect all test cases in this class
testcasesGetDataForTransaction = ["noReconciledValue", "aReconciledValue"]
suiteGetDataForTransaction = unittest.TestSuite(map(getDataForTransaction, testcasesGetDataForTransaction))

##########################################################

class setDataForTransaction(unittest.TestCase):
    """ Test cases of setDataForTransaction """
    
    def  setUp(self):
        """ Build the *** for the test """
        self.transaction = Transaction()
        self.transaction.reconciled = None
        self.reconciledColumn = ReconciledColumn()

    def reconciled(self):
        """ Test that setDataForTransaction properly handles when there is a reconciled """
        value = True
        dataSet = self.reconciledColumn.setDataForTransaction(self.transaction, value)
        assert dataSet, "Should have data set"
        assert self.transaction.reconciled, "Should have the Transaction Reconciled"

    def unreconciled(self):
        """ Test that setDataForTransaction properly handles when there is a reconciled """
        value = False
        dataSet = self.reconciledColumn.setDataForTransaction(self.transaction, value)
        assert dataSet, "Should have data set"
        assert not self.transaction.reconciled, "Should have the Transaction Unreconciled"

# Collect all test cases in this class
testcasesSetDataForTransaction = ["reconciled", "unreconciled"]
suiteSetDataForTransaction = unittest.TestSuite(map(setDataForTransaction, testcasesSetDataForTransaction))

##########################################################

# Collect all test cases in this file
suites = [suiteGetDataForTransaction, suiteSetDataForTransaction]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()