from . import db


class JobGroupModel(db.Model):
    __tablename__ = 'jobgroup'
    __schema__ = "payroll"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    history = db.relationship('HistoryModel', backref='jobgroup', lazy=True)
    rate = db.relationship('RateModel', backref='jobgroup', lazy=True)

    def __repr__(self):
        return f"Job Group={self.name} id={self.id}"

    def __init__(self, name):
        self.name = name
