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

# Collect all test cases in this file
suites = [suiteGetHorizontalHeader]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()