from fabric.api import env

def set_host_rpi():
    env.host ="192.168.29.205"
    env.user ="mg"
    env.password ="mg"
    print("logging to %s as user %s with password %s " % (env.host,env.user,env.password))


set_host_rpi()