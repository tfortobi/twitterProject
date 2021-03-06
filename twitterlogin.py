from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import getpass


class TwitterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/')
        time.sleep(3)
        email = bot.find_element_by_name("session[username_or_email]")
        password = bot.find_element_by_name("session[password]")
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)


e = input("What is your twitter username?\nUsername:")
print("what is your twitter password?")
p = getpass.getpass()
print("Password Entered\nLoading...")
user = TwitterBot(e, p)
user.login()
