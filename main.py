import rylog

# from rylog import *


class TestClass(object):

    def foo(self, log):
        log.warn("This is another test message!")


def main():
    r = rylog.RyLog()
    r.set_logging_level(rylog.level.warn)

    logger = r.getLoggerInstance()
    logger.debug("Ahhhh!  I'm scared. :'(")
    logger.info("Ahhhh!  I'm scared. :'(")
    logger.warn("Ahhhh!  I'm scared. :'(")
    logger.error("Ahhhh!  I'm scared. :'(")
    logger.log(level=rylog.level.error, msg="AHH")

    t = TestClass()
    t.foo(logger)


main()
