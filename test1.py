from selenium import webdriver
import time
import random
from selenium.webdriver.chrome import options
from fake_useragent import UserAgent
from seleniumwire import webdriver

options = webdriver.ChromeOptions()
user_agents_list = [
    "hello_world",
    "best_of_the_best",
    "python"
]

useragent = UserAgent()

# set proxy
options.add_argument("--proxy-server=138.128.91.65:8000")

proxy_options= {
    "proxy": {

    }
}
# options.add_argument("user-agent=HelloWorld :)")
# options.add_argument(f"user-agent={random.choice(user_agents_list)}")
options.add_argument(f"user-agent={useragent.random}")

# url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent"
driver = webdriver.Chrome(options = options)




try:
    # driver.get(url=url)
    driver.get("https://2ip.ru/")
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()