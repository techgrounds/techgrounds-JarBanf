# CF, R53, EFS, RDS & EB

<ins>CloudFront</ins>

Amazon CloudFront is a web service that speeds up distribution of your static and dynamic web content, such as .html, .css, .js, and image files, to your users. 

<ins>Route 53</ins>

Amazon Route 53 is a highly available and scalable Domain Name System (DNS) web service.

<ins>Elastic File System</ins>

Amazon Elastic File System provides serverless, fully elastic file storage so that you can share file data without provisioning or managing storage capacity and performance.

<ins>Relational Database Service</ins>

Amazon Relational Database Service is a web service that makes it easier to set up, operate, and scale a relational database in the cloud. 

<ins>Aurora</ins>



<ins>Elastic Beanstalk</ins>

With Amazon Elastic Beanstalk, you can quickly deploy and manage applications in the AWS Cloud without worrying about the infrastructure that runs those applications.

## Key-terms


## Assignment

<ins>Gain theoretical knowledge of:</ins>

- CloudFront
- Route 53

<ins>Gain practical experience with:</ins>

- EFS
- RDS/Aurora
- Elastic Beanstalk

### Used sources
- [What is Amazon CloudFront?](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html)
- [What is an Edge Location in AWS? A Simple Explanation](https://www.lastweekinaws.com/blog/what-is-an-edge-location-in-aws-a-simple-explanation/)
- [Understanding AWS Backbone: A Comprehensive Guide](https://manuabhijit.medium.com/understanding-aws-backbone-a-comprehensive-guide-8ac38e6d4179)
- [What is Amazon Route 53?](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html)
- [What is Amazon Elastic File System?](https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html)
- [What is Amazon Relational Database Service?](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html)
- [What is AWS Elastic Beanstalk?](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome.html)

### Encountered problems
None

### Result

**<ins>Gain theoretical knowledge of:</ins>**

**CloudFront**

![cloudfront](/05_AWS_2/includes/03_cf-r53-efs-rds-eb1.jpg)<br><br>

Amazon CloudFront is a web service that speeds up distribution of your static and dynamic web content, such as .html, .css, .js, and image files, to your users. CloudFront delivers your content through a worldwide network of data centers called edge locations. When a user requests content that you're serving with CloudFront, the request is routed to the edge locations that provides the lowest latency (time delay), so that content is delivered with the best possible performance.

- What problem does CloudFront solve?
    - It speeds up distribution of web contents to you users using edge locations. 
- Which key terms belong to CloudFront?
    - <ins>Edge locations</ins>: data centers designed to deliver services with the lowest latency possile. Amazon has dozens of these data centers spread across the world. They're closer to users than Regions or Availability Zones, often in major cities, so responses can be fast and snappy.
    - <ins>AWS backbone network</ins>: a comprehensive global network infrastructure. This infrastructure consists of a vast interconnected web of fiber optic cables and network devices that span the globe, ensuring fast, efficient data transfer between Amazon's data centres and edge locations.
- How does CloudFront fit-in/replace an on-premises setting?
    - Before AWS CloudFront, companies would pay CDN operators to deliver their content to their end users. In turn, a cdn pays ISP's, carriers, and network operators for hosting its servers in their data centers. With CloudFront, this CDN is within AWS and eliminates the need to use outside CDN providers.
- How can I combine CloudFront with other services?
    - If the content is not in the needed edge location, CloudFront retrieves it from an origin that you've defined, such as:
        - <ins>AWS S3</ins>: used to store and retrieve any amount of object based data using highly scalable, reliable, fast, and inexpensive data storage. 
        - <ins>AWS EC2 Web Server</ins>: virtual server where websites and their contents are stored.
        - <ins>AWS Elemental MediaPackage</ins>: a video delivery service that allows video providers to securily and reliably distribute streaming video at scale.
        - <ins>AWS Lambda</ins>: with Lambda you can run code without provisioning or managing servers.
- What is the difference between CloudFront and other similar services?
    - Integration with other AWS Services.
    - Features and Offerings.
    - Pricing and Billing Models.
    - Performance and Speed.

**Route 53**

![route 53](/05_AWS_2/includes/03_cf-r53-efs-rds-eb2.png)<br><br>

Amazon Route 53 is a highly available and scalable Domain Name System (DNS) web service. Route 53 to perform three main functions in any combination:  

<ins>Domain registration</ins>: Route 53 lets you register a name for your website or web application, known as a domain name.  

<ins>DNS routing</ins>: When a user opens a web browser and enters your domain name or subdomain name in the address bar, Route 53 helps connect the browser with your website or web application.  

<ins>Health checking</ins>: Route 53 sends automated requests over the internet to a resource, such as a web server, to verify that it's reachable, available, and functional.

- What problem does Route 53 solve?
    - <ins>Domain registration</ins>: lets you register a name for your website or web application, known as a domain name.
    - <ins>DNS routing</ins>: when a user opens a web browser and enters your domain name or subdomain name in the address bar, Route 53 helps connect the browser with your website or web application.
    - <ins>Health checking</ins>: sends automated requests over the internet to a resource, such as a web server, to verify that it's reachable, available, and functional.
- Which key terms belong to Route 53?
    - <ins>DNS</ins>: Domain Name System. Maps IP addresses to hosts connected to either the public or private internet via a process caled DNS resolution, making it an essential part of an orginization's infrastructure. 
- How does Route 53 fit-in/replace an on-premises setting?
    - <ins>Domain registration</ins>: replaces the use of 3rd party domain name registration.
    - <ins>DNS routing</ins>: in an on-premises setting, DNS services are typically managed by local DNS servers within the organization's infrastructure. These servers handle domain name resolutions, mapping domain names to IP addresses, and routing traffic within the local network and to the internet.
- How can I combine Route 53 with other services?
    - Map domain names to AWS:
        - Elastic Load Balancers
        - EC2 instances
        - S3 buckets
        - CloudFront distributions
        - and other AWS resources
    - Non-AWS resources
- What is the difference between Route 53 and other similar services?
    - Integration with other AWS Services
    - Scalability and Performance
    - DNS Services Offered
    - Pricing Structure


**Gain practical experience with:**

**Elastic File System**

![elastic file system](/05_AWS_2/includes/03_cf-r53-efs-rds-eb3.png)<br><br>

Amazon Elastic File System (Amazon EFS) provides serverless, fully elastic file storage so that you can share file data without provisioning or managing storage capacity and performance. Amazon EFS is built to scale on demand to petabytes without disrupting applications, growing and shrinking automatically as you add and remove files. Because Amazon EFS has a simple web services interface, you can create and configure file systems quickly and easily. The service manages all the file storage infrastructure for you, meaning that you can avoid the complexity of deploying, patching, and maintaining complex file system configurations. 

- What problem does EFS solve?
    - provides serverless, fully elastic file storage so that you can share file data without provisioning or managing storage capacity and performance.
- Which key terms belong to EFS?
    - <ins>File system</ins>: a method and data structure that is used to control how data is stores and retrieved.
- How does EFS fit-in/replace an on-premises setting?
    - replaces the file server and then local file system (mass storage)
- How can I combine EFS with other services?
    - AWS services that can access an Amazon EFS file system at the same time:
        - EC2
        - ECS
        - Lambda
- What is the difference between EFS and other similar services?
    - Elasticity and Scalability
    - Performance
    - Cost
- Where can I find this service in the console?
    - Under the Storage category.
- How do I enable this service?
    - By choosing "Create file system" and following the steps.
- How can I link this service to other resources?
    - While creating the other resources, you can link them to this service.

**Relational Database Service**

![relational database service](/05_AWS_2/includes/03_cf-r53-efs-rds-eb4.png)<br><br>

Amazon Relational Database Service (Amazon RDS) is a web service that makes it easier to set up, operate, and scale a relational database in the AWS Cloud. It provides cost-efficient, resizable capacity for an industry-standard relational database and manages common database administration tasks.

- What problem does RDS solve?
    - makes it easier to set up, operate, and scale a relational database in the AWS Cloud. It provides cost-efficient, resizable capacity for an industry-standard relational database and manages common database administration tasks.
- Which key terms belong to RDS?
    - Relational database: a relational database organizes data into rows and columns, which collectively form a table.
- How does RDS fit-in/replace an on-premises setting?
    - Managed Service
    - Scalability
    - High Availability
    - Security
- How can I combine RDS with other services?
    - EC2
    - Outpost
- What is the difference between RDS and other similar services?
    - RDS supports several popular relational database engines such as MySQL, PostgreSQL, MariaDB, Oracle, and Microsoft SQL Server.
    - It offers managed services for these databases, handling routine database tasks like backups, patching, automatic failover, and scaling
    - RDS provides features for read replicas to offload read traffic and Multi-AZ deployments for high availability
    - It's suitable for transactional workloads and applications that require the capabilities of traditional relational databases
- Where can I find this service in the console?
    - under the Database category.
- How do I enable this service?
    - By choosing "Create database" and following the steps.
- How can I link this service to other resources?

**Elastic Beanstalk**

![elastic beanstalk](/05_AWS_2/includes/03_cf-r53-efs-rds-eb5.png)<br><br>

- What problem does EB solve?
- Which key terms belong to EB?
- How does EB fit-in/replace an on-premises setting?
- How can I combine EB with other services?
- What is the difference between EB and other similar services?
- Where can I find this service in the console?
- How do I enable this service?
- How can I link this service to other resources?