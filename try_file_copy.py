from fabric import Connection
result = Connection("192.168.29.113",user="mg",connect_kwargs={'password':'mg'}).run('dmesg', hide=True)
msg = "Ran {0.command!r} on {0.connection.host}, got stdout:\n{0.stdout}"
print(msg.format(result))
result = Connection("192.168.29.113",user="mg",connect_kwargs={'password':'mg'}).put('./test_01.txt',remote='/home/mg/')
print("Uploaded {0.local} to {0.remote}".format(result))
result = Connection("192.168.29.113",user="mg",connect_kwargs={'password':'mg'}).run('cat /home/mg/test_01.txt')
print(msg.format(result))
