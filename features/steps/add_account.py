import os

from dogtail.procedural import *
from dogtail.tc import TCNode, TCBool
from dogtail.tree import *
from dogtail.utils import screenshot

coy_config_file = "/tmp/coy-config.json"

@given(u'the user has no account configured')
def step_impl(context):
  if os.path.isfile(coy_config_file):
    os.remove(coy_config_file)

@when(u'the user opens the application')
def step_impl(context):
  coyimPath = os.environ.get('COYIM_PATH')
  if coyimPath != None:
    executable = "%s -debug -config-file %s" % (coyimPath, coy_config_file)

  context.coy_pid = run(executable)
  context.coyim_app = root.application("CoyIM")

@when(u'choses to not encrypt the configuration file')
def step_impl(context):
  encryptAlert = context.coyim_app.child(name = "Question", roleName = "alert")
  encryptAlert.button("No").doActionNamed("click")

@then(u'add account dialog is displayed')
def step_impl(context):
  addAccount = context.coyim_app.child(name="Account Details", roleName = "dialog")
  TCNode().compare("Found add account dialog", None, addAccount)
