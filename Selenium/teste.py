from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


def blogs(driver):
    entrada = driver.find_element_by_class_name('btn-secundario')
    entrada = entrada.find_elements_by_css_selector('li')
    entrada[3].click()
    sleep(1)
    driver.switch_to.window(driver.window_handles[-1])
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')


path = r'E:\Users\JP\Downloads\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get(r'http://www.colegiosion.com.br/')
sleep(1)
blogs(driver)
