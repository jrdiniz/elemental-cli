import click

@click.group()
def cli():
    pass

@click.command('configure')
@click.option('--all', help="List all configured elementals", required=False, is_flag=True)
@click.option('--add', help="Add Elemental credential", required=False, is_flag=True)
def configure(all, add):
    if add:
        elemental_name = click.prompt('Enter the Elemental Hostname')
        elemental_ip = click.prompt('Enter the Elemental IP')
        elemental_username = click.prompt('Enter the Elemental API Username')
        elemental_key = click.prompt("Enter the Elemental API Key")
    click.echo('Configure Module')

@click.command('server')
@click.argument('elemental')
@click.option('--all', help="List last 100 jobs", required=False, is_flag=True)
@click.option('--id', help="Get job information.", required=False, type=(int))
@click.option('--delete', help="Delete job.", required=False, type=(int))
@click.option('--status', help="Get job status", required=False, type=(int))
def server(elemental, all, id, delete,status):
    if all:
        print("# List of last 100 jobs")
    click.echo(f'Elemental Server Jobs: {elemental}, {all}, {id}')

@click.command('live')
def live():
    click.echo('Elemental Live Jobs')

cli.add_command(configure)
cli.add_command(server)
cli.add_command(live)

if __name__ == '__main__':
    cli()