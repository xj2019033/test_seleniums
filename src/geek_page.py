from selenium import webdriver
from selenium.webdriver.common.by import By


class GeekPage:

    def __init__(self):
        # self.driver=webdriver.Chrome()
        # self.driver.get('https://time.geekbang.org/')
        chrome_options = webdriver.ChromeOptions()
        self.driver = webdriver.Remote(
            command_executor='http://192.168.0.246:5001/wd/hub',
            options=chrome_options
        )

        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get('https://time.geekbang.org/')
        self.driver.find_element(By.CSS_SELECTOR,'a.iconfont').click()
    def quit(self):
        self.driver.quit()
    def login(self):

        self.driver.find_element(By.CSS_SELECTOR,'a.pc').click()



