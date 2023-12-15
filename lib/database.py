from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Policy, Policyholder, Claim

engine = create_engine('sqlite:///insurance.db')
Session = sessionmaker(bind=engine)
session = Session()


def create_policy(policy_type, start, end, premium, coverage, policyholder_id):
    new_policy = Policy(
        policy_type=policy_type,
        start=start,
        end=end,
        premium=premium,
        coverage=coverage,
        policyholder_id=policyholder_id
    )
    session.add(new_policy)
    session.commit()
    return new_policy


def get_policy_by_id(policy_id):
    return session.query(Policy).filter_by(id=policy_id).first()


def update_policy(policy_id, **kwargs):
    policy = get_policy_by_id(policy_id)
    if policy:
        for key, value in kwargs.items():
            setattr(policy, key, value)
        session.commit()
    return policy


def delete_policy(policy_id):
    policy = get_policy_by_id(policy_id)
    if policy:
        session.delete(policy)
        session.commit()
        return True
    return False


def create_policyholder(name, email, phone_number, address):
    new_policyholder = Policyholder(
        name=name,
        email=email,
        phone_number=phone_number,
        address=address
    )
    session.add(new_policyholder)
    session.commit()
    return new_policyholder


def get_policyholder_by_id(policyholder_id):
    return session.query(Policyholder).filter_by(id=policyholder_id).first()


def update_policyholder(policyholder_id, **kwargs):
    policyholder = get_policyholder_by_id(policyholder_id)
    if policyholder:
        for key, value in kwargs.items():
            setattr(policyholder, key, value)
        session.commit()
    return policyholder


def delete_policyholder(policyholder_id):
    policyholder = get_policyholder_by_id(policyholder_id)
    if policyholder:
        session.delete(policyholder)
        session.commit()
        return True
    return False


def create_claim(policy_id, policyholder_id, claim_date, claim_details, status):
    new_claim = Claim(
        policy_id=policy_id,
        policyholder_id=policyholder_id,
        claim_date=claim_date,
        claim_details=claim_details,
        status=status
    )
    session.add(new_claim)
    session.commit()
    return new_claim


def get_claim_by_id(claim_id):
    return session.query(Claim).filter_by(id=claim_id).first()


def update_claim(claim_id, **kwargs):
    claim = get_claim_by_id(claim_id)
    if claim:
        for key, value in kwargs.items():
            setattr(claim, key, value)
        session.commit()
    return claim


def delete_claim(claim_id):
    claim = get_claim_by_id(claim_id)
    if claim:
        session.delete(claim)
        session.commit()
        return True
    return False
