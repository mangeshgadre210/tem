from fabric.api import env
from fabric import Connection

def set_host_rpi():
    env.host ="192.168.29.205"
    env.user ="mg"
    env.password ="mg"
    print("logging to %s as user %s with password %s " % (env.host,env.user,env.password))

def show_rpi_dmesg()
    c = Connection(env.host,user=env.usr,connect_kwargs={'password':env.password})
    c.run("sudo dmesg")
    

set_host_rpi()
show_rpi_dmesg()
