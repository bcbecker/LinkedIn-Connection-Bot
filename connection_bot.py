#WARNING: don't use on your personal account unless you accept the risks
#time.slee(20 is for precaution, page loading times)

from selenium import webdriver
import time

#need to download web driver and give it path
driver = webdriver.Chrome('<path_to_exe>')
driver.get('https://www.linkedin.com')
time.sleep(2)

username = driver.find_element_by_xpath("//input[@name='session_key']")
password = driver.find_element_by_xpath("//input[@name='session_password']")

username.send_keys(<username>)
password.send_keys(<my_password>)
time.sleep(2)

submit = driver.find_element_by_xpath("//button[@type='submit']").click()

driver.get(<url_to_redirect_to>)
time.sleep(2)

all_buttons = driver.find_elements_by_tag_name("button")
connect_buttons = [btn for btn in all_buttons if btn.text == "Connect"]

for bnt in connect_buttons:
	#click connect
	driver.execute_script("arguments[0].click();", btn)
	time.sleep(2)

	#click send invite
	send_invite = driver.find_element_by_xpath("//button[@aria-label='Send now']")
	driver.execute_script("arguments[0].click();", send_invite)

	#click close/dismiss invite
	close_invite = driver.find_element_by_xpath("//button[@aria-label='Dismiss']")
	driver.execute_script("arguments[0].click();", close_invite)
	time.sleep(2)

