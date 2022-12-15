import paramiko
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname='172.22.99.99', username='guest',password='1', port=7010)
ssh_client.exec_command('sudo pkill -9 stress-ng')
