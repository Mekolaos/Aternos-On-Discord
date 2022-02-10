from selenium.webdriver.common.by import By

import Settings
from selenium import webdriver

from mcstatus import MinecraftServer

server = MinecraftServer("scowws.aternos.me")


driver = webdriver.Chrome(options=Settings.woptions)


def connect_account():
    driver.get("https://aternos.org/go/")

    usernamelement = driver.find_element(By.ID, "user")
    usernamelement.click()
    usernamelement.send_keys(Settings.Username)

    passelement = driver.find_element(By.ID, "password")
    passelement.click()
    passelement.send_keys(Settings.Password)

    loginelement = driver.find_element(By.ID, "login")
    loginelement.click()

    driver.implicitly_wait(2)
    acceptcookiesid = driver.find_element(By.ID, "accept-choices")
    acceptcookiesid.click()
    driver.implicitly_wait(2)

    serverelement = driver.find_element(By.CLASS_NAME, "server-body")
    serverelement.click()

    driver.implicitly_wait(2)


def fix_serverlist():
    try:
        serverelement = driver.find_element(By.CLASS_NAME, "server-body")
        serverelement.click()

        driver.implicitly_wait(2)

    except:
        pass

def start_server():
    startelement = driver.find_element(By.ID, "start")
    startelement.click()
    driver.implicitly_wait(4)
    # hides the notification question
    element = driver.find_element(By.CLASS_NAME, "btn-red")
    element.click
    # server state span
    while get_status() == "Waiting in queue":
        # while in queue, check for the confirm button and try click it
        driver.implicitly_wait(2)
        try:
            element = driver.find_element(By.ID, 'confirm')
            element.click()
        except:
            pass


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
