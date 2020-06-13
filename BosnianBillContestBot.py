#This bot will register the given mail and user on each of the
# 4 weekly contest hosted by Bosnian Bill on his page.
#Is meant to be runned by an acrontab job on Linux Systems
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time
import pdb
#setup
email = "your@email.com"  #Your Email
user = "User"   #Your YouTube Username
days = ['//*[@title="Weekend Review Giveaway"]', '//*[@title="Monday Fan Appreciation Free Giveaway"]', '//*[@title="Wednesday Fan Appreciation Free Giveaway"]', '//*[@title="Friday Fan Appreciation Free Giveaway"]']
contest = ["Weekend Review Giveaway", "Monday Fan Appreciation Free Giveaway", "Wednesday Fan Appreciation Free Giveaway", "Friday Fan Appreciation Free Giveaway"]
#browser setup
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
browser = webdriver.Chrome(chrome_options=options)

for i in range(0, 4):

        browser.get("https://locklab.com/")
        button = browser.find_element_by_xpath(days[i])
        button.click()

        emailform = browser.find_element_by_xpath('//*[@placeholder="Email"]')
        emailform.send_keys(email)

        userform = browser.find_element_by_xpath('//*[@placeholder="YouTube Username"]')
        userform.send_keys(user)

        submitbutton = browser.find_element_by_xpath('//*[@class="button submit-button"]')
        submitbutton.click()
        print("Submitted to", contest[i])
        time.sleep(2)

time.sleep(5)
print("Submitted for all contest this week")
browser.quit()
