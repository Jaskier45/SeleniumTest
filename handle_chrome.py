from selenium import webdriver
import time

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

driver.get("http://demo.automationtesting.in/Windows.html")
driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()
time.sleep(3)
print(driver.current_window_handle)
# tags name
parent = driver.window_handles[0]
chld = driver.window_handles[1]
# swich tags
driver.switch_to.window(parent)
driver.close()
driver.switch_to.window(chld)
time.sleep(3)
driver.quit()
    # for handle in handles:
    #     driver.switch_to.window(handle)
    #     print(driver.title)

# except Exception as ex:
#     print(ex)
# finally:
#     driver.close()
#     driver.quit()

