from . import db


class SalaryModel(db.Base):
    __tablename__ = 'rate'
    __schema__ = "payroll"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def __repr__(self):
        return f"Job Group={self.name} id={self.id}"

