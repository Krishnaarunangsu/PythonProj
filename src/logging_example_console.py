import logging.config

import yaml

with open('..\\src\\configurations\\logging.config', 'r') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

logger = logging.getLogger(__name__)

logger.debug('This is a debug message')

# https://fangpenlin.com/posts/2012/08/26/good-logging-practice-in-python/
# https://realpython.com/lessons/logger-config-file/
# https://coderzcolumn.com/tutorials/python/logging-config-simple-guide-to-configure-loggers-from-dictionary-and-config-files-in-python
# https://zetcode.com/python/logging/
# https://www.toptal.com/python/in-depth-python-logging
# https://docs.python.org/3/library/logging.config.html
# https://www.codegrepper.com/code-examples/python/sample+logging+configuration+file+python
