from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def transaction(func):
    def inner(*args, **kwargs):
        session = db.session()
        try:
            func(session, *args, **kwargs)
            session.commit()
        except Exception as e:

            session.rollback()
            raise e
        finally:
            db.session.remove()
    return inner
