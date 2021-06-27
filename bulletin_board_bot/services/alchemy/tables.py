from sqlalchemy import Integer, Column, DateTime, func, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class AdTable(Base):
    __tablename__ = "ad"

    id = Column(Integer, primary_key=True)
    creation_date = Column(DateTime, server_default=func.now())
    text = Column(String(300), nullable=False)

    def __repr__(self):
        return f"AdTable(id={self.id!r}, " \
               f"creation_date={self.creation_date!r}, " \
               f"text={self.text!r})"
