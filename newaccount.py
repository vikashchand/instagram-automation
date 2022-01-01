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
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[2]/div/p/a/span").click()
driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/form/div[3]/div/label/input").send_keys("chandvikash1477@gmail.com")
driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/form/div[4]/div/label/input").send_keys("dwddwidsihdsiuh")
driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/form/div[5]/div/label/input").send_keys("dihodeihodwhpoewihpoedioh")
driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/form/div[6]/div/label/input").send_keys("287213821870")
driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/form/div[7]/div/button").click()