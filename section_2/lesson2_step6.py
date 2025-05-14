from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://SunInJuly.github.io/execute_script.html"

with webdriver.Chrome() as browser:

    browser.get(link)

    x = browser.find_element(By.ID, "input_value")
    x = x.text
    print(x)
    result = calc(x=x)

    browser.execute_script("window.scrollBy(0, 150);")

    input_1 = browser.find_element(By.ID, "answer")
    input_1.send_keys(f"{result}")

    check_box = browser.find_element(By.ID, "robotCheckbox")
    check_box.click()

    radio_box = browser.find_element(By.ID, "robotsRule")
    radio_box.click()

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    time.sleep(10)
