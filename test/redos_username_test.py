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
username.send_keys("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa!")
email.send_keys("a@a.com")
submit.send_keys(Keys.RETURN)

try:
    timeout = 10
    text_present = EC.text_to_be_present_in_element((By.ID, 'message'),
                                                    "Error: invalid username, please try again. Note: The username can only be characters from a to z uppercase or lowercase with no spaces")
    WebDriverWait(selenium, timeout).until(element_present)
except TimeoutException:
    print("ReDos was caused")

try:
    assert "localhost:8000" in selenium.current_url
except AssertionError:
    print("ReDos was caused at register and did not allow the webpage url to change")
#selenium.quit()