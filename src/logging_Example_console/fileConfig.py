import logging.config

# logging.config.fileConfig('/path/to/logging.ini', disable_existing_loggers=False)
logging.config.fileConfig('\\src\\configurations\\logging.ini', disable_existing_loggers=False)
logger = logging.getLogger(__name__)

# https://www.datadoghq.com/blog/python-logging-best-practices/
# https://coralogix.com/blog/python-logging-best-practices-tips/
