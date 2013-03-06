from reset_db import ResetDatabase

from db.Test.suite import suite as db_suite
from Qt.Test.suite import suite as qt_suite
import unittest

# Collect all the test suites
suites = [db_suite, qt_suite]
alltests = unittest.TestSuite(suites)

# Run all the tests
if __name__ == "__main__":
    ResetDatabase() # Reset Database to make sure it is fully up to date
    runner = unittest.TextTestRunner()
    runner.run(alltests)
