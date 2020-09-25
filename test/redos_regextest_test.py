from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

selenium = webdriver.Firefox()
selenium.get('http://localhost:8000/')
username = selenium.find_element_by_id('id_username')
email = selenium.find_element_by_id('id_email')
submit = selenium.find_element_by_id('register')
username.send_keys("ReDoS Tester")
email.send_keys("a@a.com")
submit.send_keys(Keys.RETURN)
timeout = 5
try:
    element_present = EC.presence_of_element_located((By.ID, 'id_regexString'))
    WebDriverWait(selenium, timeout).until(element_present)
except TimeoutException:
    print("Timed out waiting for page to load")
# Testing matching regex and input string
regexString = selenium.find_element_by_id('id_regexString')
inputString = selenium.find_element_by_id('id_inputString')
testRegex = selenium.find_element_by_id('testRegexBtn')
regexString.send_keys("^((a+)+)$")
inputString.send_keys("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa!")
submit = selenium.find_element_by_id("testRegexBtn")
submit.send_keys(Keys.RETURN)

try:
    timeout = 10
    text_present = EC.text_to_be_present_in_element((By.ID, 'regexResult'), "Result: String found in regex")
    WebDriverWait(selenium, timeout).until(text_present)
except TimeoutException:
    print("ReDos was caused")

try:
    regexResult = selenium.find_element_by_id('regexResult')
    assert "Result: String found in regex" in regexResult.text
    print("ReDos was not caused")
except AssertionError:
    print("ReDos was caused at regex checker")