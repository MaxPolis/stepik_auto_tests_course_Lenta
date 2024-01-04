from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os 

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'test_file.txt')           # добавляем к этому пути имя файла 

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")

    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Test")   
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Testovy")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("test@test.test")
    file1 = browser.find_element(By.ID, "file")
    file1.send_keys(file_path)
    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()


finally:     # успеваем скопировать код за 30 секунд
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()
