# Terraform
Terraform is an `Infrastructure as Code (IAC)` tool that lets you define both cloud and on-prem resources in human-readable configuration files that you can version, reuse, and share. Terraform can manage low-level components like compute, storage, and networking resources, as well as high-level components like DNS entries and SaaS features.

It's a cloud-agnostic, open-source provisioning tool written in the Go language and created by HashiCorp. Terraform allows you to describe your complete infrastructure in the form of code. Even if your servers come from different providers such as AWS or Azure, Terraform helps you build and manage these resources in parallel across providers.

## How does it work?
Terraform creates and manages resources on cloud platforms and other services through its application programming interfaces (APIs). Providers enable Terraform to work with virtually any platform or service with an accessible API.

![intro-terraform-apis](assets/img/intro-terraform-apis.png)

The core **Terraform workflow** consists of three stages:
* **Write**
   - You define resources, which may be across multiple cloud providers and services.
   - You'll declare your infrastructure resources as code using the Hashicorp Configuration Language (HCL).
* **Plan**
   - Creates an execution plan describing the infrastructure it will create, update, or destroy based on the existing infrastructure and your configuration.
* **Apply**
   - On approval, Terraform performs the proposed operations in the correct order, respecting any resource dependencies.

![intro-terraform-workflow](assets/img/intro-terraform-workflow.png)

### How Terraform Core Works
The first is the source input that the user configures into Terraform, defining what resources need to be created or provisioned. The second input source consists of data feeds into Terraform about what the current infrastructure setup looks like.

Terraform then takes these inputs and determines what actions need to be taken. It takes the user-specified desired state, compares it with the current state, and configures the architecture in a way that closes the gaps. Terraform Core essentially figures out what needs to be created, updated, or deleted to fully provision your infrastructure.

## How Terraform Providers Work
The second key component that makes Terraform go is providers for specific technologies. Terraform has more than one hundred providers for various technologies, granting users access to its resources. If you're using AWS, for instance, Terraform will also have access to EC2 instances and other resources within the tech stack. This is how Terraform works, using both Core and Provider functionality to complete your application and infrastructure setup quickly and using only code.


## What is Terraform used for?
One of the main functions of Terraform is for public cloud provisioning on one of the major providers. Terraform enables the use of these public clouds via a provider, a plugin that wraps existing APIs and languages like Azure Bicep, and creates Terraform syntax. The second main use for Terraform is to facilitate multi-cloud deployments. One of the main draws of Terraform is that it performs across all cloud providers simultaneously, unlike some of its other IaC competitors. The third most common use of Terraform is deploying, managing, and orchestrating resources with custom cloud providers. A provider is a way in Terraform to wrap an existing API and convert it to the Terraform declarative syntax, and this can be done even if you're not using AWS or another of the major cloud services.

## Reference
* [Introduction](https://www.terraform.io/intro)
* [Introduction to HashiCorp Terraform](https://youtu.be/h970ZBgKINg)
* [What is Terraform: Everything You Need to Know](https://www.varonis.com/blog/what-is-terraform)