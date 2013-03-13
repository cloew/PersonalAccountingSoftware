from ORM.category import Category
from Qt.Model.Category.name_column import NameColumn

import unittest

class getDataForCategory(unittest.TestCase):
    """ Test cases of getDataForCategory """
    
    def  setUp(self):
        """ Build the Category and the Column for the test """
        self.category = Category()
        self.nameColumn = NameColumn()
        
    def noName(self):
        """ Test that getDataForCategory properly handles when there is no name """
        self.category.name = None
        data = self.nameColumn.getDataForCategory(self.category)
        assert data is None, "Should get no data when the category name is None"

    def aName(self):
        """ Test that getDataForCategory properly handles when there is a name """
        name = "Some Name"
        self.category.name = name
        data = self.nameColumn.getDataForCategory(self.category)
        assert data == name, "Should get the same name as a string"

# Collect all test cases in this class
testcasesGetDataForCategory = ["noName", "aName"]
suiteGetDataForCategory = unittest.TestSuite(map(getDataForCategory, testcasesGetDataForCategory))

##########################################################

class setDataForCategory(unittest.TestCase):
    """ Test cases of setDataForCategory """
    
    def  setUp(self):
        """ Build the *** for the test """
        self.category = Category()
        self.category.name = None
        self.nameColumn = NameColumn()

    def nameString(self):
        """ Test that setDataForCategory properly handles when there is a description """
        value = "Some Name"
        dataSet = self.nameColumn.setDataForCategory(self.category, value)
        assert dataSet, "Should have data set"
        assert self.category.name == value, "Should have the Transaction Description"

# Collect all test cases in this class
testcasesSetDataForCategory = ["nameString"]
suiteSetDataForCategory = unittest.TestSuite(map(setDataForCategory, testcasesSetDataForCategory))

##########################################################

# Collect all test cases in this file
suites = [suiteGetDataForCategory, suiteSetDataForCategory]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()