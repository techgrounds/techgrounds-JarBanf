# Security groups
A security group controls the traffic that is allowed to reach and leave the resources that is associated with. For example, after you associate a security group with an EC2 instance, it controls the inbound and outbound traffic for the instance.

When you create a VPC, it comes with a default security group. You can create additional security groups for a VPC, each with their own inbound and outbound rules. You can specify the source, port range, and protocol for each inbound rule. You can specify the destination, port range, and protocol for each outbound rule.

## Key-term

## Assignment

<ins>Study:</ins>
- Security Groups in AWS
- Network Access Control Lists in AWS

### Used sources
- [Control traffic to your AWS resources using security groups](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html)

### Encountered problems
None

### Result

**<ins>Study:</ins>**

**- Security Groups in AWS**

<ins>Security group basics:</ins>
- You can assign a security group only to resources created in the same VPC as the security group. You can assign multiple security groups to a resource.
- Security groups are stateful. For example, if you send a request from an instance, the response traffic for that request is allowed to reach the instance regardless of the inbound security group rules. Responses to allowed inbound traffic are allowed to leave the instance, regardless of the outbound rules.
- Security groups do not filter traffic destined to and from the following:
    - Amazond Domain Name Services (DNS)
    - Amazon Dynamic Host Configuration Protocol (DHCP)
    - Amazon EC2 instance metadata
    - Amazon EC2 task metadata endpoint
    - License activation for Windows instances
    - Amazon Time Sync Service
    - Reserved IP addresses used by the default VPC router
- There are quotas on the number of security groups that you can create per VPC, the number of rules that you can add to each security group, and the number of security groups that you can associate with a network interface.

<ins>Best practices:</ins>
- Authorize only specific IAM principals to create and modify security grous.
- Create the minimum number of security groups that you need, to decrease the risk of error. Use each security group to manage access to resources that have similar functions and security requirements.
- When you add inbound rules for port 22 (SSH) or 3389 (RDP) so that you can access your EC2 instancec, authorize only specific IP address ranges. If you specify 0.0.0.0/0 (IPv4) and ::/(IPv6), this enables anyone to access your instances from any IP address using the specified protocol.
- Do not open large port ranges. Ensure that access through each port is restricted to the sources or destinations that require it.
- Consider creating network ACLs with rules similar yo your security groups, to add an additional layer of security to your VPC.

**- Network Access Control Lists in AWS**