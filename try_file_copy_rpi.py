from fabric import Connection
c = Connection("192.168.29.205",user="mg",connect_kwargs={'password':'mg'})

c.run("sudo dmesg")
c.run("dmesg > dmesg.txt")
c.run("tar -cvzf dmesg.tar.gz dmesg.txt")
c.get("dmesg.tar.gz")
#c.run("sudo systemctl reboot")




#result = Connection("192.168.29.113",user="mg",connect_kwargs={'password':'mg'}).run('dmesg', hide=True)
#msg = "Ran {0.command!r} on {0.connection.host}, got stdout:\n{0.stdout}"
#print(msg.format(result))
#result = Connection("192.168.29.113",user="mg",connect_kwargs={'password':'mg'}).put('./test_01.txt',remote='/home/mg/')
#print("Uploaded {0.local} to {0.remote}".format(result))
#result = Connection("192.168.29.113",user="mg",connect_kwargs={'password':'mg'}).run('cat /home/mg/test_01.txt')
#print(msg.format(result))
