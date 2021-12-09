# Home: добавление комментария
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
# Проскролльте страницу вниз на 600 пикселей
driver.execute_script("window.scrollBy(0, 600);")
# Нажмите на название книги "Selenium Ruby" или на кнопку "READ MORE"
sel_ruby = driver.find_element(By.CSS_SELECTOR, "[title='Selenium Ruby']")
sel_ruby.click()
# Нажмите на вкладку "REVIEWS"
sel_ruby_rev = driver.find_element(By.CSS_SELECTOR, "[href='#tab-reviews']")
sel_ruby_rev.click()
# Поставьте 5 звёзд
rate_5 = driver.find_element(By.CLASS_NAME, "star-5")
rate_5.click()
# [class='star-5']
# Заполните поле "Review" сообщением: "Nice book!"
comnt = driver.find_element(By.ID, "comment")
comnt.send_keys("Nice book!")
# Заполните поле "Name"
nme = driver.find_element(By.ID, "author")
nme.send_keys("Mr. Robato")
# Заполните "Email"
eml = driver.find_element(By.ID, "email")
eml.send_keys("mr@roba.to")
# Нажмите на кнопку "SUBMIT"
submt = driver.find_element(By.ID, "submit")
submt.click()
time.sleep(5)
driver.quit()