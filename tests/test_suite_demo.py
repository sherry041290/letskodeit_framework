from tests.login.login_test import LoginTests
from tests.register_page.enroll_course_csvdata_test import EnrollCSVDataTest
import unittest

# Get all testa from test classes
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
tc2 = unittest.TestLoader().loadTestsFromTestCase(EnrollCSVDataTest)

# Create a test suite combining all test classes
smokeTest = unittest.TestSuite([tc1,tc2])
unittest.TextTestRunner(verbosity=2).run(smokeTest)

