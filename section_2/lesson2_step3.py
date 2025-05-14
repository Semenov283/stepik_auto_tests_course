from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


link = "https://suninjuly.github.io/selects1.html"


def calc(x, y) -> int:
    result = int(x) + int(y)
    return result


with webdriver.Chrome() as browser:
    browser.get(link)

    num1 = browser.find_element(By.ID, "num1")
    num2 = browser.find_element(By.ID, "num2")

    num1_text = int(num1.text)
    num2_text = int(num2.text)

    result = calc(num1_text, num2_text)

    dropdown = Select(browser.find_element(By.ID, "dropdown"))
    dropdown.select_by_value(f"{result}")

    btn_submit = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    btn_submit.click()

    time.sleep(30)
