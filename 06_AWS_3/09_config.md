# Config

AWS Config provides a detailed view of the resources associated with your AWS account, including how they are configured, how they are related to one another, and how the configurations and their relationships have changed over time.

## Key-terms


## Assignment

<ins>Gain theoretical knowledge of Config</ins>

### Used sources
- [What Is AWS Config?](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html)

### Encountered problems
None

### Result

**<ins>Theory</ins>**

![Config](/06_AWS_3/includes/09_config1.png)<br><br>

AWS Config provides a detailed view of the configuration of AWS resources in your AWS account. This includes how the resources are related to one another and how they were configured in the past so that you can see how the configurations and relationships change over time.

When you run your applications on AWS, you usually use AWS resources, which you must create and manage collectively. As the demand for your application keeps growing, so does your need to keep track of your AWS resources. AWS Config is designed to help you oversee your application resources.

- What problem does Config solve?
    - AWS Config primarily solves the challenges of maintaining visibility, ensuring compliance, and managing changes within an AWS environment. It provides a comprehensive view of resource configurations, tracks changes over time, aids in auditing for compliance, enhances security by monitoring for unauthorized alterations, and helps in understanding resource relationships and dependencies. Ultimately, it enables better governance, risk management, and control of AWS resources.

- Which key terms belong to Config?
    - <ins>Configuration Items (CIs)</ins>: These are the AWS resources that AWS Config monitors and tracks. Each resource is represented as a configuration item, containing metadata and configuration details. 
    - <ins>Configuration History</ins>: It refers to the record of configuration changes made to AWS resources over time. AWS Config maintains a history of these changes, allowing users to view, track, and analyze alterations.
    - <ins>Configuration Snapshot</ins>: A point-in-time view of the configuration state of AWS resources captured by AWS Config. These snapshots provide a specific view of configurations at a particular moment. 
    - <ins>Rules</ins>: AWS Config allows users to define rules or policies that evaluate the configuration settings of resources against desired configurations or compliance standards. These rules help in identifying compliance violations, security vulnerabilities, or deviations from predefined configurations. 
    - <ins>Compliance</ins>: Refers to the state of adherence to predefined rules, standards, or policies. AWS Config helps in assessing and ensuring compliance by continuously evaluating resource configurations against defined rules.

- How does Config fit-in/replace an on-premises setting?
    - AWS Config serves as a configuration management and compliance service within the AWS cloud environment. While it doesn't directly replace an on-premises configuration management system, it offers similar functionalities and benefits in the cloud context.

    AWS Config's capabilities align closely with the objectives of configuration management in on-premises settings, but its functionalities are tailored specifically for AWS cloud resources and services. Organizations with a hybrid infrastructure might continue to use on-premises tools alongside AWS Config to manage configurations across both environments.

- How can I combine Config with other services?
    - AWS Config can be combined with various other AWS services to enhance its capabilities, automate responses, and enable comprehensive management of your AWS environment.
        - <ins>CloudTrail</ins>: Combine activity logs with AWS Config for a complete view of resource changes.
        - <ins>CloudWatch</ins>: Set triggers for automated actions based on AWS Config changes.
        - <ins>Lambda</ins>: Automatically respond to non-compliant setups identified by AWS Config using Lambda.
        - <ins>Systems Manager (SSM)</ins>: Automate fixes for non-compliance through Systems Manager Automation driven by AWS Config.
        - <ins>S3</ins>: Store and analyze AWS Config's configuration history snapshots in S3.