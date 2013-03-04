from ORM.transaction import Transaction
from db.transactions import Transactions

import datetime
import unittest

class add(unittest.TestCase):
    """ Test cases of add """
    
    def  setUp(self):
        """ Build the *** for the test """
        self.amount = 200
        self.description = "Some Description"
        self.income = False
        self.date = datetime.date(2013, 3, 1)
        self.transaction = Transaction(amount=self.amount, description=self.description, income=self.income, date=self.date)
        
    def addTransaction(self):
        """ Test that ... """
        transactionCountBefore = len(Transactions.all())
        Transactions.add(self.transaction)
        transactionCountAfter = len(Transactions.all())
        assert transactionCountBefore == transactionCountAfter-1, "Should have a new Transaction in the database"

    def transactionSaved(self):
        """ Test that the Transaction is saved properly """
        Transactions.add(self.transaction)
        found_transaction = Transactions.find(self.transaction)
        assert found_transaction.amount == self.amount, "Amount should be the same"
        assert found_transaction.description == self.description, "Description should be the same"
        assert found_transaction.income == self.income, "Income should be the same"
        assert found_transaction.date == self.date, "Date should be the same"

# Collect all test cases in this class
testcasesAdd = ["addTransaction", "transactionSaved"]
suiteAdd = unittest.TestSuite(map(add, testcasesAdd))

##########################################################

# Collect all test cases in this file
suites = [suiteAdd]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()