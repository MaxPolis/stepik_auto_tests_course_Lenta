from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")

    browser.find_element(By.CLASS_NAME, "btn").click()


    new_window = browser.window_handles[1]
    old_window = browser.window_handles[0]

    browser.switch_to.window(new_window)
        
    input1 = browser.find_element(By.ID, "input_value")
    x = input1.text
    y = calc(x)
    input2 = browser.find_element(By.ID, "answer")
    input2.send_keys(y)
    button = browser.find_element(By.CLASS_NAME, "btn").click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()