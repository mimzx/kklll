from os import getenv
from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "26788480"))
API_HASH = getenv("API_HASH", "858d65155253af8632221240c535c314")

BOT_TOKEN = getenv("BOT_TOKEN", "5493514510:AAG6KZ74d3gf6nfuxP5HPv4YyOO1Qo7G3c8")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID", "5163444566"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/4faa7266294d6040d8084.png")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/e572cc7d5af715fca3ec0.jpg")

SESSION = getenv("SESSION", "AQBfMD8925WdDB8bb28kgncvPBRECtl1UjSmYpC1CMcDqrypcdI5cTm8L2EO5aiSd3LjKrTMCgHMdkrf2A7P9mH0PJVOxAyxpHJGKkNEAxFI0X3mj9BqJQDeTAV79DRp8dQj1DfDcwmMciyyrUGNHPdKjDRBPKuQiaFBoP0E86TADLNWBhxZ0UXEAdD4oTvaRJ05fAumAYwyS_6o8YmrLmGBIfQ_MQzFyRHBxn022tpcjUSWa5L50h0TZBbxeowhAiuzfhYMqbGpAA1XUBZCoNV5uCCu3vsqnYSptdOArpTx6ye_QXSrXJOizY-AYXTfqIt-QYmDSqndNXNvKCc7zo8FAAAAAWPZSVQA") 

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/TogaSupport")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/TogaSupport")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))


FAILED = "https://telegra.ph/file/e572cc7d5af715fca3ec0.jpg"
