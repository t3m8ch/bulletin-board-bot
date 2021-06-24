from abc import ABC, abstractmethod

from bulletin_board_bot.models import Ad


class BaseAdService(ABC):
    @abstractmethod
    async def next_ad(self) -> Ad:
        pass

    @abstractmethod
    async def back_ad(self) -> Ad:
        pass


class FakeAdService(BaseAdService):
    def __init__(self):
        self._ads = [
            Ad("Ad1"),
            Ad("Ad2"),
            Ad("Ad3"),
            Ad("Ad4"),
        ]
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
