from reset_db import ResetDatabase

from ORM.transaction import Transaction
from db.transactions import Transactions

import datetime
import unittest

class TransactionHelper:
    amount = 200
    description = "Some Description"
    income = False
    date = datetime.date(2013, 3, 1)

def BuildTransaction():
    """ Builds and returns a new transaction """
    return Transaction(amount=TransactionHelper.amount, description=TransactionHelper.description, income=TransactionHelper.income, date=TransactionHelper.date)

class add(unittest.TestCase):
    """ Test cases of add """
    
    def  setUp(self):
        """ Build the *** for the test """
        self.transaction = BuildTransaction()
        
    def addTransaction(self):
        """ Test that adding a transaction adds a new record """
        transactionCountBefore = len(Transactions.all())
        Transactions.add(self.transaction)
        transactionCountAfter = len(Transactions.all())
        assert transactionCountBefore == transactionCountAfter-1, "Should have a new Transaction in the database"

    def transactionSaved(self):
        """ Test that the Transaction is saved properly """
        Transactions.add(self.transaction)
        found_transaction = Transactions.find(self.transaction)
        assert found_transaction.amount == TransactionHelper.amount, "Amount should be the same"
        assert found_transaction.description == TransactionHelper.description, "Description should be the same"
        assert found_transaction.income == TransactionHelper.income, "Income should be the same"
        assert found_transaction.date == TransactionHelper.date, "Date should be the same"

# Collect all test cases in this class
testcasesAdd = ["addTransaction", "transactionSaved"]
suiteAdd = unittest.TestSuite(map(add, testcasesAdd))

##########################################################

class all(unittest.TestCase):
    """ Test cases of all """
    
    def  setUp(self):
        """ Build the *** for the test """
        ResetDatabase()
        
    def findAllTransactions_One(self):
        """ Test that a transaction is returned in all the transactions """
        transactions = Transactions.all()
        assert len(transactions) == 0, "Should have no entries"
        transaction = BuildTransaction()
        Transactions.add(transaction)
        transactions = Transactions.all()
        assert len(transactions) == 1, "Should have a single entry"
        assert transactions[0] is transaction, "Should have received the added transaction"

    def findAllTransactions_Multiple(self):
        """ Test that multiple transactions are returned in all the transactions """
        transactions = Transactions.all()
        assert len(transactions) == 0, "Should have no entries"
        transaction1 = BuildTransaction()
        Transactions.add(transaction1)
        transaction2 = BuildTransaction()
        Transactions.add(transaction2)
        transactions = Transactions.all()
        assert len(transactions) == 2, "Should have a multiple entries"
        assert transaction1 in transactions, "Should have received the first added transaction"
        assert transaction2 in transactions, "Should have received the second added transaction"

# Collect all test cases in this class
testcasesAll = ["findAllTransactions_One", "findAllTransactions_Multiple"]
suiteAll = unittest.TestSuite(map(all, testcasesAll))

##########################################################

class find(unittest.TestCase):
    """ Test cases of find """
    
    def  setUp(self):
        """ Build the *** for the test """
        self.transaction = BuildTransaction()
        
    def findTransaction_Success(self):
        """ Test that a transaction in the database can be found """
        Transactions.add(self.transaction)
        found_transaction = Transactions.find(self.transaction)
        assert found_transaction is self.transaction, "Should receive the same transaction that was just added"

    def findTransaction_Failure(self):
        """ Test that when a transaction doesn't exist no record is returned """
        found_transaction = Transactions.find(self.transaction)
        assert found_transaction is None, "Should get no transaction"

# Collect all test cases in this class
testcasesFind = ["findTransaction_Success", "findTransaction_Failure"]
suiteFind = unittest.TestSuite(map(find, testcasesFind))

##########################################################

# Collect all test cases in this file
suites = [suiteAdd, suiteAll, suiteFind]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()