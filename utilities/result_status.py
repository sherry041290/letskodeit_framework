"""
@package utilities

CheckPoint class implementation
It provides functionality to assert the result

Example:
    self.check_point.markFinal("Test Name", result, "Message")
"""
import utilities.custom_logger as cl
import logging
from base.selenium_driver import SeleniumDriver


class ResultStatus(SeleniumDriver):

    log = cl.customLogger(logging.INFO)

    def __init__(self, driver):
        super().__init__(driver)
        self.resultList = []

    def setResult(self, result, result_message):
        try:
            if result is not None:
                if result:
                    self.resultList.append("PASS")
                    self.log.info("### VERIFICATION SUCCESSFUL :: + " + result_message)
                else:
                    self.resultList.append("FAIL")
                    self.log.error("### VERIFICATION FAILED :: + " + result_message)
            else:
                self.resultList.append("FAIL")
                self.log.error("### VERIFICATION FAILED :: + " + result_message)
        except:
            self.resultList.append("FAIL")
            self.log.error("### Exception Occurred !!!")

    def mark(self, result, result_message):
        """
        Mark the result of the verification point in a test case
        """
        self.setResult(result, result_message)

    def markFinal(self, test_name, result, result_message):
        """
        Mark the final result of the verification point in a test case
        This needs to be called at least once in a test case
        This should be final test status of the test case
        """
        self.setResult(result, result_message)

        if "FAIL" in self.resultList:
            self.log.error(test_name + " ### TEST FAILED")
            self.resultList.clear()
            assert True == False
        else:
            self.log.info(test_name + " ### TEST SUCCESSFUL")
            self.resultList.clear()
            assert True == True

