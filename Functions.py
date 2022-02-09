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

def get_status():
    return driver.find_element(By.CLASS_NAME, "statuslabel-label").text


def refreshBrowser():
    driver.refresh()


def get_players():
    try:
        server = MinecraftServer.lookup("scowws.aternos.me")
        status = server.status()
        #print(status.players.sample)
        names = []
        for a in status.players.sample:
            names.append(a.name)
        return names
    except:
        return "ERR"
