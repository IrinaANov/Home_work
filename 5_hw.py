from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")


from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")


username_field = driver.find_element(By.CSS_SELECTOR, "input#user-name")

if username_field:
    print('Элементы найдены')
else:
    print('Элементы не найдены')


password_field = driver.find_element(By.CSS_SELECTOR, "input#password")

if password_field:
    print('Элементы найдены')
else:
    print('Элементы не найдены')


submit_button = driver.find_element(By.CSS_SELECTOR, "[type='submit']")

if submit_button:
    print('Элементы найдены')
else:
    print('Элементы не найдены')
  
