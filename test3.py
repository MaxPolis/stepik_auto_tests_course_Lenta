import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/execute_script.html")
    input1 = browser.find_element(By.ID, "input_value")
    x = input1.text
    y = calc(x)
    input4 = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input4)
    input4.click()   
    input2 = browser.find_element(By.ID, "answer")
    input2.send_keys(y)
    input3 = browser.find_element(By.ID, "robotCheckbox")
    input3.click()
    button = browser.find_element(By.CLASS_NAME, "btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)   
    button.click()


finally:     # успеваем скопировать код за 30 секунд
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла