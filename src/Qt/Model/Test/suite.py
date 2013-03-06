from amount_column_test import suite as amount_column_suite
from transaction_column_test import suite as transaction_column_suite

import unittest

suites = [amount_column_suite,
          transaction_column_suite]
suite = unittest.TestSuite(suites)