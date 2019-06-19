from flask import Flask
import configparser
from flask_restful import Api
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
    from resource.UploadResource import UploadResource
    from resource.ReportResource import ReportResource

    api = Api(server)
    api.add_resource(UploadResource, '/upload')
    api.add_resource(ReportResource, '/report')


def init_db(server):
    with app.app_context():
        from model import db
        from model.JobGroup import JobGroupModel
        from model.Employee import EmployeeModel
        from model.Files import FilesModel
        from model.History import HistoryModel
        from model.Rate import RateModel
        db.init_app(app=server)
        db.create_all()
        init_values()
        logger.info(f"Init db={db}")


def init_values():
    from model.Rate import RateModel
    from model import db
    a_rate = RateModel(rate=20, jid=1)
    b_rate = RateModel(rate=30, jid=2)
    session = db.session()
    try:
        session.add(a_rate)
        session.add(b_rate)
        session.commit()
    except Exception as e:
        logger.error(e)
        session.rollback()
    finally:
        db.session.remove()


def main():
    server = init_app(app)
    init_db(server=server)
    init_resources(server=server)
    server.run()


if __name__ == '__main__':
    main()
