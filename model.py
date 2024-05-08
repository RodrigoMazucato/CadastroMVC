from sqlalchemy import Integer, String, Column
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
  pass


class User(Base):
  __tablename__ = 'User'
  id = Column(Integer, primary_key=True, autoincrement=True)
  nome = Column(String)
  idade = Column(Integer)


