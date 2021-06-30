import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor
from bulletin_board_bot.misc.user_data import UserDataStorage

from bulletin_board_bot.services.alchemy.user_service import AlchemyUserService
from sqlalchemy.ext.asyncio import create_async_engine

from bulletin_board_bot.dependencies import DIContainer

from bulletin_board_bot.config import cfg, UpdateMethod

from bulletin_board_bot.handlers import register_handlers
from bulletin_board_bot.middlewares import setup_middlewares
from bulletin_board_bot.services.alchemy import AlchemyAdService


async def on_startup(dp: Dispatcher):
    if cfg.update_method == UpdateMethod.WEBHOOKS:
        await dp.bot.set_webhook(cfg.tg_webhook_url)

    logging.warning("START BOT!")


async def on_shutdown(dp: Dispatcher):
    await dp.bot.delete_webhook()

    await dp.storage.close()
    await dp.storage.wait_closed()

    logging.warning("BOT STOPPED!")


def run():
    # Logging configuration
    logging.basicConfig(
        level=cfg.log_level,
        format=cfg.log_format
    )

    # Base
    event_loop = asyncio.get_event_loop()
    storage = MemoryStorage()  # TODO: Redis
    bot = Bot(
        token=cfg.tg_token,
        parse_mode=cfg.parse_mode
    )
    dp = Dispatcher(bot, storage=storage)

    engine = create_async_engine(cfg.db_connection_str)
    container = DIContainer(
        lambda: AlchemyAdService(engine),
        lambda: AlchemyUserService(engine)
    )

    user_data = UserDataStorage()
    setup_middlewares(dp, user_data, container)

    # Register
    register_handlers(dp)

    # Start bot!
    if cfg.update_method == UpdateMethod.LONG_POLLING:
        executor.start_polling(
            dispatcher=dp,
            on_startup=on_startup,
            on_shutdown=on_shutdown,
            loop=event_loop,
            skip_updates=True
        )

    elif cfg.update_method == UpdateMethod.WEBHOOKS:
        executor.start_webhook(
            dispatcher=dp,
            on_startup=on_startup,
            on_shutdown=on_shutdown,
            loop=event_loop,
            webhook_path=cfg.tg_webhook_path,
            host=cfg.webapp_host,
            port=cfg.webapp_port,
            skip_updates=True
        )


if __name__ == "__main__":
    run()
