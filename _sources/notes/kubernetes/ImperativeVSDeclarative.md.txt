# Imperative vs Declarative

Kubernetes is a declarative system. Instead of a single controller, however, it has several controllers that are each responsible for a different Kubernetes object type, such as ReplicaSet or Deployment, for example. The API Server acts as the processor, applying the commands given by the controllers to the system state, which is stored in the Kubernetes Object Store.

<img src = "https://miro.medium.com/max/2400/1*OoPeNDU1WwsiP8OLhRgnAw.png" style = "background: #ffffff"><br />

In an imperative system, the user is responsible for knowing how to drive the system to the desired state, whereas in a declarative system, the system is responsible for knowing how to drive itself to the desired state.

## Imperative

The user knows the desired state, determines the sequence of commands to transition to the system to the desired state and supplies a representation of the commands to the system. The component of the system that applies the command to transition the state is called a processor.

<img src = "https://miro.medium.com/max/2400/1*TmGqScQkRz7Qn70j0AD7aQ.png" style = "background: #ffffff"><br />

Using an imperative paradigm, the user is responsible for defining exact steps which are necessary to achieve the end goal, such as instructions for software installation, configuration, database creation, etc. Those steps are later executed in a fully automated way. The ultimate state of the environment is a result of particular operations defined by the user. While keeping full control over the automation framework, users have to carefully plan every step and the sequence in which they are executed. Although suitable for small deployments, imperative DevOps does not scale and fails while deploying big software environments, such as OpenStack.

## Declarative

The user knows the desired state, supplies a representation of the desired state to the system, then the system reads the current state and determines the sequence of commands to transition the system to the desired state. The component that determines the necessary sequence of commands is called a controller. Declarative systems have the distinct advantage of being able to react to unintended state changes without further supervision: In the event of an unintended state change leading to a state drift, the system may autonomously determine and apply the set of mitigating actions leading to a state match. This process is called a **control loop**, a popular choice for the implementation of controllers.

Declarative define the ***desired state*** of our system and let Kubernetes automation work to ensure that the ***actual state*** of the system reflects these desires. Kubernetes will detect when the actual state of the system doesn't meet these expectations and it will intervene on your behalf to fix the problem. This enables our systems to be **self-healing** and react to problems without the need for human intervention. The "state" of your system is defined by a collection of **objects**. Each Kubernetes object has (1) a ***specification*** in which you provide the desired state and (2) a ***status*** which reflects the current state of the object. If an object's status has drifted from the specification, Kubernetes will issue the necessary commands to drive that object back to its desired state.

<img src = "https://miro.medium.com/max/2400/1*YZZY5GwXRnGZGo_UJ77mkA.png" style = "background: #ffffff"><br />

## Why “declarative over imperative”?

A declarative API makes the system more robust to component failures. With an imperative API, the crashed component may have missed a call while it was down and requires some external component to “catch it up” when it comes back up. But with a declarative API, the components simply look at the current state of the API server when it comes back up to determine what it needs to be doing (“ah, I need to ensure this container is running”).

In an **edge triggered** system, if the system misses “*an event*” (“*an edge*”), the event must be replayed in order for the system to recover. In a **level-triggered** system, even if the system misses the “event” (maybe because it is down), when it recovers it can look at the current state of the signal and respond accordingly.

## Reference

* [Kubernetes](https://www.jeremyjordan.me/kubernetes/)
* [Imperative vs Declarative](https://dominik-tornow.medium.com/imperative-vs-declarative-8abc7dcae82e)
* [Design & Development Explained](https://thenewstack.io/kubernetes-design-and-development-explained/)