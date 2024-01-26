#!/bin/bash
sudo yum install -y httpd
sudo systemctl start httpd
sudo systemctl enable httpd
sudo su
echo '<h1>Hello From Jared's CDK created Web Server!</h1>' > /var/www/html/index.html