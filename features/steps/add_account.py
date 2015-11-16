import os
import signal
import SocketServer

from dogtail.procedural import *
from dogtail.tc import TCNode, TCBool
from dogtail.tree import *
from dogtail.utils import screenshot

coy_pid = None
coy_config_file = "/tmp/coy-config.json"
coyim_app = None
tor_server = None

class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
  pass

class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):
  def handle(self):
    pass

@given(u'the user has no account configured')
def step_impl(context):
  if os.path.isfile(coy_config_file):
    os.remove(coy_config_file)

@when(u'the user opens the application')
def step_impl(context):
  global coyim_app
  global coy_pid

  if coy_pid != None:
    os.kill(coy_pid, signal.SIGTERM)

  coyimPath = os.environ.get('COYIM_PATH')
  if coyimPath != None:
    executable = "%s -debug -config-file %s" % (coyimPath, coy_config_file)
    coy_pid = run(executable)

  coyim_app = root.application("CoyIM")

@when(u'choses to not encrypt the configuration file')
def step_impl(context):
  global coyim_app
  encryptAlert = coyim_app.child(name = "Question", roleName = "alert")
  encryptAlert.button("No").doActionNamed("click")

@then(u'add account dialog is displayed')
def step_impl(context):
  global coyim_app
  addAccount = coyim_app.child(name="Account Details", roleName = "dialog")
  TCNode().compare("Found add account dialog", None, addAccount)
