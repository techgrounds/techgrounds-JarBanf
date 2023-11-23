# CF, R53, EFS, RDS & EB

<ins>CloudFront</ins>

Amazon CloudFront is a web service that speeds up distribution of your static and dynamic web content, such as .html, .css, .js, and image files, to your users. 

<ins>Route 53</ins>

Amazon Route 53 is a highly available and scalable Domain Name System (DNS) web service.

<ins>Elastic File System</ins>

Amazon Elastic File System provides serverless, fully elastic file storage so that you can share file data without provisioning or managing storage capacity and performance.

<ins>Relational Database Service</ins>

Amazon Relational Database Service is a web service that makes it easier to set up, operate, and scale a relational database in the cloud. Amazon Aurora is part of RDS.

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

Amazon CloudFront is a web service that speeds up distribution of your static and dynamic web content, such as .html, .css, .js, and image files, to your users. CloudFront delivers your content through a worldwide network of data centers called edge locations. When a user requests content that you're serving with CloudFront, the request is routed to the edge locations that provides the lowest latency (time delay), so that content is delivered with the best possible performance.

- What problem does CloudFront solve?
    - It speeds up distribution of web contents to you users using edge locations. 
- Which key terms belong to CloudFront?
    - <ins>Edge locations</ins>: data centers designed to deliver services with the lowest latency possile. Amazon has dozens of these data centers spread across the world. They're closer to users than Regions or Availability Zones, often in major cities, so responses can be fast and snappy.
    - AWS backbone network: a comprehensive global network infrastructure. This infrastructure consists of a vast interconnected web of fiber optic cables and network devices that span the globe, ensuring fast, efficient data transfer between Amazon's data centres and edge locations.
- How does CloudFront fit-in/replace an on-premises setting?
    - Before AWS CloudFront, companies would pay CDN operators to deliver their content to their end users. In turn, a cdn pays ISP's, carriers, and network operators for hosting its servers in their data centers. With CloudFront, this CDN is within AWS and eliminates the need to use outside CDN providers.
- How can I combine CloudFront with other services?
    - If the content is not in the needed edge location, CloudFront retrieves it from an origin that you've defined, such as:
        - AWS S3: used to store and retrieve any amount of object based data using highly scalable, reliable, fast, and inexpensive data storage. 
        - AWS EC2 Web Server: Virtual server where websites and their contents are stored.
        - AWS Elemental MediaPackage: a video delivery service that allows video providers to securily and reliably distribute streaming video at scale.
        - AWS Lambda: 
- What is the difference between CloudFront and other similar services?
    - Integration with Other AWS Services.
    - Features and Offerings.
    - Pricing and Billing Models.
    - Performance and Speed.

**Route 53**

- What problem does X solve?
- Which key terms belong to X?
- How does X fit-in/replace an on-premises setting?
- How can I combine X with other services?
- What is the difference between X and other similar services?


**Gain practical experience with:**

**Elastic File System**

- What problem does X solve?
- Which key terms belong to X?
- How does X fit-in/replace an on-premises setting?
- How can I combine X with other services?
- What is the difference between X and other similar services?
- Where can I find this service in the console?
- How do I enable this service?
- How can I link this service to other resources?

**Relational Database Service**

- What problem does X solve?
- Which key terms belong to X?
- How does X fit-in/replace an on-premises setting?
- How can I combine X with other services?
- What is the difference between X and other similar services?
- Where can I find this service in the console?
- How do I enable this service?
- How can I link this service to other resources?

**Elastic Beanstalk**

- What problem does X solve?
- Which key terms belong to X?
- How does X fit-in/replace an on-premises setting?
- How can I combine X with other services?
- What is the difference between X and other similar services?
- Where can I find this service in the console?
- How do I enable this service?
- How can I link this service to other resources?