from tabnanny import check
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()

link = "https://suninjuly.github.io/math.html"

browser.get(link)

x_element = browser.find_element(By.CSS_SELECTOR, "#input_value.nowrap")
x = x_element.text

y = calc(x)

input1 = browser.find_element(By.ID, "answer")
input1.send_keys(y)

check_box = browser.find_element(By.CLASS_NAME, "form-check-label")
check_box.click()

radio_box = browser.find_element(By.ID, "robotsRule")
radio_box.click()

button_submit = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
button_submit.click()

time.sleep(30)
browser.close()
