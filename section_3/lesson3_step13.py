import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestRegistration(unittest.TestCase):
    def test_registration1(self):
        self._test_registration("https://suninjuly.github.io/registration1.html")

    def test_registration2(self):
        self._test_registration("https://suninjuly.github.io/registration2.html")

    def _test_registration(self, link):
        with webdriver.Chrome() as browser:
            browser.get(link)

            # Заполняем обязательные поля
            input1 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your first name']")
            input1.send_keys("Ivan")

            input2 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your last name']")
            input2.send_keys("Petrov")

            input3 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your email']")
            input3.send_keys("www.awerqw@mail.ru")

            # Отправляем форму
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            # Ждем загрузки страницы
            time.sleep(1)

            # Получаем текст
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            welcome_text = welcome_text_elt.text

            # Проверяем текст
            self.assertEqual(
                "Congratulations! You have successfully registered!",
                welcome_text,
                "Текст при успешной регистрации не совпадает"
            )


if __name__ == "__main__":
    unittest.main()
