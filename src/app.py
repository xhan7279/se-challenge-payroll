from flask import Flask
import configparser
from flask_restful import Api
from resource.UploadResource import UploadResource
from service import logger

app = Flask(__name__)


def init_app(server):
    conf_fpath = 'config.ini'
    config = configparser.ConfigParser()

    config.read(conf_fpath)

    server.config['SQLALCHEMY_DATABASE_URI'] = config.get('Database', 'connection_uri')
    server.config['SERVER_NAME'] = config.get('Server', 'Name')
    server.config['SECRET_KEY'] = config.get('Server', 'SecretKey')
    server.config['UPLOAD_FOLDER'] = config.get('Server', 'UploadFolder')

    return server


def init_resources(server):
    logger.info(server)
    api = Api(server)
    api.add_resource(UploadResource, '/upload')


def init_db(server):
    with app.app_context():
        from model import db
        from model.JobGroup import JobGroupModel
        from model.Employee import EmployeeModel
        from model.Files import FilesModel
        from model.History import HistoryModel
        db.init_app(app=server)
        db.create_all()
        logger.info(f"Init db={db}")


def main():
    server = init_app(app)
    init_db(server=server)
    init_resources(server=server)
    server.run()


if __name__ == '__main__':
    main()
