# Minikube Setup on Linux

These instructions should be valid for Debian, Ubuntu, or Mint Linux distributions. Your experience may vary if using other distributions such as RHEL, Arch, non-desktop distributions like Ubuntu server, or lightweight distros which may omit many expected tools.

## Install Minikube

```bash
dev@dev: curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
dev@dev: sudo install minikube-linux-amd64 /usr/local/bin/minikube
```

## Starting Minikube and Testing Installation

1. Add your user to the docker group

> Note - If this step was performed when Docker was installed, it can be skipped. In your terminal, run:

```bash
dev@dev: sudo usermod -aG docker $USER && newgrp docker
```

> Log out of the user profile and log back in so these changes take effect. If running inside a VM, you will need to restart the entire machine, not just log out.

2. Start with the default driver:

```bash
dev@dev: minikube start
```

3. Check Minikube Status

> After you see a **Done**! message in your terminal, run **minikube status** to make sure the cluster is healthy. Pay particular attention that the apiserver is in a "Running" state.

```bash
dev@dev: minikube status
```

4. Install kubectl

```bash
dev@dev: curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
dev@dev: sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
```

5. Test kubectl

> Lastly, open up your terminal and make sure that you can run **kubectl version**. Note - the client and server can be off by one minor version without error or issue.

```bash
dev@dev: kubectl version
```