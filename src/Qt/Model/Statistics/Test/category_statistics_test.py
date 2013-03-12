from db.categories import Categories
from ORM.category import Category
from ORM.transaction import Transaction
from Qt.Model.Statistics.category_statistics import CategoryStatistics

from reset_db import ResetDatabase
from seed import AddCategory, AddTransaction

import unittest

class getCategoriesAndTransactions(unittest.TestCase):
    """ Test cases of getCategoriesAndTransactions """
    
    def  setUp(self):
        """ Build the *** for the test """
        ResetDatabase()
        self.names = ["QWERTY", "ASDF", "ZXCV", "POIU"]
        self.transactionAmounts = {self.names[0]:[100],
                                   self.names[1]:[200],
                                   self.names[2]:[300],
                                   self.names[3]:[100, 300]}
        self.categoryStatistics = CategoryStatistics()
        self.categoryStatistics.categoryTransactions = {}
        self.categories = []
        for name in self.names:
            category = AddCategory(name=name)
            self.categories.append(category)
            for amount in self.transactionAmounts[name]:
                transaction = AddTransaction(amount=amount)
                transaction.category = category
        
    def hasCategories(self):
        """ Test that the Category Transactions dictionary has all the needed Catgeories """
        self.categoryStatistics.getCategoriesAndTransactions()
        assert len(self.categories) == len(self.categoryStatistics.categoryTransactions.keys()), "Should have a Category for each entry in the Catgeories list"
        for category in self.categoryStatistics.categoryTransactions:
            assert category in self.categories, "The Category should be in the categories list"

    def hasTransactions(self):
        """ Test that the proper number of transactions are received """
        self.categoryStatistics.getCategoriesAndTransactions()
        for category in self.categoryStatistics.categoryTransactions:
            assert category.name in self.transactionAmounts, "Should have transactions stored for the Category"
            assert len(self.transactionAmounts[category.name]) == len(self.categoryStatistics.categoryTransactions[category]), \
                "Should have the same number of transactions for both the Transaction Amounts and the Transactions per Category """

# Collect all test cases in this class
testcasesGetCategoriesAndTransactions = ["hasCategories", "hasTransactions"]
suiteGetCategoriesAndTransactions = unittest.TestSuite(map(getCategoriesAndTransactions, testcasesGetCategoriesAndTransactions))

##########################################################

class getTotalExpenses(unittest.TestCase):
    """ Test cases of getTotalExpenses """
    
    def  setUp(self):
        """ Build the *** for the test """
        ResetDatabase()
        self.names = ["QWERTY", "ASDF", "ZXCV", "POIU"]
        self.transactionAmounts = {self.names[0]:[100],
                                   self.names[1]:[200],
                                   self.names[2]:[300],
                                   self.names[3]:[100, 300]}
        self.categoryStatistics = CategoryStatistics()
        self.categoryStatistics.categoryTransactions = {}
        self.categories = []
        for name in self.names:
            category = Category(name=name)
            self.categories.append(category)
            self.categoryStatistics.categoryTransactions[category] = []
            for amount in self.transactionAmounts[name]:
                transaction = Transaction(amount=amount)
                self.categoryStatistics.categoryTransactions[category].append(transaction)
        
    def hasCategories(self):
        """ Test that the dictionary of Transaction totals has all the proper Categories """
        self.categoryStatistics.getTotalExpenses()
        assert len(self.categories) == len(self.categoryStatistics.totalForCategory.keys()), "Should have a Category for each entry in the Catgeories list"
        for category in self.categoryStatistics.totalForCategory:
            assert category in self.categories, "The Category should be in the categories list"

    def hasTotalPerCategory(self):
        """ Test that the list of labels has all the needed labels """
        self.categoryStatistics.getTotalExpenses()
        for category in self.categoryStatistics.totalForCategory:
            total = 0
            for amount in self.transactionAmounts[category.name]:
                total += amount
            assert self.categoryStatistics.totalForCategory[category] == total, "The Total per Category should be the total of all the Transactions given to it"

    def hasTotal(self):
        """ Test that the proper number of transactions are received """
        self.categoryStatistics.getTotalExpenses()
        assert self.categoryStatistics.total == 1000, "Should have a 1000 for the total"

# Collect all test cases in this class
testcasesGetTotalExpenses = ["hasCategories", "hasTotalPerCategory", "hasTotal"]
suiteGetTotalExpenses = unittest.TestSuite(map(getTotalExpenses, testcasesGetTotalExpenses))

##########################################################

class getLabels(unittest.TestCase):
    """ Test cases of getLabels """
    
    def  setUp(self):
        """ Build the *** for the test """
        self.names = ["QWERTY", "ASDF", "ZXCV"]
        self.categoryStatistics = CategoryStatistics()
        self.categoryStatistics.categoryTransactions = {}
        for name in self.names:
            category = Category(name=name)
            self.categoryStatistics.categoryTransactions[category] = []
        
    def hasLabels(self):
        """ Test that the list of labels has all the needed labels """
        labels = self.categoryStatistics.getLabels()
        assert len(labels) == len(self.names), "Should have a label for each entry in the names list"
        for label in labels:
            assert label in self.names, "The label should be in the names list"

# Collect all test cases in this class
testcasesGetLabels = ["hasLabels"]
suiteGetLabels = unittest.TestSuite(map(getLabels, testcasesGetLabels))

##########################################################

class getPercentages(unittest.TestCase):
    """ Test cases of getPercentages """
    
    def  setUp(self):
        """ Build the *** for the test """
        self.names = ["First", "Second", "Third", "Fourth"]
        self.values = [.1, .2, .3, .4]
        self.total = 1000
        self.categoryStatistics = CategoryStatistics()
        self.categoryStatistics.totalForCategory = {}
        self.categoryStatistics.total = self.total
        for i in range(len(self.names)):
            name = self.names[i]
            value = self.values[i]
            category = Category(name=name)
            self.categoryStatistics.totalForCategory[category] = value*self.total
        
    def hasPercentages(self):
        """ Test that the list of percentages has all the needed percentages """
        percentages = self.categoryStatistics.getPercentages()
        assert len(percentages) == len(self.values), "Should have a percentage for each entry in the vakues list"
        for percentage in percentages:
            assert percentage in self.values, "The percentage should be in the values list"

# Collect all test cases in this class
testcasesGetPercentages = ["hasPercentages"]
suiteGetPercentages = unittest.TestSuite(map(getPercentages, testcasesGetPercentages))

##########################################################

# Collect all test cases in this file
suites = [suiteGetCategoriesAndTransactions, suiteGetTotalExpenses, suiteGetLabels, suiteGetPercentages]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()