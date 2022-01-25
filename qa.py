from selenium import webdriver

class ProgHubParser(object):

    def __init__(self, driver, lang):
        self.driver = driver
        self.lang = lang

    def parse(self):
        self.go_to_tests_page()

    def go_to_tests_page(self):
        self.driver.get("https://proghub.ru/tests")
        slide_elems = self.driver.find_elements_by_class_name("list")

        for elem in slide_elems:
            print(elem.get_attribute('href'))

def main():
    driver = webdriver.Chrome()
    parser = ProgHubParser(driver, "python")
    parser.parse()
    # driver.get("https://proghub.ru/tests")
    # btn_elem = driver.find_element_by_class_name("navresults")
    # btn_elem.click()
    # titleh1 = driver.find_element_by_tag_name("h1")
    # print(titleh1.text)

if __name__ == '__main__':
    main()
    