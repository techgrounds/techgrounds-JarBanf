# ELB & Auto Scaling
[Geef een korte beschrijving van het onderwerp]

## Key-terms
[Schrijf hier een lijst met belangrijke termen met eventueel een korte uitleg.]

## Assignment

<ins>Exercise 1</ins>

- Launch an EC2 instance with the following requirements:
    - Region: Frankfurt (eu-central-1)
    - AMI: Amazon Linux 2
    - Type: t3.micro
    - User data:

    ```bash
    #!/bin/bash
    # Install Apache Web Server and PHP
    yum install -y httpd mysql php unzip
    # Download Lab files
    wget https://aws-tc-largeobjects.s3.amazonaws.com/CUR-TF-100-RESTRT-1/80-lab-vpc-web-server/lab-app.zip
    unzip lab-app.zip -d /var/www/html/
    # Turn on web server
    chkconfig httpd on
    service httpd start
    ```
    - Security Group: Allow HTTP
- Wait for the status checks to pass.
- Create an AMI from your instance with the following requirements:
    - Image name: Web server AMI

### Used sources
[Plaats hier de bronnen die je hebt gebruikt.]

### Encountered problems
[Geef een korte beschrijving van de problemen waar je tegenaan bent gelopen met je gevonden oplossing.]

### Result
[Omschrijf hoe je weet dat je opdracht gelukt is (gebruik screenshots waar nodig).]