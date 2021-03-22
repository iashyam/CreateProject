from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys


driver = webdriver.Chrome(executable_path='/home/shyam/anaconda3/Selenium/chromedriver')
driver.get('https://github.com/')

sign_in_button = driver.find_element_by_xpath('/html/body/div[1]/header/div/div[2]/div[2]/a[1]')
sign_in_button.click()


username = ''#username
password =  '' #password
repo = str(sys.argv[1])

#finding the username input
username_input = driver.find_element_by_xpath('//*[@id="login_field"]')
username_input.send_keys(username) #entering username
username_input = driver.find_element_by_xpath('//*[@id="password"]')
username_input.send_keys(password) #entering password
login_button = driver.find_element_by_xpath('//*[@id="login"]/div[4]/form/div/input[12]')
login_button.click()

new_reo_button = driver.find_element_by_xpath('//*[@id="repos-container"]/h2/a')
new_reo_button.click()

repo_name = driver.find_element_by_xpath('//*[@id="repository_name"]')
repo_name.send_keys(repo)

time.sleep(5)
create_repo_button = driver.find_element_by_xpath('/html/body/div[4]/main/div/form/div[4]/button')
create_repo_button.click()

driver.quit()