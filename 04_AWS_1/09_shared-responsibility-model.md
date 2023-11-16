# Shared Responsibility Model
The AWS shared responsibility model is a concept of dividing responsibilities between AWS and a Customer.

## Key-terms

## Assignment

<ins>Study:</ins>
- The AWS Shared Responsibility Model

### Used sources
- [Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/)

### Encountered problems
None

### Result

**<ins>Study:</ins>**

**- The AWS Shared Responsibility Model**

Security and Compliance is a shared responsibility between AWS and the customer. This shared model can help relieve the customer's operational burden as AWS operates, manages and controls the component from the host operating system and virtualization layer down to the physical security of the facilities in which the service operates. The customer assumes responsibility and management of the guest operating system (including updates and security patches), other associated application software as well as the configuration of the AWS provided securty group firewall. Customers should carefully consider the services they choose as their responsibilities vary depending on the services used, the integration of those services into their IT environment, and applicable laws and regulations. The nature of this shared responsibility also provides the flexibility and customer control that permits the deployment. As shown in the cart below, this differentiation of responsibility is commonly referred to as Security "of" the Cloud versus Security "in" the cloud.

![shared responsibility model](/04_AWS_1/images/09_srm1.jpg)<br><br>

<ins>AWS responsibility “Security of the Cloud”</ins>  
AWS is responsible for protecting the infrastructure that runs all of the services offered in the AWS Cloud. This infrastructure is composed of the hardware, software, networking, and facilities that run AWS Cloud services.

<ins>Customer responsibility “Security in the Cloud”</ins>  
Customer responsibility will be determined by the AWS Cloud services that a customer selects. This determines the amount of configuration work the customer must perform as part of their security responsibilities.

This customer/AWS shared responsibility model also extends to IT controls. Just as the responsibility to operate the IT environment is shared between AWS and its customers, so is the management, operation and verification of IT controls shared. As every customer is deployed differently in AWS, customers can take advantage of shifting management of certain IT controls to AWS which results in a (new) distributed control environment. Below are examples of controls that are managed by AWS, AWS Customers and/or both.

<ins>Inherited Controls</ins>  
Controls which a customer fully inherits from AWS.
- Physical and Environmental controls

<ins>Shared Control</ins>  
Controls which apply to both the infrastructure layer and customer layers, but in completely separate contexts or perspectives. In a shared control, AWS provides the requirements for the infrastructure and the customer must provide their own control implementation within their use of AWS services.
- Patch Management: AWS is responsible for patching and fixing flaws within the infrastructure, but customers are responsible for patching their guest OS and applications.
- Configuration Management: AWS maintains the configuration of its infrastructure devices, but a customer is responsible for configuring their own guest operating systems, databases, and applications.
- Awareness & Training: AWS trains AWS employees, but a customer must train their own employees.

<ins>Customer Specific</ins>  
Controls which are solely the responsibility of the customer based on the application they are deploying within AWS services.
- Service and Communications Protection or Zone Security which may require a customer to route or zone data within specific security environments.

<ins>Applying the AWS Shared Responsibility Model in Practice</ins>  
Once a customer understands the AWS Shared Responsibility Model and how it generally applies to operating in the cloud, they must determine how it applies to their use case. Customer responsibility varies based on many factors, including the AWS services and Regions they choose, the integration of those services into their IT environment, and the laws and regulations applicable to their organization and workload.