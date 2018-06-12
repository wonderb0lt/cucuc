from pathlib import Path

import yaml

from .model import Context, Group, ValueSet

def load_context(context_path):
  with context_path.open() as fd:
    return Context(**yaml.load(fd))

def load_contexts(contexts_paths):
  return {ctx.stem: load_context(ctx) for ctx in contexts_paths.glob('*.yaml')}

def load_group(group_path, defined_contexts):
  with group_path.open() as fd:
    contexts = {}
    for context in yaml.load(fd):
      if context not in defined_contexts.keys():
        raise Exception('Group at {} references unknown context "{}". Available contexts: {}'.format(
          group_path, 
          context,
          defined_contexts.keys()))
      else:
        contexts.update({context: defined_contexts[context]})
    
    return Group(group_path.stem, contexts)

def load_groups(groups_path, defined_contexts):
  return {group.stem: load_group(group, defined_contexts) for group in groups_path.glob('*.yaml')}

def load_valueset(vs_path, defined_groups):
  with vs_path.open() as fd:
    vs = yaml.load(fd)

    if vs['group'] not in defined_groups.keys():
      raise Exception('ValueSet at {} refers to unknown group "{}". Available groups are: {}'.format(
        vs_path,
        vs['group'],
        defined_groups.keys()
      ))
    else:
      vs['group'] = defined_groups[vs['group']]
      return ValueSet(**vs)

def load_valuesets(vss_path, defined_groups):
  return {vs.stem: load_valueset(vs, defined_groups) for vs in vss_path.glob('*.yaml')}

def load_all(cucucdir):
  contexts = load_contexts(Path(cucucdir, 'contexts'))
  groups = load_groups(Path(cucucdir, 'groups'), contexts)
  valuesets = load_valuesets(Path(cucucdir, 'valuesets'), groups)

  return (contexts, groups, valuesets)
