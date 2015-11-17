import os, signal
from dogtail.procedural import *
from psutil import process_iter

def before_scenario(context, scenario):
  context.coy_pid = None
  context.coyim_app = None

def after_scenario(context, scenario):
  if context.coy_pid != None:
    os.kill(context.coy_pid, signal.SIGTERM)
  #context.coy_pid is shared fine between the steps but here is None
#  for process in process_iter():
#    if process.pid != os.getpid():
#      for path in process.cmdline():
#        if "coyim" in path:
#          process.terminate()
#          exit()
#
