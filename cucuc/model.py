from collections import namedtuple

Context = namedtuple('Context', [
  'name', # A readable name for the context (not used as an identifier, so go nuts)
  'get', # Command to execute to find the current value
  'set', # Command to execute to set a new value
  'parser', # With what to parse the result. Can be either null or "json"
])

Group = namedtuple('Group', [
  'name',
  'contexts'
])

ValueGroup = namedtuple('ValueGroup', [
  'name',
  'group',
  'values'
])
