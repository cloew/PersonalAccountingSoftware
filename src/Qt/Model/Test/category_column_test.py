from db.categories import Categories
from ORM.category import Category
from ORM.transaction import Transaction
from PyQt4.QtCore import QVariant
from Qt.Model.category_column import CategoryColumn

import unittest

class getDataForTransaction(unittest.TestCase):
    """ Test cases of getDataForTransaction """
    
    def  setUp(self):
        """ Build the *** for the test """
        self.transaction = Transaction()
        self.categoryColumn = CategoryColumn()
        self.name = "Category"
        self.category = Category(name=self.name)
        
    def noCategory(self):
        """ Test that getDataForTransaction properly handles when there is no category """
        self.transaction.category = None
        data = self.categoryColumn.getDataForTransaction(self.transaction)
        assert data is None, "Should get no data when the transaction category is None"

    def aCategory(self):
        """ Test that getDataForTransaction properly handles when there is a category """
        self.transaction.category = self.category
        data = self.categoryColumn.getDataForTransaction(self.transaction)
        assert str(data.toString()) == self.name, "Should get the category name as the data"

# Collect all test cases in this class
testcasesGetDataForTransaction = ["noCategory", "aCategory"]
suiteGetDataForTransaction = unittest.TestSuite(map(getDataForTransaction, testcasesGetDataForTransaction))

##########################################################

class setDataForTransaction(unittest.TestCase):
    """ Test cases of setDataForTransaction """
    
    def  setUp(self):
        """ Build the *** for the test """
        self.transaction = Transaction()
        self.transaction.category = None
        self.categoryColumn = CategoryColumn()

        if len(Categories.all()) == 0:
            self.category = Category(name="Some Category")
            Categories.add(self.category)

    def categoryString(self):
        """ Test that setDataForTransaction properly handles when there is a category """
        category = Categories.all()[0]
        value = QVariant(category.name)
        dataSet = self.categoryColumn.setDataForTransaction(self.transaction, value)
        assert dataSet, "Should have data set"
        assert self.transaction.category == category, "Should have the Transaction Category"
        assert self.transaction.category.name == category.name, "Should have the Transaction Category Name"

# Collect all test cases in this class
testcasesSetDataForTransaction = ["categoryString"]
suiteSetDataForTransaction = unittest.TestSuite(map(setDataForTransaction, testcasesSetDataForTransaction))

##########################################################

# Collect all test cases in this file
suites = [suiteGetDataForTransaction, suiteSetDataForTransaction]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()