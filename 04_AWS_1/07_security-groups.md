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
- [Control traffic to subnets using network ACLs](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html)
- [Infrastructure security in Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/infrastructure-security.html#VPC_Security_Comparison)

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
- Authorize only specific IAM principals to create and modify security groups.
- Create the minimum number of security groups that you need, to decrease the risk of error. Use each security group to manage access to resources that have similar functions and security requirements.
- When you add inbound rules for port 22 (SSH) or 3389 (RDP) so that you can access your EC2 instancec, authorize only specific IP address ranges. If you specify 0.0.0.0/0 (IPv4) and ::/(IPv6), this enables anyone to access your instances from any IP address using the specified protocol.
- Do not open large port ranges. Ensure that access through each port is restricted to the sources or destinations that require it.
- Consider creating network ACLs with rules similar to your security groups, to add an additional layer of security to your VPC.

**- Network Access Control Lists in AWS**

A network access control list (ACL) allows or denies specific inbound or outbound traffic at the subnet level. You can use the default network ACL for you VPC, or you can create a custom network ACL for your VPC with rules that are similar to the rules for your security groups in order to add an additional layer of security to your VPC.

<ins>Network ACL basic:</ins>

- Your VPC automatically comes with a modifiable default network ACL. by default, it allows all inbound and outbound IPv4 trafic, if applicable, IPv6 traffic.
- You can create a custm network ACL and associate it with a subnet to allow or deny specific inbound or outbound traffic at the subnet level.
- Each subnet in you VPC must be associated with a network ACL. If you don't explicitly associate a subnet with a network ACL, the subnet is automatically associated with the default network ACL.
- You can associate a network ACL with multiple subnets. However, a subnet can be associated with only one network ACL at a time. When you associate a network ACL with a subnet, the previous association is removed.
- A network ACL has inbound rules and outbound rules. Each rule can either allow or deny traffic. Each rule has a number from 1 to 32766. We evaluate the rules in order, starting with the lowest numbered rule, when deciding whether allow or deny traffic. If the traffic matches a rule, the rule is applied and we do not evaluate any additional rules. It is recommended that you start by creating rules in increments (for example, incrememts of 10 or 100) so that you can insert new rules later on, if needed.
- We evaluate the network ACL rules when traffic enters and leaves the subnet, not as it is routed within a subnet.
- NACLs are stateless, which means that information about previously sent or received traffic is not saved. If, for example, you create a NACL rule to allow specific inbound traffic to a subnet, responses to that traffic are not automatically allowed. This is in contrast to how security groups work.
- Network ACLs can't block DNS requests to or from the Route 53 Resolver (also known as the VPC+2 IP address or AmazonProvidedDNS). To filter DNS requests through the Route 53 Resolver, you can enable Route 53 Resolver DNS Firewall in the Amazon Route 53 Developer Guide.
- Network ACLs can't block traffic to the Instance Metadata Service (IMDS).
- Network ACLs do not filter traffic destined to and from the following:
    - Amazon Domain Name Services (DNS)
    - Amazon Dynamic Host Configuration Protocol (DHCP)
    - Amazon EC2 instance metadata
    - Amazon ECS task metadata endpoints
    - License activation for Windows instances
    - Amazon Time Sync Service
    - Reserved IP addresses used by the default VPC router
- There are quotas (also known as limits) for the number of network ACLs per VPC and the number of rules per network ACL.

<ins>Security Groups - Network ACL comparison.</ins>

The following table summarizes the basic differences between security groups and network ACLs.

| **Security Group** | **Network ACL** |
|---|---|
| Operates at the instance level | Operates at the subnet level |
| Applies to an instance only if it is associated with the instance | Applies to all instances deployed in the associated subnet (providing an additional layer of defense if security group rules are too permissive) |
| Supports allow rules only | Support allow rules and deny rules |
| Evaluates all rulles before deciding whether to allow traffic | Evaluates rules in order, starting with the lowest numbered rule, when deciding whether to allow traffic |
| Stateful: Return traffic is allowed, regardless of the rules | Stateless: Return traffic must be explicitly allowed by the rules |