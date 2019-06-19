from . import db
import datetime


class FilesModel(db.Model):
    __tablename__ = 'files'
    __schema__ = "payroll"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    date = db.Column(db.DateTime)
    history = db.relationship('HistoryModel', backref='files', lazy=True)

    def __repr__(self):
        return f"File={self.name} uploaded at {self.date}"

    def __init__(self, name):
        self.name = name
        self.date = datetime.datetime.now()

