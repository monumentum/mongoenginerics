def err_handler(fn):
    def wrapper():
        try:
            fn()
        except Exception as e:
            raise e
    return wrapper
