from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import time

driver = webdriver.Chrome()
driver.get("https://instagram.com")
driver.implicitly_wait(4)
driver.find_element_by_class_name("_2Lks6").click()
driver.implicitly_wait(4)
driver.find_element_by_xpath("/html/body/div[1]/section/main/div[2]/div/div/div/div/div[4]/form/label/input").send_keys("+918448520755")

driver.find_element_by_xpath("/html/body/div[1]/section/main/div[2]/div/div/div/div/div[5]/button").click()

#i have edited the file
