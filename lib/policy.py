from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Policy(Base):
    __table__ = 'policies'

    id = Column(Integer, primary_key=True)
    policy_type = Column(String)
    start = Column(String)
    end = Column(String)
    premium = Column(Integer)
    coverage = Column(String)
    policyholder_id = Column(Integer, ForeignKey('policyholders.id'))

    policyholder = relationship('Policyholder', back_populates='policies')


class Policyholder(Base):
    __table__ = 'policyholders'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    phone_number = Column(String)
    address = Column(String)

    policies = relationship('Policy', back_populates='policyholder')


class Claim()
