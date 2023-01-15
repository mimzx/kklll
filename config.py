from os import getenv
from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "26788480"))
API_HASH = getenv("API_HASH", "858d65155253af8632221240c535c314")

BOT_TOKEN = getenv("BOT_TOKEN", "5654221248:AAGHYhLeyVNlqlbodQ2mAOhBLOS2mjhcWB4")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID", "5675937545"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/4faa7266294d6040d8084.png")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/2fc2b008e321ae4592ee4.jpg")

SESSION = getenv("SESSION", "AQA-oE2rXZpjVTRZg_mZqgY_Y-NdmlOFMNvgdJHMg3_be7C1TfxpWHfBflN5ClyZQCW8n97e93y9FSzdmVcYbLkBmSqFMU2OYnr62FmfbzXMiXo3NyPphqjJm5sv8nfg8YtWhNZHepdDLIVPrAdIIZ6EPgYSIAeDeG34VdL7ireOOgKKsrcJfQ8iTPcbGdQp96tCLSwl5ezbXVpY8K3zRfY-uAxPZLhQBxmB-8TGze-eZsT1TQfzK0w-Vsfk3FK1GD_NsyOFoKMRqePb8_GB_EHSzTrSRBKKbr3vn0IX_dAqUJCZ4JwIbOqhE2_wU8dsBIsK-ZNbeFlmIO0UFPnMyJ8NAAAAAVA_P_wA") 

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/TogaSupport")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/TogaSupport")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))


FAILED = "https://telegra.ph/file/2fc2b008e321ae4592ee4.jpg"
