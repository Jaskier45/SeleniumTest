from selenium import webdriver
import time

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

driver.maximize_window()

try:
    driver.get("https://www.worldometers.info/geography/flags-of-the-world/")
    time.sleep(2)
    # *************
    # scroll down by pixel
    # *************
    # driver.execute_script("window.scrollBy(0,1500)","")
    
    # *************
    # scroll down by page element
    # *************
    # flags = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[1]/div/div/div/div[161]/div/a/img")
    # driver.execute_script("arguments[0].scrollIntoView();",flags)
    # time.sleep(5)
    
    # *************
    # scroll down page till end window.scrollBy(0,document.body.scrollHeight)
    # *************
    # driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    # time.sleep(3)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()