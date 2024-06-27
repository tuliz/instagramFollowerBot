from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
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

        # After logging in there is a message for saving info, find the save button and click it
        time.sleep(10)
        save_info = self.driver.find_element(By.XPATH,"//button[contains(text(), 'שמירת פרטים')]")
        save_info.click()

        # After that there is a pop up, find the ignore button and click it
        time.sleep(2)
        pop_up = self.driver.find_element(By.XPATH,"//button[contains(text(), 'לא עכשיו')]")
        pop_up.click()

    def find_followers(self, account):

        # Go to the account you chose to find its followers
        self.driver.get(f'https://www.instagram.com/{account}')
        time.sleep(5)

        # Get the button that opens the followers window  and click it
        account_followers = self.driver.find_element(By.CSS_SELECTOR, 'a[href="/eran_brownstain/followers/"]')
        account_followers.click()
        time.sleep(2)

        # Create a new ActionChains object for the scrolling
        action = ActionChains(self.driver)

        # Get all the follow buttons in the followers window
        followers_follow_btns = self.driver.find_elements(By.XPATH, "//*[contains(text(), 'מעקב')]")

        # Move the Mouse to the area of the follow buttons
        action.move_to_element(to_element=followers_follow_btns[3])

        while True:

            # Each time do a loop with all the follow buttons found
            for btn in followers_follow_btns:
                # If its a follower you already follow pass it
                if btn.text == 'במעקב':
                    pass
                else:
                    btn.click()
                    time.sleep(1)

            # After going trough all the followers that currently are in the list,
            # scroll down to the bottom and load more followers and get again all the follow buttons
            action.scroll_to_element(followers_follow_btns[-2])
            time.sleep(4)
            followers_follow_btns = self.driver.find_elements(By.XPATH, "//*[contains(text(), 'מעקב')]")
