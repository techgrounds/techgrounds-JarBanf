#!/bin/bash
# perform a quick software update on instance
sudo dnf update -y
# install the latest versions of Apache web server and PHP packages for AL2023
sudo dnf install -y httpd wget php-fpm php-mysqli php-json php php-devel
# get lab files from local S3 bucket for load testing
sudo aws s3 cp s3://cdkbucket-forwebserver-121212/ /var/www/html/ --recursive
# start the Apache web server
sudo systemctl start httpd
# configure the Apache web server to start at each system boot
sudo systemctl enable httpd
# Enable TLS/SSL support, mod_ssl also automatically creates a self-signed certificate.
sudo dnf install mod_ssl -y
# Fully restart Apache
sudo systemctl restart httpd.service