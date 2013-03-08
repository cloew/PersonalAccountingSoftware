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
        assert len(labels) == len(self.names), "Should have a label for each entry in the name's list"
        for label in labels:
            assert label in self.names, "The label should be in the names"

# Collect all test cases in this class
testcasesGetLabels = ["hasLabels"]
suiteGetLabels = unittest.TestSuite(map(getLabels, testcasesGetLabels))

##########################################################

# Collect all test cases in this file
suites = [suiteGetLabels]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()