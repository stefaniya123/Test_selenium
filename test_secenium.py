from asyncio import timeout

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v140.accessibility import disable
from selenium.webdriver.support.ui import WebDriverWait, Select

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(15)
wait=WebDriverWait(driver, timeout= 15)


driver.get("https://www.selenium.dev/selenium/web/web-form.html")

text_input=driver.find_element(By.ID, value="my-text-id")
text_input.clear()
text_input.send_keys("Privet!!!")

pass_input=driver.find_element(By.NAME, value="my-password")
pass_input.clear()
pass_input.send_keys("secret123")

textarea=driver.find_element(By.NAME, value="my-textarea")
textarea.clear()
textarea.send_keys("hhh")

# disable_my=driver.find_element(By.NAME, value="my-disable")
# readonly_my=driver.find_element(By.NAME, value="my-readonly")

# assert disable_my.get_attribute("disabled")=="true"
# assert readonly_my.get_attribute("readonly")=="true"
#
select_elem=Select(driver.find_element(By.NAME, value="my-select"))
select_elem.select_by_value("2")

