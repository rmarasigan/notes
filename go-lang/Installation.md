# Installation

To **download and install**, please follow the instructions describe [here](https://go.dev/doc/install).

Prerequisite:
- GO
- GIT (Optional)
- GCC Compiler
- Visual Studio Code (Optional)

## Linux

#### Go Installation
```bash
dev@dev:~$ sudo apt install software-properties-common apt-transport-https wget
dev@dev:~$ wget -c https://go.dev/dl/go1.xx.xx.linux-amd64.tar.gz
dev@dev:~$ sudo tar -C /usr/local -xzf go1.xx.xx.linux-amd64.tar.gz
dev@dev:~$ sudo vim .profile
```

NOTE: Please remember to change the xx.xx to your desired version of go.

## File Hierarchy
```
go
│
└───bin
|
└───pkg
│   
└───src
│   │
│   └───github.com
```
<br>

Add this inside the .profile
```bash
## GO configuration ##
PATH="$HOME/bin:$HOME/.local/bin:$PATH"
export PATH=$PATH:/usr/local/go/bin
export GOPATH=$HOME/go
export PATH=$PATH:$GOPATH/bin
```

**NOTE**: The changes made to the `.profile` will not be applied until the next time you log into your machine. Please restart your machine.

To check if it's already installed:
```bash
dev@dev:~$ go version
go version go1.xx.xx linux/amd64
```

#### GIT Installation
```bash
dev@dev:~$ sudo apt update
dev@dev:~$ sudo apt-get install git
# Git configuration
dev@dev:~$ git config --global user.name "username"
dev@dev:~$ git config --global user.email "email@email.com"
```

#### GCC Installation
```bash
dev@dev:~$ sudo apt update
dev@dev:~$ sudo apt install build-essential
dev@dev:~$ gcc --version
gcc (Ubuntu 7.4.0-1ubuntu1~18.04) 7.4.0
Copyright (C) 2017 Free Software Foundation, Inc.
This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
```

#### VS Code Installation
```bash
dev@dev:~$ sudo apt update
dev@dev:~$ sudo apt install software-properties-common apt-transport-https
dev@dev:~$ wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
dev@dev:~$ sudo install -o root -g root -m 644 packages.microsoft.gpg /etc/apt/trusted.gpg.d/
dev@dev:~$ sudo sh -c 'echo "deb [arch=amd64 signed-by=/etc/apt/trusted.gpg.d/packages.microsoft.gpg] https://packages.microsoft.com/repos/vscode stable main" > /etc/apt/sources.list.d/vscode.list'
dev@dev:~$ sudo apt update
dev@dev:~$ sudo apt install code
```
**NOTE:** Due to its size, the installation takes approximately 5 minutes.

##### VS Code Plugin Installation
* Go to **Extension** on the left side panel and install **Go by lukehoban**