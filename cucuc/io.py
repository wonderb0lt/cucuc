import os.path as path

import yaml

def load_context(ctx_file):
  with open(ctx_file, 'r') as fd:
    return yaml.load(fd)

def load_contexts(group_file, ctx_dir):
  with open(group_file) as fd:
    for ctx in yaml.load(fd):
      yield load_context(path.join(ctx_dir, ctx + '.yaml'))
