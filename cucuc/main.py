#/usr/bin/env python3
from pathlib import Path

import click

from .io import load_all
from .run import run_context

INDENT = '  '
@click.group(invoke_without_command=True)
@click.option('--cucucdir', default='./confs/')
@click.pass_context
def cli(ctx, cucucdir):
  ctx.obj = cucucdir

  if ctx.invoked_subcommand is None:
    ctx.invoke(show)

@cli.command()
@click.pass_obj
def show(cucucdir):
  _, groups, valuesets = load_all(cucucdir)
  for group in groups.values():
    click.secho('Group ', nl=False)
    click.secho(group.name, nl=False, bold=True)
    click.secho(':')
    
    for context in group.contexts:
      click.secho(INDENT, nl=False)
      click.secho('Context ', nl=False)
      click.secho(context.name, nl=False, bold=True)
      click.secho(': ', nl=False)
      click.secho(run_context(context, 'get'))
