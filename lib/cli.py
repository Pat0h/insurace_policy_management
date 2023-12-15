import click
from models import Policy, Policyholder, Claim

@click.group()
def cli():
    pass

@cli.command()
def list_policies():
    click.echo('All policies')

@cli.command()
def view_policy(policy_id)
    click.echo(f'Viewing policy with Id: {policy_id}')

@cli.command()
@click.argument('')