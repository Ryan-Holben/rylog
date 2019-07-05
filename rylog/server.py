from time import time
from colorama import Fore, Style
import inspect

from .misc import level
from .client import LoggerClient


class RyLog(object):
    colors = {
        level.debug: Style.DIM + level.debug.name + Style.RESET_ALL,
        level.info: Fore.GREEN + level.info.name + Style.RESET_ALL,
        level.warn: Fore.YELLOW + level.warn.name + Style.RESET_ALL,
        level.error: Fore.RED + level.error.name + Style.RESET_ALL,
    }

    def __init__(self):
        self.format_string = "|{level}|{function}> - {msg}"
        self.level = level.info
        self.colored = True
        self.clients = []
        self.allowed_categories = set()

    def set_format(self, fmt):
        self.format_string = fmt

    def set_logging_level(self, level):
        self.level = level

    def add_category(self, category):
        self.allowed_categories.add(category)

    def remove_category(self, category):
        self.allowed_categories.remove(category)

    def set_categories(self, categories):
        self.allowed_categories = set(categories)

    def use_colored_text(self, colored):
        self.colored = colored

    def set_format(self, format_string):
        """Valid keywords:
            level, category, function, name, msg
        """
        self.format_string = format_string

    def log(self, **kwargs):
        if kwargs["level"] < self.level:
            return

        kwargs["function"] = self.__get_calling_function_name()
        kwargs["level"] = self.colors[
            kwargs["level"]] if self.colored else kwargs["level"].name
        kwargs["time"] = time()
        if kwargs["category"] and kwargs[
                "category"] not in self.allowed_categories:
            return

        print(self.format_string.format(**kwargs))

    def debug(self, msg):
        return self.log(level=level.debug, msg=msg)

    def info(self, message):
        return self.log(level=level.info, msg=message)

    def warn(self, message):
        return self.log(level=level.warn, msg=message)

    def error(self, message):
        return self.log(level=level.error, msg=message)

    def __get_calling_function_name(self):
        """Assumed to be called by a member variable of this class, which in
        turn was called by some outside function f().  If if is a member of
        class C, we return "C.f", otherwise we return "f"."""
        f = inspect.currentframe()
        caller = f.f_back.f_back.f_back
        name = caller.f_code.co_name
        if "self" in caller.f_locals:
            return caller.f_locals['self'].__class__.__name__ + "." + name
        else:
            return name

    def connect_to_client(self, client):
        if client not in self.clients:
            self.clients.append(client)

    def get_logger_instance(self):
        logger = LoggerClient()
        logger.connect_to_server(self)
        return logger

    def get_named_logger_instance(self, category):
        logger = self.get_logger_instance()
        logger.set_category(category)
        return logger
