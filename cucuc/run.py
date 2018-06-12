import delegator
import json

def run_context(context, method):
  r = delegator.run(getattr(context, method))
  if context.parser is None:
    return r.out
  else:
    return json.loads(r.out)
