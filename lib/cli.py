import click
from models import Policy, Policyholder, Claim


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
