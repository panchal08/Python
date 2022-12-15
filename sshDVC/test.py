import paramiko
ssh_client = paramiko.SSHClient()
script = """
            #!/bin/bash
            stress-ng --cpu 4 --timeout 86400s;
        """
for i in range(1,30):
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname = '172.22.3.74', username = 'root', key_filename = 'DVC_key', port=7010)
    ssh_client.exec_command(f"bash -c {script}")
