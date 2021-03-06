from abc import ABC, abstractmethod

from bulletin_board_bot.services.base_service import BaseService

from bulletin_board_bot.models import AdModel


class BaseAdService(BaseService, ABC):
    @abstractmethod
    async def next_ad(self) -> AdModel:
        pass

    @abstractmethod
    async def back_ad(self) -> AdModel:
        pass
