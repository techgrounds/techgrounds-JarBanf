# Lambda

With AWS Lambda, you can run code without provisioning or managing servers. You pay only for the compute time that you consume, there's no charge when your code isn't running. You can run code for virtually any type of application or backend service—all with zero administration. Just upload your code and Lambda takes care of everything required to run and scale your code with high availability.

## Key-terms


## Assignment

<ins>Gain theoretical and practical knowledge of Lambda</ins>

### Used sources
- [What is AWS Lambda?](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)
- [Getting started with Lambda](https://docs.aws.amazon.com/lambda/latest/dg/getting-started.html)

### Encountered problems
None

### Result

**<ins>Theory</ins>**

![lambda](/06_AWS_3/includes/04_lambda1.png)<br><br>

AWS Lambda is a compute service that lets you run code without provisioning or managing servers.

Lambda runs code on a high-availability compute infrastructure and performs all of the administration of the compute resources, including server and operating system maintenance, capacity provisioning and automatic scaling, and logging. With Lambda, all you need to do is supply your code in one of the language runtimes that Lambda supports.

You organize your code into Lambda functions. The Lambda service runs your function only when needed and scales automatically. You only pay for the compute time that you consume, there is no charge when your code is not running.

- What problem does Lambda solve?
    - AWS Lambda solves the problem of managing infrastructure by allowing developers to run code without provisioning or managing servers. It offers scalability, cost efficiency, and simplifies event-driven architecture, enabling faster development and higher availability.

- Which key terms belong to Lambda?
    - <ins>Serverless Computing</ins>: allows you to build and run applications and services without thinking about servers. With serverless computing, your application still runs on servers, but all the server management is done by AWS.
    - <ins>Function</ins>: The code you upload and execute on Lambda is referred to as a function. It's a piece of code that performs a specific task and can be triggered by various events.
    - <ins>Event Sources</ins>: These are triggers that invoke your Lambda function. They can be from various sources such as AWS services like S3, DynamoDB, API Gateway, SNS, CloudWatch Events, etc., or custom events.
    - <ins>Runtime</ins>: Lambda supports multiple programming languages and the runtime is the execution environment for your function.
    - <ins>Invocation</ins>: The process of triggering or calling a Lambda function is referred to as invocation. Invocations can be synchronous (using APIs) or asynchronous (triggered by events). 
    - <ins>Execution Role</ins>: An AWS Identity and Access Management (IAM) role associated with Lambda function, defining the permissions it has to access other AWS resources.
    - <ins>Triggers</ins>: These are events or conditions that cause a Lambda function to execute. Triggers can be AWS services, HTTP requests, schedule-based, or custom events.
    - <ins>Concurrency</ins>: The number of invocations of your function that can run simultaneously. Lambda manages concurrency to ensure that your function scales according to demand.

- How does Lambda fit-in/replace an on-premises setting?
    - <ins>Eliminating Infrastructure Management</ins>: No need for physical/virtual servers.
    - <ins>Cost Efficiency</ins>: Pay only for actual compute time, avoiding idle resource costs.
    - <ins>Automatic Scalability</ins>: Scales seamlessly with incoming requests, unlike on-premises systems that may struggle with sudden spikes.
    - <ins>Accelerated Development</ins>: Swift deployment without managing infrastructure, speeding up development cycles.
    - <ins>Reliability and High Availability</ins>: Operates across multiple avialability zones, ensuring reliability without the need for extensive on-premises redundancy.

- How can I combine Lambda with other services?
    - <ins>S3</ins>: Trigger Lambda functions whenever a file is uploaded, modified, or deleted in an S3 bucket. 
    - <ins>DynamoDB</ins>: React to changes in a DynamoDB table.
    - <ins> CloudWatch Events/Logs</ins>: Respond to event or log data in CloudWatch.
    - <ins>RDS/Aurora</ins>: Perform database operations by triggering Lambda functions in response to changes in Amazon RDS or Aurora databases.

**<ins>Practice</ins>**

<ins>Create a Lambda function with the console</ins>

- Create function

![lambda](/06_AWS_3/includes/04_lambda2-1.png)

- Modify the code in console

```json
import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    
    # Get the length and width parameters from the event object. The 
    # runtime converts the event object to a Python dictionary
    length=event['length']
    width=event['width']
    
    area = calculate_area(length, width)
    print(f"The area is {area}")
        
    logger.info(f"CloudWatch logs group: {context.log_group_name}")
    
    # return the calculated area as a JSON string
    data = {"area": area}
    return json.dumps(data)
    
def calculate_area(length, width):
    return length*width
```

![lambda](/06_AWS_3/includes/04_lambda2-2.png)

- Create test event.

```json
{
  "length": 6,
  "width": 7
}
```

![lambda](/06_AWS_3/includes/04_lambda2-3.png)

- Test function.

![lambda](/06_AWS_3/includes/04_lambda2-4.png)

- View function's invocation records in CloudWatch Logs.

![lambda](/06_AWS_3/includes/04_lambda2-5.png)