from lib2to3.pgen2 import driver
from tkinter import W
from selenium import webdriver
import HTMLTestRunner
import unittest
import time

# options = webdriver.ChromeOptions()
# driver = webdriver.Chrome(options=options)


# try:
#     driver.maximize_window()
#     driver.get("https://www.hltv.org/")
#     driver.find_element_by_class_name("navsignin").click()
#     time.sleep(5)
#     # rame = driver.find_element_by_xpath("//*[@id='loginpopup']/div")
#     # driver.switch_to.default_content(rame)
#     driver.find_element_by_xpath("//*[@id='loginpopup']/form/input[1]").send_keys("123456")
#     time.sleep(5)
# except Exception as ex:
#     print(ex)
# finally:
#     driver.close()
#     driver.quit()

class hltvTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="D:\андрій\Selenium\chromedriver.exe")
        cls.driver.maximize_window()
    
    def test_login (self):
        self.driver.get("https://www.hltv.org/")
        # print(self.driver.title)
        self.assertEqual("CS:GO News & Coverage | HLTV.org", self.driver.title, "Test is done")
        time.sleep(1)

    def test_auth (self):
        self.driver.get("https://www.hltv.org/")
        self.driver.find_element_by_class_name("navsignin").click()
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_xpath("//*[@id='loginpopup']/form/input[1]").send_keys("123456")
        self.driver.find_element_by_xpath("//*[@id='loginpopup']/form/input[2]").send_keys("123456")
        self.driver.find_element_by_xpath("//*[@id='loginpopup']/form/button").click
        time.sleep(3)

    def test_results (self):
        self.driver.get("https://www.hltv.org/")
        self.driver.find_element_by_class_name("navresults").click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/div[3]/div[4]/div[1]/div[2]/div[2]/a/div").click()
        time.sleep(3)

    def test_stats (self):
        self.driver.get("https://www.hltv.org/")
        self.driver.find_element_by_class_name("navstats").click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/div[3]/div[7]/div[1]/div[3]/a").click()
        time.sleep(3)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test complete...")


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner.HTMLTestRunner(output='D:\\андрій\\Selenium\\Reports'))

# 

    
