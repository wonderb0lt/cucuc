#/usr/bin/env python3
import click

from .aks import AksContext

@click.command()
def main():
  for name, ctx in AksContext().contexts.items():
    click.echo('{}: {}'.format(name, ctx.current()))

if __name__ == '__main__':
  main()
