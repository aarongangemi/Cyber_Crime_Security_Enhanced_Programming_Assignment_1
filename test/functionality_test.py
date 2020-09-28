# Created by Kay Men Yap 19257442
# Last updated: 28/09/2020
# Purpose: Test all of the functionality of the program

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

selenium  =  webdriver.Firefox()

selenium.get('http://localhost:8000/')

# Testing invalid username
username = selenium.find_element_by_id('id_username')
email = selenium.find_element_by_id('id_email')
submit = selenium.find_element_by_id('register')

username.send_keys("aa!")
email.send_keys("a@a.com")

submit.send_keys(Keys.RETURN)

timeout = 5
try:
    text_present = EC.text_to_be_present_in_element((By.ID, 'message'), "Error: invalid username")
    WebDriverWait(selenium, timeout).until(text_present)
except TimeoutException:
    print("Timed out waiting for page to load")

assert "http://localhost:8000" in selenium.current_url

# Testing invalid email
username = selenium.find_element_by_id('id_username')
email = selenium.find_element_by_id('id_email')
submit = selenium.find_element_by_id('register')

username.clear()
username.send_keys("aa")
email.clear()
email.send_keys("a@.com")

submit.send_keys(Keys.RETURN)

try:
    text_present = EC.text_to_be_present_in_element((By.ID, 'message'), "Error: Invalid Email")
    WebDriverWait(selenium, timeout).until(text_present)
except TimeoutException:
    print("Timed out waiting for page to load")

assert "http://localhost:8000" in selenium.current_url

# Testing valid register

username = selenium.find_element_by_id('id_username')
email = selenium.find_element_by_id('id_email')
submit = selenium.find_element_by_id('register')

username.clear()
username.send_keys("aa")
email.clear()
email.send_keys("a@a.com")

submit.send_keys(Keys.RETURN)

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

regexString.clear()
inputString.clear()
regexString.send_keys("abce")
inputString.send_keys("abcdd")

testRegex.send_keys(Keys.RETURN)

try:
    text_present = EC.text_to_be_present_in_element((By.ID, 'regexResult'), "Result: No result")
    WebDriverWait(selenium, timeout).until(text_present)
except TimeoutException:
    print("Timed out waiting for page to load")

regexResult = selenium.find_element_by_id('regexResult')
assert "Result: No result" in regexResult.text


goToSpace = selenium.find_element_by_id('goToSpaceBtn')
goToSpace.send_keys(Keys.RETURN)

try:
    element_present = EC.presence_of_element_located((By.ID, 'id_spaceInput'))
    WebDriverWait(selenium, timeout).until(element_present)
except TimeoutException:
    print("Timed out waiting for page to load")

assert "http://localhost:8000/inputTrim" in selenium.current_url


# Testing string that needs trimming
spaceInput = selenium.find_element_by_id('id_spaceInput')
trim = selenium.find_element_by_id('trimBtn')

spaceTestInput = "  abc a  "

spaceInput.send_keys(spaceTestInput)

trim.send_keys(Keys.RETURN)

try:
    text_present = EC.text_to_be_present_in_element((By.ID, 'spaceResult'), "Trimmed String: {}".format(spaceTestInput.strip()))
    WebDriverWait(selenium, timeout).until(text_present)
except TimeoutException:
    print("Timed out waiting for page to load")

spaceResult = selenium.find_element_by_id('spaceResult')
assert "Trimmed String: {}".format(spaceTestInput.strip()) in spaceResult.text

# Testing string that doesn't need trimming
spaceInput = selenium.find_element_by_id('id_spaceInput')
trim = selenium.find_element_by_id('trimBtn')

spaceTestInput = "abc a"

spaceInput.clear()
spaceInput.send_keys(spaceTestInput)
trim.send_keys(Keys.RETURN)

try:
    text_present = EC.text_to_be_present_in_element((By.ID, 'spaceResult'), "Result: Nothing needed trimming")
    WebDriverWait(selenium, timeout).until(text_present)
except TimeoutException:
    print("Timed out waiting for page to load")

spaceResult = selenium.find_element_by_id('spaceResult')
assert "Result: Nothing needed trimming" in spaceResult.text

# Testing going to regex page from space trimmer page
goToRegex = selenium.find_element_by_id('goToRegexBtn')
goToRegex.send_keys(Keys.RETURN)

try:
    element_present = EC.presence_of_element_located((By.ID, 'id_regexString'))
    WebDriverWait(selenium, timeout).until(element_present)
except TimeoutException:
    print("Timed out waiting for page to load")

assert "http://localhost:8000/regextest" in selenium.current_url

print("All tests passed")
selenium.quit()