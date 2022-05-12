import logging.config

import yaml

with open('..\\..\\src\\configurations\\config_2.yaml', 'r') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

logger = logging.getLogger(__name__)

logger.debug('This is a debug message')
logger.error('This is a debug message')
logger.info('This is a debug message')

# https://gist.github.com/kingspp/9451566a5555fb022215ca2b7b802f19
