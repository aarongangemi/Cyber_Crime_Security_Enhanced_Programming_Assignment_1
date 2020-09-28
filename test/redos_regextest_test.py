from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

## Purpose: To test the regex tester can cause ReDos
## Contributor: Aaron Gangemi
## Date Modified: 28/09/2020
selenium = webdriver.Firefox()
selenium.get('http://localhost:8000/')
username = selenium.find_element_by_id('id_username')
email = selenium.find_element_by_id('id_email')
submit = selenium.find_element_by_id('register')
## Set HTML Elements using Selenium
username.send_keys("ReDoSTester")
email.send_keys("a@a.com")
submit.send_keys(Keys.RETURN)
## send values and set timeout value to 5
## This should always work as values are valid
timeout = 5
try:
    element_present = EC.presence_of_element_located((By.ID, 'id_regexString'))
    WebDriverWait(selenium, timeout).until(element_present)
    ## Check regex string is valid. If element is valid then ReDos was not caused
except TimeoutException:
    print("Timed out waiting for page to load")
# Testing matching regex and input string
## Below code tests ReDos occurs with evil regex
regexString = selenium.find_element_by_id('id_regexString')
inputString = selenium.find_element_by_id('id_inputString')
testRegex = selenium.find_element_by_id('testRegexBtn')
regexString.send_keys("^((a+)+)$") ##evil regex
inputString.send_keys("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa!") ##invalid string
submit = selenium.find_element_by_id("testRegexBtn")
submit.send_keys(Keys.RETURN)
## submit values

try:
    timeout = 10
    ## timeout of 10 seconds
    text_present = EC.text_to_be_present_in_element((By.ID, 'regexResult'), "No result")
    WebDriverWait(selenium, timeout).until(text_present)
    ## if result is found then regex is valid and reDos not occured
except TimeoutException:
    print("ReDos was caused")
    ##redos should be caused

##Test Regex will be caused
try:
    regexResult = selenium.find_element_by_id('regexResult')
    assert "Result: String found in regex" in regexResult.text
    print("ReDos was not caused")
    ## if assert works then redos not caused
except AssertionError:
    print("ReDos was caused at regex checker")
    ## assertion error thrown if redos caused