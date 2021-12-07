import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Aleeza")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_NAME = getenv("OWNER_NAME", "AnujaSupulsara")
ALIVE_NAME = getenv("ALIVE_NAME", "Anuja_Supulsara")
BOT_USERNAME = getenv("BOT_USERNAME", ".....")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Anujasupulsara")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "anujasu")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "MUSICWorldanu")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/e79fcbac40874cd40ca28.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "260"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Anuja2003/VeezMusic.git")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/e79fcbac40874cd40ca28.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
