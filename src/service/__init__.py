import logging, logging.config

def init_logging():
    logging.config.fileConfig("log.ini")
    return logging.getLogger('root')

logger = init_logging()
