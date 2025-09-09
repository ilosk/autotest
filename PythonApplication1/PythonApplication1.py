print("hello world!")

import time
from selenium import webdriver
Chrome =webdriver.Chrome()
Chrome.get('https://google.com')
time.sleep(5)
Chrome.get('https://penza.hh.ru')
e_form = Chrome.find_element_by_id("testing_form")
Chrome.save_screenshot('e:\\РАБОТА\\Тестирование\\PythonApplication1\\1.png')
Chrome.refresh()
Chrome.quit()