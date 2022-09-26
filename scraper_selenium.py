from selenium import webdriver
from selenium.webdriver.common.by import By
from ahk import AHK
from time import sleep

url = 'https://myeilp.gowercollegeswansea.ac.uk/myEILPTimetable.aspx'
username = 'geu51866554'
password = 'M#gcS$y7hV'

# Create a new instance of the chrome driver
driver = webdriver.Chrome()
driver.get(url)

sleep(1)

# input login credentials and submit using ahk
ahk = AHK()
ahk.type(username)
ahk.key_press('Tab')
ahk.type(password)
sleep(.2)
ahk.key_press('Enter')

sleep(3)

# get data from page
days = driver.find_elements(By.TAG_NAME, 'a')
for day in days:
    # print(day.text)
    day.click()
    sleep(3)
    driver.back()
    sleep(5)