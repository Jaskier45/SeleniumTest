from selenium import webdriver
from selenium.webdriver import ActionChains
import time

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

driver.maximize_window()

try:
    driver.get("http://testautomationpractice.blogspot.com/")
    
    button = driver.find_element_by_xpath("//*[@id='HTML10']/div[1]/button")
    driver.implicitly_wait(3)

    actions = ActionChains(driver)
    actions.double_click(button).perform()
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()