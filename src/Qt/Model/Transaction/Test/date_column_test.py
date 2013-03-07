from datetime import date, datetime
from dateutil import parser
from ORM.transaction import Transaction
from PyQt4.QtCore import QVariant
from Qt.Model.Transaction.date_column import DateColumn

import unittest

class getDataForTransaction(unittest.TestCase):
    """ Test cases of getDataForTransaction """
    
    def  setUp(self):
        """ Build the *** for the test """
        self.transaction = Transaction()
        self.dateColumn = DateColumn()
        
    def noDate(self):
        """ Test that getDataForTransaction properly handles when there is no date """
        self.transaction.date = None
        data = self.dateColumn.getDataForTransaction(self.transaction)
        assert data is None, "Should get no data when the transaction date is None"

    def aDate(self):
        """ Test that getDataForTransaction properly handles when there is a date """
        today = date.today()
        self.transaction.date = today
        data = self.dateColumn.getDataForTransaction(self.transaction)
        assert parser.parse(str(data.toString())) == datetime(today.year, today.month, today.day), "Should get the same date as a string"

# Collect all test cases in this class
testcasesGetDataForTransaction = ["noDate", "aDate"]
suiteGetDataForTransaction = unittest.TestSuite(map(getDataForTransaction, testcasesGetDataForTransaction))

##########################################################

class setDataForTransaction(unittest.TestCase):
    """ Test cases of setDataForTransaction """
    
    def  setUp(self):
        """ Build the *** for the test """
        self.transaction = Transaction()
        self.transaction.date = None
        self.dateColumn = DateColumn()
        
    def badString(self):
        """ Test that setDataForTransaction properly handles a bad string """
        value = QVariant("abcd")
        dataSet = self.dateColumn.setDataForTransaction(self.transaction, value)
        assert dataSet is None, "Should get not have data Set when the value is a bad string"
        assert self.transaction.date is None, "Should not have the Transaction Amount set"

    def dateString(self):
        """ Test that setDataForTransaction properly handles when there is a date """
        value = QVariant("3/5/2013")
        dataSet = self.dateColumn.setDataForTransaction(self.transaction, value)
        assert dataSet, "Should have data set"
        assert self.transaction.date == datetime(2013, 3, 5), "Should have the Transaction Date"

# Collect all test cases in this class
testcasesSetDataForTransaction = ["badString", "dateString"]
suiteSetDataForTransaction = unittest.TestSuite(map(setDataForTransaction, testcasesSetDataForTransaction))

##########################################################

# Collect all test cases in this file
suites = [suiteGetDataForTransaction, suiteSetDataForTransaction]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()