# rylog

> simple yet functional logging for Python 3.x

Why?  I found that the rather simple functionality I wanted out of a logging module in Python wasn't as easy to accomplish with Pyton's `logging` module as it should be.  So I reinvented the wheel-- sorry in advance.

## usage
Logging with rylog is controlled with a simple server-client model.  First, create the server and set options and filters:

```python
r = rylog.RyLog()
r.set_logging_level(rylog.level.warn)
r.set_format("|{category}|{level}|{function}> - {msg}")
```

You can then create logger instances in categories of your choosing:
```python
basic_log = r.get_logger_instance()
memory_log = r.get_named_logger_instance("memory")
action_log = r.get_named_logger_instance("action")
output_log = r.get_named_logger_instance("output")
```

Updates to the server affect all derived loggers.
```python
r.set_categories(["memory", "output"])  # Whitelist categories
memory_log.info("hello")                # Won't be logged since info < warn
action_log.warn("gutentag2")            # Won't be logged since action isn't turned on
output_log.warn("konnichiwa")           # Will be logged
```

The `{function}` name will give a format of `foo.bar` or `baz` depending on if logging occurred in a class method or a free function.

```python
def bar(log):
  log.error("I'm in a function!")


class TestClass(object):
  def foo(self, log):
    log.warn("I'm in a class method!")

t = TestClass()
t.foo(basic_log)  # |warn|TestClass.foo> - This is another test message!
bar(basic_log)    # |error|bar> - I'm in a function!
```

## formatting
Formatting is done through [named placeholders](https://pyformat.info/#named_placeholders).  The current supported keywords are:
* level
* function
* category
* time
* msg
