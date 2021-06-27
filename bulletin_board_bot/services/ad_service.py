from abc import ABC, abstractmethod
from datetime import datetime

from bulletin_board_bot.services.base_service import BaseService

from bulletin_board_bot.models import Ad


class BaseAdService(BaseService, ABC):
    @abstractmethod
    async def next_ad(self) -> Ad:
        pass

    @abstractmethod
    async def back_ad(self) -> Ad:
        pass


class FakeAdService(BaseAdService):
    def __init__(self):
        self._ads = sorted([
            Ad(
                id=6,
                creation_date=datetime(year=2021, month=6, day=26, hour=15, minute=30, second=21),
                text="Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. "
                     "Aenean massa."
            ),
            Ad(
                id=3,
                creation_date=datetime(year=2021, month=5, day=28, hour=23, minute=50, second=19),
                text="Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus."
            ),
            Ad(
                id=2,
                creation_date=datetime(year=2021, month=5, day=28, hour=23, minute=52, second=56),
                text="Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis "
                     "enim."
            ),
            Ad(
                id=1,
                creation_date=datetime(year=2021, month=3, day=19, hour=9, minute=45, second=59),
                text="Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, "
                     "imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer "
            ),
        ], key=lambda ad: ad.creation_date, reverse=True)
        self._current_ad_index = -1

    async def next_ad(self) -> Ad:
        if self._current_ad_index == len(self._ads) - 1:
            self._current_ad_index = 0
        else:
            self._current_ad_index += 1

        return self._ads[self._current_ad_index]

    async def back_ad(self) -> Ad:
        if self._current_ad_index in (0, -1):
            self._current_ad_index = len(self._ads) - 1
        else:
            self._current_ad_index -= 1

        return self._ads[self._current_ad_index]
