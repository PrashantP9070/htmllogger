htmllogger
=====================

<img src="./htmllogger_logo.png"  height="150">

Python library provides customized Test Report for selenium or any other automation framework

Introduction.
============

* A htmllogger is designed inorder to provide customized logs for autumated tests.
* So user can able to write step log and test case details.

  

Main Features:
=============

* Create an interactive html report for automation suite.
* It can be easily integrated with unit testing frameworks eg. unittest,pytest
* It provides three methods inorder to generate report for tests.
* It combines execution result of all tests which are executed in batch.

Installation
=============
pip install:

```shell
> pip install htmllogger
```
Pre-Requisite
=============
1) You will have to initialise htmllogger object to start use of reporting functions.
2) At the start of each test you have to use 'assert_testcase_log("Test_Case_name")',
3) Inorder to detailing of testcase steps you will have to use 'assert_step_log('Test_step_details')'
4) To handle failures you will write your test in 'Try Except' block and in except block call 
   'assert_step_fail_log(driver, str(e))' pass First argument as driver object to capture screenshot of failure.
    second argument is except object converted in string format.
	
Follow below examples for more understanding...	
	
Examples
=============
1. Python - Unittest

```python
import unittest
from selenium import webdriver
from Main.Utility import HTMlLogger
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

class InputFormsCheck2(unittest.TestCase):

    # Opening browser.
    def setUp(self):
        self.logger = HTMlLogger()
        binary = FirefoxBinary('Binary Path for your browser')
        self.driver = webdriver.Firefox(firefox_binary=binary,
                                                executable_path=r"/geckodriver.exe")

    # Testing Single Input Field.
    def test_singleInputField(self):
        self.logger.assert_testcase_log("Test Single Input Field")   # ****Writting Test case Name
        try:
            pageUrl = "http://www.seleniumeasy.com/test/basic-first-form-demo.html"
            driver = self.driver
            driver.maximize_window()
            driver.get(pageUrl)

            # Finding "Single input form" input text field by id. And sending keys(entering data) in it.
            eleUserMessage = driver.find_element_by_id("user-message")
            eleUserMessage.clear()
            eleUserMessage.send_keys("Test Python")
            self.logger.assert_step_log("Entered text [Test Python] in [user-message] EditBox.")         # ****Writting step log
            # Finding "Show Your Message" button element by css selector using both id and class name. And clicking it.
            eleShowMsgBtn = driver.find_element_by_css_selector('#get-input > .btn')
            eleShowMsgBtn.click()
            self.logger.assert_step_log("Clicked on [Show Message] Button.")                         # ****Writting step log
            # Checking whether the input text and output text are same using assertion.
            eleYourMsg = driver.find_element_by_id("display")
            assert "Test Python" in eleYourMsg.text
        except Exception as e:
            self.logger.assert_step_fail_log(driver, str(e))        # Capturing failure

    # Closing the browser.
    def tearDown(self):
        self.driver.close()


# This line sets the variable “__name__” to have a value “__main__”.
# If this file is being imported from another module then “__name__” will be set to the other module's name.
if __name__ == "__main__":
    unittest.main()
```
2. Python - Pytest

Inside test_Login.py
```python
import pytest
from selenium import webdriver
from Main.Utility import HTMlLogger
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

@pytest.fixture()
def setup(request):
    print("initiating driver")
    logger = HTMlLogger()
    binary = FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe')
    driver = webdriver.Firefox(firefox_binary=binary,executable_path=r"D:/SeleniumTest/SeleniumTest/MainResources/drivers/geckodriver.exe")
    request.instance.driver = driver
    request.instance.logger = logger
    driver.get("http://seleniumeasy.com/test")
    driver.maximize_window()

    yield driver
    driver.close()

@pytest.mark.usefixtures("setup")
class TestExample:
    def test_title(self):
        try:
            self.logger.assert_testcase_log("Testcase :Testing Title")            # ****Writting Test case Name
            print("Verify title...")
            assert "Selenium Easy" in self.driver.title
            self.logger.assert_step_log("Successfully verified title")            # ****Writting step log
        except Exception as e:
            self.logger.assert_step_fail_log(self.driver, str(e))
    def test_content_text(self):
        self.logger.assert_testcase_log("Testcase : Testing Content")
        try:
            print("Verify content on the page...")
            centerText = self.driver.find_element_by_css_selector('.tab-content .text-center').text
            self.logger.assert_step_log("Verify content on page")
            assert "WELCOME TO SELENIUM EASY DEMO" == centerText
        except Exception as e:
            self.logger.assert_step_fail_log(self.driver, str(e))
```

