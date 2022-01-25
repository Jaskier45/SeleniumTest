from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()

driver = webdriver.Chrome(options=options)

try:
    driver.get("https://www.hltv.org/")
    time.sleep(2)
    driver.find_element(By.LINK_TEXT, "Stats").click()
    time.sleep(5)
    # driver.get("https://www.w3.org/")
    # time.sleep(2)
    # links = driver.find_elements(By.TAG_NAME, "a")
    # print("Number of links: ",len(links)) #print how many links in a page
    # for link in links:
    #     print(link)    
# except Exception as ex:
#     print(ex)
finally:
    driver.close()
    driver.quit()