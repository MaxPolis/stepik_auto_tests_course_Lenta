import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects1.html")
    num1_element = browser.find_element(By.ID, "num1")
    num1 = num1_element.text
    num2_element = browser.find_element(By.ID, "num2")
    num2 = num2_element.text
    x = (str(int(num1)+int(num2)))
    select = Select(browser.find_element(By.ID, "dropdown"))
    
    select.select_by_value(str(x))
    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()



finally:     # успеваем скопировать код за 30 секунд
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()