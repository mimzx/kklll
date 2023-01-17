from os import getenv
from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "26788480"))
API_HASH = getenv("API_HASH", "858d65155253af8632221240c535c314")

BOT_TOKEN = getenv("BOT_TOKEN", "5654221248:AAEKuIi39nwQNFXFwEr8YTgpC2YTDRNSH1s")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID", "5675937545"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/4faa7266294d6040d8084.png")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/2fc2b008e321ae4592ee4.jpg")

SESSION = getenv("SESSION", "AQCvg0rBRe1AcEJTa-Rfcd1Hf3MHsgeiZw0uFK1wwIXcPzLFBxtL9IugHMMMlteA5BBFiagZQiOHIY-3jefE2wBNoirjJE-bM3HCni5LfXl_b6Lng9f_szgcxoqwPvVULspMIQr5f4RGaIlMAZfAqXNnz-yltKkwylYME_JqVJXIvnZCLNZpP3HIWEmVBUFQvv3QXy5C-akrph6R8FSSfJVxhx8wThx1Y6sq8lZp64fqy0087afztnFiGlNukW5ex5z4aw2ii4xvlem4ceOafFfiZSkFOCLQJSODBosdHmsJ1t-FcdcnPfM6P7L69OqENRPJE2G3gvfpSmlrialdU7LXAAAAAVJP7wkA") 

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/TogaSupport")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/TogaSupport")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))


FAILED = "https://telegra.ph/file/2fc2b008e321ae4592ee4.jpg"
