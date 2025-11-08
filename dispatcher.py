from aiogram.types import Message
from aiogram import Bot, Dispatcher, F
from loguru import logger
import os
from dotenv import load_dotenv

# --- BASIC SETTING ---

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(TOKEN)  # type: ignore

logger.remove()
logger.add(
    sink="bot_logs.log",
    format="{time:DD:MM:YYYY | HH:mm:ss} | {level} | {message}",
    level="INFO",
)


# --- SETUP Dispatcher ---
def setup_dispatcher(bot: Bot) -> Dispatcher:
    dp = Dispatcher()

    @dp.message(F.text)
    async def echo_handler(message: Message):
        if message.text != "/start":
            logger.info(f"Taked message: {message.text}")
            await message.reply(f"You wrote: {message.text}")
        else:
            logger.info("💽 Handled start command")
        logger.info("✅ Handler done")

    return dp
