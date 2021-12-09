# # Registration_login: регистрация аккаунта
#
# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
#
#
# path_to_extension = r'C:\Users\User\AppData\Local\Google\Chrome\User Data\Default\Extensions\gighmmpiobklfepjocnamgkkbiglidom\4.40.0_1'
# chrome_options = Options()
# chrome_options.add_argument('load-extension=' + path_to_extension)
# driver = webdriver.Chrome(chrome_options=chrome_options)
# driver.create_options()
# time.sleep(10)
# driver.maximize_window()
#
# first_browser_tab = driver.window_handles[0]
# driver.switch_to.window(first_browser_tab)
# driver.implicitly_wait(5)
# driver.get("http://practice.automationtesting.in/")
# # Нажмите на вкладку "My Account Menu"
# my_acc = driver.find_element(By.CSS_SELECTOR, "[href='http://practice.automationtesting.in/my-account/']")
# my_acc.click()
# #  В разделе "Register", введите email для регистрации
# reg_em = driver.find_element(By.ID, "reg_email")
# reg_em.send_keys("mr@roba.to")
# time.sleep(1)
# # В разделе "Register", введите пароль для регистрации
# reg_pas = driver.find_element(By.ID, "reg_password")
# reg_pas.send_keys("MrRobato2021")
# # Нажмите на кнопку "Register"
# time.sleep(1)
# reg_subm = driver.find_element(By.CSS_SELECTOR, "[name='register']")
# reg_subm.click()
#
# time.sleep(3)
# driver.quit()









# Registration_login: логин в систему

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

path_to_extension = r'C:\Users\User\AppData\Local\Google\Chrome\User Data\Default\Extensions\gighmmpiobklfepjocnamgkkbiglidom\4.40.0_1'
chrome_options = Options()
chrome_options.add_argument('load-extension=' + path_to_extension)
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.create_options()
time.sleep(10)
driver.maximize_window()

first_browser_tab = driver.window_handles[0]
driver.switch_to.window(first_browser_tab)
driver.implicitly_wait(5)
driver.get("http://practice.automationtesting.in/")
# Нажмите на вкладку "My Account Menu"
my_acc = driver.find_element(By.CSS_SELECTOR, "[href='http://practice.automationtesting.in/my-account/']")
my_acc.click()
# В разделе "Login", введите email для логина
usr_name = driver.find_element(By.ID, "username")
usr_name.send_keys("mr@roba.to")
# В разделе "Login", введите пароль для логина
usr_pass = driver.find_element(By.ID, "password")
usr_pass.send_keys("MrRobato2021")
# Нажмите на кнопку "Login"
log_btn = driver.find_element(By.CSS_SELECTOR, "[name='login']")
log_btn.click()
# Добавьте проверку, что на странице есть элемент "Logout"
logout_btn = driver.find_element(By.CSS_SELECTOR, "li > [href='http://practice.automationtesting.in/my-account/customer-logout/']")
logout_btn_get_text = logout_btn.text
assert logout_btn_get_text == 'Logout'
time.sleep(3)
driver.quit()




