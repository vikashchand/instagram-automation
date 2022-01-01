from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from LoginCredentials import userName,password

driver = webdriver.Chrome()
driver.get("https://instagram.com")
driver.implicitly_wait(4)

driver.find_element_by_name("username").send_keys(userName)
driver.find_element_by_name("password").send_keys(password)
button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()