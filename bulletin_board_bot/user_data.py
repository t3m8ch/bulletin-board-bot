class UserDataStorage:
    def __init__(self):
        self._users = {}

    def for_user(self, user_id: int):
        result = self._users.get(user_id)

        if result is None:
            user_data = {}
            self._users[user_id] = user_data
            return user_data

        return result
