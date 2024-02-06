#!/bin/bash
# perform a quick software update on instance
sudo dnf update -y
# install the latest versions of Apache web server and PHP packages for AL2023
sudo dnf install -y httpd wget php-fpm php-mysqli php-json php php-devel
# download lab files for load testing
wget https://aws-tc-largeobjects.s3.amazonaws.com/CUR-TF-100-RESTRT-1/80-lab-vpc-web-server/lab-app.zip
# unzip files to html directory
sudo unzip lab-app.zip -d /var/www/html/
# start the Apache web server
sudo systemctl start httpd
# configure the Apache web server to start at each system boot
sudo systemctl enable httpd