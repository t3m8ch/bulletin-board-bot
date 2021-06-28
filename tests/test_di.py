from typing import NamedTuple

from bulletin_board_bot.services.base_service import BaseService

from bulletin_board_bot.di import UserSpecificServiceContainer, SingletonServiceContainer


# TODO: Fix this
class FakeService(BaseService, NamedTuple):
    something: str


def test_user_specific_service_container_get_container_user_doesnt_exists():
    container = UserSpecificServiceContainer(lambda: FakeService("some"))
    user_id_1 = 123
    user_id_2 = 345

    service_1 = container.get_service(user_id_1)
    service_2 = container.get_service(user_id_2)

    assert service_1 is not service_2


def test_user_specific_service_container_get_container_user_exists():
    container = UserSpecificServiceContainer(lambda: FakeService("some"))
    user_id = 123

    service_1 = container.get_service(user_id)
    service_2 = container.get_service(user_id)

    assert service_1 is service_2


def test_user_specific_service_container_get_container_necessary_new_is_true():
    container = UserSpecificServiceContainer(lambda: FakeService("some"))
    user_id = 123

    service_1 = container.get_service(user_id, True)
    service_2 = container.get_service(user_id, True)

    assert service_1 is not service_2


def test_singleton_service_container_get_container_service_is_created():
    container = SingletonServiceContainer(lambda: FakeService("some"))

    service_1 = container.get_service()
    service_2 = container.get_service()

    assert service_1 is service_2


def test_singleton_service_container_get_container_necessary_new_is_true():
    container = SingletonServiceContainer(lambda: FakeService("some"))

    service_1 = container.get_service()
    service_2 = container.get_service(True)

    assert service_1 is not service_2
