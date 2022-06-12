# Introduction

## What is Container Orchestration?

A container orchestrator is a system that automatically deploys and manages containerized apps. For example, the orchestrator can dynamically respond to changes in the environment to increase or decrease the deployed instances of the managed app. Or, it can ensure all deployed container instances get updated if a new version of a service is released.

<img src = "https://docs.microsoft.com/en-us/learn/modules/intro-to-kubernetes/media/2-tasks-of-orchestrator.svg"><br />

## Kubernetes

Kubernetes is a portable, extensible open-source platform for managing and orchestrating containerized workloads. Kubernetes abstracts away complex container management tasks, and provides you with declarative configuration to orchestrate containers in different computing environments. This orchestration platform gives you the same ease of use and flexibility you may already know from platform as a service (PaaS) or infrastructure as a service (IaaS) offerings.

<img src = "https://docs.microsoft.com/en-us/learn/modules/intro-to-kubernetes/media/2-deploy-multiple-containers-k8s.png"><br />

## Kubernetes benefits

The benefits of using Kubernetes are based on the abstraction of tasks.

<img src = "https://docs.microsoft.com/en-us/learn/modules/intro-to-kubernetes/media/2-kubernetes-benefits.svg"><br />

These tasks include:

* Self-healing of containers. An example would be restarting containers that fail or replacing containers.
* Scaling deployed container count up or down dynamically, based on demand.
* Automating rolling updates and rollbacks of containers.
* Managing storage.
* Managing network traffic.
* Storing and managing sensitive information, such as usernames and passwords.

## Kubernetes considerations

With Kubernetes, you can view your datacenter as one large compute resource. You don't worry about how and where you deploy your containers, only about deploying and scaling your apps, as needed.

<img src = "https://docs.microsoft.com/en-us/learn/modules/intro-to-kubernetes/media/2-kubernetes-considerations.svg"><br />

However, it's important to understand that Kubernetes isn't a single installed app that comes with all possible components needed to manage and orchestrate a containerized solution:

* Aspects such as deployment, scaling, load balancing, logging, and monitoring are all optional. You're responsible for finding the best solution that fits your needs to address these aspects.
* Kubernetes doesn't limit the types of apps that can run on the platform. If your app can run in a container, it can run on Kubernetes. To make optimal use of containerized solutions, your developers need to understand concepts, such as microservices architecture.
* Kubernetes doesn't provide middleware, data-processing frameworks, databases, caches, or cluster storage systems. All these items are run as containers, or as part of another service offering.
* For Kubernetes to run containers, it needs a container runtime, like Docker. The container runtime is the object that's responsible for managing containers. For example, the container runtime starts, stops, and reports on the container's status.
* You're responsible for maintaining your Kubernetes environment. For example, you need to manage OS upgrades and the Kubernetes installation and upgrades. You also manage the hardware configuration of the host machines, such as networking, memory, and storage.
