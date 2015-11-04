import os
import signal
import sys

from dogtail.procedural import *
from dogtail.tree import *

coyim_app = None

@given(u'the user has no account configured')
def step_impl(context):
    # Remove the test configuration file
    # coy_config_file = "/tmp/coy-config.json"
    raise NotImplementedError(u'STEP: Given the user has no account configured')

@when(u'the user opens the application')
def step_impl(context):
    coyim_app = root.application("CoyIM")

@then(u'the configuration assistant is displayed')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the configuration assistant is displayed')

@given(u'Tor is listening on port 9050')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given Tor is listening on port 9050')

@then(u'the "Welcome" page is displayed')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the "Welcome" page is displayed')

@then(u'the user goes to the next page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the user goes to the next page')

@then(u'the "Account details" page is displayed')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the "Account details" page is displayed')

@then(u'Tor is detected to be running on port 9050')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Tor is detected to be running on port 9050')

@then(u'the user provides the following account information')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the user provides the following account information')

@then(u'the account "coyim@riseup.net" will be configured')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the account "coyim@riseup.net" will be configured')

@then(u'it will have a safe default configuration')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then it will have a safe default configuration')

@then(u'the XMPP server can\'t be found')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the XMPP server can\'t be found')

@then(u'the "Server configuration" section is displayed with the following config')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the "Server configuration" section is displayed with the following config')

@then(u'the user accepts the configuration')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the user accepts the configuration')