# What is Infrastructure as Code?
Infrastructure as Code (IaC) can be defined as managing and provisioning of infrastructure through code instead of through manual processes like provisioning resources through AWS, GCP console, etc. This allows you to automatically provision and patch new resources, which saves time and leads to fewer configuration mistakes. IaC tools use either a declarative or imperative programming language to execute configuration scripts.

### Imperative
With this approach, we define our desired configuration as a sequence of commands executed in a certain order. You tell your IaC tool how to create each environment using a sequence of command imperatives. [Chef](https://www.chef.io/) is a popular imperative IaC tool, and both Ansible and Salt have some support for imperative programming as well.

Example:
```bash
$ aws s3api create-bucket --bucket "bucket-name"
```

Imperative infrastructures call for an understanding of both the programming language being used and the target system's business logic. It focuses on how you want your infrastructure to be created with scripts that are typically written in languages like Ruby or Ptyhon. Imperative Infrastructure as Code is a style of coding the infrastructure that focuses on giving a list of instructions for completing a task.

Imperative Infrastructure as Code focuses on describing what you need your infrastructure to do. You write code that specifies how virtual machines should be set up and what instances should be created for your application. It also includes modifying these scripts to accommodate changing needs and altering the configuration of the system.

### Declarative
A declarative approach defines the system's desired state, including what resources you need and any properties they should have. A declarative approach also keeps a list of the current state of your system objects, which makes taking down the infrastructure simpler to manage.

Example:
```
S3Bucket:
   Type: AWS::S3::Bucket
   Properties:
      BucketName: bucket-name
```

Declarative infrastructures can be written in any language for any type of target system so long as it follows the declarative syntax. It focuses on describing what you want your infrastructure to look like. This means that the entire process is done through a declarative language, for example YAML or JSON.

This is a powerful way to ensure that your desired configuration is maintained across all parts of your system. It also makes it easy to manage changes and deployments. Declarative Infrastructure as Code is all about making your infrastructure more reliable, faster, and cheaper. Thant means that you'll spen less time on day-to-day operations and more time innovating. You'll be able to do this by automating the entire software delivery pipeline for your applications.

## Benefits of Infrastructure-as-Code (IaC)
Instead of manually configuring cloud nodes or physical hardware, IaC automates the process infrastructure management through source code. Here are several of the major key benefits of using an IaC solution like Terraform.

* **Consistency**
   - The goal of IaC is to eliminate manual processes which helps us iterate faster while maintaining consistency as our infrastructure evolves.
* **Speed and Simplicity**
   - IaC eliminates manual processes, thereby accelerating the delivery and management lifecycles. IaC makes it possible to spin up an entire infrastructure architecture by simply running a script.
   - We can pretty much provision not only for development but also for staging, and production environments which makes our [software development life cycle (SDLC)](https://www.tutorialspoint.com/sdlc/sdlc_overview.htm) much simpler.
* **Team Collaboration**
   - Various team members can collaborate on IaC software in the same way they would with regular application code through tools like Github.
* **Error Reduction**
   - IaC minimizes the probability of errors or deviations when provisioning your infrastructure. The code completely standardizes your setup, allowing applications to run smoothly and error-free without the constant need for admin oversight.
* **Disaster Recovery**
   - With IaC you can recover from disasters more rapidly. You can usually just re-run scripts and have the exact same software provisioned again.
* **Enhanced Security**
   - IaC relies on automation that removes many security risks associated with human error. When an IaC-base is installed correctly, the overall security of your computing architecture and associated data improves massively.
* **Risk minimization**
   - Imagine having a DevOps engineer who's the only one who knows your infrastructure setup and its ins and outs. Now, imagine that engineer is leaving your company. Here, IaC is a perfect fit as a new engineer is onboarded, they won't need to spend much time understanding how our infrastructure is provisioned.

# Infrastructure as Code with Terraform
Infrastructure as Code (IaC) tools allow you to manage infrastructure with configuration files rather than through a graphical user interface. IaC allows you to build, change, and manage your infrastructure in a safe, consistent, and repeatable way by defining resource configurations that you can version, reuse, and share. Terraform uses **HashiCorp Language (HCL)** as its language to define a resource regardless of the provider being used.


* Terraform can manage infrastructure on multiple cloud platforms
* The human-readable configuration language helps you write infrastructure code quickly
* Terraform's state allows you to track resource changes throughout your deployments
* You can commit your configurations to version control to safely collaborate on infrastructure

## Standardize your deployment workflow
**Providers** define individual units of infrastructure, for example, compute instances or private networks, as resources. You can compose resources from different providers into reusable Terraform configurations called **modules**, and manage them with a consistent language and workflow.

Terraform's configuration language is *declarative*, meaning that it describes the desired end-state for your infrastructure, in contrast to procedural programming languages  that require step-by-step instructions to perform tasks. Terraform automatically calculate dependencies between resources to create or destroy them in the correct order.

![terraform-iac](assets/img/terraform-iac.png)

To deploy infrastructure with Terraform:
* **Scope** - identify the infrastructure for your project
* **Author** - write the configuration for your infrastructure
* **Initialize** - install the plugins Terreform needs to manage the infrastructure
* **Plan** - preview the changes Terraform will make to match your configuration
* **Apply** - make the planned changes

## Reference
* [What is Infrastructure as Code (IaC)?](https://www.redhat.com/en/topics/automation/what-is-infrastructure-as-code-iac)
* [What is Infrastructure as Code with Terraform?](https://learn.hashicorp.com/tutorials/terraform/infrastructure-as-code)
* [What is Terraform: Everything You Need to Know](https://www.varonis.com/blog/what-is-terraform)
* [Infrastructure as Code Declarative vs Imperative](https://www.devgeon.com/infrastructure-as-code-declarative-vs-imperative/)
* [Introduction to Infrastructure as Code with Terraform](https://dev.to/karanpratapsingh/introduction-to-infrastructure-as-code-with-terraform-4f29)