from Qt.Model.Category.Test.suite import suite as category_suite
from Qt.Model.Statistics.Test.suite import suite as statistics_suite
from Qt.Model.Transaction.Test.suite import suite as transaction_suite

import unittest

suites = [category_suite,
          statistics_suite, 
          transaction_suite]
suite = unittest.TestSuite(suites)