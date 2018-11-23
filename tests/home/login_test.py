from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.home.login_page import Loginpage
import unittest


class LoginTests(unittest.TestCase):

    def test_validLogin(self):
        base_url = "https://letskodeit.teachable.com/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(base_url)

        lg = Loginpage(driver)
        lg.login("test@email.com", "abcabc")
        userIcon = driver.find_element(By.XPATH, ".//*[@id='navbar']//span[text()='Test User']")
        if userIcon is not None:
            print("Login Successful")
        else:
            print("Login Failed")

