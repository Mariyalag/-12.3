import unittest
from tests_12_3 import RunnerTest
from tests_12_3 import TournamentTest

test_suite = unittest.TestSuite()
test_loader = unittest.TestLoader()

test_suite.addTests(test_loader.loadTestsFromTestCase(RunnerTest))
test_suite.addTests(test_loader.loadTestsFromTestCase(TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(test_suite)
