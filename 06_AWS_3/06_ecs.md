# ECS

Amazon Elastic Container Service (Amazon ECS) is a highly scalable, fast, container management service that makes it easy to run, stop, and manage Docker containers on a cluster of Amazon EC2 instances.

## Key-terms


## Assignment

<ins>Gain theoretical knowledge of ECS</ins>

### Used sources
- [What is Amazon Elastic Container Service?](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html)

### Encountered problems
None

### Result

**<ins>Theory</ins>**

![ECS](/06_AWS_3/includes/06_ecs1.png)<br><br>

Amazon Elastic Container Service (Amazon ECS) is a fully managed container orchestration service that helps you easily deploy, manage, and scale containerized applications. As a fully managed service, Amazon ECS comes with AWS configuration and operational best practices built-in. It's integrated with both AWS and third-party tools, such as Amazon Elastic Container Registry and Docker. This integration makes it easier for teams to focus on building the applications, not the environment. You can run and scale your container workloads across AWS Regions in the cloud, and on-premises, without the complexity of managing a control plane. 

- What problem does ECS solve?
    - Amazon Elastic Container Service (ECS) solves the challenges of deploying, managing, and scaling containerized applications by offering simplified orchestration, scalability, high availability, resource optimization, seamless integration with AWS services, and streamlined deployment processes.

- Which key terms belong to ECS?
    - <ins>Cluster</ins>: A cluster is a grouping of container instances (Amazon EC2 instances or AWS Fargate) on which ECS tasks are deployed. It acts as the logical infrastructure where tasks run.
    - <ins>Task Definition</ins>: A task definition is a blueprint that describes how a containerized application should be run. It includes configuration details like Docker image, CPU and memory requirements, networking information, and storage settings.
    - <ins>Service</ins>: A service in ECS allows for the continuous running (or desired state) of a specified number of tasks, ensuring that the specified number of tasks are always available and replacing any that fail or become unhealthy.
    - <ins>Container Instance</ins>: A container instance is an Amazon EC2 instance that is part of an ECS cluster and has the ECS container agent running on it. It can host multiple containers as defined by the tasks.
    - <ins>Container Agent</ins>: The ECS container agent is software that runs on each EC2 instance within an ECS cluster. It communicates with the ECS service and manages the containers on that instance.
    - <ins>Scheduler</ins>: ECS uses a scheduler to place tasks onto container instances within a cluster based on resource availability, task requirements, and constraints.
    - <ins>Load Balancing</ins>: ECS integrates with Elastic Load Balancing (ELB) to distribute incoming traffic across the tasks within a service, ensuring high availability and scalability.
    - <ins>Repository</ins>: Repositories are used for storing Docker container images. ECS supports the use of Amazon Elastic Container Registry (ECR) as a private Docker container image registry.

- How does ECS fit-in/replace an on-premises setting?
    - Amazon ECS offers a scalable, fully managed cloud platform for running containerized applications, replacing on-premises setups by eliminating infrastructure management, providing scalability, high availability, and cost-efficiency. It streamlines deployment, reduces operational overhead, and ensures global accessibility within AWS infrastructure.

- How can I combine ECS with other services?
    - <ins>AWS IAM</ins>: AWS Identity and Access Management is an access management service that helps you securely control access to AWS resources. You can use IAM to control who's authenticated (signed in) and authorized (has permissions) to view or perform specific actions on resources. In Amazon ECS, you can use IAM to control access at the container instance level using IAM roles. You can also use it to control access at the task level using IAM task roles.
    - <ins>Amazon EC2 Auto Scaling</ins>: Auto Scaling is a service that sets up automatic scaling for your tasks. The scaling is based on user-defined policies, health status checks, and schedules. You can use Auto Scaling alongside a Fargate task within a service to scale in response to a number of metrics. Or, alternatively, you can use it with an EC2 task to scale the container instances within your cluster.
    - <ins>AWS ELB</ins>: The Elastic Load Balancing service automatically distributes incoming application traffic across the tasks in your Amazon ECS service. You can use it to achieve greater levels of fault tolerance in your applications. At the same time, you can use it to also provide the amount of load-balancing capacity that's required to distribute application traffic. You can use Elastic Load Balancing to create an endpoint that balances traffic across services in a cluster.
    - <ins>AWS ECR</ins>: Amazon ECR is a managed AWS Docker registry service that's secure, scalable, and reliable. Amazon ECR supports private Docker repositories with resource-based permissions using IAM so that specific users or tasks can access repositories and images. Developers can use the Docker CLI to push, pull, and manage images.
    - <ins>AWS CloudFormation</ins>: AWS CloudFormation gives developers and systems administrators an easy way to create and manage a collection of related AWS resources. More specifically, it makes provisioning and updating resources more predictable. You can define clusters, task definitions, and services as entities in an AWS CloudFormation script.