from selenium import webdriver
import HTMLTestRunner
import unittest

class OrangeHRMTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="D:\андрій\Selenium\chromedriver.exe")
        cls.driver.maximize_window()
    
    def test_homePageTitle(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.assertEqual("OrangeHRM", self.driver.title, "website title is not matching")

    def test_login(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        self.driver.find_element_by_xpath("//*[@id='btnLogin']").click()
        self.assertEqual("OrangeHRM", self.driver.title, "website title is not matching")
        
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test compleat...")

if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner.HTMLTestRunner(output='D:\\андрій\\Selenium\\Reports'))
    