# # Shop: отображение страницы товара
#
# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
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
# #  Залогиньтесь
# my_acc = driver.find_element(By.CSS_SELECTOR, "[href='http://practice.automationtesting.in/my-account/']")
# my_acc.click()
# usr_name = driver.find_element(By.ID, "username")
# usr_name.send_keys("mr@roba.to")
# usr_pass = driver.find_element(By.ID, "password")
# usr_pass.send_keys("MrRobato2021")
# log_btn = driver.find_element(By.CSS_SELECTOR, "[name='login']")
# log_btn.click()
# # Нажмите на вкладку "Shop"
# shop_btn = driver.find_element(
#     By.CSS_SELECTOR, "[id='menu-item-40'] > [href='http://practice.automationtesting.in/shop/']")
# shop_btn.click()
# # Откройте книгу "HTML 5 Forms"
# book_html = driver.find_element(By.CSS_SELECTOR, "[title='Mastering HTML5 Forms']")
# book_html.click()
# # Добавьте тест, что заголовок книги назвается: "HTML5 Forms"
# book_title = driver.find_element(By.CSS_SELECTOR, "[class='product_title entry-title']")
# book_title_get_text = book_title.text
# assert book_title_get_text == 'HTML5 Forms'
#
# time.sleep(3)
# driver.quit()








# Shop: количество товаров в категории
# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
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
# #  Залогиньтесь
# my_acc = driver.find_element(By.CSS_SELECTOR, "[href='http://practice.automationtesting.in/my-account/']")
# my_acc.click()
# usr_name = driver.find_element(By.ID, "username")
# usr_name.send_keys("mr@roba.to")
# usr_pass = driver.find_element(By.ID, "password")
# usr_pass.send_keys("MrRobato2021")
# log_btn = driver.find_element(By.CSS_SELECTOR, "[name='login']")
# log_btn.click()
# # Нажмите на вкладку "Shop"
# shop_btn = driver.find_element(
#     By.CSS_SELECTOR, "[id='menu-item-40'] > [href='http://practice.automationtesting.in/shop/']")
# shop_btn.click()
# # Откройте категорию "HTML"
# cat_html = driver.find_element(
#     By.CSS_SELECTOR, "[href='http://practice.automationtesting.in/product-category/html/']")
# cat_html.click()
# # Добавьте тест, что отображается три товара
# items_count = driver.find_elements(By.CSS_SELECTOR, "[data-quantity='1']")
# if len(items_count) == 3:
#      print("Отображается 3 товара")
# else:
#       print('Отображается '+str(len(items_count))+' товара')
#
# time.sleep(3)
# driver.quit()







# Shop: сортировка товаров
# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.select import Select
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
# #  Залогиньтесь
# my_acc = driver.find_element(By.CSS_SELECTOR, "[href='http://practice.automationtesting.in/my-account/']")
# my_acc.click()
# usr_name = driver.find_element(By.ID, "username")
# usr_name.send_keys("mr@roba.to")
# usr_pass = driver.find_element(By.ID, "password")
# usr_pass.send_keys("MrRobato2021")
# log_btn = driver.find_element(By.CSS_SELECTOR, "[name='login']")
# log_btn.click()
# # Нажмите на вкладку "Shop"
# shop_btn = driver.find_element(
#     By.CSS_SELECTOR, "[id='menu-item-40'] > [href='http://practice.automationtesting.in/shop/']")
# shop_btn.click()
# # Добавьте тест, что в селекторе выбран вариант сортировки по умолчанию
# order_by = driver.find_element(By.CLASS_NAME, "orderby")
# order_by_value = order_by.get_attribute("value")
# assert order_by_value == 'menu_order'
# # Отсортируйте товары от большего к меньшему
# select_order=Select(order_by)
# select_order.select_by_value("price-desc")
# # Снова объявите переменную с локатором основного селектора сортировки
# order_by = driver.find_element(By.CLASS_NAME, "orderby")
# order_by_value = order_by.get_attribute("value")
# # обавьте тест, что в селекторе выбран вариант сортировки от большего к меньшему
# assert order_by_value == 'price-desc'
#
# time.sleep(3)
# driver.quit()





# Shop: отображение, скидка товара
# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
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
# #  Залогиньтесь
# my_acc = driver.find_element(By.CSS_SELECTOR, "[href='http://practice.automationtesting.in/my-account/']")
# my_acc.click()
# usr_name = driver.find_element(By.ID, "username")
# usr_name.send_keys("mr@roba.to")
# usr_pass = driver.find_element(By.ID, "password")
# usr_pass.send_keys("MrRobato2021")
# log_btn = driver.find_element(By.CSS_SELECTOR, "[name='login']")
# log_btn.click()
# # Нажмите на вкладку "Shop"
# shop_btn = driver.find_element(
#     By.CSS_SELECTOR, "[id='menu-item-40'] > [href='http://practice.automationtesting.in/shop/']")
# shop_btn.click()
# # Откройте книгу "Android Quick Start Guide"
# book_btn = driver.find_element(By.CSS_SELECTOR, "[alt='Android Quick Start Guide']")
# book_btn.click()
# # Добавьте тест, что содержимое старой цены = "₹600.00"
# old_price = driver.find_element(By.CSS_SELECTOR, "del > .woocommerce-Price-amount.amount")
# old_price_text = old_price.text
# assert old_price_text == '₹600.00'
# # Добавьте тест, что содержимое новой цены = "₹450.00"
# new_price = driver.find_element(By.CSS_SELECTOR, "ins > .woocommerce-Price-amount.amount")
# new_price_text = new_price.text
# assert new_price_text == '₹450.00'
# #  Добавьте явное ожидание и нажмите на обложку книги
# wait = WebDriverWait(driver, 8)
# book_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[title='Android Quick Start Guide']")))
# book_btn.click()
# # Добавьте явное ожидание и закройте предпросмотр нажав на крестик (кнопка вверху справа)
# close_btn = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "pp_close")))
# close_btn.click()
#
# time.sleep(3)
# driver.quit()











# Shop: проверка цены в корзине
# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
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
#
# # Откройте http://practice.automationtesting
# driver.get("http://practice.automationtesting.in/")
# # Нажмите на вкладку "Shop"
# shop_btn = driver.find_element(
#      By.CSS_SELECTOR, "[id='menu-item-40'] > [href='http://practice.automationtesting.in/shop/']")
# shop_btn.click()
# # Добавьте в корзину книгу "HTML5 WebApp Development"
# book_btn = driver.find_element(By.CSS_SELECTOR, "[data-product_id='182']")
# book_btn.click()
# # Добавьте тест, что в возле коризны(вверху справа) количество товаров = "1 Item"
# time.sleep(2)
# cart_qnty = driver.find_element(By.CLASS_NAME, "cartcontents")
# cart_qnty_text = cart_qnty.text
# assert cart_qnty_text == '1 Item'
# # а стоимость = "₹180.00"
# cart_amount = driver.find_element(By.CSS_SELECTOR, "span[class='amount']")
# cart_amount_text = cart_amount.text
# assert cart_amount_text == "₹180.00"
# # Перейдите в корзину
# view_basket = driver.find_element(By.CSS_SELECTOR, "[title='View Basket']")
# view_basket.click()
# # Используя явное ожидание, проверьте что в Subtotal отобразилась стоимость
# wait = WebDriverWait(driver, 8)
# subtotal = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-title='Subtotal'] > .woocommerce-Price-amount.amount")))
# subtotal_text = subtotal.text
# assert subtotal_text == '₹180.00'
# # Используя явное ожидание, проверьте что в Total отобразилась стоимость
# total = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "strong > .woocommerce-Price-amount.amount")))
# total_text = total.text
# assert total_text == '₹189.00'
#
# time.sleep(3)
# driver.quit()















# Shop: работа в корзине
# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
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
#
# # Откройте http://practice.automationtesting
# driver.get("http://practice.automationtesting.in/")
# # Нажмите на вкладку "Shop"
# shop_btn = driver.find_element(
#      By.CSS_SELECTOR, "[id='menu-item-40'] > [href='http://practice.automationtesting.in/shop/']")
# shop_btn.click()
# # Добавьте в корзину книги "HTML5 WebApp Development" и "JS Data Structures and Algorithm"
# # • Перед добавлением первой книги, проскролльте вниз на 300 пикселей
# # • После добавления 1-й книги добавьте sleep
# driver.execute_script("window.scrollBy(0, 300);")
# book1_btn = driver.find_element(By.CSS_SELECTOR, "[data-product_id='182']")
# book1_btn.click()
# time.sleep(2)
# book2_btn = driver.find_element(By.CSS_SELECTOR, "[data-product_id='180']")
# book2_btn.click()
# #  Перейдите в корзину
# view_basket = driver.find_element(By.CSS_SELECTOR, "[title='View Basket']")
# view_basket.click()
# #  Удалите первую книгу
# time.sleep(2)
# book1_remove = driver.find_element(By.CSS_SELECTOR, ".remove[data-product_id='182']")
# book1_remove.click()
# # Нажмите на Undo (отмена удаления)
# book1_remove_undo = driver.find_element(By.CSS_SELECTOR, ".woocommerce-message > a")
# book1_remove_undo.click()
# #  В Quantity увеличьте количесто товара до 3 шт для "JS Data Structures and Algorithm“
# # • Предварительно очистите поле с помощью локатор_поля.clear()
# book2_qnty = driver.find_element(By.CSS_SELECTOR, "[max='9911']")
# book2_qnty.clear()
# book2_qnty.send_keys(3)
# # Нажмите на кнопку "UPDATE BASKET"
# baskt_update = driver.find_element(By.CSS_SELECTOR, "[name='update_cart']")
# baskt_update.click()
# #  Добавьте тест, что value элемента quantity для "JS Data Structures and Algorithm" равно 3
# book2_qnty = driver.find_element(By.CSS_SELECTOR, "[max='9911']")
# book2_qnty_value = book2_qnty.get_attribute("value")
# assert book2_qnty_value == '3'
# # Нажмите на кнопку "APPLY COUPON"
# time.sleep(2)
# appl_cpn = driver.find_element(By.CSS_SELECTOR, "[value='Apply Coupon']")
# appl_cpn.click()
# # Добавьте тест, что возникло сообщение: "Please enter a coupon code."
# coup_err = driver.find_element(By.CSS_SELECTOR, ".woocommerce-error > li")
# coup_err_text = coup_err.text
# assert coup_err_text == 'Please enter a coupon code.'
#
# time.sleep(3)
# driver.quit()












# Shop: покупка товара
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

# Откройте http://practice.automationtesting
driver.get("http://practice.automationtesting.in/")
# Нажмите на вкладку "Shop" и проскролльте на 300 пикселей вниз
shop_btn = driver.find_element(
     By.CSS_SELECTOR, "[id='menu-item-40'] > [href='http://practice.automationtesting.in/shop/']")
shop_btn.click()
driver.execute_script("window.scrollBy(0, 300);")
#  Добавьте в корзину книгу "HTML5 WebApp Development"
book1_btn = driver.find_element(By.CSS_SELECTOR, "[data-product_id='182']")
book1_btn.click()
# Перейдите в корзину
view_basket = driver.find_element(By.CSS_SELECTOR, "[title='View Basket']")
view_basket.click()
#  Нажмите "PROCEED TO CHECKOUT"
wait = WebDriverWait(driver, 8)
proceed_btn = wait.until(
     EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='checkout-button button alt wc-forward']")))
proceed_btn.click()
# Заполните все обязательные поля
# Перед заполнением first name, добавьте явное ожидание
first_name = wait.until(
     EC.element_to_be_clickable((By.ID, "billing_first_name")))
first_name.send_keys("Mister")
last_name = driver.find_element(By.ID, "billing_last_name")
last_name.send_keys("Robato")
bil_email = driver.find_element(By.ID, "billing_email")
bil_email.send_keys("mister@roba.to")
bil_phone = driver.find_element(By.ID, "billing_phone")
bil_phone.send_keys("+7 812 600 00 00")
#  Для заполнения country нужно: нажать на селектор - > ввести название в поле ввода - > нажать на вариант который
#  отобразится ниже ввода
# • Чтобы выбрать селектор нижний вариант после ввода, используйте кнопку нажмите на неё, затем на вариант в списке ниже
country_sel = driver.find_element(By.ID, "select2-chosen-1")
country_sel.click()
country_field = driver.find_element(By.ID, "s2id_autogen1_search")
country_field.send_keys("Russia")
country_sel_confirm = driver.find_element(By.CLASS_NAME, "select2-match")
country_sel_confirm.click()
addr_field = driver.find_element(By.CSS_SELECTOR, "input[id='billing_address_1']")
addr_field.send_keys("Elm street, 13")
city_field = driver.find_element(By.CSS_SELECTOR, "input[id='billing_city']")
city_field.send_keys("Silent Hill")
state_field = driver.find_element(By.CSS_SELECTOR, "input[id='billing_state']")
state_field.send_keys("Russia")
post_field = driver.find_element(By.CSS_SELECTOR, "input[id='billing_postcode']")
post_field.send_keys("90210")




# Выберите способ оплаты "Check Payments"
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(2)
check_btn = driver.find_element(By.ID, "payment_method_cheque")
check_btn.click()
# Нажмите PLACE ORDER
plc_order = driver.find_element(By.ID, "place_order")
plc_order.click()
# Используя явное ожидание, проверьте что отображается надпись "Thank you. Your order has been received."
thank_you = wait.until(
     EC.element_to_be_clickable((By.CLASS_NAME, "woocommerce-thankyou-order-received")))
thank_you_text = thank_you.text
assert thank_you_text == 'Thank you. Your order has been received.'
#  Используя явное ожидание, проверьте что в Payment Method отображается текст "Check Payments"
check_pmnts = wait.until(
     EC.element_to_be_clickable((By.CSS_SELECTOR, ".method > strong")))
check_pmnts_text = check_pmnts.text
assert check_pmnts_text == 'Check Payments'
time.sleep(3)
driver.quit()