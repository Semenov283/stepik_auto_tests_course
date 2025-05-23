from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
link = "http://suninjuly.github.io/explicit_wait2.html"

with webdriver.Chrome() as browser:
    browser.get(link)

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), str(100))
    )

    button = browser.find_element(By.ID, "book")
    button.click()

    x = browser.find_element(By.ID, "input_value")
    x = x.text

    result = calc(x)

    input_1 = browser.find_element(By.ID, "answer")
    input_1.send_keys(result)

    button_2 = browser.find_element(By.ID, "solve")
    button_2.click()

    time.sleep(10)
