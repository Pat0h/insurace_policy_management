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


@cli.command()
def list_policies():
    click.echo('All policies')


@cli.command()
def view_policy(policy_id):
    click.echo(f'Viewing policy with Id: {policy_id}')


@cli.command()
@click.argument('policy_type')
@click.argument('start')
@click.argument('end')
def create_policy(policy_type, start, end):
    click.echo(f'Creating new policy- Type: {policy_type}, Start Date: {start}, End Date: {end}')


@cli.command()
@click.argument('policy_id')
def delete_policy(policy_id):
    click.echo(f'Deleting policy with Id: {policy_id}')


if __name__ == '__main__':
    cli()

@cli.command()
@click.argument('policy_type')
@click.argument('start')
@click.argument('end')
@click.argument('policyholder_age', type=int)  # Assuming age is provided as an argument
@click.argument('coverage')
def create_policy(policy_type, start, end, policyholder_age, coverage):
    premium = calculate_premium(policy_type, coverage, policyholder_age)
    new_policy = create_policy(policy_type, start, end, premium, coverage)
    click.echo(f'Creating new policy- Type: {policy_type}, Start Date: {start}, End Date: {end}, Premium: {premium}')
