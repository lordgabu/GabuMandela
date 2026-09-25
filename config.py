import os
from dotenv import load_dotenv

load_dotenv()

# Telegram API credentials from my.telegram.org
API_ID = int(os.environ.get("API_ID", "5910854772"))
API_HASH = os.environ.get("API_HASH", "5910854772eef58bab25ec9aa78a9742")

# Bot Token from @BotFather
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN") or os.getenv("BOT_TOKEN", "8922066156:AAE55IQNXrwLox6aZSsn_J-TcSYpZWPpj0g")

# Owner ID and Authorized Users
OWNER_ID = int(os.environ.get("OWNER_ID", "8701689281"))

# Authorized users stored in memory (in a real app, use a database)
AUTH_USERS = [OWNER_ID]
