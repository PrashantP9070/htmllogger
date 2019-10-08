import pytest
from selenium import webdriver
from htmllogger.Htmllogger import HTMlLogger
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

@pytest.fixture()
def setup(request):
    print("initiating driver")
    logger = HTMlLogger()
    binary = FirefoxBinary('Path to your firefox_binary')
    driver = webdriver.Firefox(firefox_binary=binary,executable_path=r"path to geckodriver")
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
            self.logger.assert_testcase_log("Testcase :Testing Title")
            print("Verify title...")
            assert "Selenium Easy" in self.driver.title
            self.logger.assert_step_log("Successfully verified title")
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