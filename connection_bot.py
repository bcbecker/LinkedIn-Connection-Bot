from selenium import webdriver
import time
from config import Config

TARGET_CONNECTION_URL = 'https://www.linkedin.com/search/results/people/?network=%5B%22S%22%5D&origin=FACETED_SEARCH&sid=3%3Bb'

#You need to download web driver and give it path
driver = webdriver.Chrome(Config.PATH_TO_SELENIUM)
driver.get('https://www.linkedin.com')
time.sleep(2)


#LOGIN
username = driver.find_element_by_xpath("//input[@name='session_key']")
password = driver.find_element_by_xpath("//input[@name='session_password']")

username.send_keys(Config.LINKEDIN_USERNAME)
password.send_keys(Config.LINKEDIN_PASSWORD)
time.sleep(2)

submit = driver.find_element_by_xpath("//button[@type='submit']").click()


#FIND BUTTONS ON URL
driver.get(TARGET_CONNECTION_URL)
time.sleep(2)

all_buttons = driver.find_elements_by_tag_name("button")
connect_buttons = [button for button in all_buttons if button.text == "Connect"]


#ITERATE AND SEND INVITE
for button in connect_buttons:
	#click connect
	driver.execute_script("arguments[0].click();", button)
	time.sleep(2)

	#click send invite
	send_invite = driver.find_element_by_xpath("//button[@aria-label='Send now']")
	driver.execute_script("arguments[0].click();", send_invite)

	#click close/dismiss invite
	close_invite = driver.find_element_by_xpath("//button[@aria-label='Dismiss']")
	driver.execute_script("arguments[0].click();", close_invite)
	time.sleep(2)

