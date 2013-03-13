from ORM.transaction import Transaction
from Qt.Model.Transaction.amount_column import AmountColumn

import unittest

class getDataForTransaction(unittest.TestCase):
    """ Test cases of getDataForTransaction """
    
    def  setUp(self):
        """ Build the *** for the test """
        self.transaction = Transaction()
        self.amountColumn = AmountColumn()
        
    def noAmount(self):
        """ Test that getDataForTransaction properly handles when there is no amount """
        self.transaction.amount = None
        data = self.amountColumn.getDataForTransaction(self.transaction)
        assert data is None, "Should get no data when the transaction amount is None"

    def anAmount(self):
        """ Test that getDataForTransaction properly handles when there is an amount """
        amount = 1234
        self.transaction.amount = amount
        data = self.amountColumn.getDataForTransaction(self.transaction)
        assert data == "$12.34", "Should get the amount data formatted as a number in dollars"

# Collect all test cases in this class
testcasesGetDataForTransaction = ["noAmount", "anAmount"]
suiteGetDataForTransaction = unittest.TestSuite(map(getDataForTransaction, testcasesGetDataForTransaction))

##########################################################

class setDataForTransaction(unittest.TestCase):
    """ Test cases of setDataForTransaction """
    
    def  setUp(self):
        """ Build the *** for the test """
        self.transaction = Transaction()
        self.transaction.amount = None
        self.amountColumn = AmountColumn()
        
    def badString(self):
        """ Test that setDataForTransaction properly handles a bad string """
        value = "abcd"
        dataSet = self.amountColumn.setDataForTransaction(self.transaction, value)
        assert dataSet is None, "Should get not have data Set when the value is a bad string"
        assert self.transaction.amount is None, "Should not have the Transaction Amount set"

    def stringOfDollars(self):
        """ Test that setDataForTransaction properly handles when there is an amount """
        value = "$12.34"
        dataSet = self.amountColumn.setDataForTransaction(self.transaction, value)
        assert dataSet, "Should have data set"
        assert self.transaction.amount == 1234, "Should have the Transaction Amount in cents"

    def decimalString(self):
        """ Test that setDataForTransaction properly handles when there is an amount """
        value = "12.34"
        dataSet = self.amountColumn.setDataForTransaction(self.transaction, value)
        assert dataSet, "Should have data set"
        assert self.transaction.amount == 1234, "Should have the Transaction Amount in cents"

# Collect all test cases in this class
testcasesSetDataForTransaction = ["badString", "stringOfDollars", "decimalString"]
suiteSetDataForTransaction = unittest.TestSuite(map(setDataForTransaction, testcasesSetDataForTransaction))

##########################################################

# Collect all test cases in this file
suites = [suiteGetDataForTransaction, suiteSetDataForTransaction]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()