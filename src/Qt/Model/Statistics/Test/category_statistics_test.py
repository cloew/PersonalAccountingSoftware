from ORM.category import Category
from Qt.Model.Statistics.category_statistics import CategoryStatistics

import unittest

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
suites = [suiteGetLabels, suiteGetPercentages]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()