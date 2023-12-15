from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.models import Policy, Policyholder, Claim

engine = create_engine('sqlite:///insurance.db')
Session = sessionmaker(bind=engine)
session = Session()
