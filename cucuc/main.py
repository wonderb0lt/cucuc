#/usr/bin/env python3
import click
import delegator

from .io import load_contexts
from .format import format_output

@click.command()
def main():
  contexts = load_contexts('./confs/groups/aks.yaml', './confs/contexts')
  for ctx in contexts:
    name = ctx['name']
    current = delegator.run(ctx['get']).out
    formatted = format_output(current, ctx.get('format', ''))
    click.echo('{}: {}'.format(name, formatted))

if __name__ == '__main__':
  main()
