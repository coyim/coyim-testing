from dogtail.procedural import *
from psutil import process_iter

def before_all(context):
  context.coy_pid = None
  context.coyim_app = None

def after_all(context):
  #context.coy_pid is shared fine between the steps but here is None
  for process in process_iter():
    for path in process.cmdline():
      if "coyim" in path:
        process.terminate()
        exit()

