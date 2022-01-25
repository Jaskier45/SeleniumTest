from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome import options
import time

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

try:
    driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
    driver.implicitly_wait(5)

    button = driver.find_element_by_xpath("/html/body/div/section/div/div/div/p/span")

    actions = ActionChains(driver)
    actions.context_click(button).perform()
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()