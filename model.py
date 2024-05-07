from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine("sqlite:///exemplo.db", echo=True)

Session = sessionmaker(bind=engine) # bind é para Ligar de fato a sessão
session = Session()

Base = declarative_base()

class User(Base):
  __tablename__ = 'users'
  id = Column(Integer, primary_key=True, autoincrement=True)
  nome = Column(String)
  idade = Column(Integer)