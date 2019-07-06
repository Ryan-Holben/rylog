import rylog


class TestClass(object):

    def foo(self, log):
        log.warn("This is another test message!")


def bar(log):
    log.error("I'm in a function!")


def main():
    r = rylog.RyLog()
    r.set_logging_level(rylog.level.warn)
    r.set_format("|{level}|{function}> - {msg}")
    r.add_category("action")

    basic_log = r.get_logger_instance()
    memory_log = r.get_named_logger_instance("memory")
    action_log = r.get_named_logger_instance("action")
    output_log = r.get_named_logger_instance("output")

    basic_log.debug("Ahhhh!  I'm scared. :'(")
    basic_log.info("Ahhhh!  I'm scared. :'(")
    basic_log.warn("Ahhhh!  I'm scared. :'(")
    basic_log.error("Ahhhh!  I'm scared. :'(")

    r.set_categories(["memory", "output"])

    memory_log.warn("hello")
    action_log.warn("gutentag1")
    action_log.warn("gutentag2")
    output_log.warn("konnichiwa")

    t = TestClass()
    t.foo(basic_log)
    bar(basic_log)


main()
