from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome import options
import time

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

try:
    driver.get("https://opensource-demo.orangehrmlive.com/")
    time.sleep(1)
    # login text box
    login = driver.find_element_by_xpath("//*[@id='txtUsername']")
    login.clear()
    login.send_keys("Admin")
    driver.implicitly_wait(2)

    # password text box
    password = driver.find_element_by_xpath("//*[@id='txtPassword']")
    password.clear()
    password.send_keys("admin123")
    driver.implicitly_wait(2)

    # LOGIN button
    driver.find_element_by_xpath("//*[@id='btnLogin']").click() 
    

    # mouse movement
    # step_one = driver.find_element_by_xpath("//*[@id='menu_admin_viewAdminModule']")
    # step_two = driver.find_element_by_xpath("//*[@id='menu_admin_UserManagement']")
    # step_three = driver.find_element_by_xpath("//*[@id='menu_admin_viewSystemUsers']")
    
    # driver.implicitly_wait(2)
    
    # actions = ActionChains(driver)
    # actions.move_to_element(step_one).move_to_element(step_two).move_to_element(step_three).click().perform()
    
    # ****************************
    
    job_one = driver.find_element_by_xpath("//*[@id='menu_admin_viewAdminModule']")
    job_two = driver.find_element_by_xpath("//*[@id='menu_admin_Job']")
    job_three = driver.find_element_by_xpath("//*[@id='menu_admin_jobCategory']")
    driver.implicitly_wait(2)

    actions = ActionChains(driver)
    actions.move_to_element(job_one).move_to_element(job_two).move_to_element(job_three).click().perform()
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()