from abc import abstractmethod, ABC

from bulletin_board_bot.models import AdModel

from bulletin_board_bot.models.user import UserModel
from bulletin_board_bot.services.base_service import BaseService


class BaseUserService(BaseService, ABC):
    @abstractmethod
    async def register_user(self, telegram_id: int) -> UserModel:
        pass

    @abstractmethod
    async def add_ad_to_favorites(self, ad: AdModel, user_telegram_id: int):
        pass

    @abstractmethod
    async def remove_ad_from_favorites(self, ad: AdModel, user_telegram_id: int):
        pass
