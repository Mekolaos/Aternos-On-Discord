# Aternos On Discord 
[![Build Status](https://travis-ci.com/Mekolaos/JackADit.svg?branch=master)](https://travis-ci.com/Mekolaos/JackADit)

A simple tool to serve your own discord bot, so you can manage an Aternos server from discord.

- [Aternos On Discord](#aternos-on-discord)
  - [Getting Started](#getting-started)
    - [Windows/Mac/Linux (x64)](#windowsmaclinux-x64)
    - [Raspberry Pi (ARM)](#raspberry-pi-arm)
  - [Prerequisites](#prerequisites)
  - [Discord Commands](#discord-commands)
  - [Cloud Hosting Note](#cloud-hosting-note)

## Getting Started

### Windows/Mac/Linux (x64)

1. Git clone this repository
2. Install it using either:
   * Copy, paste and execute this command inside the project folder: ```pip install -r requirements.txt```
   * Alternatively you can create a virtual environment using ```python -m venv venv``` and then ```source venv/bin/activate``` to finally ```pip install -r  requirements.txt```
3. Setup a [Bot Account](https://discordpy.readthedocs.io/en/latest/discord.html)
   - You'll need the Bot Token for setting up the Bot
4. Execute using this command inside the project folder : ```python3 Bot.py```

**Note:** When running ```Bot.py``` for the first time, you'll be prompted to enter your Aternos account and bot token. You'll need to run ```python3 Bot.py``` again after you finish setting your information.

* Should you ever need to change the information you can edit the ```.env``` directly or delete it and run ```Bot.py``` again.

### Raspberry Pi (ARM)

Before following the instructions, make sure you have the following installed: 
- `sudo apt-get install libxml2-dev libxslt-dev python-dev`
- `sudo apt-get install python3-lxml python-lxml`
- `sudo apt-get install python3-wheel`
- `sudo apt-get install python3-tk`


1. Git clone this repository
2. Install it using `pip3 install -r requirements.txt` inside the folder
   - **NOTE**: This may take a while even on higher end Pi's
3. Setup a [Bot Account](https://discordpy.readthedocs.io/en/latest/discord.html)
   - You'll need the Bot Token for setting up the Bot
4. If you don't have a GUI:
   - Create a `.env` file in the following format:
      ```dotenv
        BOT_TOKEN= DISCORD_BOT_TOKEN
        USERNAME_C= ATERNOS_USERNAME
        PASSWORD_C= ATERNOS_PASSWORD
      ```
5. Setup Chromium 
   1. `sudo apt-get install chromium-browser`
   2. `sudo apt-get install chromium-chromedriver`
   3. In `connect_and_launch.py`, change driver executable path to `'/usr/lib/chromium-browser/chromedriver'`
6. Run the bot with `python3 Bot.py`


## Prerequisites

* Python 3.7 or higher
* A Discord server for which you have the rights to add a bot
* An Aternos account

## Discord Commands

* --launch
* --status
* --info
* --players
* --stop
* --help


## Cloud Hosting Note

Cloud hosting this bot would require some workarounds as Aternos recognizes you are connecting from a data center and prompts for a captcha test.


