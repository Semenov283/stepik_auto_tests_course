from selenium import webdriver
from selenium.webdriver.common.by import By


link = "http://suninjuly.github.io/cats.html"

with webdriver.Chrome() as browser:
    browser.find_element(By.ID, "button")
