from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome()
url="https://github.com"
driver.get(url)
time.sleep(2)


searchInput=driver.find_element_by_xpath("/html/body/div[1]/header/div/div[2]/div[2]/div[1]/div/div/form/label/input[1]")
time.sleep(1)
searchInput.send_keys("erdmkaramn")
time.sleep(2)
searchInput.send_keys(Keys.ENTER)
time.sleep(2)

searchInput=driver.find_element_by_xpath("//*[@id='js-pjax-container']/div/div[2]/nav[1]/a[10]").click()
time.sleep(2)

searchInput=driver.find_element_by_xpath("//*[@id='user_search_results']/div/div/div[2]/div[1]/div[1]/a[2]/em").click()

time.sleep(3)
driver.close()