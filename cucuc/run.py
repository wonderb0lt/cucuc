import delegator
import json

def run_context(context, method, *args):
  r = delegator.run(getattr(context, method).format(*args))
  if context.parser is None:
    return r.out
  else:
    return json.loads(r.out)
