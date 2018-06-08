class Context:
  def current(self):
    pass
  def change(self, to):
    pass

class ContextGroup():
  def __init__(self, contexts=None):
    self.contexts = contexts | {}
