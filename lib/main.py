from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Policy, Policyholder, Claim

engine = create_engine('sqlite:///insurance.db')
Session = sessionmaker(bind=engine)
session = Session()
