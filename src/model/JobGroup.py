from . import Column, Integer, String, Base


class FilesModel(Base):
    __tablename__ = 'jobgroup'
    __schema__ = "payroll"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return f"Job Group={self.name} id={self.id}"

