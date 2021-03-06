from bulletin_board_bot.models import AdModel

from bulletin_board_bot.models.user import UserModel
from sqlalchemy import insert, select, delete
from sqlalchemy.ext.asyncio import AsyncEngine

from bulletin_board_bot.services.alchemy import UserTable, FavoriteTable
from bulletin_board_bot.services.user_service import BaseUserService


class AlchemyUserService(BaseUserService):
    def __init__(self, engine: AsyncEngine):
        self._engine = engine

    async def register_user(self, telegram_id: int) -> UserModel:
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

            return UserModel(
                id=user.id,
                creation_date=user.creation_date,
                telegram_id=user.telegram_id
            )

    async def add_ad_to_favorites(self, ad: AdModel, user_telegram_id: int):
        user_id = await self._check_user(user_telegram_id)

        async with self._engine.connect() as conn:
            await conn.execute(
                insert(FavoriteTable)
                .values(
                    user_id=user_id,
                    ad_id=ad.id
                )
            )
            await conn.commit()

        ad.in_favorites = True

    async def remove_ad_from_favorites(self, ad: AdModel, user_telegram_id: int):
        user_id = await self._check_user(user_telegram_id)

        async with self._engine.connect() as conn:
            await conn.execute(
                delete(FavoriteTable)
                .where(FavoriteTable.ad_id == ad.id)
                .where(FavoriteTable.user_id == user_id)
            )
            await conn.commit()

        ad.in_favorites = False

    async def _check_user(self, user_telegram_id: int) -> UserModel:
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

        return user_id
