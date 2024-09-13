from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

username_field = driver.find_element(By.CSS_SELECTOR, "input#user-name")
password_field = driver.find_element(By.CSS_SELECTOR, "input#password")
submit_button = driver.find_element(By.CSS_SELECTOR, "[type='submit']")

assert username_field.is_displayed()
assert password_field.is_displayed()
assert submit_button.is_displayed()

     
if username_field:
    print('Элементы найдены')
else:
    print('Элементы не найдены')

if password_field:
    print('Элементы найдены')
else:
    print('Элементы не найдены')

if submit_button:
    print('Элементы найдены')
else:
    print('Элементы не найдены')
  
