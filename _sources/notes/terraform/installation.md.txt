# Installation

### Linux
Ensure that your system is up to date, and you have the `gnupg`, `software-properties-common`, and `curl` packages installed.
```bash
dev@dev:~$ sudo apt-get update && sudo apt-get install -y gnupg software-properties-common
Reading package lists... Done
Reading package lists... Done
Building dependency tree       
Reading state information... Done
gnupg is already the newest version (2.2.19-3ubuntu2.2).
gnupg set to manually installed.
software-properties-common is already the newest version (0.99.9.8).
0 upgraded, 0 newly installed, 0 to remove and 104 not upgraded.
```

#### Install the HashiCorp [GPG key](https://apt.releases.hashicorp.com/gpg)
```bash
dev@dev:~$ wget -O- https://apt.releases.hashicorp.com/gpg | \
>     gpg --dearmor | \
>     sudo tee /usr/share/keyrings/hashicorp-archive-keyring.gpg
--2022-08-03 16:20:31--  https://apt.releases.hashicorp.com/gpg
Resolving apt.releases.hashicorp.com (apt.releases.hashicorp.com)... 13.226.58.122, 13.226.58.55, 13.226.58.96, ...
Connecting to apt.releases.hashicorp.com (apt.releases.hashicorp.com)|13.226.58.122|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 3195 (3.1K) [binary/octet-stream]
Saving to: ‘STDOUT’

-                                                   100%[================================================================================================================>]   3.12K  --.-KB/s    in 0s      

2022-08-03 16:20:31 (107 MB/s) - written to stdout [3195/3195]
```

#### Verify the key's fingerprint.
```bash
dev@dev:~$ gpg --no-default-keyring \
>     --keyring /usr/share/keyrings/hashicorp-archive-keyring.gpg \
>     --fingerprint
/usr/share/keyrings/hashicorp-archive-keyring.gpg
-------------------------------------------------
pub   rsa4096 2020-05-07 [SC]
      E8A0 32E0 94D8 EB4E A189  D270 DA41 8C88 A321 9F7B
uid           [ unknown] HashiCorp Security (HashiCorp Package Signing) <security+packaging@hashicorp.com>
sub   rsa4096 2020-05-07 [E]
```

The gpg command will report the key fingerprint.  The fingerprint must match `E8A0 32E0 94D8 EB4E A189 D270 DA41 8C88 A321 9F7B`. You can also verify the key on [Security at HashiCorp](https://www.hashicorp.com/security) under Linux Package Checksum Verification.

Add the official HashiCorp repository to your system. The `lsb_release -cs` command finds the distribution release codename for your current system, such as `buster`, `groovy`, or `sid`.
```bash
dev@dev:~$ echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] \
>     https://apt.releases.hashicorp.com $(lsb_release -cs) main" | \
>     sudo tee /etc/apt/sources.list.d/hashicorp.list
deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg]     https://apt.releases.hashicorp.com focal main
```

#### Install Terraform
Download the package information from HashiCorp.
```bash
dev@dev:~$ sudo apt update
Fetched 91.2 kB in 2s (57.5 kB/s)    
Reading package lists... Done
Building dependency tree       
Reading state information... Done
104 packages can be upgraded. Run 'apt list --upgradable' to see them.

dev@dev:~$ sudo apt-get install terraform
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following NEW packages will be installed:
  terraform
0 upgraded, 1 newly installed, 0 to remove and 104 not upgraded.
Need to get 19.9 MB of archives.
After this operation, 62.9 MB of additional disk space will be used.
Get:1 https://apt.releases.hashicorp.com focal/main amd64 terraform amd64 1.2.6 [19.9 MB]
Fetched 19.9 MB in 1s (15.3 MB/s)    
Selecting previously unselected package terraform.
(Reading database ... 243340 files and directories currently installed.)
Preparing to unpack .../terraform_1.2.6_amd64.deb ...
Unpacking terraform (1.2.6) ...
Setting up terraform (1.2.6) ...
```

#### Verify the installation
Verify the installation by opening a new terminal session and listing Terafform's available subcommands.
```bash
dev@dev:~$ terraform -help
Usage: terraform [global options] <subcommand> [args]

The available commands for execution are listed below.
The primary workflow commands are given first, followed by
less common or more advanced commands.

Main commands:
  init          Prepare your working directory for other commands
  validate      Check whether the configuration is valid
  plan          Show changes required by the current configuration
  apply         Create or update infrastructure
  destroy       Destroy previously-created infrastructure

All other commands:
  console       Try Terraform expressions at an interactive command prompt
  fmt           Reformat your configuration in the standard style
  force-unlock  Release a stuck lock on the current workspace
  get           Install or upgrade remote Terraform modules
  graph         Generate a Graphviz graph of the steps in an operation
  import        Associate existing infrastructure with a Terraform resource
  login         Obtain and save credentials for a remote host
  logout        Remove locally-stored credentials for a remote host
  output        Show output values from your root module
  providers     Show the providers required for this configuration
  refresh       Update the state to match remote systems
  show          Show the current state or a saved plan
  state         Advanced state management
  taint         Mark a resource instance as not fully functional
  test          Experimental support for module integration testing
  untaint       Remove the 'tainted' state from a resource instance
  version       Show the current Terraform version
  workspace     Workspace management

Global options (use these before the subcommand, if any):
  -chdir=DIR    Switch to a different working directory before executing the
                given subcommand.
  -help         Show this help output, or the help for a specified subcommand.
  -version      An alias for the "version" subcommand.
```

## Reference
* [Install Terraform](https://learn.hashicorp.com/tutorials/terraform/install-cli)