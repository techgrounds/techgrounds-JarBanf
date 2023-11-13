# AWS Global Infrastructure
The AWS Global Infrastructure is a cloud platform, offering over 200 fully featured services from data centers globally. The AWS Cloud spans 102 Availability Zones within 32 geographic regions around the world, with announced plans for 15 more Availabilty Zones and 5 more AWS Regions in Canada, Germany, Malaysia, New Zealand, and Thailand.

## Key-terms
- **Latency**: a synonym for delay. In computer networking, latency is an expression of how much time it takes for a data packet to travel from one designated point to another.

## Assignment
<ins>Study:</ins>
1. What is an AWS Availability Zone?
2. What is a Region?
3. What is an Edge Location?
4. Why would you choose one region over another? (e.g. eu-central-1 (Frankfurt) over us-west-2 (Oregon)).

### Used sources
- [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/)
- [Regions and Availability Zones](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/?p=ngi&loc=2)
- [AWS Cloud Availability Zones](https://www.w3schools.com/aws/aws_cloudessentials_awsavailabilityzones.php)
- [What is an Edge Location in AWS? A Simple Explanation](https://www.lastweekinaws.com/blog/what-is-an-edge-location-in-aws-a-simple-explanation/)
- [AWS Local Zones: the Basics and How to Get Started](https://cloudian.com/guides/hybrid-it/aws-local-zones-the-basics-and-how-to-get-started/)
- [What to Consider when Selecting a Region for your Workloads](https://aws.amazon.com/blogs/architecture/what-to-consider-when-selecting-a-region-for-your-workloads/)

### Encountered problems
None

### Result
**1. What is an AWS Availability Zone?**  

An Availability Zone (AZ) is one or more data centers with redundant power, networking, and connectivity in an AWS Region. All AZ's in an AWS Region are interconnected with high-bandwidth, low-latency networking, over fully redundant dedicated metro fiber.  
AZ's are physically separated by a meaningful distance, many kilometers, from any other AZ. Having them apart reduces the risk of them all going down if a disaster happens in the region. Altough all are within 100 km of each other, close enough to have ow latency.

**2. What is a Region?**

AWS has the concept of a Region, which is a physical location around the world where they cluster data centers. They call each group of data centers an Availability Zone (AZ). Each AWS Region consists of a minimum of three, isolated, and physically seperate AZ's within a geographical area.

**3. What is an Edge Location?**

Edge locations are AWS data centers strategically placed worldwide to cache and serve content closer to end-user, reducing latency and improving performance. Amazon has dozens of these data centers spread across the world. They're closer to users than Regions or AZ's, often in major cities, so responses can be fast and snappy. 

**4. Why would you choose one region over another? (e.g. eu-central-1 (Frankfurt) over us-west-2 (Oregon)).**

There are four main factors that play into evaluating each AWS Region for a workload deployment:
- **Compliance**: if your workload contains data that is bounded by local regulations, then selecting the Region that complies with the regulation overrides other evaluation factors. This applies to workloads that are bound by data residency laws where choosing an AWS Region located in that country is mandatory.
- **Latency**: A major factor to consider for user experience is latency. Reduced network latency can make substantial impact on enhancing the user experience. Choosing an AWS Region with close proximity to your user base location can achieve lower network latency. It can also increase communication quality, given that network packets have fewer exchange points to travel through.
- **Cost**: AWS services are priced differently from one Region to another. Some regions have lower cost than others, which can result in a cost reduction for the same deployment.
- **Services and features**: Newer services and features are deployed to Regions gradually. Although all AWS Regions have the same service level agreement (SLA), some larger Regions are usually first to offer newer services, features, and software releases. Smaller Regions may not get these services or features in time for you to use them to support your workload.

Evaluating all these factors can make coming to a decision complicated. This is where your priorities as a business should influence the decision.