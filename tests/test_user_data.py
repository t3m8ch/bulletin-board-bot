from bulletin_board_bot.user_data import UserDataStorage


def test_user_data_if_user_is_not_found():
    user_id_1 = 123
    user_id_2 = 456
    storage = UserDataStorage()

    user_data_1 = storage.for_user(user_id_1)
    user_data_2 = storage.for_user(user_id_2)

    assert user_data_1 is not user_data_2


def test_user_data_if_user_is_found():
    user_id = 123
    storage = UserDataStorage()

    user_data_1 = storage.for_user(user_id)
    user_data_2 = storage.for_user(user_id)

    assert user_data_1 is user_data_2
