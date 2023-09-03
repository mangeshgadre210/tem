import getpass
from fabric import Connection, Config
import fabric.config
import paramiko
import getpass

#import logging
#logging.basicConfig(level=logging.DEBUG)

sudo_pass = "mg"

config = Config(overrides={'sudo': {'password': sudo_pass}})

c = Connection(host = '192.168.29.205', user = 'mg'
    , connect_kwargs={ "password": "mg"} 
    , config=config
    )

c.run("ls -a")

c.sudo("df -H")