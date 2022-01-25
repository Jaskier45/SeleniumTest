from selenium import webdriver
import pytest

class TestOrangeHRM():

    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome(executable_path="D:\андрій\Selenium\chromedriver.exe")
        self.driver.maximize_window()
        yield
        self.driver.close()

    def test_homePage(self, setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        assert self.driver.title == "OrangeHRM"
    
    def test_login(self, setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        self.driver.find_element_by_xpath("//*[@id='btnLogin']").click()
        # self.driver.get("https://opensource-demo.orangehrmlive.com/")
        # self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        # self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        # self.driver.find_element_by_id("btnLogin").click()
        assert self.driver.title == "OrangeHRM"

# pytest -v -s --html=report.html --self-contained-html testcase_pytest.py
# pytest -v -s testcase_pytest.py