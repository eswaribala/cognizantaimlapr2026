#create click cli automation
import click

@click.group()
def cli():
    pass

@click.command()
@click.option('--ipaddress', prompt='Network IP Address', help='The IP address of the network.')
@click.option('--port', prompt='Port', help='The port of the network.')
@click.option('--username', prompt='Username', help='The username for the network.')
@click.option('--password', prompt='Password', help='The password for the network.')
def mysqlconfig(ipaddress, port, username, password):
    click.echo(f'Configuring MySQL with the following settings:')
    click.echo(f'IP Address: {ipaddress}')
    click.echo(f'Port: {port}')
    click.echo(f'Username: {username}')
    click.echo(f'Password: {password}')

@click.command()
@click.option('--endpoint', prompt='API Endpoint', help='The endpoint of the API.')
@click.option('--method', prompt='HTTP Method', help='The HTTP method to use (e.g., GET, POST).')
def accessapi(endpoint, method):
    click.echo(f'Accessing API with the following settings:')
    click.echo(f'Endpoint: {endpoint}')
    click.echo(f'Method: {method}')

cli.add_command(mysqlconfig)
cli.add_command(accessapi)

if __name__ == '__main__':
    cli()
