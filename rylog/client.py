from .misc import level


class LoggerClient(object):

    def __init__(self):
        self.server = None
        self.category = ""

    def connect_to_server(self, server):
        self.server = server
        server.connect_to_client(self)

    def log(self, **kwargs):
        return self.server.log(**kwargs)

    def debug(self, msg):
        return self.server.log(
            level=level.debug, msg=msg, category=self.category)

    def info(self, message):
        return self.server.log(
            level=level.info, msg=message, category=self.category)

    def warn(self, message):
        return self.server.log(
            level=level.warn, msg=message, category=self.category)

    def error(self, message):
        return self.server.log(
            level=level.error, msg=message, category=self.category)

    def set_category(self, cat):
        self.category = cat
