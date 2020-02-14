from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import asyncio
import time
from dotenv import load_dotenv
import os

load_dotenv()
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')

options = webdriver.ChromeOptions()
options.add_argument('headless')

driver = webdriver.Chrome(options=options)
async def start_server():
    driver.get("https://aternos.org/go/")
    e = driver.find_element_by_xpath('//*[@id="user"]')
    e.send_keys(USER)
    e = driver.find_element_by_xpath('//*[@id="password"]')
    e.send_keys(PASSWORD)
    e = driver.find_element_by_xpath('//*[@id="login"]')
    e.click()
    time.sleep(3)
    e = driver.find_element_by_xpath('//*[@id="start"]')
    e.click()
    time.sleep(3)
    e = driver.find_element_by_xpath('//*[@id="nope"]/main/div/div/div/main/div/a[1]')
    e.click()
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
            except:
                print("except")
                pass

        
    # TODO: Add loop to check if in queue and click the confirm button if it popped up
    driver.close()



