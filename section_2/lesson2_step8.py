from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
link = "http://suninjuly.github.io/file_input.html"

with webdriver.Chrome() as browser:

    browser.get(link)

    input_1 = browser.find_element(By.NAME, "firstname")
    input_1.send_keys("Sergey")

    input_2 = browser.find_element(By.NAME, "lastname")
    input_2.send_keys("Semenov")

    input_3 = browser.find_element(By.NAME, "email")
    input_3.send_keys("s@mail.ru")

    send_file = browser.find_element(By.NAME, "file")
    send_file.send_keys(file_path)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    time.sleep(10)
