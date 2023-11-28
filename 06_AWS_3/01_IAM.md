# IAM

AWS Identity and Access Management is a web service for securely controlling access to AWS services. With IAM, you can centrally manage users, security credentials such as access keys, and permissions that control which AWS resources users and applications can access.

## Key-terms


## Assignment

<ins>Gain theoretical knowledge of IAM</ins>

### Used sources
- [What is IAM?](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html)
- [AWS IAM Overview in 7 minutes | Beginner Overview ](https://www.youtube.com/watch?v=y8cbKJAo3B4)
- 

### Encountered problems
None

### Result

**<ins>Gain theoretical knowledge of IAM</ins>**

![cloudfront](/06_AWS_3/includes/01_iam1.png)<br><br>

AWS Identity and Access Management (IAM) is a web service that helps you securely control access to AWS resources. With IAM, you can centrally manage permissions that control which AWS resources users can access. You use IAM to control who is authenticated (signed in) and authorized (has permissions) to use resources.

- What problem does IAM solve?
    - IAM provides authentication and authorization for AWS services. A service evaluates if an AWS request is allowed or denied. Access is denied by default and is allowed only when a policy explicitly grants access. You can attach policies to roles and resources to control access across AWS.
- Which key terms belong to IAM?
    - <ins>Users</ins>: specific individuals, can receive personal logins
    - <ins>Groups</ins>: collection of users
    - <ins>Roles</ins>: collection of policies (DB Read, DB Write)
    - <ins>Policies</ins>: low level permission to resources (allow or deny)
- How does IAM fit-in/replace an on-premises setting?
    - AWS IAM is similar to an on-premises directory service (such as Active Directory) where users, groups, and access policies are managed.
- How can I combine IAM with other services?
    - <ins>AWS Organizations</ins>: can be integrated with AWS Organizations to manage multiple AWS accounts centrally.
    - <ins>AWS S3</ins>: can control access to S3 buckets and objects by defining policies.
    - <ins>AWS Lambda</ins>: IAM roles can be assigned to Lambda funstions.
    - <ins>AWS EC2</ins>: IAM roles can be attached to EC2 instances, granting applications running on those instances access to other AWS services.
    - <ins>AWS CloudFormation</ins>: IAM permissions can be used to control who can create, update, or delete CloudFormation stacks and what resources can be provisioned within those stacks
    - <ins>AWS RDS</ins>: IAM authentication allows you to manage database acces using IAM users and roles. 
- What is the difference between IAM and other similar services?
- Where can I find this service in the console?
- How do I enable this service?
- How can I link this service to other resources?