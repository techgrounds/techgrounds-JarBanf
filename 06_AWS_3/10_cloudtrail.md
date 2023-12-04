# CloudTrail

With AWS CloudTrail, you can monitor your AWS deployments in the cloud by getting a history of AWS API calls for your account, including API calls made by using the AWS Management Console, the AWS SDKs, the command line tools, and higher-level AWS services. You can also identify which users and accounts called AWS APIs for services that support CloudTrail, the source IP address from which the calls were made, and when the calls occurred.

## Key-terms


## Assignment

<ins>Gain theoretical knowledge of CloudTrail</ins>

### Used sources
- [What Is AWS CloudTrail?](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html)

### Encountered problems
None

### Result

**<ins>Theory</ins>**

![CloudTrail](/06_AWS_3/includes/10_cloudtrail1.png)<br><br>

AWS CloudTrail is an AWS service that helps you enable operational and risk auditing, governance, and compliance of your AWS account. Actions taken by a user, role, or an AWS service are recorded as events in CloudTrail. Events include actions taken in the AWS Management Console, AWS Command Line Interface, and AWS SDKs and APIs.

CloudTrail is active in your AWS account when you create it and doesn't require any manual setup. When activity occurs in your AWS account, that activity is recorded in a CloudTrail event.

Visibility into your AWS account activity is a key aspect of security and operational best practices. You can use CloudTrail to view, search, download, archive, analyze, and respond to account activity across your AWS infrastructure. You can identify who or what took which action, what resources were acted upon, when the event occurred, and other details to help you analyze and respond to activity in your AWS account.

You can integrate CloudTrail into applications using the API, automate trail or event data store creation for your organization, check the status of event data stores and trails you create, and control how users view CloudTrail events.

- What problem does CloudTrail solve?
    - AWS CloudTrail solves the challenges of tracking and monitoring user activity within an AWS account. It offers visibility, security, and compliance by providing detailed logs of actions taken, helping in accountability, security analysis, compliance adherence, and operational insights.

- Which key terms belong to CloudTrail?
    - <ins>Trail</ins>: A configuration that enables logging of AWS API activity, defining where logs are stored and settings for log retention, encryption, and delivery.
    - <ins>Event</ins>: An activity recorded by CloudTrail, representing an API call made within an AWS account. Each event contains details such as the action performed, the user who initiated the action, the time of the action, and other relevant information.
    - <ins>Log File</ins>: The record created by CloudTrail for each API call made within an AWS account. Log files contain information about events, including details such as the event name, time, user identity, source IP address, and more.
    - <ins>Log Group</ins>: A collection of log files organized together, typically within an Amazon S3 bucket, where CloudTrail delivers log files based on the specified configurations. 
    - <ins>Event History</ins>: The history of recorded events within an AWS account, accessible through CloudTrail logs. This history provides a chronological record of API calls made over time.

- How does CloudTrail fit-in/replace an on-premises setting?
    - AWS CloudTrail, compared to on-premises logging systems, offers centralized, scalable, and accessible logging of AWS API activities without the need for hardware maintenance. It enhances security, meets compliance needs, and integrates with other AWS services for automated responses, providing cost efficiency and flexibility in a cloud environment.

- How can I combine CloudTrail with other services?
    - Certainly! AWS CloudTrail can be integrated with services like Amazon CloudWatch for real-time monitoring, AWS Lambda for automated responses, Amazon S3 for log storage, AWS Config for resource monitoring, IAM for user activity insights, and third-party SIEM tools for advanced security analysis. These integrations help enhance monitoring, automation, and security within your AWS environment.