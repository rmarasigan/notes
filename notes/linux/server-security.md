# Basic Server Security Checking

If something is wrong with your Server:

1. If there is someone downloading, uploading, putting some scripts or installing Trojan horse, disconnect it from the network.

   ✓ Restart your system.

   ✓ Keep pressing SHIFT after the reboot to go to the GRUB menu.

   ✓ If it takes longer on hopping (booting):
      * Change the Quick Boot (Boot Tab in BIOS) to **Enabled** to not let it do the slow hopping.

   ✓ Go to the **Advanced** option, **Recovery Mode**

   ✓ After going to the **Recovery Mode** of your current Kernel, you'll get the screen root. Now you have root access to the computer.

   ✓ Remount your hard drive with appropriate permission.
   ```bash
   rw -o remount /
   ```
   This should allow you to make changes to the data on the hard drive.

2. Check the `/etc/shadow` file. If there's an anonymous account, **delete that user**.
   ```bash
   dev@dev:~$ sudo vim /etc/shadow
   dev@dev:~$ sudo userdel username
   ```
   `userdel` is used to delete a user account and related files.

3. Check for the `/etc/passwd`, if there is another existing account that you are not sure of, remove it. Make sure in `/etc/passwd` there is only one accessible. The rest is `nologin` or `false`.
   ```bash
   dev@dev:~$ sudo vim /etc/passwd
   ```
   `/etc/passwd` contains a list of system's account, giving for each account some useful information like user ID, group ID, home directory, shell, etc.

4. Change the password
   ```bash
   dev@dev:~$ passwd username
   ```
   The system will ask you to type a new UNIX password and then retype it.

5. Once you've entered and confirmed the new password, reboot the system.
   ```bash
   dev@dev:~$ shutdown -r
   ```
   Your system should restart. Don't press any keys, let the system boot up to the login screen and test to make sure the new password works.

6. Remove every tor or debian-tor package in the server.

7. Block the IP from the network, firewall on the one-side of the core and add it to the incoming.

8. Check SSH logs.
   ```bash
   dev@dev:~$ cat ssh /var/log/auth.log
   ```

9. Check who is logged in to your server.
   * `who`: show who is logged on
   * `w`: show who is logged on and what they are doing

   ```bash
   dev@dev:~$ who
   root pts/4 2022-06-18 01:00 (xxx.xxx.xxx.xxx)

   ## Or you can use this:
   dev@dev:~$ w
   01:00:00 up 6 days, 24:30,       2 users,    load average: 3.62, 3.89, 5.09
   USER     TTY      FROM              LOGIN@   IDLE     JCPU  PCPU     WHAT
   root     pts/4    xxx.xxx.xxx.xxx   12:06    1.00s    0.05s 0.00s    w
   root     pts/5    xxx.xxx.xxx.xxx   08:30    6:23     0.08s 0.08s    -bash
   ```
