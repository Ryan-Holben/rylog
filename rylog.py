"""
  rylog.py

  Logging happening in a 3-dimensional Cartesian product.

  1. The logging level: [debug, info, warn, error]
  2. The logging category: e.g. software event, action, output
  3. The namespace: e.g. my_class.class_method
"""

from time import time
from colorama import Fore, Style
import inspect

from orderedenum import OrderedEnum

level = OrderedEnum('level', 'debug info warn error')


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

    def set_logging_level(self, level):
        self.level = level

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


class TestClass(object):

    def foo(self, log):
        log.debug("This is another test message!")


def main():
    r = RyLog()
    r.set_logging_level(level.debug)
    r.debug("hi")
    r.info("hi")
    r.warn("hi")
    r.error("hi")

    t = TestClass()
    t.foo(r)


main()
