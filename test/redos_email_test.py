from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

## Purpose: To test that the email field will cause ReDoS
## Contributor: Aaron Gangemi
## Date Modified: 28/09/2020
selenium = webdriver.Firefox()
selenium.get('http://localhost:8000/')
username = selenium.find_element_by_id('id_username')
submit = selenium.find_element_by_id('register')
## set email fields to HTML elements
username.send_keys("tester")
## Send values
selenium.execute_script('document.getElementById("id_email").value="@".repeat(200000)')
submit.send_keys(Keys.RETURN)
## return data
try:
    timeout = 10
    ## timeout value of 10 seconds
    text_present = EC.text_to_be_present_in_element((By.ID, 'message'),
                                                    "Error: Invalid Email")
    WebDriverWait(selenium, timeout).until(text_present)
    ## start count in another thread. Error should be present if ReDos is not caused
except TimeoutException:
    print("ReDos was caused")
    ## if timeout reached, error caused
try:
    ## ReDos not caused if URL does not change for error
    message = selenium.find_element_by_id("message")
    assert "Invalid Email" in message.text
    print("No ReDoS occurred")
except AssertionError:
    ## ReDos caused if assertion error reached
    print("ReDos was caused at register and did not allow the webpage display email error message")