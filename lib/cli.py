import click
from lib.models import Policy, Policyholder, Claim
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

@cli.command()
def list_policies():
    policies = []  # Retrieve policies from the database using appropriate function
    click.echo('All policies:')
    for policy in policies:
        click.echo(f'- Policy ID: {policy.id}, Type: {policy.policy_type}, Start Date: {policy.start}, End Date: {policy.end}')

@cli.command()
@click.argument('policy_id')
def view_policy(policy_id):
    policy = get_policy_by_id(policy_id)
    if policy:
        click.echo(f'Policy Details for ID {policy_id}:')
        click.echo(f'- Type: {policy.policy_type}')
        click.echo(f'- Start Date: {policy.start}')
        click.echo(f'- End Date: {policy.end}')
        # Add other attributes as needed
    else:
        click.echo(f'Policy with ID {policy_id} not found.')

@cli.command()
@click.argument('policy_type')
@click.argument('start')
@click.argument('end')
@click.argument('policyholder_age', type=int)  # Assuming age is provided as an argument
@click.argument('coverage')
def create_policy(policy_type, start, end, policyholder_age, coverage):
    premium = calculate_premium(policy_type, coverage, policyholder_age)
    new_policy = create_policy(policy_type, start, end, premium, coverage)
    click.echo(f'Created new policy - Type: {policy_type}, Start Date: {start}, End Date: {end}, Premium: {premium}')

if __name__ == '__main__':
    cli()
