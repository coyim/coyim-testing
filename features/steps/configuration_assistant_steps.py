import os
import signal
import sys
import socket
import threading
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

@then(u'the configuration assistant is displayed')
def step_impl(context):
    global coyim_app
    configAssistant = coyim_app.child(name="Configuration Assistant", roleName = "frame")
    TCNode().compare("Found assistant", None, configAssistant)

@given(u'Tor is listening on port 9050')
def step_impl(context):
    global tor_server
    if tor_server != None:
        tor_server.shutdown()

    tor_server = ThreadedTCPServer(("127.0.0.1", 9050), ThreadedTCPRequestHandler)
    server_thread = threading.Thread(target=tor_server.serve_forever)
    server_thread.daemon = True
    server_thread.start()

@then(u'the "Welcome" page is displayed')
def step_impl(context):
    global coyim_app
    configAssistant = coyim_app.child(name="Configuration Assistant", roleName = "frame")
    welcomeMsg = configAssistant.child(name = "Welcome to CoyIM, the safe and secure xmpp client.", roleName = "label")
    TCNode().compare("Found welcome message", None, welcomeMsg)

@then(u'the user goes to the next page')
def step_impl(context):
    global coyim_app
    configAssistant = coyim_app.child(name="Configuration Assistant", roleName = "frame")
    configAssistant.button("Next").doActionNamed("click")

@then(u'Tor is detected to be running on port 9050')
def step_impl(context):
    global coyim_app
    configAssistant = coyim_app.child(name="Configuration Assistant", roleName = "frame")
    torMsg = configAssistant.child(name = "Tor detected successfully. Continue.", roleName = "label")
    TCNode().compare("Tor is running", None, torMsg)

@then(u'the user provides the following account information')
def step_impl(context):
    global coyim_app
    configAssistant = coyim_app.child(name="Configuration Assistant", roleName = "frame")
    configAssistant.child(roleName = "text").typeText(context.table[0]["XMPP ID"])
    configAssistant.child(roleName = "password text").typeText(context.table[0]["Password"])

@then(u'SRV consult will returns the server info')
def step_impl(context):
    global coyim_app
    configAssistant = coyim_app.child(name="Configuration Assistant", roleName = "frame")
    SRVMsg = configAssistant.child(name = "All right with SRV", roleName = "label")
    TCNode().compare("SRV consult ok", None, SRVMsg)

@then(u'the configuration step will be finished')
def step_impl(context):
    global coyim_app
    configAssistant = coyim_app.child(name="Configuration Assistant", roleName = "frame")
    enjoyMsg = configAssistant.child(name = "You are all set. Enjoy.", roleName = "label")
    TCNode().compare("Configuration was finished", None, enjoyMsg)

@then(u'the user applies the configuration')
def step_impl(context):
    global coyim_app
    configAssistant = coyim_app.child(name="Configuration Assistant", roleName = "frame")
    configAssistant.button("Apply").doActionNamed("click")

@then(u'the assistent will be closed')
def step_impl(context):
    global coyim_app
    configAssistant = coyim_app.child(name="Configuration Assistant", roleName = "frame")
    TCBool().compare("Assitent window is closed", not configAssistant.showing())

@then(u'the account "user@riseup.net" will be configured')
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
