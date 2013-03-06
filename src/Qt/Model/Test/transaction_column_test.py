from db.transactions import Transactions
from Qt.Model.transaction_column import TransactionColumn

import unittest

class getHorizontalHeader(unittest.TestCase):
    """ Test cases of getHorizontalHeader """
    
    def  setUp(self):
        """ Build the *** for the test """
        self.transactionColumn = TransactionColumn()
        
    def header(self):
        """ Test that the header is properly returned """
        assert TransactionColumn.header_name == self.transactionColumn.getHorizontalHeader(), "Should receive the classes header_name variable for the horizontal header"

# Collect all test cases in this class
testcasesGetHorizontalHeader = ["header"]
suiteGetHorizontalHeader = unittest.TestSuite(map(getHorizontalHeader, testcasesGetHorizontalHeader))

##########################################################

class getTransactionForRow(unittest.TestCase):
    """ Test cases of getTransactionForRow """
    
    def  setUp(self):
        """ Build the *** for the test """
        self.transactionColumn = TransactionColumn()
        
    def validRow(self):
        """ Test that a- proper Transaction is returned when a valid row is provided """
        assert len(Transactions.all()) > 0, "Should have a transaction"
        row = len(Transactions.all()) - 1
        assert Transactions.all()[row] == self.transactionColumn.getTransactionForRow(row), "Should receive the Transaction in the given row"

    def invalidRow(self):
        """ Test that None is returned when a valid row is provided """
        assert len(Transactions.all()) > 0, "Should have a transaction"
        row = len(Transactions.all())
        assert self.transactionColumn.getTransactionForRow(row) is None, "Should receive None when the row is too high"

# Collect all test cases in this class
testcasesGetTransactionForRow = ["validRow", "invalidRow"]
suiteGetTransactionForRow = unittest.TestSuite(map(getTransactionForRow, testcasesGetTransactionForRow))

##########################################################

# Collect all test cases in this file
suites = [suiteGetHorizontalHeader, suiteGetTransactionForRow]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()