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
  _, groups, _ = load_all(cucucdir)
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

@cli.command()
@click.pass_obj
@click.argument('vs_name')
def set(cucucdir, vs_name):
  vs_dir = Path(cucucdir, 'valuesets')
  _, groups, vss = load_all(cucucdir)
  click.secho('Switching to ', nl=False)
  click.secho(vs_name, bold=True)

  if vs_name in vss:
    print(vss)
    vs = vss[vs_name]
    group = vs.group
    for ctx_name, value in vs.values.items():
      click.secho('Setting context {} to "{}"'.format(ctx_name, value))
      ctx = group.contexts[ctx_name]
      run_context(ctx, 'set', value)
  else:
    # TODO: There should be a list command for all the different types that this error refers to
    raise click.UsageError('"{}" is not known as a value set, does it exist in {}?'.format(vs_name, vs_dir))
