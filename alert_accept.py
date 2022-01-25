from typing import Optional
from selenium import webdriver
import time

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

try:
    driver.get("http://testautomationpractice.blogspot.com/")
    time.sleep(3)
    driver.find_element_by_xpath("//*[@id='HTML9']/div[1]/button").click()
    time.sleep(2)
    driver.switch_to_alert().accept()
    # driver.switch_to_alert().dismiss()
    # time.sleep(3)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
