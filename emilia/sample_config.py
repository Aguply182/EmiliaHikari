# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.

import json

import os

def get_user_list(config, key):

    with open("{}/EmiliaRobot/{}".format(os.getcwd(), config), "r") as json_file:

        return json.load(json_file)[key]


# Create a new config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True

    # REQUIRED
    API_KEY = "YOUR KEY HERE"
    OWNER_ID = "YOUR ID HERE"  # If you dont know, run the bot and do /id in your private chat with it
    OWNER_USERNAME = "YOUR USERNAME HERE"
    # Some API is required for more features
    API_OPENWEATHER = ""
    API_ACCUWEATHER = ""
    MAPS_API = ""

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = 'sqldbtype://username:pw@hostname:port/db_name'  # needed for any database modules
    MESSAGE_DUMP = None  # needed to make sure 'save from' messages persist
    LOAD = []
    NO_LOAD = ['translation', 'rss', 'sed', 'weather']
    WEBHOOK = False
    URL = None

    # OPTIONAL
    SUDO_USERS = []  # List of id's (not usernames) for users which have sudo access to the bot.
    SUPPORT_USERS = []  # List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    WHITELIST_USERS = []  # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = False  # Whether or not you should delete "blue text must click" commands
    STRICT_GBAN = False
    WORKERS = 8  # Number of subthreads to use. This is the recommended amount - see for yourself what works best!
    BAN_STICKER = 'CAADAgADOwADPPEcAXkko5EB3YGYAg'  # banhammer marie sticker
    ALLOW_EXCL = False  # DEPRECATED, USE BELOW INSTEAD! Allow ! commands as well as /
    CUSTOM_CMD = False # Set to ('/', '!') or whatever to enable it, like ALLOW_EXCL but with more custom handler!
    SPAMMERS = "" # Will not allow to interact with bot
    TEMPORARY_DATA = None # Temporary data for backup module, use int number


class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
