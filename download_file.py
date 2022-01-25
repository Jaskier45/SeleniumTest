from selenium.webdriver.chrome import options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

driver.maximize_window()

try:
    driver.get("http://demo.automationtesting.in/FileDownload.html")
    time.sleep(3)
    driver.find_element_by_xpath("//*[@id='textbox']").send_keys("123456")
    driver.find_element_by_xpath("//*[@id='createTxt']").click()
    driver.find_element_by_xpath("/html/body/section/div[1]/div/div/div[1]/a").click()
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()