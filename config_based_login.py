import getpass
from fabric import Connection, Config
import fabric.config
import paramiko
import getpass
import yaml

with open("my_config.yml", "r") as ymlfile:
    cfg = yaml.safe_load(ymlfile)
for section in cfg:
    print(section)
    
print(cfg["setup"])
print(cfg["setup"]["host"])
print(cfg["setup"]["user"])
print(cfg["setup"]["passwd"])
print(cfg["setup"]["sudo_user"])
print(cfg["setup"]["sudo_pwd"])

#import logging
#logging.basicConfig(level=logging.DEBUG)

sudo_pass = cfg["setup"]["sudo_pwd"]

config = Config(overrides={'sudo': {'password': sudo_pass}})

c = Connection(host = cfg["setup"]["host"], user = cfg["setup"]["user"]
    , connect_kwargs={ "password": cfg["setup"]["passwd"]} 
    , config=config
    )

c.run("ls -a")

c.sudo("df -H")