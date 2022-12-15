import paramiko

ssh_client = paramiko.SSHClient()
host = '172.22.3.74'
user = 'root'
key = 'DVC_key'
port = 7010

ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname = host, username = user, key_filename = key, port=port)

stdin,stdout,stderr=ssh_client.exec_command('bash ramtest.sh')

output = stdout.readlines()
for items in output:
    print(items)