import delegator

from .model import Context

class KubernetesContext(Context):
  def current(self):
    return delegator.run('kubectl config current-context').out.strip()
    
  def change(self, to):
    return delegaotr.run('kubectl config set-context {}'.format(to)).out.strip()
