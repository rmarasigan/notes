# Installation

### What is Samba?


### Installing Samba
To install Samba:
```bash
dev@dev:~$ sudo apt update
dev@dev:~$ sudo apt install samba
```

Check if the installation was successful:
```bash
dev@dev:~$ whereis samba
samba: /usr/sbin/samba /usr/lib/x86_64-linux-gnu/samba /etc/samba /usr/share/samba /usr/share/man/man7/samba.7.gz /usr/share/man/man8/samba.8.gz
```

### Setting up Samba
Create a directory for it to share:
```bash
dev@dev:~$ mkdir /home/<username>/sambashare/
```

Add the new directory as a share on the configuration file for Samba
```bash
dev@dev:~$ sudo vim /etc/samba/smb.conf
```

At the bottom of the file, add the following:
```bash
[sambashare]
   comment = Samba on Ubuntu
   path = /home/username/sambahsare
   read only = no
   browsable = yes
```
**NOTE**: Remember to change the "username"

Save the new share configured and restart Samba for it to take effect. Also update the firewall rules to allow Samba traffic.
```bash
dev@dev:~$ sudo service smbd restart
dev@dev:~$ sudo ufw allow samba
Rules updated
Rules updated (v6)
```

Set the persmission to the directory. It means that the new files or directories created under it will inherit the group ownership of the parent directory.
```bash
dev@dev:~$ sudo chmod 2770 /home/username/sambashare/
```

### Setup a Samba password for the user account
```bash
dev@dev:~$ sudo smbpasswd -a username
New SMB password:
Retype new SMB password:
Added user username
```

### Connecting to a Samba Share from Linux

Install `smbclient` on Ubuntu:
```bash
dev@dev:~$ sudo apt install smbclient
```

Syntax to access a Samba share:
```bash
dev@dev:~$ smbclient //xxx.xxx.xxx.xxx/sambashare -U username
Enter WORKGROUP\username's password:
```

## Reference
* [Install and Configure Samba](https://ubuntu.com/tutorials/install-and-configure-samba#1-overview)