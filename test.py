from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)

LOGIN_STRING = (By.ID, "pseudonym_session_unique_id")
PASSWORD_STRING = (By.ID, "pseudonym_session_password")
LOGIN_BTN = (By.CSS_SELECTOR, "button.Button.Button--login")
LOGIN_REJECTED = (By.CSS_SELECTOR, "li.ic-flash-error")

# I am on loginpage
driver.get( 'https://honorlock.instructure.com/login/canvas' )

# Input wrong email into login string
search = driver.find_element(*LOGIN_STRING)
search.clear()
search.send_keys('WrongPassword1234!@gmail.com')

# Input  wrong password
search = driver.find_element(*PASSWORD_STRING)
search.clear()
search.send_keys('WrongPassword1234!')

# Click on login button
driver.find_element(*LOGIN_BTN).click()

# Verify "Invalid username or password" sign is here
assert 'Invalid username or password' in driver.find_element(*LOGIN_REJECTED).text
print('Sign is here: ', str(driver.find_element(*LOGIN_REJECTED).text),'.')

# wait before exit
sleep(5)

# exit
driver.quit()