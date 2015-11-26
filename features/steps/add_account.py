import os, sys

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
  coyimPath = os.getenv('COYIM_PATH')
  sys.stdout.write(coyimPath)
  executable = "%s -debug -config-file %s" % (coyimPath, coy_config_file)

  try:
    context.coy_pid = run(executable)
    context.coyim_app = root.application("CoyIM")
  except OSError:
    sys.stdout.write("\nBad configuration")

@when(u'choses to not encrypt the configuration file')
def step_impl(context):
  encryptAlert = context.coyim_app.child(name = "Information", roleName = "alert")
  encryptAlert.button("No").doActionNamed("click")

@then(u'should display add account dialog')
def step_impl(context):
  addAccount = context.coyim_app.child(name = "Account Details", roleName = "dialog")
  TCNode().compare("Found add account dialog", None, addAccount)

@when(u'user provides the account details')
def step_impl(context):
  addAccount = context.coyim_app.child(name = "Account Details", roleName = "dialog")
  addAccount.child(roleName = "text").typeText(context.table[0]["XMPP ID"])
  addAccount.child(roleName = "password text").typeText(context.table[0]["Password"])

@when(u'saves the account')
def step_impl(context):
  addAccount = context.coyim_app.child(name = "Account Details", roleName = "dialog")
  addAccount.button("Save").doActionNamed("click")

@then(u'account should be added to account list')
def step_impl(context):
  accountMenu = context.coyim_app.menu("Accounts")
  menuItem = accountMenu.child(context.text)
  TCNode().compare("Account was added to menu", None, menuItem)
