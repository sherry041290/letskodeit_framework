from pages.login.login_page import LoginPage
from utilities.result_status import ResultStatus
import unittest
import pytest
import time


@pytest.mark.usefixture("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=2)
    def classSetUp(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = ResultStatus(self.driver)

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.clearFields()
        # self.lp.logout()
        self.lp.wait(10)
        self.lp.login("test@email.com", "abcabc")
        result1 = self.lp.verifyTitle()
        self.ts.mark(result1, "Title Verification")
        result2 = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_validLogin", result2, "Login Verification")
        self.driver.quit()

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp.logout()
        self.lp.login("test@email.com", "abcabcabc")
        result = self.lp.verifyLoginFailed()
        assert result == True
        self.lp.wait(10)
