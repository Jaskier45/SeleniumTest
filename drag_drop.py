from selenium import webdriver
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.chrome import options

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

driver.maximize_window()
try:
    # driver.get("http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
    # driver.implicitly_wait(5)

    # first_item = driver.find_element_by_xpath("//*[@id='box4']")
    # main_item = driver.find_element_by_xpath("//*[@id='box104']")
    # actions= ActionChains(driver)
    
    # actions.drag_and_drop(first_item,main_item).perform()

    # *********************
    # Example 2
    # *********************

    driver.get("http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-1.html")
    driver.implicitly_wait(5)

    tiger_item = driver.find_element_by_xpath("//*[@id='box3']")
    cat_item = driver.find_element_by_xpath("//*[@id='box1']")
    log_box = driver.find_element_by_xpath("//*[@id='dropBox2']")
    
    actions = ActionChains(driver)
    actions.drag_and_drop(tiger_item,log_box).perform()
    actions.drag_and_drop(cat_item,log_box).perform()
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()