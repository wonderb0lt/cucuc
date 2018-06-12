import json

def parse_output(output, parse):
  if parse == 'json':
    return json.loads(output)
  
  return output
