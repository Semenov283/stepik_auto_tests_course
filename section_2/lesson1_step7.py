from webbrowser import get
from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/get_attribute.html"

browser = webdriver.Chrome()
browser.get(link)

get_img = browser.find_element(By.ID, "treasure")
x = get_img.get_attribute("valuex")

y = calc(x)
# result = browser.get_attribute()

input1 = browser.find_element(By.ID, "answer")
input1.send_keys(y)

check_box = browser.find_element(By.CLASS_NAME, "check-input")
check_box.click()

radio_box = browser.find_element(By.ID, "robotsRule")
radio_box.click()

button_submit = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
button_submit.click()

time.sleep(30)
browser.close()
