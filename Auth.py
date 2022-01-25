from selenium import webdriver
import time
import random
from selenium.webdriver.chrome import options
# from fake_useragent import UserAgent
from selenium.webdriver.common.keys import Keys
from password import mail, passwrd
import pickle

options = webdriver.ChromeOptions()

# options.add_argument("user-agent=HelloWorld :)")
# options.add_argument(f"user-agent={random.choice(user_agents_list)}")
# url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent"
driver = webdriver.Chrome(options = options)
# def size():
#     options.add_argument('--start-maximized')
#     options.add_argument('--window-size=1600,900')
#     return options
#   driver.get(url=url)

try:
    

    # tools_input = driver.find_element_by_class_name("navbreakline2").click()
    # time.sleep(5)

    # email_input = driver.find_element_by_class_name("navsignin").click()
    # time.sleep(5)

    # *----*
    # Auth
    # *----*

    driver.get("https://www.instagram.com/")
    time.sleep(5)
    mail_input = driver.find_element_by_name("username")
    mail_input.clear()
    mail_input.send_keys(mail)
    time.sleep(2)

    pas_input = driver.find_element_by_name("password")
    pas_input.clear()
    pas_input.send_keys(passwrd)
    time.sleep(2)
    pas_input.send_keys(Keys.ENTER)
    time.sleep(10)

    # cookies
    # pickle.dump(driver.get_cookies(), open(f"{mail}_cookies", "wb"))

    # driver.get("https://www.instagram.com/")
    # time.sleep(5)

    # for cookie in pickle.load(open(f"{mail}_cookies", "rb")):
    #     driver.add_cookie(cookie)

    # time.sleep(5)
    # driver.refresh()
    # time.sleep(5)


except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()