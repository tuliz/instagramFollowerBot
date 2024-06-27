from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import time

class InstaFollower:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=self.chrome_options)

    def instagram_login(self,password,email):

        self.driver.get('https://www.instagram.com/')
        time.sleep(2)

        # Getting the user and password fields and send there the user and password
        email_input = self.driver.find_element(By.NAME, 'username')
        password_input = self.driver.find_element(By.NAME, 'password')
        email_input.send_keys(email)
        password_input.send_keys(password, Keys.ENTER)

        # After logging in there is a messege for saving info, find the save button and click it
        time.sleep(10)
        save_info = self.driver.find_element(By.XPATH,"//button[contains(text(), 'שמירת פרטים')]")
        save_info.click()

        # After that there is a pop up, find the ignore button and click it
        time.sleep(2)
        pop_up = self.driver.find_element(By.XPATH,"//button[contains(text(), 'לא עכשיו')]")
        pop_up.click()
