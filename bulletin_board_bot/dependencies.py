from typing import Callable

from bulletin_board_bot.di import UserSpecificServiceContainer

from bulletin_board_bot.services.ad_service import BaseAdService


class DIContainer:
    def __init__(self,
                 ad_service_register: Callable[[], BaseAdService]):
        self._ad_service = UserSpecificServiceContainer(ad_service_register)

    @property
    def ad_service(self):
        return self._ad_service
