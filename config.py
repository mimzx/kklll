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

SESSION = getenv("SESSION", "AQAkGxMR326usVUVHWXl8A_AKlbP0M2Be5gHyTsnjrVVQdqYhIo4cy6vIl7HTNOX4cHFTfglweBoxt93w6W3yRlQjglifZIkwyHJ5gtqMH1gSyi6_SRKCWt9EsqllRB_rcDLlqC7Y72Fr0ttETciRJ6807KfCLRiTWz_GlodsnYsZ33pW8ZAggYn8hOFooZYHXz_hQedGCZS3YmtNx9p3SecKew7HahSLfDAXPY3g7mguEmQi94-mKT6onVgFePbG7vHohCB4OjTS6qT2-LE2i2JXhK4S_MvopuZuyqIIQdcusB83pPy2MU3KMxDhab3C0j7lTuZcxlF_xewpq07jEv3AAAAAVJP7wkA") 

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/TogaSupport")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/TogaSupport")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))


FAILED = "https://telegra.ph/file/2fc2b008e321ae4592ee4.jpg"

SESSION = getenv("SESSION", "AQAkGxMR326usVUVHWXl8A_AKlbP0M2Be5gHyTsnjrVVQdqYhIo4cy6vIl7HTNOX4cHFTfglweBoxt93w6W3yRlQjglifZIkwyHJ5gtqMH1gSyi6_SRKCWt9EsqllRB_rcDLlqC7Y72Fr0ttETciRJ6807KfCLRiTWz_GlodsnYsZ33pW8ZAggYn8hOFooZYHXz_hQedGCZS3YmtNx9p3SecKew7HahSLfDAXPY3g7mguEmQi94-mKT6onVgFePbG7vHohCB4OjTS6qT2-LE2i2JXhK4S_MvopuZuyqIIQdcusB83pPy2MU3KMxDhab3C0j7lTuZcxlF_xewpq07jEv3AAAAAVJP7wkA")
