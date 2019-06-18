from flask import Flask
import configparser
import logging
import logging.config
from model import engine
import sqlalchemy

logger = None


def init_app(server):
    logger = init_logging()
    conf_fpath = 'config.ini'
    config = configparser.ConfigParser()

    config.read(conf_fpath)

    server.config['SQLALCHEMY_DATABASE_URI'] = config.get('Database', 'connection_uri')
    server.config['SERVER_NAME'] = config.get('Server', 'Name')
    server.config['SECRET_KEY'] = config.get('Server', 'SecretKey')

    engine = sqlalchemy.create_engine(config.get('Database', 'Connection_Uri'))
    logger.info(f"engine created ={engine}")

    return server


def init_logging():
    logging.config.fileConfig("log.ini")
    return logging.getLogger('root')


def main():
    server = init_app(Flask(__name__))
    server.run()


if __name__ == '__main__':
    main()
