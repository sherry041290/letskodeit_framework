from pages.home.login_page import Loginpage
import unittest
import pytest


@pytest.mark.usefixture("oneTimeSetUp","setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=2)
    def classSetUp(self, oneTimeSetUp):
        self.lg = Loginpage(self.driver)

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lg.clearFields()
        self.lg.login("test@email.com", "abcabc")
        result = self.lg.verifyLoginSuccessful()
        assert result == True

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lg.login("test@email.com", "abcabccc")
        result = self.lg.verifyLoginFailed()
        assert result == True

