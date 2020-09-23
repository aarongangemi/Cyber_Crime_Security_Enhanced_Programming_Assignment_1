from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

selenium  =  webdriver.Firefox()

selenium.get('http://localhost:8000/')

# Testing valid register

username = selenium.find_element_by_id('id_username')
email = selenium.find_element_by_id('id_email')
submit = selenium.find_element_by_id('register')

username.send_keys("aa")
email.send_keys("a@a.com")

submit.send_keys(Keys.RETURN)

timeout = 5
try:
    element_present = EC.presence_of_element_located((By.ID, 'id_regexString'))
    WebDriverWait(selenium, timeout).until(element_present)
except TimeoutException:
    print("Timed out waiting for page to load")

assert "http://localhost:8000/regextest" in selenium.current_url


# Testing matching regex and input string
regexString = selenium.find_element_by_id('id_regexString')
inputString = selenium.find_element_by_id('id_inputString')
testRegex = selenium.find_element_by_id('testRegexBtn')

regexString.send_keys("abc")
inputString.send_keys("abcdd")

testRegex.send_keys(Keys.RETURN)

try:
    text_present = EC.text_to_be_present_in_element((By.ID, 'regexResult'), "Result: String found in regex")
    WebDriverWait(selenium, timeout).until(text_present)
except TimeoutException:
    print("Timed out waiting for page to load")

regexResult = selenium.find_element_by_id('regexResult')
assert "Result: String found in regex" in regexResult.text


# Testing non-matching regex and input string
regexString = selenium.find_element_by_id('id_regexString')
inputString = selenium.find_element_by_id('id_inputString')
testRegex = selenium.find_element_by_id('testRegexBtn')

regexString.send_keys("abc")
inputString.send_keys("abcdd")

testRegex.send_keys(Keys.RETURN)

try:
    text_present = EC.text_to_be_present_in_element((By.ID, 'regexResult'), "Result: No result")
    WebDriverWait(selenium, timeout).until(text_present)
except TimeoutException:
    print("Timed out waiting for page to load")

regexResult = selenium.find_element_by_id('regexResult')
assert "Result: No result" in regexResult.text


goToSpaceBtn = selenium.find_element_by_id('goToSpaceBtn')
goToSpace.send_keys(Keys.RETURN)

try:
    element_present = EC.presence_of_element_located((By.ID, 'id_regexString'))
    WebDriverWait(selenium, timeout).until(element_present)
except TimeoutException:
    print("Timed out waiting for page to load")

assert "http://localhost:8000/regextest" in selenium.current_url


selenium.quit()