import asyncio
from os import getenv
from aiogram import Bot
from dotenv import load_dotenv
from dispatcher import TOKEN, setup_dispatcher
from loguru import logger


# --- MAIN FUNC ---
async def main():
    load_dotenv()
    token = getenv("BOT_TOKEN")
    if not token:
        logger.critical("❌ TOKEN IS NOT AVAILABLE, CHECK .env")
        return
    bot = Bot(TOKEN)
    dp = setup_dispatcher(bot)

    await dp.start_polling(bot)
    logger.info("Bot started")


if __name__ == "__main__":
    asyncio.run(main())
