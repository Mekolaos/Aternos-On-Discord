from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementNotInteractableException
import asyncio
import time
from dotenv import load_dotenv
import os

load_dotenv()
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')
URL = "https://aternos.org/go/"

options = webdriver.ChromeOptions()
options.add_argument('headless')

driver = webdriver.Chrome(options=options)


async def start_server():
    driver.get("https://aternos.org/go/")
    element = driver.find_element_by_xpath('//*[@id="user"]')
    element.send_keys(USER)
    element = driver.find_element_by_xpath('//*[@id="password"]')
    element.send_keys(PASSWORD)
    element = driver.find_element_by_xpath('//*[@id="login"]')
    element.click()
    time.sleep(3)
    
    element = driver.find_element_by_xpath('//*[@id="start"]')
    element.click()
    time.sleep(3)
    element = driver.find_element_by_xpath('//*[@id="nope"]/main/div/div/div/main/div/a[1]')
    element.click()
    state = False
    while state == False:
        print("working")
        status = driver.find_element_by_xpath('//*[@id="nope"]/main/section/div[3]/div[2]/div/div/span[2]/span')
        if status.text == "Waiting in queue":
            try:
                element = driver.find_element_by_xpath('//*[@id="confirm"]')
                print("found")
                element.click()
                state = True
            except ElementNotInteractableException as e:
                print(e)
                pass
    driver.close()



