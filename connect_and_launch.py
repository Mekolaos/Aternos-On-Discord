import asyncio
import time
import os
from selenium import webdriver
from selenium.common.exceptions import ElementNotInteractableException
from dotenv import load_dotenv
from chromedriver_py import binary_path

load_dotenv()
USER = os.getenv('USERNAME_C')
PASSWORD = os.getenv('PASSWORD_C')
URL = "https://aternos.org/go/"

# chrome variables
adblock = False  # for those with network wide ad blockers
headless = True  # if you want a headless window

options = webdriver.ChromeOptions()
if headless:
    options.add_argument('--headless')
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                     "AppleWebKit/537.36 (KHTML, like Gecko) "
                     "Chrome/87.0.4280.88 Safari/537.36")

driver = webdriver.Chrome(options=options, executable_path=binary_path)


async def start_server():
    """ Starts the server by clicking on the start button.
        The try except part tries to find the confirmation button, and if it
        doesn't, it continues to loop until the confirm button is clicked."""
    element = driver.find_element_by_xpath("//*[@id=\"start\"]")
    element.click()
    await asyncio.sleep(3)
    # hides the notification question
    driver.execute_script('hideAlert();')
    # server state span
    state = driver.find_element_by_xpath('//*[@id="nope"]/main/section/div[3]'
                                         '/div[3]/div[1]/div/span[2]/span')
    while state.text == "Waiting in queue":
        # while in queue, check for the confirm button and try click it
        await asyncio.sleep(3)
        state = driver.find_element_by_xpath('//*[@id="nope"]/main/section/'
                                             'div[3]/div[3]/div[1]/div/span[2]'
                                             '/span')
        try:
            element = driver.find_element_by_xpath('//*[@id="confirm"]')
            element.click()
        except ElementNotInteractableException:
            pass
    print("Server Started")


def get_status():
    """ Returns the status of the server as a string."""
    element = driver.find_element_by_xpath('//*[@id="nope"]/main/section/'
                                           'div[3]/div[3]/div[1]/div/span[2]'
                                           '/span')
    return element.text


def get_number_of_players():
    """ Returns the number of players as a string."""
    element = driver.find_element_by_xpath('//*[@id="players"]')
    return element.text


def connect_account():
    """ Connects to the accounts through a headless chrome tab so we don't
        have to do it every time we want to start or stop the server."""
    driver.get(URL)
    # login to aternos
    element = driver.find_element_by_xpath('//*[@id="user"]')
    element.send_keys(USER)
    element = driver.find_element_by_xpath('//*[@id="password"]')
    element.send_keys(PASSWORD)
    element = driver.find_element_by_xpath('//*[@id="login"]')
    element.click()
    time.sleep(2)

    # selects server from server list
    element = driver.find_element_by_css_selector('body > div > main > section'
                                                  '> div > div.servers.single '
                                                  '> div > div.server-body')
    element.click()

    # by passes the 3 second adblock
    if adblock:
        time.sleep(1)
        element = driver.find_element_by_xpath('//*[@id="sXMbkZHTzeemhBrPtXgBD'
                                               'DwAboVOOFxHiMjcTsUwoIOJ"]/div/'
                                               'div/div[3]/div[2]/div[3]/div'
                                               '[1]')
        element.click()
        time.sleep(3)

    print("Headless Tab Ready")


async def stop_server():
    """ Stops server from aternos panel."""
    element = driver.find_element_by_xpath("//*[@id=\"stop\"]")
    element.click()
    print("Server Stopped")


def quitBrowser():
    """ Quits the browser driver cleanly."""
    driver.quit()
