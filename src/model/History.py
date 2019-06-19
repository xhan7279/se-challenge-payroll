from . import db


class HistoryModel(db.Model):
    __tablename__ = 'history'
    __schema__ = "payroll"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    hours = db.Column(db.Float)
    eid = db.Column(db.Integer, db.ForeignKey('employee.id'), nullable=False)
    jid = db.Column(db.Integer, db.ForeignKey('jobgroup.id'), nullable=False)
    fid = db.Column(db.Integer, db.ForeignKey('files.id'), nullable=False)

    def __repr__(self):
        return f"Payment history={self.date} employee={self.eid} hours={self.hours}"

    def __init__(self, date, hours, eid, jid, fid):
        self.date = date
        self.hours = hours
        self.eid = eid
        self.jid = jid
        self.fid = fid

