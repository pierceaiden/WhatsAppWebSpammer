from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import sys
import time

print('\n\nCLOSE ANY OTHER INSTANCES OF WHATSAPP WEB \n\n')

# Get spam details
spam_victim = input('Enter the victim\'s name (exact) in your contact list: ' )
spam_message_count = int(input('How many messages do you wanna send? '))
spam_message = []
for i in range(0, spam_message_count):
    spam_message.append(input('Enter the spam message: '))

spam_count = int(input('How many times do you want to spam? '))
print('\n\nBE SURE TO SCAN THE CODE ON YOUR PHONE\n\n')


# Open browser
driver = webdriver.Chrome()
driver.get('http://web.whatsapp.com')
driver.implicitly_wait(20)

# Search for victim and enter the chat
search = driver.find_element_by_id('input-chatlist-search')
#search.clear()
search.send_keys(spam_victim)
search.send_keys(Keys.RETURN)

# Find chat input field
for temp in driver.find_elements_by_css_selector('div.pluggable-input-body.copyable-text.selectable-text'):
    if temp.get_attribute('contenteditable') == "true":
        input = temp

for num in range(0, spam_count):
    for message in spam_message:
        input.clear()
        input.send_keys(message)
        input.send_keys(Keys.RETURN)
        print('\rDONE: ')
        print(num+1)
        sys.stdout.flush()
        time.sleep(1)

print('\n\nSPAMMING SUCCESSFUL! \n\n')
