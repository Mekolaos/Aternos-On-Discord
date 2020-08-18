from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from helper import can_fire
import asyncio
import time
from dotenv import load_dotenv
import os

if os.path.exists(os.path.relpath(".env")):
    load_dotenv()
    USER = os.getenv('USERNAME')
    PASSWORD = os.getenv('PASSWORD_C')
    URL = "https://aternos.org/go/"
    SERVER_STATUS_URI = "http://" + os.getenv("SERVER_STATUS_URI")
   


options = webdriver.ChromeOptions()
options.add_argument('headless')

driver = webdriver.Chrome(options=options)

@can_fire
async def start_server():
    """ Starts the server by clicking on the start button.
        The try except part tries to find the confirmation button, and if it 
        doesn't, it continues to loop until the confirm button is clicked."""
    
    element = driver.find_element_by_xpath('//*[@id="start"]')
    element.click()
    asyncio.wait(10)
    element = driver.find_element_by_xpath('//*[@id="nope"]/main/div/div/div/main/div/a[1]')
    element.click()
    state = driver.find_element_by_xpath('//*[@id="nope"]/main/section/div[3]/div[2]/div/div/span[2]/span')
    while state.text == "Waiting in queue":
        state = driver.find_element_by_xpath('//*[@id="nope"]/main/section/div[3]/div[2]/div/div/span[2]/span')
        try:
            element = driver.find_element_by_xpath('//*[@id="confirm"]')
            element.click()
        except ElementNotInteractableException as e:
            pass
    driver.close()

@can_fire
def get_status():
    # Piece of shit code that returns the fucking status of the server as a string.

    driver.get(SERVER_STATUS_URI)
    element = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, '/html/body/div/div[3]/div/div/div[1]/span')))
    return element.text
@can_fire
def get_number_of_players():
    # Returns the number of players as a string
    driver.get(SERVER_STATUS_URI)
    number_of_players = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, '/html/body/div/div[4]/div/div/div/span[1]')))
    return number_of_players.text

@can_fire
async def connect_account():
    """ Connects to the accounts through a headless chrome tab so we don't
        have to do it every time we want to start or stop the server."""

    driver.get(URL)
    element = driver.find_element_by_xpath('//*[@id="user"]')
    element.send_keys(USER)
    element = driver.find_element_by_xpath('//*[@id="password"]')
    element.send_keys(PASSWORD)
    element = driver.find_element_by_xpath('//*[@id="login"]')
    element.click()
    asyncio.wait(10)

@can_fire
async def stop_server():
    driver.get(URL)
    element = driver.find_element_by_xpath('//*[@id="stop"]')
    element.click()

