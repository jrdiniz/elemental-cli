import click

@click.group()
def server():
    pass

@server.command('server')
def job_list():
    print('Elemental Server Jobs')

@click.group()
def live():
    pass

@live.command('live')
def jobs():
    print('Elemental Live Jobs')

cli = click.CommandCollection(sources=[server,live])

if __name__ == '__main__':
    cli()