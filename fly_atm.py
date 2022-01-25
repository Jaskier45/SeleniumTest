from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.chrome import options


options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

driver.maximize_window()

try:
    driver.get("https://www.expedia.com/")
    time.sleep(3)

    driver.find_element_by_xpath("//*[@id='wizardMainRegionV2']/div/div/div/div/ul/li[2]/a").click()
    driver.implicitly_wait(5)

    driver.find_element_by_xpath("//*[@id='location-field-leg1-origin-menu']/div[1]/div[1]").click()
    time.sleep(1)
    first_tour = driver.find_element_by_id("location-field-leg1-origin")
    first_tour.send_keys("Chicago")
    driver.implicitly_wait(5)
    first_tour.send_keys(Keys.ENTER)
    driver.implicitly_wait(5)
    

    driver.find_element_by_xpath("//*[@id='location-field-leg1-destination-menu']/div[1]/div[1]/button").click()
    time.sleep(1)
    second_tour = driver.find_element_by_id("location-field-leg1-destination")
    second_tour.send_keys("New York")
    driver.implicitly_wait(5)
    second_tour.send_keys(Keys.ENTER)
    driver.implicitly_wait(5)
    
    driver.find_element_by_xpath("//*[@id='wizard-flight-pwa-1']/div[3]/div[2]/button").click()
    time.sleep(10)

    # driver.find_element_by_class_name("uitk-tab active").click()
    # driver.find_element_by_class_name("uitk-tab active").click()
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
    





# uitk-fake-input uitk-form-field-trigger
# uitk-fake-input uitk-form-field-trigger