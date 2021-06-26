from typing import Callable

from bulletin_board_bot.services.base_service import BaseService


class UserSpecificServiceContainer:
    r"""Container for a service **instance** that is **unique for each bot user**"""
    def __init__(self, create_service_function: Callable[[], BaseService]):
        r"""
        Parameters
        ----------
        create_service_function :
            Function returning a new service instance
        """
        self._create_service = create_service_function
        self._services = {}

    def get_service(self, user_id: int, necessary_new=False):
        if self._services.get(user_id) is None or necessary_new:
            service = self._create_service()
            self._services[user_id] = service
            return service

        return self._services[user_id]


class SingletonServiceContainer:
    r"""Container for service that is in a **single instance**"""
    def __init__(self, create_service_function):
        r"""
        Parameters
        ----------
        create_service_function :
            Function returning a new service instance
        """
        self._create_service = create_service_function
        self._service = None

    def get_service(self, necessary_new=False):
        if self._service is None or necessary_new:
            self._service = self._create_service()
            return self._service

        return self._service
