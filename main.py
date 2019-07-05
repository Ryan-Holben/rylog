import rylog

# from rylog import *


class TestClass(object):

    def foo(self, log):
        log.warn("This is another test message!")


def main():
    r = rylog.RyLog()
    r.set_logging_level(rylog.level.warn)
    r.set_format("|{category}|{level}|{function}> - {msg}")
    r.add_category("action")

    logger = r.get_logger_instance()
    memory_log = r.get_named_logger_instance("memory")
    action_log = r.get_named_logger_instance("action")
    output_log = r.get_named_logger_instance("output")

    logger.debug("Ahhhh!  I'm scared. :'(")
    logger.info("Ahhhh!  I'm scared. :'(")
    logger.warn("Ahhhh!  I'm scared. :'(")
    logger.error("Ahhhh!  I'm scared. :'(")

    r.set_categories(["memory", "output"])

    memory_log.warn("hello")
    action_log.warn("gutentag1")
    action_log.warn("gutentag2")
    output_log.warn("konnichiwa")

    t = TestClass()
    t.foo(logger)


main()
