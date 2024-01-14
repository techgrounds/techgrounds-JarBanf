# User Stories
The Product Owners have already had a meeting and have drawn up the following epics and backlog. You will work on these epics and user stories as a team.

If you and your team identify user stories that need to be split into smaller stories, your team is free to do so.

The following epics apply to the project:

| Epic | Description | Deadline |
| - | - | - |
| Exploration | The exploration epic is intended to make choices about the project. Once you've finished this epic, make sure you don't have to come back to it. You don't have enough time to make major adjustments. | 12 Jan '24 |
| v1.0 | Epic v1.0 is the delivery of the Infrastructure as Code and all required documentation to the requirements you discovered during the exploration. | 02 Feb '24 |
| v1.1 | Version 1.1 is the delivery of the Infrastructure as Code and all required documentation according to the requirements that will become available later. | 23 Feb '24 |
<br>

## Exploration
Here are the user stories for the epic Exploration.

|  | User Story | Description | Deliverable |
| - | - | - | - |
| 1 | As a team, we want to be clear about the requirements of the application. | You have already received a lot of information. Some requirements are already mentioned in this document, but this list may be incomplete or unclear. It is important to sort out all the uncertainties before you start doing major work. | A point-by-point description of all requirements. |
| 2 | As a team, we want a clear overview of the assumptions we have made. | You have already received a lot of information. There may be questions that none of the stakeholders have been able to answer. Your team should be able to produce an overview of the assumptions you are making as a result. | A point-by-point overview of all assumptions. |
| 3 | As a team, we want to have a clear overview of the Cloud Infrastructure that the application needs. | You have already received a lot of information. And already a design. Only aspects such as IAM/AD are still missing from the design. Identify these additional services you will need and make an overview of all services. | An overview of all services that will be used. |
<br>

## V1.0
Here are the user stories for the epic V1.0.

|  | User Story | Description | Deliverable |
| - | - | - | - |
| 1 | As a customer, I want a working application with which I can deploy a secure network. | The application must build a network that meets all requirements. An example of a stated requirement is that only traffic from trusted sources may access the management server. | IaC code for the network and all components. |
| 2 | As a customer I want a working application with which I can deploy a working web server. | The application must start a web server and make it available to the general public. | IaC code for a web server and all supplies. |
| 3 | As a customer, I want a working application with which I can deploy a working management server. | The application must start a management server and make it available to a limited audience. | IaC code for a management server with all the necessities. |
| 4 | As a customer I want a storage solution in which bootstrap/post-deployment script can be stored. | There must be a location available where bootstrap scripts become available. This script should not be publicly accessible. | IaC code for a script storage solution. |
| 5 | As a customer, I want all my data in the infrastructure to be encrypted. | Much value is attached to the security of data at rest and in motion. All data must be encrypted. | IaC code for encryption facilities. |
| 6 | As a customer, I want to have a backup every day that is retained for 7 days. | The customer would like to have a backup available should it be necessary to restore the servers to a previous state. (Make sure the Backup actually works) | IaC code for backup facilities. |
| 7 | As a customer I want to know how I can use the application. | Make sure the customer can understand how to use the application. Make sure it is clear what the customer must configure before the deployment can start and which arguments the program needs. | Documentation for using the application. |
| 8 | As a customer, I want to be able to deploy an MVP for testing. | The customer wants to test your architecture internally before using the code in production. Ensure that configuration is available that allows the customer to deploy an MVP. | Configuration for an MVP deployment. |
<br>

## V1.1
Here are the user stories for the epic V1.1.

|  | User Story | Description | Deliverable |
| - | - | - | - |
| 1 | - | - | - |
| 2 | - | - | - |
| 3 | - | - | - |
<br>

## Checklist
### Exploration, deadline 12 jan '24
- [x] 1. A point-by-point description of all requirements.
- [ ] 2. A point-by-point overview of all assumptions.
- [ ] 3. An overview of all services that will be used.

### Exploration, deadline 12 jan '24
- ✅ 1. A point-by-point description of all requirements.
- 🔲 2. A point-by-point overview of all assumptions.
- 🔲 3. An overview of all services that will be used.

### Exploration, deadline 12 jan '24
| Done? | Deliverable |
| :-: | - |
| ✅ | 1. A point-by-point description of all requirements. |
| 🔲 | 2. A point-by-point overview of all assumptions. |
| 🔲 | 3. An overview of all services that will be used. |

### v1.0
- [ ]
- [ ]
- [ ]
- [ ]
- [ ]
- [ ]
- [ ]
- [ ]