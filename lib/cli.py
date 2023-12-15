import click
from models import Policy, Policyholder, Claim
from premium import calculate_premium
from database import (
    create_policy,
    get_policy_by_id,
    delete_policy,
    create_policyholder,
    get_policyholder_by_id,
    delete_policyholder,
    create_claim,
    get_claim_by_id,
    delete_claim,
)

@click.group()
def cli():
    pass

# Policy-related commands
@cli.command()
@click.option('--policyholder-id', type=int, help='ID of the policyholder')
@click.option('--start', type=str, help='Start date of the policy')
@click.option('--end', type=str, help='End date of the policy')
@click.option('--coverage', type=str, help='Coverage type')
def create_policy(policyholder_id, start, end, coverage):
    policyholder = get_policyholder_by_id(policyholder_id)
    if policyholder:
        premium = calculate_premium('health', coverage, policyholder.age)
        new_policy = create_policy('health', start, end, premium, coverage, policyholder_id)
        click.echo(f"Policy created with ID: {new_policy.id}")
    else:
        click.echo("Policyholder not found.")

@cli.command()
@click.argument('policy_id', type=int)
def get_policy(policy_id):
    policy = get_policy_by_id(policy_id)
    if policy:
        click.echo(f"Policy ID: {policy.id}, Start Date: {policy.start}, End Date: {policy.end}, Premium: {policy.premium}, Coverage: {policy.coverage}")
    else:
        click.echo("Policy not found.")

@cli.command()
@click.argument('policy_id', type=int)
def remove_policy(policy_id):
    deleted = delete_policy(policy_id)
    if deleted:
        click.echo("Policy deleted successfully.")
    else:
        click.echo("Policy not found.")


@cli.command()
@click.option('--name', type=str, help='Name of the policyholder')
@click.option('--email', type=str, help='Email of the policyholder')
@click.option('--phone-number', type=str, help='Phone number of the policyholder')
@click.option('--address', type=str, help='Address of the policyholder')
def create_policyholder(name, email, phone_number, address):
    new_policyholder = create_policyholder(name, email, phone_number, address)
    click.echo(f"Policyholder created with ID: {new_policyholder.id}")

@cli.command()
@click.argument('policyholder_id', type=int)
def get_policyholder(policyholder_id):
    policyholder = get_policyholder_by_id(policyholder_id)
    if policyholder:
        click.echo(f"Policyholder ID: {policyholder.id}, Name: {policyholder.name}, Email: {policyholder.email}, Phone: {policyholder.phone_number}, Address: {policyholder.address}")
    else:
        click.echo("Policyholder not found.")

@cli.command()
@click.argument('policyholder_id', type=int)
def remove_policyholder(policyholder_id):
    deleted = delete_policyholder(policyholder_id)
    if deleted:
        click.echo("Policyholder deleted successfully.")
    else:
        click.echo("Policyholder not found.")


@cli.command()
@click.option('--policy-id', type=int, help='ID of the policy associated with the claim')
@click.option('--claim-date', type=str, help='Date of the claim')
@click.option('--claim-details', type=str, help='Details of the claim')
@click.option('--status', type=str, help='Status of the claim')
def create_claim(policy_id, claim_date, claim_details, status):
    policy = get_policy_by_id(policy_id)
    if policy:
        new_claim = create_claim(policy_id, policy.policyholder_id, claim_date, claim_details, status)
        click.echo(f"Claim created with ID: {new_claim.id}")
    else:
        click.echo("Policy not found.")

@cli.command()
@click.argument('claim_id', type=int)
def get_claim(claim_id):
    claim = get_claim_by_id(claim_id)
    if claim:
        click.echo(f"Claim ID: {claim.id}, Policy ID: {claim.policy_id}, Policyholder ID: {claim.policyholder_id}, Date: {claim.claim_date}, Details: {claim.claim_details}, Status: {claim.status}")
    else:
        click.echo("Claim not found.")

@cli.command()
@click.argument('claim_id', type=int)
def remove_claim(claim_id):
    deleted = delete_claim(claim_id)
    if deleted:
        click.echo("Claim deleted successfully.")
    else:
        click.echo("Claim not found.")

if __name__ == '__main__':
    cli()
