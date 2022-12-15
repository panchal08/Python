import paramiko
ssh_client = paramiko.SSHClient()
host = '172.22.99.99'
user = 'root'
key = 'DVC_key'
port = 7010

script = """
            #!/bin/bash
            apt install stress-ng -y; sleep 2s;
            uptime;
            screen -S cputest -d -m stress-ng --cpu 4 --timeout 86400s;
        """

ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname = host, username = user, key_filename = key, port=port)

stdin,stdout,stderr=ssh_client.exec_command(f"bash -c {script}")

output = stdout.readlines()

for items in output:
    print(items)