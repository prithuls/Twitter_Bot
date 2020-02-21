from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time

class TwitterBot:
    def __init__(self,username,password):
        self.username = username
        self.password = password

        self.bot = webdriver.Firefox(executable_path = './geckodriver.exe')


    def login(self):
        bot = self.bot
        bot.get('https://twitter.com')

        time.sleep(3)

        email = bot.find_element_by_name('session[username_or_email]')
        password = bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)

        time.sleep(2)

    def like_tweet(self, hashtag):
        bot = self.bot
        bot.get('https://twitter.com/search?q='+hashtag+'&src=typed')
        time.sleep(3)

        for i in range(1,3):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(2)
            tweets = bot.find_elements_by_class_name('tweet')
            links = 

if __name__ == '__main__':
    tw_bot = TwitterBot('prithul.pro@gmail.com ','160121')

    tw_bot.login()
    tw_bot.like_tweet('webdevelopment')
