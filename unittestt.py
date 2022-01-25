import unittest
from selenium import webdriver
from selenium.webdriver.firefox import options

# driver = webdriver.Chrome(options=options)

class SearchTest(unittest.TestCase):
    def test_google(self):
        driver = webdriver.Chrome(executable_path="D:\андрій\Selenium\chromedriver.exe")
        driver.get("https://www.google.com/")
        titleOfBrowser = driver.title
        #self.assertEqual("Google", titleOfBrowser, "website title is the same")
        self.assertNotEqual("Gogle", titleOfBrowser, "Different title")
        # self.driver.close()



    # def test_hltv(self):
    #     self.driver = webdriver.Chrome(executable_path="D:\андрій\Selenium\chromedriver.exe")
    #     self.driver.get("https://www.hltv.org/")
    #     print("Title of the page: "+self.driver.title)
    #     self.driver.close()

if __name__ == "__main__":
    unittest.main()

