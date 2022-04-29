class Level:
    DEBUG = 0
    INFO = 1
    WARNING = 2


def check_level(level):
    def wrapper(func):
        def check(*args):
            if args[0].level <= level:
                return func(*args)
            return None

        return check

    return wrapper


class Log:
    level = Level.DEBUG

    @classmethod
    @check_level(Level.DEBUG)
    def debug(cls, _class, text):
        print(f"[DEBUG] {_class.__class__.__name__}: {text}")

    @classmethod
    @check_level(Level.INFO)
    def info(cls, _class, text):
        print(f"[INFO] {_class.__class__.__name__}: {text}")

    @classmethod
    @check_level(Level.WARNING)
    def warning(cls, _class, text):
        print(f"[WARNING] {_class.__class__.__name__}: {text}")
