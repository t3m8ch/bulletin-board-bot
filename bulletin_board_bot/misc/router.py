from aiogram import Dispatcher


class Router:
    """The Router class allows you to register handlers using decorators,
    without using the global variable of the dispatcher"""
    def __init__(self):
        self._registrars = []

    def register_handlers(self, dp: Dispatcher):
        """Register all handlers defined by the router through the decorators.
        It is recommended to call the method from the parent module,
        where the dispatcher object is available"""
        for reg in self._registrars:
            reg(dp)

    def message(self, *args, **kwargs):
        def decorator(callback):
            def registrar(dp: Dispatcher):
                dp.register_message_handler(callback, *args, **kwargs)

            self._registrars.append(registrar)
            return callback

        return decorator

    def edited_message(self, *args, **kwargs):
        def decorator(callback):
            def registrar(dp: Dispatcher):
                dp.register_edited_message_handler(callback, *args, **kwargs)

            self._registrars.append(registrar)
            return callback

        return decorator

    def channel_post(self, *args, **kwargs):
        def decorator(callback):
            def registrar(dp: Dispatcher):
                dp.register_channel_post_handler(callback, *args, **kwargs)

            self._registrars.append(registrar)
            return callback

        return decorator

    def edited_channel_post(self, *args, **kwargs):
        def decorator(callback):
            def registrar(dp: Dispatcher):
                dp.register_edited_channel_post_handler(callback, *args, **kwargs)

            self._registrars.append(registrar)
            return callback
        return decorator

    def inline(self, *args, **kwargs):
        def decorator(callback):
            def registrar(dp: Dispatcher):
                dp.register_inline_handler(callback, *args, **kwargs)

            self._registrars.append(registrar)
            return callback

        return decorator

    def chosen_inline(self, *args, **kwargs):
        def decorator(callback):
            def registrar(dp: Dispatcher):
                dp.register_chosen_inline_handler(callback, *args, **kwargs)

            self._registrars.append(registrar)
            return callback

        return decorator

    def callback_query(self, *args, **kwargs):
        def decorator(callback):
            def registrar(dp: Dispatcher):
                dp.register_callback_query_handler(callback, *args, **kwargs)

            self._registrars.append(registrar)
            return callback

        return decorator

    def shipping_query(self, *args, **kwargs):
        def decorator(callback):
            def registrar(dp: Dispatcher):
                dp.register_shipping_query_handler(callback, *args, **kwargs)

            self._registrars.append(registrar)
            return callback

        return decorator

    def pre_checkout_query(self, *args, **kwargs):
        def decorator(callback):
            def registrar(dp: Dispatcher):
                dp.register_pre_checkout_query_handler(callback, *args, **kwargs)

            self._registrars.append(registrar)
            return callback

        return decorator

    def poll(self, *args, **kwargs):
        def decorator(callback):
            def registrar(dp: Dispatcher):
                dp.register_poll_handler(callback, *args, **kwargs)

            self._registrars.append(registrar)
            return callback

        return decorator

    def poll_answer(self, *args, **kwargs):
        def decorator(callback):
            def registrar(dp: Dispatcher):
                dp.register_poll_answer_handler(callback, *args, **kwargs)

            self._registrars.append(registrar)
            return callback

        return decorator

    def my_chat_member(self, *args, **kwargs):
        def decorator(callback):
            def registrar(dp: Dispatcher):
                dp.register_my_chat_member_handler(callback, *args, **kwargs)

            self._registrars.append(registrar)
            return callback

        return decorator

    def chat_member(self, *args, **kwargs):
        def decorator(callback):
            def registrar(dp: Dispatcher):
                dp.register_chat_member_handler(callback, *args, **kwargs)

            self._registrars.append(registrar)
            return callback

        return decorator

    def errors(self, *args, **kwargs):
        def decorator(callback):
            def registrar(dp: Dispatcher):
                dp.register_errors_handler(callback, *args, **kwargs)

            self._registrars.append(registrar)
            return callback

        return decorator
