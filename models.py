from sqlalchemy import Column, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Card(Base):
    __tablename__ = "cards"

    id = Column(String, primary_key=True)
    status = Column(String)
    atm_limit = Column(Float)
    pos_limit = Column(Float)
    ecom_limit = Column(Float)
    currency = Column(String)
    transaction_types = Column(String)  # comma-separated for simplicity