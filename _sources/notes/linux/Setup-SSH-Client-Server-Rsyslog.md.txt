# Setup centralized SSH logging with RSyslog

## Install RSyslog
```bash
dev@dev:~$ sudo apt update
dev@dev:~$ sudo apt install rsyslog
```

Once the **rsyslog** is installed, you need to start the service, enable it to auto-start at boot and check its status.
```bash
dev@dev:~$ sudo systemctl start rsyslog
dev@dev:~$ sudo systemctl enable rsyslog
dev@dev:~$ sudo systemctl status rsyslog
```

## SSH Logs

### Remote Server Client RSyslog configuration
Open the main configuration file:
```bash
dev@dev:~$ sudo vim /etc/rsyslog.conf
```

Add it at the end of the file:
```bash
##### SERVER CLIENT CONFIG #####
# remote host is: name/ip:port, e.g. xxx.xxx.xxx.xxx:514, port optional.
# *.* @@remote-host:514                 all messages sent to remote-host via TCP
# *.priority @remote-host               with low prirotiy or higher priority will be sent via UDP
# Logs all the auth forwarding rule
auth,auth.*     @@xxx.xxx.xxx.xxx:514
### END OF FORWARDING RULE ####

# Define Disk Queue Buffer in case the server goes down
$ActionQueueFileName queue      # define a file name for disk assistance.
$ActionQueueMaxDiskSpace 1g     # The maximum size that all queue files together will use on disk.
$ActionQueueSaveOnShutdown on   # specifies that data should be saved at shutdown
$ActionQueueType LinkedList     # holds enqueued messages in memory which makes the process very fast. 
$ActionResumeRetryCount -1      # prevents rsyslog from dropping messages when retrying to connect if server is not responding
```

Save the configuration, check the rsyslog configuration for any syntax error and restart the rsyslog service:
```bash
dev@dev:~$ rsyslogd -f /etc/rsyslog.d/remotehost.conf -N1
rsyslogd: version 8.32.0, config validation run (level 1), master config /etc/rsyslog.conf
rsyslogd: End of config validation run. Bye.
dev@dev:~$ sudo systemctl restart syslog.socket rsyslog.service
```

### Remote logging Server RSyslog configuration
Create a new file named, **`remote_host.conf`**:
```bash
dev@dev:~$ sudo vim /etc/rsyslog.d/remote_host.conf
```

Add it to the said file:
```bash
#### REMOTE LOGGING SERVER RSYSLOG CONFIG ####
#################
#### MODULES ####
#################

# Provides UDP syslog reception
module(load="imudp")
input(type="imudp" port="514")

# Provides TCP syslog reception
module(load="imtcp")
input(type="imtcp" port="514")

###########################
#### GLOBAL DIRECTIVES ####
###########################
# Allowed sender lists can be defined for UDP and TCP senders separately. The syntax to specify them is:
# $AllowedSender [UDP/TCP], ip[/bits], ip[/bits]
# $AllowedSender TCP, xxx.xxx.xxx.xxx/22, 10.0.0.0/8
# $AllowedSender UDP, xxx.xxx.xxx.xxx/22, 10.0.0.0/8
$AllowedSender TCP, xxx.xxx.xxx.xxx


######################################################
#### Custom Template based on Client's IP Address ####
######################################################

# template (name="" type="{list | subtree | string | plugin}") { list-description }
# name: the name of the property to access
# outname: the output field name (for structured outputs)
# dateformat: date format to use
# securepath: used for creating pathnames suitable for use in dynafile templates
# format: specify format on a field basis (csv | json | jsonf | jsonr | jsonfr)
# droplastlf: drop a trailing LF, if it is present
# spifno1stsp:  expert options for RFC3164 template processing
# STANDARD TEMPLATE FOR WRITING TO FILES
template(name="log_path" type="list") {
        constant(value="/var/log/ssh_log/")
        property(name="fromhost-ip")
        constant(value="_")
        property(name="timereported")
        constant(value=".log")

}

template(name="server_client" type="list") {
        property(name="timestamp" dateformat="rfc3339")
        constant(value=" ")
        property(name="hostname")
        constant(value=" ")
        property(name="syslogtag")
        constant(value=" ")
        property(name="msg" spifno1stsp="on")
        property(name="msg" droplastlf="on")
        constant(value="\n")

}

# Make sure nothing interferes with the following definitions
$umask 0000

if $programname contains "sshd" then {
	if prifilt("auth,authpriv.*") then {
                # Write to file
                action(type="omfile" dynaFile="logPath" template="serverClient" FileCreateMode="0666" DirCreateMode="0777")

                # Stop directive is required to stop processing this messages, otherwise they will get to common system syslog
                stop
        }
}
```

`$umask` parameter allows to specify the rsyslogd processes' umask. If not specified, the system-provided default is used. The value given must always be a 4-digit octal number, with the initial digit being zero. If `$umask` is specified multiple times in the configuraiton file, results may be somewhat unpredicted. It is recommended to specify it only once.

**Sample:**
```
$umask 0000
```
This sample removes all restrictions.


Save the configuration, check the rsyslog configuration for any syntax error and restart the rsyslog service:
```bash
dev@dev:~$ rsyslogd -f /etc/rsyslog.d/remotehost.conf -N1
rsyslogd: version 8.32.0, config validation run (level 1), master config /etc/rsyslog.conf
rsyslogd: End of config validation run. Bye.
dev@dev:~$ sudo systemctl restart syslog.socket rsyslog.service
```

## Reference
* [RSyslog Configuration Documentation](https://www.rsyslog.com/doc/master/configuration/index.html)