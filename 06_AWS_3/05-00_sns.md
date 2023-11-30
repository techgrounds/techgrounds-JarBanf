# SNS

Amazon Simple Notification Service (Amazon SNS) is a web service that enables applications, end-users, and devices to instantly send and receive notifications from the cloud.

## Key-terms


## Assignment

<ins>Gain theoretical and practical knowledge of SNS</ins>

### Used sources
- [What is Amazon SNS?](https://docs.aws.amazon.com/sns/latest/dg/welcome.html)
- [Getting started with Amazon SNS](https://docs.aws.amazon.com/sns/latest/dg/sns-getting-started.html)

### Encountered problems
None

### Result

**<ins>Theory</ins>**

![sns](/06_AWS_3/includes/05_SNS1.jpg)<br><br>

Amazon Simple Notification Service is a managed service that provides message delivery from publishers to subscribe (also known as producers and consumers). Publishers communicate asynchronously with subscribers by sending messages to a topic, which is a logical access point and communication channel. Clients can subscribe to the SNS topic and receive published messages using a supported endpoint type, such as Amazon Kinesis Data Firehose, Amazon SQS, AWS Lambda, HTTP, email, mobile push notifications, and mobile text messages (SMS).

![snsa](/06_AWS_3/includes/05_SNS1-2.png)<br><br>

- What problem does SNS solve?
    - It helps solve various communication challenges within applications and systems by allowing reliable, scalable, and secure message publication and delivery.

- Which key terms belong to SNS?
    - <ins>Topics</ins>: These are logical communication channels to which message are published.
    - <ins>Subscriptions</ins>: These are endpoints that receive messages published to topics.
    - <ins>Publishers</ins>: These are entities that send messages to SNS topics. Publishers can be applications or systems that generate events or messages
    - <ins>Messages</ins>: These are units of information published to SNS topics by publishers. Messages contain the content to be delivered to subscribers.
    - <ins>Endpoints</ins>: These are the target destinations that receive messages sent by SNS.

- How does SNS fit-in/replace an on-premises setting?
    - Amazon SNS serves as a robust replacement for on-premises messaging systems by offering scalability, reliability, and ease of management. It simplifies setup, ensures high availability, and scales effortlessly to handle large volumes of messages and subscribers. With a pay-as-you-go model, it reduces operational costs and provides global reach for message delivery across regions. Its seamless integration with various AWS services simplifies communication within your infrastructure, making it a modern, cost-effective, and efficient solution compared to traditional on-premises messaging setups.

- How can I combine SNS with other services?
    - <ins>AWS Lambda</ins>: You can trigger AWS Lambda functions with SNS messages. This integration allows you to execute code in response to events published to an SNS topic.
    - <ins>Amazon SQS</ins>: SNS can deliver messages to SQS queues, allowing you to decouple message publishers from subscribers. This combination enables reliable and scalable message processing where subscribers consume messages from SQS queues.
    - <ins>S3</ins>: SNS can be integrated with Amazon S3 to send notifications when objects are uploaded, deleted, or modified in S3 buckets. This helps in triggering actions or workflows based on changes in S3 objects.
    - <ins>EC2 Auto Scaling</ins>: SNS can be used in combination with EC2 Auto Scaling to send notifications about scaling events. You can configure SNS to notify when instances are launched, terminated, or face any scaling events.
    - <ins>CloudWatch</ins>: SNS can be linked with CloudWatch alarms to trigger notifications based on predefined thresholds or events.

**<ins>Practice</ins>**

- Create a topic.

![sns](/06_AWS_3/includes/05_SNS2-1.png)<br><br>

- Create a subscription to the topic

![sns](/06_AWS_3/includes/05_SNS2-2.png)<br><br>

- Confirm subscription

![sns](/06_AWS_3/includes/05_SNS2-3.png)<br>

![sns](/06_AWS_3/includes/05_SNS2-4.png)<br><br>

- Publish a message to the topic

![sns](/06_AWS_3/includes/05_SNS2-5.png)<br>

![sns](/06_AWS_3/includes/05_SNS2-6.png)<br><br>