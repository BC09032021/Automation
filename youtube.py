
import time

from selenium import webdriver
driver: object = webdriver.Chrome()

driver.get('https://www.youtube.com/')
search_box = driver.find_element_by_xpath('//*[@id="search"]')
search_box.send_keys('DusktillDawn')
search_button = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
search_button.click()
play = driver.find_element_by_xpath('//*[@id="img"]')
play.click()
time.sleep(15)
#driver.quit()

search_box1=driver.find_element_by_xpath('//*[@id="search"]')
search_box1.clear()
search_box1.send_keys('bilionera')


#search_box = driver.find_element_by_xpath('//*[@id="search"]')


play = driver.find_element_by_xpath('//*[@id="img"]')
play.click()














