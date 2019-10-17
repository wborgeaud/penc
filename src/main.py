import click
from . import b64
from . import hexx

@click.group()
def cli():
    pass

@cli.command()
@click.argument('s', required=False)
@click.option('-u', '--url-encode', 'url', is_flag=True)
def b(s, url):
    "Base64 encode"
    if s is None:
        s = click.prompt("Enter the string to encode:", prompt_suffix='\n')
    click.echo(b64.encode(s, url))

@cli.command()
@click.argument('s', required=False)
@click.option('-u', '--url-encode', 'url', is_flag=True)
def bd(s, url):
    "Base64 decode"
    if s is None:
        s = click.prompt("Enter the string to decode:", prompt_suffix='\n')
    try:
        click.echo(b64.decode(s, url))
    except:
        click.secho("Can not decode base64 string", bg='red', fg='white')



@cli.command()
@click.argument('s', required=False)
def x(s):
    "Hex encode"
    if s is None:
        s = click.prompt("Enter the string to encode:", prompt_suffix='\n')
    click.echo(hexx.encode(s))

@cli.command()
@click.argument('s', required=False)
def xd(s):
    "Hex decode"
    if s is None:
        s = click.prompt("Enter the string to decode:", prompt_suffix='\n')
    try:
        click.echo(hexx.decode(s))
    except hexx.NonHexCharacter:
        click.secho("Non-hex character found in string", bg='red', fg='white')
    except hexx.OddLengthString:
        click.secho("Odd-length string", bg='red', fg='white')

if __name__ == '__main__':
    cli()
