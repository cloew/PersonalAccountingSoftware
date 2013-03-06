from ORM.transaction import Transaction
from Qt.Model.amount_column import AmountColumn

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
        assert data.toString() == "$12.34", "Should get the amount data formatted as a number in dollars"

# Collect all test cases in this class
testcasesGetDataForTransaction = ["noAmount", "anAmount"]
suiteGetDataForTransaction = unittest.TestSuite(map(getDataForTransaction, testcasesGetDataForTransaction))

##########################################################

# Collect all test cases in this file
suites = [suiteGetDataForTransaction]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()