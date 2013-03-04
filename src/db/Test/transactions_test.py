from ORM.transaction import Transaction
from db.transactions import Transactions

import unittest

class add(unittest.TestCase):
    """ Test cases of add """
    
    def  setUp(self):
        """ Build the *** for the test """
        
    def addTransaction(self):
        """ Test that ... """
        transactionCountBefore = len(Transactions.all())
        transaction = Transaction(amount=200)
        Transactions.add(transaction)
        transactionCountAfter = len(Transactions.all())
        assert transactionCountBefore == transactionCountAfter-1, "Should have a new Transaction in the database"

# Collect all test cases in this class
testcasesAdd = ["addTransaction"]
suiteAdd = unittest.TestSuite(map(add, testcasesAdd))

##########################################################

# Collect all test cases in this file
suites = [suiteAdd]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()