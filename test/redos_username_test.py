from selenium import webdriver
from selenium.webdriver.common.keys import Keys

selenium  =  webdriver.Firefox()

selenium.get('http://localhost:8000/')

username = selenium.find_element_by_id('id_username')
email = selenium.find_element_by_id('id_email')
submit = selenium.find_element_by_id('register')

username.send_keys("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa!")
email.send_keys("a@a.com")

submit.send_keys(Keys.RETURN)

#selenium.quit()