from . import db


class EmployeeModel(db.Model):
    __tablename__ = 'employee'
    __schema__ = "payroll"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    history = db.relationship('HistoryModel', backref='employee', lazy=True)


    def __repr__(self):
        return f"Employee={self.name} id={self.id}"

