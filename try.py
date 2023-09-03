from fabric import Connection
result = Connection("192.168.29.113",user="mg",connect_kwargs={'password':'mg'}).run('dmesg', hide=True)
msg = "Ran {0.command!r} on {0.connection.host}, got stdout:\n{0.stdout}"
print(msg.format(result))


