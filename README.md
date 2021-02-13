# Aternos On Discord [![Build Status](https://travis-ci.com/Mekolaos/JackADit.svg?branch=master)](https://travis-ci.com/Mekolaos/JackADit)

A simple tool to serve your own discord bot, so you can manage an Aternos server from discord.

## Getting Started

1. Git clone this repository
2. Install it using either:
   * Copy, paste and execute this command inside the project folder: ```pip install -r requirements.txt```
   * Alternatively you can create a virtual environment using ```python -m venv venv``` and then ```source venv/bin/activate``` to finally ```pip install -r  requirements.txt```
3. Execute using this command inside the project folder : ```python3 Bot.py```

**Note:** When running ```Bot.py``` for the first time, you'll be prompted to enter your Aternos account and bot token. You'll need to run ```python3 Bot.py``` again after you finish setting your information.

* Should you ever need to change the information you can edit the ```.env``` directly or delete it and run ```Bot.py``` again.

### Prerequisites

* Python 3.7 or higher
* A Discord server for which you have the rights to add a bot
* An Aternos account

### Discord Commands

* --launch
* --status
* --info
* --players
* --stop
* --help


### Cloud Hosting Note

Cloud hosting this bot would require some workarounds as Aternos recognizes you are connecting from a data center and prompts for a captcha test.
