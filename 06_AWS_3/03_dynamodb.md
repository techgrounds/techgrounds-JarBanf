# DynamoDB

Amazon DynamoDB is a fully managed NoSQL database service that provides fast and predictable performance with seamless scalability. You can use Amazon DynamoDB to create a database table that can store and retrieve any amount of data, and serve any level of request traffic. Amazon DynamoDB automatically spreads the data and traffic for the table over a sufficient number of servers to handle the request capacity specified by the customer and the amount of data stored, while maintaining consistent and fast performance.

## Key-terms


## Assignment

<ins>Gain practical knowledge of DynamoDB</ins>

### Used sources
- [What is Amazon DynamoDB?](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html)
- [Getting started with DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStartedDynamoDB.html)

### Encountered problems
None

### Result

**<ins>Gain practical knowledge of DynamoDB</ins>**

![dynamodb](/06_AWS_3/includes/03_DynamoDB1.png)<br><br>

Amazon DynamoDB is a fully managed NoSQL database service that provides fast and predictable performance with seamless scalability. DynamoDB lets you offload the administrative burdens of operating and scaling a distributed database so that you don't have to worry about hardware provisioning, setup and configuration, replication, software patching, or cluster scaling. DynamoDB also offers encryption at rest, which eliminates the operational burden and complexity involved in protecting sensitive data.

With DynamoDB, you can create database tables that can store and retrieve any amount of data and serve any level of request traffic. You can scale up or down your tables' throughput capacity without downtime or performance degradation. You can use the AWS Management Console to monitor resource utilization and performance metrics.

DynamoDB provides on-demand backup capability. It allows you to create full backups of your tables for long-term retention and archival for regulatory compliance needs.

You can create on-demand backups and enable point-in-time recovery for your tables. Point-in-time recovery helps protect your tables from accidental write or delete operations. With point-in-time recovery, you can restore a table to any point in time during the last 35 days.

DynamoDB allows you to delete expired items from tables automatically to help you reduce storage used and the cost of storing data that is no longer relevant.

- What problem does DynamoDB solve?
    - DynamoDB, a fully managed NoSQL database service, is designed to solve several challenges related to data storage and management:
        - <ins>Scalability without managing infrastructure</ins>: It automatically scales to handle massive workloads without requiring manual provisioning or configuration.
        - <ins>Low-latency performance</ins>: Provides consistent, single-digit millisecond latency for read and write operations, even with large amounts of data.
        - <ins>Flexible NoSQL capabilities</ins>: Supports various data models, making it adaptable to different application needs.
        - <ins>Fully managed service</ins>: AWS handles maintenance, backups, and updates, reducing operational overhead for users.
        - <ins> High availability and reliability</ins>: Replicates data across multiple availability zones for resilience against failures and data loss.
        - <ins>Adaptable performance and cost optimization</ins>: Allows dynamic adjustment of throughput to match workload demands, enabling efficient resource utilization.
        - <ins>Integrated security</ins>: Offers fine-grained access control and encryption at rest for enhanced security.
        - <ins>Read Capacity Units (RCUs)</ins>: Units representing the read capacity of a table. Each RCU allows one strongly consistent read per second (or two eventually consistent reads per second) of an item up to 4 KB in size.
        - <ins>Write Capacity Units (WCUs)</ins>: Units representing the write capacity of a table. Each WCU allows one write per second of an item up to 1 KB in size.

- Which key terms belong to DynamoDB?
    - <ins>Tables</ins>: The primary data storage structure, similar to a table in a relational database, containing items (rows) and attributes (columns).
    - <ins>Items</ins>: Individual data records stored within a table. Each item typically consists of multiple atributes.
    - <ins>Attributes</ins>: Pieces of data within an item. Attributes can be various data types, such as strings, numbers, binary data, sets, etc.
    - <ins>Primary Key</ins>: A unique identifier for each item in a table. It can be either a single attribute (Simple Primary Key) or a composite of two attributes (Composite Primary Key).
    - <ins>Partition Key</ins>: In the context of a Simple Primary Key, this is the single attribute used to uniquely identify an item in a table. For composite keys, it's the first part of the composite key.
    - <ins>Sort Key (Range Key)</ins>: In a Composite Primary Key, it's the second attribute that, combined with the partition key, allows sorting of items with the same partition key value.
    - <ins>Secondary Indexes</ins>: Additional indexes that allow querying on non-primary key attributes.


- How does DynamoDB fit-in/replace an on-premises setting?
    - <ins>Scalability</ins>: Effortlessly scales up or down to handle varying workloads without manual intervention.
    - <ins>Performance</ins>: Delivers high performance with consistenly low latency, ensuring speedy access to data.
    - <ins>Managed Service</ins>: Fully managed by AWS, eliminating the need for manual administraion and reducing operational overhead.
    - <ins>Availability and Durability</ins>: Provides high availability and durability by replicating data across multiple availability zones.
    - <ins>Cost-effectiveness</ins>: Operates on a pay-as-you-go model, potentially reducing the total cost of ownership compared to on-premises databases.
    - <ins>Global Reach</ins>: Allows global replication with Global Tables for low-latency access across regions, a complex feat in on-premises setups.

- How can I combine DynamoDB with other services?
    - <ins>AWS Lambda</ins>: Use Lambda with DynamoDB Streams for real-time processing of database.
    - <ins>Amazon S3</ins>: Trigger Lambda functions via DynamoDB Streams to store data in S3 for archiving or analytics.
    - <ins>Amazon API Gateway</ins>: Create APIs to access DynamoDB securely for applications and clients.
    - <ins>AWS CloudWatch</ins>: Monitor DynamoDB performance and set alerts for metrics.
    - <ins>AWS IAM</ins>: Manage access control to DynamoDB resources using IAM roles and policies.

- What is the difference between DynamoDB and other similar services?
    - <ins>Managed Service vs. Self-Managed Databases</ins>: DynamoDB is fully managed by AWS, meaning AWS handles infrastructure provisioning, scaling, backups, and maintenance. In contrast, other NoSQL databases like MongoDB or Cassandra might require more hands-on management from users.
    - <ins>Scalability</ins>: DynamoDB offers seamless scalability with automatic sharding and distribution of data, allowing it to handle high throughput and massive workloads without manual intervention. Some other databases may require more effort to scale effectively.
    - <ins>Performance</ins>: DynamoDB provides consistent, single-digit millisecond latency for read and write operations across various scales. While many NoSQL databases offer good performance, DynamoDB's speed remains a standout feature.
    - <ins>Integration with AWS Ecosystem</ins>: DynamoDB seamlessly integrates with various AWS services like Lambda, S3, API Gateway, and more. While other databases can integrate with AWS services, DynamoDB's tight integration simplifies building end-to-end solutions within the AWS ecosystem.

- Where can I find this service in the console?
    - Under the "Database" category.

- How do I enable this service?
    - By choosing "Create table" and following the steps.

- How can I link this service to other resources?
    - DynamoDB can be linked or integrated with various AWS services to create robust and versatile solutions. By linking DynamoDB with these AWS services, you can create scalable, high-performance applications that fulfill various use cases, from real-time data processing to analytics and beyond.