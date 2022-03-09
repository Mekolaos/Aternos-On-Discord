import datetime

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import Settings

import colorama


from mcstatus import MinecraftServer

driver = webdriver.Chrome(options=Settings.woptions)


def connect_account():
    driver.get("https://aternos.org/go/")

    print_out("Logging into Aternos...", colorama.Fore.YELLOW)

    wait = WebDriverWait(driver, 10)
    usernamelement = wait.until(EC.element_to_be_clickable((By.ID, "user"))).click()

    usernamelement = driver.find_element(By.ID, "user")
    usernamelement.send_keys(Settings.Username)

    passelement = wait.until(EC.element_to_be_clickable((By.ID, "password"))).click()

    passelement = driver.find_element(By.ID, "password")
    passelement.send_keys(Settings.Password)

    loginelement = wait.until(EC.element_to_be_clickable((By.ID, "login"))).click()

    print_out("Logged in", colorama.Fore.GREEN)

    driver.implicitly_wait(2)
    acceptcookiesid = wait.until(EC.element_to_be_clickable((By.ID, "accept-choices"))).click()
    driver.implicitly_wait(2)

    serverelement = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "server-body"))).click()

    driver.implicitly_wait(2)

    print_out("Successfully on server page.", colorama.Fore.GREEN)


def fix_serverlist():
    try:
        serverelement = driver.find_element(By.CLASS_NAME, "server-body")
        serverelement.click()

        driver.implicitly_wait(2)

    except:
        pass

def start_server():
    print_out("Starting the server..", colorama.Fore.YELLOW)

    wait = WebDriverWait(driver, 10)
    startelement = wait.until(EC.element_to_be_clickable((By.ID, "start"))).click()
    driver.implicitly_wait(4)
    # hides the notification question
    element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn-red"))).click()
    # server state span
    while get_status() == "Waiting in queue":
        # while in queue, check for the confirm button and try click it
        driver.implicitly_wait(2)
        try:
            wait = WebDriverWait(driver, 2)
            element = wait.until(EC.element_to_be_clickable((By.ID, 'confirm'))).click()
        except:
            pass

    print_out("Started the server..", colorama.Fore.GREEN)


def get_status():
    return driver.find_element(By.CLASS_NAME, "statuslabel-label").text


def refreshBrowser():
    driver.refresh()


def get_players():
    try:
        server = MinecraftServer.lookup(get_ip())
        status = server.status()
        #print(status.players.sample)
        names = []
        for a in status.players.sample:
            names.append(a.name)
        return names
    except:
        return []
    
    
    

def get_number_of_players():
   return len(get_players())


def get_ip():
    """ Returns the severs IP address.
        Works: Always works"""
    return driver.find_element(By.ID, "ip").text


def get_software():
    """ Returns the server software.
        Works: Always works"""
    return driver.find_element(By.ID, "software").text


def get_version():
    """ Returns the server version.
        Works: Always works"""
    return driver.find_element(By.ID, "version").text


def get_tps():
    """ Returns the server TPS
        Works; When the server is online--Returns '0' if offline"""
    try:
        return driver.find_element(By.CLASS_NAME, "js-tps").text
    except NoSuchElementException:
        return '0'


def get_server_info():
    """ Returns a string of information about the server
        Returns: server_ip, server_status, number of players, software,
        version"""
    return get_ip(), get_status(), get_number_of_players(), \
           get_software(), get_version(), get_tps()


def print_out(out, color):
    print("")
    print("[" + datetime.datetime.now().strftime("%H:%M:%S") + "]" + color, out, colorama.Style.RESET_ALL)
