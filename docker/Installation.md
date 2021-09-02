# Installation

### **Docker on Ubuntu**
**OS requirements**

You need the 64-bit version of one of these Ubuntu versions and minimum of 8GB RAM
* Ubuntu Hirsute 21.04
* Ubuntu Groovy 20.10
* Ubuntu Focal 20.04 (LTS)
* Ubuntu Bionic 18.04 (LTS)

**Installation Guide**
1. Update the apt package index and install packages to allow apt to use a repository over HTTPS
```
dev@dev:~$ sudo apt update

dev@dev-PC:~$ sudo apt install \
  apt-transport-https \
  ca-certificates \
  curl \
  gnupg \
  lsb-release
```

2. Add Docker’s official GPG key
```
dev@dev:~$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
```

3. Install Docker Engine
```
dev@dev:~$ sudo apt install docker-ce docker-ce-cli containerd.io
```

4. Verify that Docker Engine is installed correctly by running the hello-world image
```
dev@dev-PC:~$ sudo docker run hello-world
```

5. Create [Dockerhub](https://hub.docker.com/signup) account

Reference:
* [Install Docker on Ubuntu Documenation](https://docs.docker.com/engine/install/ubuntu/)

### **Run as ROOTLESS**
**Check if the group exist**
```
dev@dev:~$ grep "docker" /etc/group
```

**Steps**
```
dev@dev:~$ sudo groupadd docker
dev@dev:~$ sudo usermod -aG docker $USER
dev@dev:~$ newgrp docker
```

After that, restart your PC.

Reference:
* [Docker can not connect to docker daemon and permission denied](https://jhooq.com/permission-denied-docker-daemon/)
* [Fixing - permission denied trying to connect to Docker daemon socket at unix:///var/run/docker.sock
](https://www.youtube.com/watch?v=FcZ1Dh3X5JQ)
* [Run without Sudo](https://docs.docker.com/install/linux/linux-postinstall/#manage-docker-as-a-non-root-user)


### **Docker Compose on Ubuntu**
1. Run this command to download the current stable release of Docker Compose
```
dev@dev:~$ sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```
To install a different version of Compose, substitute `1.29.2` with the version of Compose you want to use.

2. Apply executable permissions to the binary
```
dev@dev:~$ sudo chmod +x /usr/local/bin/docker-compose
```

3. Test the installation.
```
dev@dev:~$ docker-compose --version
```

Reference:
* [Install Docker Compose on Ubuntu Documenation](https://docs.docker.com/compose/install/)

### **Docker on MAC**

**Installation Guide**
1. Sign up for a [Docker Hub Account](https://www.docker.com/) and click on `Get Started` and find `Download for Mac`.
2. Download / Install Docker for Mac
3. Log-in to Docker
4. Verify Docker installation
```
dev@dev:~$ docker version
```