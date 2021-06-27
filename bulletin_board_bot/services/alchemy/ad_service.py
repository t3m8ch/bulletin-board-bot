import logging

from sqlalchemy import select, func, desc
from sqlalchemy.ext.asyncio import AsyncEngine

from bulletin_board_bot.models import Ad
from bulletin_board_bot.services.ad_service import BaseAdService
from bulletin_board_bot.services.alchemy import AdTable


class AlchemyAdService(BaseAdService):
    def __init__(self, engine: AsyncEngine):
        self._engine = engine

        # These are the ads loaded in one SQL query
        self._ads = []

        # This is which declaration will be returned from the ones we took from the same SQL query
        self._current_ad_index = 0

        # The first time next_ad is called, this variable will become zero because -1 + 1 = 0
        self._current_page = -1

        # How many ads we will take per SQL query
        self._page_size = 10

    # TODO: Add this method to the base class
    async def number_of_ads(self) -> int:
        async with self._engine.connect() as conn:
            result = await conn.execute(
                func.count(AdTable.id)
            )
            return result.fetchall()[0][0]

    async def next_ad(self) -> Ad:
        # If we have already used all the declarations
        # previously loaded by the SQL query, and we need more
        if self._current_ad_index >= len(self._ads):
            self._current_page += 1
            await self._load_page()

        # If we call next_ad for the first time
        if not self._ads:
            await self._load_page()

        # If the user gets to the oldest ad and decides to next, we have to display the newest ad to the user.
        # We returned the oldest ad if even after calling _load_page we got an empty _ads
        if not self._ads:
            self._current_page = 0
            await self._load_page()

        ad = self._ads[self._current_ad_index]
        self._current_ad_index += 1

        return Ad(ad.id, ad.creation_date, ad.text)

    async def back_ad(self) -> Ad:
        self._current_ad_index -= 1

        # If we are at the beginning of the list of uploaded ads
        # in one SQL query, we have to go to the previous page
        if self._current_ad_index == 0:
            self._current_page -= 1

            # If we were on the first page and want to go
            # back, we have to go to the last page
            if self._current_page < 0:
                number_of_ads = await self.number_of_ads()
                last_page = (number_of_ads - 1) // self._page_size
                self._current_page = last_page

            await self._load_page(at_end=True)

        ad = self._ads[self._current_ad_index - 1]
        return Ad(ad.id, ad.creation_date, ad.text)

    async def _load_page(self, *, at_end=False):
        logging.debug("-----------------------Loading next page-----------------------")
        async with self._engine.connect() as conn:
            ads = await conn.execute(
                select(AdTable).order_by(desc(AdTable.creation_date)).slice(
                    self._current_page * self._page_size,
                    self._current_page * self._page_size + self._page_size
                )
            )
            self._ads = list(ads)
            self._current_ad_index = len(self._ads) if at_end else 0
