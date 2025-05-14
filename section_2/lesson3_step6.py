# Задание: переход на новую вкладку
# В этом задании после нажатия кнопки страница откроется в новой вкладке, нужно переключить WebDriver на новую вкладку и решить в ней задачу.

from unittest import result
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


link = "http://suninjuly.github.io/redirect_accept.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

with webdriver.Chrome() as browser:
    browser.get(link)

    button_1 = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button_1.click()

    first_window = browser.window_handles[0]
    new_window = browser.window_handles[1]

    browser.switch_to.window(new_window)

    x = browser.find_element(By.ID, "input_value")
    x = x.text

    result = calc(x)

    input_1 = browser.find_element(By.ID, "answer")
    input_1.send_keys(result)

    button_2 = browser.find_element(By.TAG_NAME, "button")
    button_2.click()

    time.sleep(10)
