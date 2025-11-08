from aiogram import Bot, Dispatcher
import os
from dotenv import load_dotenv
from loguru import logger

# --- BASIC SETTING ---
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(TOKEN)  # type: ignore

logger.remove()
logger.add(
    sink="bot_logs.log",
    format="{time:DD:MM:YYYY HH:mm:ss} - {level} - {message}",
    level="INFO",
)

dispatcher = Dispatcher(bot=Bot)
