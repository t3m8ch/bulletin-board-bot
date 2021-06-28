import logging

from bulletin_board_bot.models.user import User
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncEngine

from bulletin_board_bot.services.alchemy import UserTable, FavoriteTable
from bulletin_board_bot.services.user_service import BaseUserService


class AlchemyUserService(BaseUserService):
    def __init__(self, engine: AsyncEngine):
        self._engine = engine

    async def register_user(self, telegram_id: int) -> User:
        async with self._engine.connect() as conn:
            user = await conn.execute(
                insert(UserTable)
                .values(telegram_id=telegram_id)
                .returning(
                    UserTable.id,
                    UserTable.creation_date,
                    UserTable.telegram_id
                )
            )
            await conn.commit()
            user = user.fetchall()[0]

            return User(
                id=user.id,
                creation_date=user.creation_date,
                telegram_id=user.telegram_id
            )

    async def add_ad_to_favorites(self, ad_id: int, user_telegram_id: int):
        async with self._engine.connect() as conn:
            user_id = await conn.execute(
                select(UserTable.id)
                .where(UserTable.telegram_id == user_telegram_id)
            )
            user_id = user_id.fetchall()

            if not user_id:
                user = await self.register_user(user_telegram_id)
                user_id = user.id
            else:
                user_id = user_id[0].id

            await conn.execute(
                insert(FavoriteTable)
                .values(
                    user_id=user_id,
                    ad_id=ad_id
                )
            )
            await conn.commit()
