# Terminologies

## Object Types

**Pods**

- Runs one or more closely related containers
- Runs a single set of containers
- Good for one-off dev purposes
- Rarely used directly in production

**Deployments**

- Administers and manages a set of pods
- Maintains a set of identical pods, ensuring that they have the correct config and that the right number exists
- Runs and manage a set of identical pods (one or more)
- Monitors the state of each pod, updating as necessary
- Good for development environment
- Good for production

**Services**

- Sets up networking in a Kubernetes Cluster
  * **ClusterIP**: Exposes a set of pods to *other objects in the cluster*
  * **NodePort**
    - Exposes a set of pods to the outside world (only good for dev purposes!)
    - Service: `port`, `targetPort`, `nodePort`
  * **LoadBalancer**: Legacy way of getting network traffic into a cluster
  * **Ingress**
    - Exposes a set of services to the outside world
    - Setup of ingress-nginx changes depending on your environment (local, GC, AWS, Azure)

**Secrets**

- Securely stores a piece of information in the cluster, such as a database password

<br />

## Path to Production
* Create config files for each service and deployment
* Test locally on minikube
* Create a Github/Travis flow to build images and deploy
* Deploy app to a cloud provider

<br />

### Controller

Any type of object that constantly works to make some desired state a reality of our cluster.

<br />

### Ingress Config

An object that has a set of configuration rules describing how traffic should be routed.

<br />

### Ingress Controller

Watches for changes to the ingress and updates the ‘thing’ that handles traffic.

<br />

## Volume

**PVC** = Persistent Volume Claim

**“Volume” in generic container terminology**

Some type of mechanism that allows a container to access filesystem outside itself

**“Volume” in Kubernetes**

An **object** that allows a container to store data at the pod level

<br />

## Why Google Cloud?

* Google created Kubernetes
* AWS only “recently” got Kubernetes support
* Far, far easier to poke around Kubernetes on Google Cloud
* Excellent documentation for beginners

<br />

## Role Based Access Control (RBAC)

* Limits who can access and modify objects in our cluster
* Enabled on Google Cloud by default
* Tiller wants to make changes to our cluster, so it needs to get some permissions set