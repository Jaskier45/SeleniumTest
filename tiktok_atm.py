from selenium import webdriver
import time
import random
from selenium.webdriver.chrome import options
# from fake_useragent import UserAgent
from selenium.webdriver.common.keys import Keys
from password import mail, passwrd


options = webdriver.ChromeOptions()

driver = webdriver.Chrome(options = options)

try:
    driver.get("https://www.tiktok.com")
    time.sleep(7)
    
    # close pikchy
    driver.find_element_by_class_name("verify-bar-close--icon").click()
    driver.implicitly_wait(5)
    
    # login button 
    driver.find_element_by_class_name("ehk74z00").click()
    driver.implicitly_wait(5)

    #switch to iframe
    iframe = driver.find_element_by_xpath("//iframe[@class='tiktok-tpndsz-IframeLoginSite eaxh4gs3']")
    driver.switch_to.frame(iframe)
    driver.implicitly_wait(5)
    
    # Switch login mode
    driver.find_element_by_xpath("//div[contains(text(),'Введите телефон / почту / имя пользователя')]").click()
    driver.implicitly_wait(5)

    driver.find_element_by_class_name("link-2j8GS").click()
    driver.implicitly_wait(5)
    
    # driver.find_elements_by_name("email").click()
    # time.sleep(2)
    # mail input
    mail_input = driver.find_element_by_name("email")
    mail_input.clear()
    mail_input.send_keys(mail)
    driver.implicitly_wait(5)

    # password input
    sword_input = driver.find_element_by_name("password")
    sword_input.clear()
    sword_input.send_keys(passwrd)
    driver.implicitly_wait(5)
    sword_input.send_keys(Keys.ENTER)
    time.sleep(5)

    driver.switch_to.window(driver.window_handles[0])
    # close adv
    driver.find_element_by_class_name("eaxh4gs2").click()
    time.sleep(5)
    driver.refresh()
    time.sleep(10)
    # tiktok-ppm7qc-StyledXMark eaxh4gs2
    # tiktok-18zg3yf-ButtonCloseWrapper eaxh4gs1
    # tiktok-ppm7qc-StyledXMark 


except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()