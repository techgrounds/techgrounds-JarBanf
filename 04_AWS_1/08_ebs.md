# EBS
Amazon Elastic Block Storage (EBS) provides block level storage volumes for use with EC2 instances. EBS volumes behave like raw, unformatted block devices. You can mount these volumes as devices on your instances. EBS volumes that are attached to an instance are exposed as storage volumes that persist independently from the life of instance. You can create a file system on top of these volumes, or use them in any way you would use a block device (such as a hard drive). You can dynamically change the configuration of a volume attached to an instance.

Amazon EBS is recommended for data that must be quickly accesible and requires long-term persistence. EBS volumes are particularly well-suited for use as the primary storage for file systems, databases, or for any applications that require fine granular updates and access to raw, unformatted, block-level storage. Amazon EBS is well suited to both database-style applications that rely on random reads and writes, and to throughput-intensive applications that perform long, continuous reads and writes.

## Key-terms

## Assignment

<ins>Exercise 1:</ins>
- Navigate to the EC2 menu.
- Create a t2.micro Amazon Linux 2 machine with all the default settings.
- Create a new EBS volume with the following requirements:
    - Volume type: General Purpose SSD (gp3)
    - Size: 1 GiB
    - Availability Zone: same as your EC2
- Wait for its state to be available.

<ins>Exercise 2:</ins>
- Attach your new EBS volume to your EC2 instance.
- Connect to your EC2 instance using SSH.
- Mount the EBS volume on your instance.
- Create a text file and write it to the mounted EBS volume.

<ins>Exercise 3:</ins>
- Create a snapshot of your EBS volume.
- Remove the text file from your original EBS volume.
- Create a new volume using your snapshot.
- Detach your original EBS volume.
- Attach the new volume to your EC2 and mount it.
- Find your text file on the new EBS volume.

### Used sources
- [Amazon Elastic Block Store (Amazon EBS)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AmazonEBS.html)
- [Create an Amazon EBS volume](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-creating-volume.html)
- [Attach an Amazon EBS volume to an instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-attaching-volume.html)
- [Make an Amazon EBS volume available for use on Linux](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-using-volumes.html)

### Encountered problems


### Result

**<ins>Exercise 1:</ins>**

**- Create a t2.micro Amazon Linux 2 machine with all the default settings.**

![create instance](/04_AWS_1/images/08_ebs1-1.png)<br><br>

**- Create a new EBS volume with the following requirements: Volume type: General Purpose SSD (gp3), Size: 1 GiB, Availability Zone: same as your EC2**

![create volume](/04_AWS_1/images/08_ebs1-2.png)<br><br>

**<ins>Exercise 2:</ins>**

**- Attach your new EBS volume to your EC2 instance.**

![attach ebs to instance](/04_AWS_1/images/08_ebs2-1.png)<br><br>

**- Connect to your EC2 instance using SSH.**

```bash
ssh -i /Users/Jared/Desktop/mytestkeypair.pem ec2-user@ec2-3-120-190-177.eu-central-1.compute.amazonaws.com
```

![connect to instance](/04_AWS_1/images/08_ebs2-2.png)<br><br>

**- Mount the EBS volume on your instance.**

1. View available disks devices and their mount points te help determine the correct device name to use.

    ```bash
    lsblk
    ```
    
    and

    ```bash
    lsblk -f
    ```

    The device `xvda` has one partition named `xvda1` using the XFS file system and is mounted.  
    The device `xvdf` has no partitions, no file system, and is not yet mounted.

![view available disks](/04_AWS_1/images/08_ebs2-3-1.png)<br><br>

2. Use the `mkfs -t` command to create a file system on the `xvdf` volume.

    ```bash
    sudo mkfs -t xfs /dev/xvdf
    ```

![create file system](/04_AWS_1/images/08_ebs2-3-2.png)<br><br>

3. Use the `mkdir` command to create a mount point directory for the `/dev/xvdf` volume. The moint point is where the volume is located in the file system tree and where you read and write files to after you mount the volume. The following command creates a directory named `/data`.

    ```bash
    sudo mkdir /data
    ```
4. Mount the `/dev/xvdf` volume at the `/data` mount point directory I created in the previous step.

    ```bash
    sudo mount /dev/xvdf /data
    ```
5. Check if `/dev/xvdf` volume has a file system, and is mounted correctly.

    ```bash
    lsblk -f
    ```
![check volume](/04_AWS_1/images/08_ebs2-3-5.png)<br><br>

6. Review the file permissions of the new volume mount to make sure that users and applications can write to the volume.

    ```bash
    sudo ls -l / | grep data
    ```

    ```bash
    sudo chown ec2-user /data
    ```

![review permission](/04_AWS_1/images/08_ebs2-3-6.png)<br><br>

7. <ins>The mount point is not automatically preserved after rebooting your instance.</ins>

**- Create a text file and write it to the mounted EBS volume.**

```bash
echo 'This is a test textfile' > /data/test.txt
```

![review permission](/04_AWS_1/images/08_ebs2-4.png)<br><br>

**<ins>Exercise 3:</ins>**