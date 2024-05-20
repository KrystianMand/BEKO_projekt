from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import ARRAY
from webapp.database import db

class GatewaysModel(db.Model):
    __tablename__ = 'gateways'

    id = Column(Integer, primary_key=True)
    ip = Column(String())

class AnimationsModel(db.Model):
    __tablename__ = 'animations'

    id = Column(Integer, primary_key=True)
    name = Column(String())
    rgb_values = Column(ARRAY(Integer, dimensions=3), nullable=False)
