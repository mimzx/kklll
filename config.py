from os import getenv
from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "26788480"))
API_HASH = getenv("API_HASH", "858d65155253af8632221240c535c314")

BOT_TOKEN = getenv("BOT_TOKEN", "5628206377:AAE3BU-o-pSxr-2dDlcuqrhc6zHi8j5hYM4")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID", "5163444566"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/48b6691e6c8ca9b26d221.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/f8ba75bdbb9931cbc8229.jpg")

SESSION = getenv("SESSION", "AQBfMD8925WdDB8bb28kgncvPBRECtl1UjSmYpC1CMcDqrypcdI5cTm8L2EO5aiSd3LjKrTMCgHMdkrf2A7P9mH0PJVOxAyxpHJGKkNEAxFI0X3mj9BqJQDeTAV79DRp8dQj1DfDcwmMciyyrUGNHPdKjDRBPKuQiaFBoP0E86TADLNWBhxZ0UXEAdD4oTvaRJ05fAumAYwyS_6o8YmrLmGBIfQ_MQzFyRHBxn022tpcjUSWa5L50h0TZBbxeowhAiuzfhYMqbGpAA1XUBZCoNV5uCCu3vsqnYSptdOArpTx6ye_QXSrXJOizY-AYXTfqIt-QYmDSqndNXNvKCc7zo8FAAAAAWPZSVQA") 

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/TogaSupport")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/FallenAssociation")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
