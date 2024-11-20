from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    firstname = browser.find_element(By.CSS_SELECTOR, 'input[name="firstname"]')
    firstname.send_keys("Ivan")
    familyname = browser.find_element(By.CSS_SELECTOR, 'input[name="lastname"]')
    familyname.send_keys("Petrov")
    email = browser.find_element(By.CSS_SELECTOR, 'input[name="email"]')
    email.send_keys("sereda_2007@mail.ru")
    #Загрузитьфайл.Файлдолжениметьрасширение.txt и может быть пустым
    element = browser.find_element(By.ID, "file")
    element.send_keys(r"C:\Users\admin\PycharmProjects\pythonProject\file.txt")
                      #"/home/user/stepik/Chapter2/file_example.txt")
    #Получаем путь до директории , где лежит текущий исполняемый  файл
    #current_dir = os.path.abspath(os.path.dirname(__file__))
    #добавляем к пути Имя файла
    #file_path = os.path.join(current_dir, 'file.txt')
    #element.send_keys(file_path)
    # Нажатькнопку"Submit"
    button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

