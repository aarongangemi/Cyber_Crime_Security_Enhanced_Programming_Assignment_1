from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
## Purpose: Test username ReDos
## Contributors: Aaron Gangemi
selenium = webdriver.Firefox()
selenium.get('http://localhost:8000/')
username = selenium.find_element_by_id('id_username')
email = selenium.find_element_by_id('id_email')
submit = selenium.find_element_by_id('register')
## Invalid regex will be caused
username.send_keys("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa!")
email.send_keys("a@a.com")
submit.send_keys(Keys.RETURN)
## submit data
try:
    timeout = 10
    ## if text not shown in 10 seconds then redos will occur
    text_present = EC.text_to_be_present_in_element((By.ID, 'message'),
                                                    "Error: invalid username")
    WebDriverWait(selenium, timeout).until(text_present)
except TimeoutException:
    print("ReDos was caused")

try:
    ## check url has not changed to confirm redos.
    assert "localhost:8000" in selenium.current_url
    print("No ReDos occurred")
except AssertionError:
    print("ReDos was caused at register and did not allow the webpage url to change")