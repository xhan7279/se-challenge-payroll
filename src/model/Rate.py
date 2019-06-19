from . import db


class RateModel(db.Model):
    __tablename__ = 'rate'
    __schema__ = "payroll"

    id = db.Column(db.Integer, primary_key=True)
    rate = db.Column(db.String)
    jid = db.Column(db.Integer, db.ForeignKey('jobgroup.id'), nullable=False)

    def __repr__(self):
        return f"Rate={self.rate} Job Group={self.jid}"

    def __init__(self, rate, jid):
        self.rate = rate
        self.jid = jid

