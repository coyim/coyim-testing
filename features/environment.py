import os, signal
from dogtail.procedural import *

def before_scenario(context, scenario):
  context.coy_pid = None
  context.coyim_app = None

def after_scenario(context, scenario):
  if context.coy_pid != None:
    os.kill(context.coy_pid, signal.SIGTERM)
