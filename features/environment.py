import os

coy_pid = None
coy_config_file = "/tmp/coy-config.json"

def before_all(context):
    print("BEFORE ALL")

    # could use config.userdata["COYIM_PATH"] but I dunno how
    coyimPath = os.environ.get('COYIM_PATH')
    if coyimPath != None:
        coy_pid = run("%s -debug -config-file %" % (coyimPath, coy_config_file))

def after_all(context):
    print("AFTER ALL")

    if coy_pid != None:
        os.kill(coy_pid, signal.SIGTERM)
