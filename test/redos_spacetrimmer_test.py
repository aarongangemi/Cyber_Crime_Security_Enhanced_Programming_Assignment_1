from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
## Purpose: To test space trimmer can cause ReDos
## Contributors: Aaron Gangemi
## Bypass register page with valid values
selenium = webdriver.Firefox()
selenium.get('http://localhost:8000/')
username = selenium.find_element_by_id('id_username')
email = selenium.find_element_by_id('id_email')
submit = selenium.find_element_by_id('register')
username.send_keys("ReDoSTester")
email.send_keys("a.a@a.com")
submit.send_keys(Keys.RETURN)
timeout = 5
## Bypass regex page by clicking space trimmer button
goToSpace = selenium.find_element_by_id('goToSpaceBtn')
goToSpace.send_keys(Keys.RETURN)

try:
    element_present = EC.presence_of_element_located((By.ID, 'id_spaceInput'))
    WebDriverWait(selenium, timeout).until(element_present)
except TimeoutException:
    print("Timed out waiting for page to load")

# Testing space trimmer ReDos
spaceInput = selenium.find_element_by_id('id_spaceInput')
trimBtn = selenium.find_element_by_id('trimBtn')
spaceInput.send_keys("asd")
## will take time to buffer - approximatety 1 minute
spaceInput.send_keys(" " * 100000)
spaceInput.send_keys("asd")
trimBtn.send_keys(Keys.RETURN)
## send data

try:
    timeout = 10
    text_present = EC.text_to_be_present_in_element((By.ID, 'spaceResult'), "asd")
    WebDriverWait(selenium, timeout).until(text_present)
    ## if result doesn't appear in 10 seconds, then timeout and ReDos
except TimeoutException:
    print("ReDoS occurred in space trimmer")

try:
    spaceResult = selenium.find_element_by_id('spaceResult')
    ## if space result shows asd then no redos, if assertion error then redos
    assert "asd" in spaceResult.text
    print("No ReDos Occurred")
except AssertionError:
    print("ReDos was caused at space trimmer")