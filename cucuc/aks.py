from .model import ContextGroup
from .contexts import KubernetesContext

class AksContext(ContextGroup):
  def __init__(self):
    super()
    self.contexts = {'k8s': KubernetesContext()}
