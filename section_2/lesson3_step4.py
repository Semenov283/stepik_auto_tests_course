from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"

with webdriver.Chrome() as browser:
    browser.get(link)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x = browser.find_element(By.ID, "input_value")
    x = x.text

    result = calc(x)

    input_1 = browser.find_element(By.ID, "answer")
    input_1.send_keys(result)

    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()


    time.sleep(5)
