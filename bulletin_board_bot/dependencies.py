from typing import Callable

from bulletin_board_bot.services.ad_service import BaseAdService
from bulletin_board_bot.services.user_service import BaseUserService
from bulletin_board_bot.di import UserSpecificServiceContainer, SingletonServiceContainer


class DIContainer:
    def __init__(self,
                 ad_service_register: Callable[[], BaseAdService],
                 user_service_register: Callable[[], BaseUserService]):
        self._ad_service = UserSpecificServiceContainer(ad_service_register)
        self._user_service = SingletonServiceContainer(user_service_register)

    @property
    def ad_service(self):
        return self._ad_service

    @property
    def user_service(self):
        return self._user_service
