import unittest
from selenium import webdriver
from htmllogger.Htmllogger import HTMlLogger
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

class InputFormsCheck2(unittest.TestCase):

    # Opening browser.
    def setUp(self):
        self.logger = HTMlLogger('directory path in which report to be created')
        binary = FirefoxBinary('Binary Path for your browser')
        self.driver = webdriver.Firefox(firefox_binary=binary,
                                                executable_path="driver path")

    # Testing Single Input Field.
    def test_singleInputField(self):
        self.logger.assert_testcase_log("Test Single Input Field")
        try:
            pageUrl = "http://www.seleniumeasy.com/test/basic-first-form-demo.html"
            driver = self.driver
            driver.maximize_window()
            driver.get(pageUrl)

            # Finding "Single input form" input text field by id. And sending keys(entering data) in it.
            eleUserMessage = driver.find_element_by_id("user-message")
            eleUserMessage.clear()
            eleUserMessage.send_keys("Test Python")
            self.logger.assert_step_log("Entered text [Test Python] in [user-message] EditBox.")         # Writting step log
            # Finding "Show Your Message" button element by css selector using both id and class name. And clicking it.
            eleShowMsgBtn = driver.find_element_by_css_selector('#get-input > .btn')
            eleShowMsgBtn.click()
            self.logger.assert_step_log("Clicked on [Show Message] Button.")
            # Checking whether the input text and output text are same using assertion.
            eleYourMsg = driver.find_element_by_id("display")
            assert "Test Python" in eleYourMsg.text
        except Exception as e:
            self.logger.assert_step_fail_log(driver, str(e))

    # Closing the browser.
    def tearDown(self):
        self.driver.close()


# This line sets the variable “__name__” to have a value “__main__”.
# If this file is being imported from another module then “__name__” will be set to the other module's name.
if __name__ == "__main__":
    unittest.main()