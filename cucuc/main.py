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
@click.argument('group', default=None, required=False)
@click.pass_obj
def show(cucucdir, group):
  _, groups, _ = load_all(cucucdir)

  if group:
    groups = {k: v for k, v in groups.items() if k == group}
    if not groups:
      raise click.BadParameter('A group with the name "{}" does not exist'.format(group))

  for group in groups.values():
    click.secho('Group ', nl=False)
    click.secho(group.name, nl=False, bold=True)
    click.secho(':')
    
    for context in group.contexts.values():
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
    vs = vss[vs_name]
    group = vs.group
    for ctx_name, value in vs.values.items():
      click.secho('Setting context {} to "{}"'.format(ctx_name, value))
      ctx = group.contexts[ctx_name]
      run_context(ctx, 'set', value)
  else:
    valuesets = ', '.join(['"{}"'.format(vs) for vs in vss.keys()])
    raise click.BadParameter('Unknown Valueset "{}", the following are available: {}'.format(vs_name, valuesets))

@cli.command()
@click.pass_obj
@click.argument('what', required=False, default=None)
def list(cucucdir, what):
  contexts, groups, valuesets = load_all(cucucdir)
  
  if what == 'contexts' or what is None:
    for context in contexts.values():
      click.secho('Context ', nl=False)
      click.secho(context.name, bold=True, nl=False)
      click.secho(' getting with ', nl=False)
      click.secho(context.get, fg='yellow', nl=False)
      click.secho(' and setting with ', nl=False),
      click.secho(context.set, fg='yellow')
      if context.parser:
        click.secho(' (parsing results with "{}")'.format(context.parser))
  if what == 'groups' or what is None:
    for group in groups.values():
      click.secho('Group ', nl=False)
      click.secho(group.name, bold=True, nl=False)
      click.secho(' consisting of contexts ', nl=False)
      click.secho(', '.join(group.contexts), bold=True)
  if what == 'valuesets' or what is None:
    for valueset in valuesets.values():
      click.secho('Valueset ', nl=False)
      click.secho(valueset.name, bold=True, nl=False)
      click.secho(' for group ', nl=False)
      click.secho(valueset.group.name, bold=True, nl=False)
      click.secho(' with values ')
      for ctx, val in valueset.values.items():
        click.secho('\t', nl=False)
        click.secho('{} = {}'.format(ctx, val))
