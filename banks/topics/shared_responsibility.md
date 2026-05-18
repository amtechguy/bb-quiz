# 📚 AWS Shared Responsibility Model

> **Study Resources for this Topic:**
>
> - 📖 **Official AWS Docs:** [https://aws.amazon.com/compliance/shared-responsibility-model/](https://aws.amazon.com/compliance/shared-responsibility-model/)
> - 🎬 **YouTube Overview:** [https://www.youtube.com/watch?v=tIb5PGW_t1o](https://www.youtube.com/watch?v=tIb5PGW_t1o)
> - 🎓 **AWS Skill Builder (Free):** [AWS Cloud Practitioner Essentials](https://explore.skillbuilder.aws/learn/course/external/view/elearning/134/aws-cloud-practitioner-essentials)
>
> 💡 **Quick Tip:** AWS = security OF the cloud (hardware, infrastructure). Customer = security IN the cloud (data, IAM, OS patching on EC2).

---

**1.** Question 902 An online retail company has seasonal sales spikes several times a year, primarily around holidays. Demand is lower at other times. The company finds it difficult to predict the increasing infrastructure demand for each season. Which advantages of moving to the AWS Cloud would MOST benefit the company? (Choose two.)
- A. Global footprint
- B. Elasticity ✅
- C. AWS service quotas
- D. AWS shared responsibility model
- E. Pay-as-you-go pricing ✅

---

**2.** Question 919 Which IT controls do AWS and the customer share, according to the AWS shared responsibility model? (Choose two.)
- A. Physical and environmental controls
- B. Patch management ✅
- C. Cloud awareness and training ✅
- D. Zone security
- E. Application data encryption

---

**3.** Question 938 Which tasks are the responsibility of AWS, according to the AWS shared responsibility model? (Choose two.)
- A. Patch the Amazon EC2 guest operating system.
- B. Upgrade the firmware of the network infrastructure. ✅
- C. Apply password rotation for IAM users.
- D. Maintain the physical security of edge locations. ✅
- E. Maintain least privilege access to the root user account.

---

**4.** Question 962 According to the AWS shared responsibility model, what responsibility does a customer have when using Amazon RDS to host a database?
- A. Manage connections to the database
- B. Install Microsoft SQL Server
- C. Design encryption-at-rest strategies
- D. Apply minor database patches ✅

---

**5.** Question 1209 Which task is a customer's responsibility, according to the AWS shared responsibility model?
- A. Management of the guest operating systems ✅
- B. Maintenance of the configuration of infrastructure devices
- C. Management of the host operating systems and virtualization
- D. Maintenance of the software that powers Availability Zones

---

**6.** Question 1226 A company is using Amazon DynamoDB for its application database. Which tasks are the responsibility of AWS, according to the AWS shared responsibility model? (Choose two.)
- A. Classify data.
- B. Configure access permissions.
- C. Manage encryption options.
- D. Provide public endpoints to store and retrieve data. ✅
- E. Manage the infrastructure layer and the operating system. ✅

---

**7.** Question 1239 A company has deployed an Amazon EC2 instance. Which option is an AWS responsibility under the AWS shared responsibility model?
- A. Managing and encrypting application data
- B. Installing updates and security patches of guest operating system
- C. Configuration of infrastructure devices ✅
- D. Configuration of security groups on each instance

---

**8.** Question 1242 Which maintenance task is the customer's responsibility, according to the AWS shared responsibility model?
- A. Physical connectivity among Availability Zones
- B. Network switch maintenance
- C. Hardware updates and firmware patches
- D. Amazon EC2 updates and security patches ✅

---

**9.** Question 1266 Which of the following is the customer's responsibility under the AWS shared responsibility model? (Choose two.)
- A. Maintain the configuration of infrastructure devices.
- B. Maintain patching and updates within the hardware infrastructure.
- C. Maintain the configuration of guest operating systems and applications. ✅
- D. Manage decisions involving encryption options. ✅
- E. Maintain infrastructure hardware.

---

**10.** Question 1277 According to the AWS shared responsibility model, the customer is responsible for applying the latest security updates and patches for which of the following?
- A. Amazon DynamoDB
- B. Amazon EC2 instances ✅
- C. Amazon RDS instances
- D. Amazon S3

---

**11.** Question 1281 Who is responsible for managing IAM user access and secret keys according to the AWS shared responsibility model?
- A. IAM access and secret keys are static, so there is no need to rotate them.
- B. The customer is responsible for rotating keys. ✅
- C. AWS will rotate the keys whenever required.
- D. The AWS Support team will rotate keys when requested by the customer.

---

**12.** Question 1284 Which of the following is entirely the responsibility of AWS, according to the AWS shared responsibility model?
- A. Security awareness and training
- B. Development of an IAM password policy
- C. Patching of the guest operating system
- D. Physical and environmental controls ✅

---

**13.** Question 1318 Which task is a responsibility of AWS, according to the AWS shared responsibility model?
- A. Encryption of application data
- B. Authentication of application users
- C. Protection of physical network infrastructure ✅
- D. Configuration of firewalls

---

**14.** Question 403 Which statements represent the cost-effectiveness of the AWS Cloud? (Choose two.)
- A. Users can trade fixed expenses for variable expenses. ✅
- B. Users can deploy all over the world in minutes.
- C. AWS offers increased speed and agility.
- D. AWS is responsible for patching the infrastructure.
- E. Users benefit from economies of scale. ✅

---

**15.** Question 434 A company wants to build an application that uses AWS Lambda to run Python code. Under the AWS shared responsibility model, which tasks will be the company's responsibility? (Choose two.)
- A. Management of the underlying infrastructure.
- B. Management of the operating system.
- C. Writing the business logic code. ✅
- D. Installation of the computer language runtime.
- E. Providing AWS Identity and Access Management (IAM) access to the Lambda service. ✅

---

**16.** Question 437 What does "security of the cloud" refer to in the AWS shared responsibility model?
- A. Availability of AWS services such as Amazon EC2
- B. Security of the cloud infrastructure that runs all the AWS services ✅
- C. Implementation of password policies for IAM users
- D. Security of customer environments by using AWS Network Firewall partners

---

**17.** Question 475 A company uses Amazon WorkSpaces. Which task is the responsibility of AWS, according to the AWS shared responsibility model?
- A. Set up multi-factor authentication (MFA) for each WorkSpaces user account. ✅
- B. Ensure the environmental safety and security of the AWS infrastructure that hosts WorkSpaces.
- C. Provide security for WorkSpaces user accounts through AWS Identity and Access Management (IAM).
- D. Configure AWS CloudTrail to log API calls and user activity.

---

**18.** Question 483 Which option is AWS responsible for under the AWS shared responsibility model?
- A. Network and firewall configuration
- B. Client-side data encryption
- C. Management of user permissions
- D. Hardware and infrastructure ✅

---

**19.** Question 497 According to the AWS shared responsibility model, which task is the customer's responsibility?
- A. Maintaining the infrastructure needed to run AWS Lambda
- B. Updating the operating system of Amazon DynamoDB instances
- C. Maintaining Amazon S3 infrastructure
- D. Updating the guest operating system on Amazon EC2 instances ✅

---

**20.** Question 498 A company is learning about its responsibilities that are related to the management of Amazon EC2 instances. Which tasks for EC2 instances are the company's responsibility, according to the AWS shared responsibility model? (Choose two.)
- A. Install and patch the machine hypervisor.
- B. Patch the guest operating system. ✅
- C. Encrypt data at rest on associated storage. ✅
- D. Install the physical hardware and cabling.
- E. Provide physical security for the EC2 instances.

---

**21.** Question 511 Which task is the responsibility of the customer, according to the AWS shared responsibility model?
- A. Patch the Amazon DynamoDB operating system.
- B. Secure Amazon CloudFront edge locations by allowing physical access according to the principle of least
- C. Protect the hardware that runs AWS services.
- D. Use AWS Identity and Access Management (IAM) according to the principle of least privilege. ✅

---

**22.** Question 535 Which task is the customer's responsibility, according to the AWS shared responsibility model?
- A. Patch a guest operating system that is deployed on an Amazon EC2 instance. ✅
- B. Control physical access to an AWS data center.
- C. Control access to AWS underlying hardware.
- D. Patch a host operating system that is deployed on Amazon S3.

---

**23.** Question 544 According to the AWS shared responsibility model, which of the following are AWS responsibilities? (Choose two.)
- A. Network infrastructure and virtualization of infrastructure ✅
- B. Security of application data
- C. Guest operating systems
- D. Physical security of hardware ✅
- E. Credentials and policies

---

**24.** Question 545 A company uses Amazon Aurora as its database service. The company wants to encrypt its databases and database backups. Which party manages the encryption of the database clusters and database snapshots, according to the AWS shared responsibility model?
- A. AWS ✅
- B. The company
- C. AWS Marketplace partners
- D. Third-party partners

---

**25.** A company is using Amazon RDS. Which task is the company's responsibility, according to the AWS shared responsibility model?

- A. Apply encryption options for the database ✅
- B. Manage the underlying server hardware on which Amazon RDS runs.
- C. Apply patches to the underlying operating system.
- D. Apply minor patches to the database.

**Explanation:** Customers are responsible for enabling and configuring encryption options for their RDS databases. AWS manages the hardware, OS patching, and handles minor database patches.

---

**26.** A company is using Amazon EC2 instances. Which tasks are the company's responsibility, according to the AWS shared responsibility model? (Choose two.)

- A. Maintain the network infrastructure.
- B. Patch the guest operating system ✅
- C. Configure a security group on deployed EC2 instances ✅
- D. Provide physical security for the underlying hardware of the EC2 instances.
- E. Manage the underlying hypervisor.

---

**27.** Which task is the shared responsibility of the customer and AWS under the AWS shared responsibility model?

- A. Installing hardware infrastructure
- B. Managing security ✅
- C. Managing guest operating systems
- D. Protecting the physical infrastructure that runs all services

---

**28.** Which Amazon RDS management task is the customer's responsibility under the AWS shared responsibility model?

- A. Configuring network access to Amazon RDS ✅
- B. Configuring physical security controls for Amazon RDS
- C. Managing Amazon RDS infrastructure
- D. Patching and updating Amazon RDS host operating systems

---

**29.** Which task is AWS NOT responsible for in the shared responsibility model? (Select TWO)
- A. Granting access to individuals and services. ✅
- B. Ensuring datacenter security.
- C. Updating Amazon EC2 host firmware.
- D. Updating operating systems of user EC2 instances ✅
**Explanation:** Under the shared responsibility model, AWS manages the underlying infrastructure. Customers are responsible for managing access permissions and patching the operating systems running on their EC2 instances.

---

**30.** According to the AWS shared responsibility model what is the sole responsibility of AWS?
- A. Application security.
- B. Edge location management. ✅
- C. Patch management.
- D. Client-side data.
**Explanation:** AWS is solely responsible for managing and maintaining its global infrastructure including edge locations. Customers never need to worry about the physical hardware or facilities that power AWS services.

---

**31.** Which AWS feature will reduce the customer's total cost of ownership (TCO)?
- A. Shared responsibility security model.
- B. Single tenancy.
- C. Elastic computing. ✅
- D. Distributed Architecture.
**Explanation:** Elastic computing lets you scale resources up and down based on demand, so you only pay for what you use. This eliminates the need to over-provision for peak loads, directly reducing TCO.

---

**32.** Under the AWS shared responsibility model, which of the following are the customer's responsibility? (Select TWO)
- A. Patching operating system components for EC2 running PostgreSQL Databases ✅
- B. Encrypting data on the client-side. ✅
- C. Training the data center staff.
- D. Configuring Hardware firewall appliances
- E. Maintaining environmental controls within a data center.
**Explanation:** Customers are responsible for patching their EC2 operating systems and encrypting their own data. AWS handles the physical infrastructure including hardware firewalls, data center staff, and environmental controls.

---

**33.** Under the shared responsibility model, which of the following is a shared control? (Select TWO)
- A. Physical controls.
- B. Patch management. ✅
- C. Zone security.
- D. Data center auditing. ✅
**Explanation:** Patch management is shared because AWS patches infrastructure while customers patch their OS and applications. Auditing is shared because both AWS and customers maintain audit processes for their respective areas.

---

**34.** What is the AWS customer responsible for according to the AWS shared responsibility model?
- A. Physical access controls.
- B. Data encryption. ✅
- C. Secure disposal of storage devices.
- D. Environmental risk management.
**Explanation:** Customers are responsible for encrypting their own data both at rest and in transit. AWS handles physical security, hardware disposal, and environmental controls in its data centers.

---

**35.** Under the shared responsibility model, which of the following is the customer NOT responsible for? (Select TWO)
- A. Ensuring that data is encrypted at rest.
- B. Ensuring that firmware is updated on hardware devices. ✅
- C. Ensuring Lambda functions are written with correct syntax.
- D. Ensuring that network cables are category six or higher. ✅
**Explanation:** AWS is solely responsible for maintaining physical hardware including firmware updates and physical network infrastructure like cables. Customers are responsible for their data encryption and application code.

---

**36.** Which activity is a customer responsibility in the AWS Cloud according to the AWS shared responsibility model?
- A. Patching and fixing flaws within the AWS Cloud infrastructure.
- B. Ensuring network connectivity from AWS to the internet.
- C. Ensuring the physical security of cloud data centers.
- D. Ensuring Amazon EBS volumes are backed up. ✅
**Explanation:** Backing up EBS volumes is the customer's responsibility. AWS provides the tools like snapshots but customers must configure and manage their own backup strategy. AWS handles physical infrastructure and network connectivity.

---

**37.** According to the AWS Shared responsibility model, which of the following are the responsibility of the customer? (Choose TWO)

- A. Protecting the confidentiality of data in transit in Amazon S3. ✅
- B. Controlling physical access to AWS Regions.
- C. Ensuring that the underlying EC2 host is configured properly.
- D. Patching applications installed on Amazon EC2. ✅
- E. Managing environmental events of AWS data centers.

**Explanation:** Customers are responsible for security IN the cloud: encrypting data in transit, managing their own applications, and patching OS and software on EC2 instances. AWS is responsible for the physical infrastructure.

---

**38.** A user is planning to migrate an application workload to the AWS Cloud. Which control becomes the responsibility of AWS once the migration is complete?

- A. Patching the guest operating system
- B. Maintaining physical and environmental controls ✅
- C. Protecting communications and maintaining zone security
- D. Patching specific applications

**Explanation:** Under the AWS Shared Responsibility Model, AWS is always responsible for the physical infrastructure including data center security, environmental controls (power, cooling), and hardware maintenance.

---

**39.** Which of the following is the customer's responsibility when using Amazon RDS?

- A. Patching the operating system of underlying hardware
- B. Controlling traffic to and from the database through security groups ✅
- C. Running backups that enable point-in-time recovery of a DB instance
- D. Replacing failed DB instances

**Explanation:** Under the shared responsibility model for RDS, AWS manages the underlying infrastructure, OS patching, backups, and hardware replacement. Customers are responsible for network access controls such as configuring security groups.

---

**40.** What is the customer's responsibility when using AWS Lambda?

- A. Operating system configuration
- B. Application management ✅
- C. Platform management
- D. Code encryption

**Explanation:** With AWS Lambda, AWS manages the infrastructure, OS, runtime, and scaling. The customer is responsible for the application code itself — its logic, dependencies, and correct functioning.

---

**41.** Which of the following tasks is the responsibility of AWS?

- A. Encrypting client-side data
- B. Configuring AWS Identity and Access Management (IAM) roles
- C. Securing the Amazon EC2 hypervisor ✅
- D. Setting user password policies

**Explanation:** Under the shared responsibility model, AWS is responsible for the security OF the cloud, including the hypervisor layer that underlies EC2 instances. Customers are responsible for configurations made on top of it.

---

**42.** Under the shared responsibility model, which of the following is a shared control between a customer and AWS?

- A. Physical controls
- B. Patch management ✅
- C. Zone security
- D. Data center auditing

**Explanation:** Patch management is a shared responsibility. AWS patches the underlying infrastructure and managed service components, while customers are responsible for patching their own operating systems and applications running on EC2.

---

**43.** Under the shared responsibility model, which of the following tasks are the responsibility of the AWS customer? (Select TWO.)

- A. Ensuring that application data is encrypted at rest ✅
- B. Ensuring that AWS NTP servers are set to the correct time
- C. Ensuring that users have received security training in the use of AWS services ✅
- D. Ensuring that access to data centers is restricted
- E. Ensuring that hardware is disposed of properly

**Explanation:** Customers are responsible for encrypting their own data and for training their users on security awareness. Physical data center access, hardware disposal, and NTP servers are all AWS responsibilities.

---

**44.** Which of the following is entirely the responsibility of AWS, according to the AWS shared responsibility model?

- A. Patching of the guest operating system
- B. Security awareness and training
- C. Physical and environmental controls ✅
- D. Development of an IAM password policy

**Explanation:** AWS is solely responsible for the physical infrastructure, including data center security, environmental controls (power, cooling, fire suppression), and hardware maintenance. Customers are never responsible for these.

---

**45.** As part of the AWS shared responsibility model, which of the following operational controls do users fully inherit from AWS?

- A. Security management of data center ✅
- B. Patch management
- C. Configuration management
- D. User and access management

**Explanation:** Physical data center security is entirely AWS's responsibility. Customers fully inherit this control and never need to manage physical access, surveillance, or environmental security of AWS facilities.

---

**46.** Under the shared responsibility model, which of the following tasks are the responsibility of the customer? (Choose two.)

- A. Maintaining the underlying Amazon EC2 hardware.
- B. Managing the VPC network access control lists. ✅
- C. Encrypting data in transit and at rest. ✅
- D. Replacing failed hard disk drives.
- E. Deploying hardware in different Availability Zones.

**Explanation:** Customers are responsible for configuring VPC network ACLs to control traffic, and for encrypting their own data at rest and in transit. Physical hardware management and maintenance are AWS responsibilities.

---

**47.** According to the AWS shared responsibility model, what is AWS responsible for?

- A. Configuring Amazon VPC
- B. Managing application code
- C. Maintaining application traffic
- D. Providing Security for Data Centers ✅

**Explanation:** AWS is responsible for the security OF the cloud, which includes protecting the physical infrastructure — data centers, hardware, networking, and facilities. VPC configuration, application code, and traffic management are customer responsibilities.

---

**48.** Which of the following is the responsibility of AWS?

- A. Setting up AWS Identity and Access Management (IAM) users and groups
- B. Physically destroying storage media at end of life ✅
- C. Patching guest operating systems

**Explanation:** AWS is responsible for decommissioning and destroying physical storage media at the end of its life, following industry standards. IAM configuration and guest OS patching are the customer's responsibility.

---

**49.** Under the shared responsibility model, which of the following areas are the customer's responsibility? (Choose two.)

- A. Firmware upgrades of network infrastructure
- B. Patching of operating systems ✅
- C. Patching of the underlying hypervisor
- D. Patching software applications installed on EC2 Instances ✅

**Explanation:** Customers are responsible for patching the guest operating systems and any software they install on EC2 instances. Firmware upgrades and hypervisor patching are AWS responsibilities as part of the underlying infrastructure.

---

**50.** According to the AWS shared responsibility model, who is responsible for configuration management?

- A. It is solely the responsibility of the customer.
- B. It is solely the responsibility of AWS.
- C. It is shared between AWS and the customer. ✅

**Explanation:** Configuration management is a shared responsibility. AWS configures and manages the underlying infrastructure components, while customers are responsible for configuring the services, operating systems, and applications they deploy.

---

**51.** Which of the following are benefits of hosting infrastructure in the AWS Cloud? (Choose two.)

- A. There are no upfront commitments. ✅
- B. AWS manages all security in the cloud.
- C. Users have the ability to provision resources on demand. ✅
- D. Storage cost is for free

**Explanation:** AWS allows you to start using services with no upfront hardware investment, and you can provision resources on demand in minutes. AWS does not manage all security — customers are responsible for their portion under the shared responsibility model.

---

**52.** Under the AWS shared responsibility model, AWS is responsible for which security-related tasks? (Choose 2)

- A. Lifecycle management of IAM credentials
- B. Physical security of global infrastructure ✅
- C. Encryption of Amazon EBS volumes
- D. Updating Security of Hypervisors and Host Hardware ✅

**Explanation:** AWS is responsible for the physical security of its global infrastructure and for maintaining the security of the hypervisor and underlying host hardware. IAM credential management and EBS encryption are customer responsibilities.

---

**53.** Which statement is true regarding the AWS Shared Responsibility Model?
- A. Responsibilities vary depending on the services used. ✅
- B. Security of the IaaS services is the responsibility of AWS.
- C. Patching the guest OS is always the responsibility of AWS.
- D. Security of the managed services is the responsibility of the customer.

---

**54.** Which of the following are examples of AWS-Managed Services, where AWS is responsible for the operational and maintenance burdens of running the service? (Choose TWO)
- A. Amazon VPC.
- B. Amazon DynamoDB. ✅
- C. Amazon Elastic MapReduce. ✅
- D. AWS IAM.
- E. Amazon Elastic Compute Cloud.

---

**55.** Under the shared responsibility model, which of the following is the responsibility of AWS?
- A. Client-side encryption.
- B. Configuring infrastructure devices. ✅
- C. Server-side encryption.
- D. Filtering traffic with Security Groups.

---

**56.** In the AWS Shared responsibility Model, which of the following are the responsibility of the customer? (Choose TWO)
- A. Disk disposal.
- B. Controlling physical access to compute resources.
- C. Patching the Network infrastructure.
- D. Setting password complexity rules. ✅
- E. Configuring network access rules. ✅

---

**57.** Which of the following is the customer’s responsibility under the AWS shared responsibility model?
- A. Patching underlying infrastructure
- B. Physical security
- C. Patching Amazon EC2 instances ✅
- D. Patching network infrastructure

---

**58.** According to the AWS shared responsibility model who is responsible for configuration management?
- A. It is solely the responsibility of the customer.
- B. It is solely the responsibility of AWS.
- C. It is shared between AWS and the customer. ✅
- D. It is not part of the AWS shared responsibility model.

---

**59.** Under the shared responsibility model, which of the following tasks are the responsibility of the AWS customer? (Select TWO)
- A. Ensuring that application data is encrypted at rest. ✅
- B. Ensuring that AWS NTP servers are set to the correct time.
- C. Ensuring that users have received security training in the use of AWS services. ✅
- D. Ensuring that access to data centers is restricted.
- E. Ensuring that hardware is disposed of properly.

---

**60.** Under the shared responsibility model, which of the following is the customer responsible for?
- A. Ensuring that disk drives are wiped after use.
- B. Ensuring that firmware is updated on hardware devices.
- C. Ensuring that data is encrypted at rest. ✅
- D. Ensuring that network cables are category six or higher.

---

**61.** Which activity is a customer responsibility in the AWS Cloud according to the AWS shared responsibility model?
- A. Ensuring network connectivity from AWS to the internet.
- B. Patching and fixing flaws within the AWS Cloud infrastructure.
- C. Ensuring the physical security of cloud data centers.
- D. Ensuring Amazon EBS volumes are backed up. ✅

---

**62.** What is a value proposition of the AWS Cloud?
- A. AWS is responsible for security in the AWS Cloud.
- B. No long-term contract is required. ✅
- C. Provision new servers in days.
- D. AWS manages user applications in the AWS Cloud.

---

**63.** Under the shared responsibility model which of the following areas are the customer’s responsibility? (Select TWO)
- A. Firmware upgrades of network infrastructure.
- B. Patching of operating systems. ✅
- C. Patching of the underlying hypervisor.
- D. Physical security of data centers.
- E. Configuration of the security group. ✅

---

**64.** According to the AWS Shared responsibility model, which of the following are the responsibility of the customer? (Choose TWO)
- A. Managing environmental events of AWS data centers.
- B. Protecting the confidentiality of data in transit in Amazon S3. ✅
- C. Controlling physical access to AWS Regions.
- D. Ensuring that the underlying EC2 host is configured properly.
- E. Patching applications installed on Amazon EC2. ✅

---

**65.** Based on the AWS Shared Responsibility Model, which of the following are the sole responsibility of AWS? (Choose TWO)
- A. Monitoring network performance.
- B. Installing software on EC2 instances.
- C. Creating hypervisors. ✅
- D. Configuring Access Control Lists (ACLs).
- E. Hardware maintenance. ✅

---

**66.** Using Amazon RDS falls under the shared responsibility model. Which of the following are customer responsibilities? (Choose TWO)
- A. Building the relational database schema. ✅
- B. Performing backups.
- C. Managing the database settings. ✅
- D. Patching the database software.
- E. Installing the database software.

---

**67.** Under the Shared Responsibility Model, which of the following controls do customers fully inherit from AWS? (Choose TWO)
- A. Patch management controls.
- B. Database controls.
- C. Awareness & Training.
- D. Environmental controls. ✅
- E. Physical controls. ✅

---

**68.** Which of the below options is true of Amazon VPC?
- A. Amazon VPC allows customers to control user interactions with all other AWS resources.
- B. AWS Customers have complete control over their Amazon VPC virtual networking environment. ✅
- C. AWS is responsible for all the management and configuration details of Amazon VPC.
- D. Amazon VPC helps customers to review their AWS architecture and adopt best practices.

---

**69.** Which of the following is the responsibility of AWS according to the AWS Shared Responsibility Model?
- A. Securing regions and edge locations. ✅
- B. Performing auditing tasks.
- C. Monitoring AWS resources usage.
- D. Securing access to AWS resources.

---

**70.** Who is responsible for scaling a DynamoDB database in the AWS Shared Responsibility Model?
- A. Your security team.
- B. Your development team.
- C. AWS. ✅
- D. Your internal DevOps team.

---

**71.** According to the AWS shared responsibility model, what are the controls that customers fully inherit from AWS? (Choose TWO)
- A. Awareness and Training.
- B. Communications controls.
- C. Data center security controls. ✅
- D. Environmental controls. ✅
- E. Resource Configuration Management.

---

**72.** Which statement is true in relation to security in AWS?
- A. AWS manages everything related to EC2 operating systems.
- B. AWS customers are responsible for patching any database software running on Amazon EC2. ✅
- C. Server side encryption is the responsibility of AWS.
- D. AWS is responsible for the security of your application.

---

**73.** According to the AWS shared responsibility model what is the sole responsibility of AWS?
- A. Application security.
- B. Edge location management. ✅
- C. Patch management.
- D. Client-side data.

---

**74.** Which AWS feature will reduce the customer’s total cost of ownership (TCO)?
- A. Shared responsibility security model.
- B. Single tenancy.
- C. Elastic computing. ✅
- D. Encryption.

---

**75.** Under the AWS shared responsibility model, which of the following activities are the customer’s responsibility? (Select TWO)
- A. Patching operating system components for Amazon Relational Database Server (Amazon RDS).
- B. Encrypting data on the client-side. ✅
- C. Training the data center staff.
- D. Configuring Network Access Control Lists (ACL). ✅
- E. Maintaining environmental controls within a data center.

---

**76.** (Q990) Which task is a responsibility of AWS, according to the AWS shared responsibility model?
- A. Enable client-side encryption for objects that are stored in Amazon S3.
- B. Configure IAM security policies to comply with the principle of least privilege.
- C. Patch the guest operating system on an Amazon EC2 instance.
- D. Apply updates to the Nitro Hypervisor. ✅

---

**77.** (Q992) Which option is a shared responsibility between AWS and its customers under the AWS shared responsibility model?
- A. Configuration of Amazon EC2 instance operating systems
- B. Application file system server-side encryption
- C. Patch management ✅
- D. Security of the physical infrastructure

---

**78.** (Q996) Which of the following is the customer responsible for updating and patching, according to the AWS shared responsibility model?
- A. Amazon FSx for Windows File Server
- B. Amazon WorkSpaces virtual Windows desktop ✅
- C. AWS Directory Service for Microsoft Active Directory
- D. Amazon RDS for Microsoft SQL Server

---

**79.** (Q1063) A company is using Amazon DynamoDB. Which task is the companys responsibility, according to the AWS shared responsibility model?
- A. Patch the operating system.
- B. Provision hosts.
- C. Manage database access permissions. ✅
- D. Secure the operating system.

---

**80.** (Q1073) What is a customer responsibility when using AWS Lambda according to the AWS shared responsibility model? mn
- A. Managing the code within the Lambda function ✅
- B. Confirming that the hardware is working in the data center
- C. Patching the operating system
- D. Shutting down Lambda functions when they are no longer in use

---

**81.** (Q1084) Which tasks are customer responsibilities, according to the AWS shared responsibility model? (Choose two.)
- A. Configure the AWS provided security group firewall. ✅
- B. Classify company assets in the AWS Cloud. ✅
- C. Determine which Availability Zones to use for Amazon S3 buckets.
- D. Patch or upgrade Amazon DynamoDB.
- E. Select Amazon EC2 instances to run AWS Lambda on.

---

**82.** (Q1108) Which option is a customer responsibility when using Amazon DynamoDB under the AWS Shared Responsibility Model? am
- A. Physical security of DynamoDB
- B. Patching of DynamoDB
- C. Access to DynamoDB tables ✅
- D. Encryption of data at rest in DynamoDB

---

**83.** (Q1115) According to security best practices, how should an Amazon EC2 instance be given access to an Amazon S3 bucket? the file. keys, then upload the file. 138. 1116# A company needs to evaluate its AWS environment and provide best practice recommendations in five categories: cost, performance, service limits, fault tolerance and security. Which AWS service can the company use to meet these requirements? 139. 1117# Which tasks are the customer's responsibility, according to the AWS shared responsibility model? (Choose two.) 140. 1117# Which tasks are the customer's responsibility, according to the AWS shared responsibility model? (Choose two.) : panes sto 141. 1118# How does AWS Cloud computing help businesses reduce costs? (Choose two.) more than 1 week. internet. 142. 1119# A company wants to establish a schedule for rotating database user credentials. Which AWS service will support this requirement with the LEAST amount of operational overhead? 143. 1120# Which task is the customer's responsibility, according to the AWS shared responsibility model? . 144. 1120# Which task is the customers responsibility, according to the AWS shared responsibility model? . 145. 1121# A company has a set of ecommerce applications. The applications need to be able to send messages to each other. Which AWS service meets this requirement? . 146. 1122# A company wants to manage its AWS Cloud resources through a web interface. Which AWS service will meet this requirement? : 147. 1123# A company is assessing its AWS Business Support plan to determine if the plan still meets the companys needs. The company is considering switching to AWS Enterprise Support. \ Which additional benefit will the company receive with AWS Enterprise Support? day, 7 days a week monitoring and optimization applications 148. 1124# Which pricing model will interrupt a running Amazon EC2 instance if capacity becomes temporarily unavailable? . 149. 1124# Which pricing model will interrupt a running Amazon EC2 instance if capacity becomes temporarily unavailable?
- A. Hard code an IAM users secret key and access key directly in the application, and upload
- B. Store the IAM users secret key and access key in a text file on the EC2 instance, read the
- C. Have the EC2 instance assume a role to obtain the privileges to upload the file. ✅
- D. Modify the S3 bucket policy so that any service can upload to it at any time.
- A. AWS Shield
- B. AWS WAF
- C. AWS Trusted Advisor ✅
- D. AWS Service Catalog
- A. Establish the global infrastructure.
- B. Perform client-side data encryption.
- C. Configure IAM credentials. ✅
- D. Secure edge locations.
- E. Patch Amazon RDS DB instances.
- A. Establish the global infrastructure.
- B. Perform client-side data encryption.
- C. Configure IAM credentials. ✅
- D. Secure edge locations.
- E. Patch Amazon RDS DB instances.
- A. AWS charges the same prices for services in every AWS Region.
- B. AWS enables capacity to be adjusted on demand.
- C. AWS offers discounts for Amazon EC2 instances that remain idle for ✅
- D. AWS does not charge for data sent from the AWS Cloud to the
- E. AWS eliminates many of the costs of building and maintaining onpremises data centers.
- A. AWS Systems Manager
- B. AWS Secrets Manager
- C. AWS License Manager ✅
- D. AWS Managed Services
- A. Maintain the security of the AWS Cloud.
- B. Configure firewalls and networks.
- C. Patch the operating system of Amazon RDS instances. ✅
- D. Implement physical and environmental controls
- A. Maintain the security of the AWS Cloud.
- B. Configure firewalls and networks.
- C. Patch the operating system of Amazon RDS instances. ✅
- D. Implement physical and environmental controls
- A. AWS Auto Scaling
- B. Elastic Load Balancing
- C. Amazon Simple Queue Service (Amazon SQS) ✅
- D. Amazon Kinesis Data Streams
- A. AWS Management Console
- B. AWS CLI
- C. AWS SDK ✅
- D. AWS Cloud9
- A. A full set of AWS Trusted Advisor checks
- B. Phone, email, and chat access to cloud support engineers 24 hours a
- C. A designated technical account manager (TAM) to assist in ✅
- D. A consultative review and architecture guidance for the companys
- A. On-Demand Instances
- B. Standard Reserved Instances
- C. Spot Instances ✅
- D. Convertible Reserved Instances
- A. On-Demand Instances
- B. Standard Reserved Instances
- C. Spot Instances ✅
- D. Convertible Reserved Instances

---

**84.** (Q1134) Which option is a customer responsibility under the AWS shared responsibility model? f
- A. Maintenance of underlying hardware of Amazon EC2 instances
- B. Application data security ✅
- C. Physical security of data centers
- D. Maintenance of VPC components

---

**85.** (Q1144) A company needs to transfer data between an Amazon S3 bucket and an on-premises application. Who is responsible for the security of this data, according to the AWS shared responsibility model?
- A. The company ✅
- B. AWS
- C. Firewall vendor
- D. AWS

---

**86.** (Q1151) What is the customer ALWAYS responsible for managing, according to the AWS shared responsibility model?
- A. Software licenses
- B. Networking
- C. Customer data ✅
- D. Encryption keys

---

**87.** (Q1162) Which task is a responsibility of AWS, according to the AWS shared responsibility model? h
- A. Configure identity and access management for applications.
- B. Manage encryption options for data that is stored on AWS.
- C. Configure security groups for Amazon EC2 instances.
- D. Maintain the physical hardware of the infrastructure. ✅

---

**88.** (Q1164) Which actions are the responsibility of AWS, according to the AWS shared responsibility model? (Choose two.) rh
- A. Securing the virtualization layer
- B. Patching the operating system on Amazon EC2 instances ✅
- C. Enforcing a strict password policy for IAM users
- D. Patching the operating system on Amazon RDS instances
- E. Configuring security groups and network ACLs

---

**89.** (Q1190) Which option is a shared control between AWS and the customer, according to the AWS shared responsibility model? h
- A. Configuration management ✅
- B. Physical and environmental controls
- C. Data integrity authentication
- D. Identity and access management

---

**90.** (Q1205) A company has deployed an Amazon EC2 instance. Which option is an AWS responsibility under the AWS shared responsibility model? 5
- A. Managing and encrypting application data
- B. Installing updates and security patches of guest operating system
- C. Configuration of infrastructure devices ✅
- D. Configuration of security groups on each instance

---

**91.** (Q443) According to the AWS shared responsibility model, which of the following are AWS responsibilities? (Choose two.)
- A. Network infrastructure and virtualization of infrastructure ✅
- B. Security of application data
- C. Guest operating systems
- D. Physical security of hardware ✅
- E. Credentials and policies

**Explanation:** *(Add explanation here)*

---

**92.** (Q450) Which activity is a customer responsibility in the AWS Cloud according to the AWS shared responsibility model?
- A. Ensuring network connectivity from AWS to the internet
- B. Patching and fixing flaws within the AWS Cloud infrastructure
- C. Ensuring the physical security of cloud data centers
- D. Ensuring Amazon EBS volumes are backed up ✅

**Explanation:** *(Add explanation here)*

---

**93.** (Q452) Which of the following are customer responsibilities under the AWS shared responsibility model? (Choose two.)
- A. Physical security of AWS facilities
- B. Configuration of security groups ✅
- C. Encryption of customer data on AWS ✅
- D. Management of AWS Lambda infrastructure
- E. Management of network throughput of each AWS Region

**Explanation:** *(Add explanation here)*

---

**94.** (Q491) Under the AWS shared responsibility model, which of the following is the customer's responsibility?
- A. Patching guest OS and applications ✅
- B. Patching and fixing flaws in the infrastructure
- C. Physical and environmental controls
- D. Configuration of AWS infrastructure devices

**Explanation:** *(Add explanation here)*

---

**95.** (Q535) Which statements represent the cost-effectiveness of the AWS Cloud? (Choose two.)
- A. Users can trade fixed expenses for variable expenses. ✅
- B. Users can deploy all over the world in minutes.
- C. AWS offers increased speed and agility.
- D. AWS is responsible for patching the infrastructure.
- E. Users benefit from economies of scale. ✅

**Explanation:** *(Add explanation here)*

---

**96.** (Q560) According to the AWS shared responsibility model, the customer is responsible for applying the latest security updates and patches for which of the following?
- A. Amazon DynamoDB
- B. Amazon EC2 instances ✅
- C. Amazon RDS instances
- D. Amazon S3

**Explanation:** *(Add explanation here)*

---

**97.** (Q587) A company wants to build an application that uses AWS Lambda to run Python code. Under the AWS shared responsibility model, which tasks will be the company's responsibility? (Choose two.)
- A. Management of the underlying infrastructure
- B. Management of the operating system.
- C. Writing the business logic code. ✅
- D. Installation of the computer language runtime.
- E. Providing AWS Identity and Access Management (IAM) access to the Lambda service. ✅

**Explanation:** *(Add explanation here)*

---

**98.** (Q594) A company is using Amazon EC2 instances. Which tasks are the company's responsibility, according to the AWS shared responsibility model? (Choose two.) operating system.
- A. Choose the initial root password of new Linux instances.
- B. Identify which users can access the EC2 instances, and manage their permissions in the ✅
- C. Apply the updates of the hypervisor where the EC2 instances are running.
- D. Choose between a Wi-Fi connection and an Ethernet connection for the global internet access.
- E. Identify and manage the users who are allowed to create or delete EC2 instances. ✅

**Explanation:** *(Add explanation here)*

---

**99.** (Q625) What is the customer ALWAYS responsible for managing, according to the AWS shared responsibility model?
- A. Software licenses
- B. Networking
- C. Customer data ✅
- D. Encryption keys

**Explanation:** *(Add explanation here)*

---

**100.** (Q644) According to the AWS shared responsibility model, which activities are the customer's responsibility for security in the AWS Cloud? (Choose two.)
- A. Hardware maintenance
- B. Amazon EC2 operating system patching ✅
- C. API access control for AWS resources ✅
- D. Configuration management of infrastructure devices
- E. Maintenance of an Availability Zone

**Explanation:** *(Add explanation here)*

---

**101.** (Q646) Which duty is a responsibility of AWS under the AWS shared responsibility model?
- A. Identity and access management
- B. Server-side encryption (SSE)
- C. Firewall configuration
- D. Maintaining physical hardware ✅

**Explanation:** *(Add explanation here)*

---

**102.** (Q592) Which task is the responsibility of AWS, according to the AWS shared responsibility model?
- A. Apply guest operating system patches to Amazon EC2 instances.
- B. Provide monitoring of human resources information management (HRIM) systems.
- C. Perform automated backups of Amazon RDS instances. ✅
- D. Optimize the costs of running AWS services.

---

**103.** (Q609) What is a customer responsibility under the AWS shared responsibility model when using AWS Lambda?
- A. Maintenance of the underlying Lambda hardware.
- B. Maintenance of the Lambda networking infrastructure.
- C. The code and libraries that run in the Lambda functions. ✅
- D. The Lambda server software.

---

**104.** (Q610) Which tasks are the responsibility of AWS according to the AWS shared responsibility model? (Choose two.)
- A. Configure AWS Identity and Access Management (IAM).
- B. Configure security groups on Amazon EC2 instances.
- C. Secure the access of physical AWS facilities. ✅
- D. Patch applications that run on Amazon EC2 instances.
- E. Perform infrastructure patching and maintenance. ✅

---

**105.** (Q627) Which tasks are responsibilities of the customer, according to the AWS shared responsibility model? (Choose two.)
- A. Secure the virtualization layer.
- B. Encrypt data and maintain data integrity. ✅
- C. Patch the Amazon RDS operating system.
- D. Maintain identity and access management controls. ✅
- E. Secure Availability Zones.

---

**106.** (Q631) Under the AWS shared responsibility model, which of the following is a responsibility of the customer?
- A. Shred disk drives before they leave a data center.
- B. Prevent customers from gathering packets or collecting traffic at the hypervisor level.
- C. Patch the guest operating system with the latest security patches. ✅
- D. Maintain security systems that provide physical monitoring of data centers.

---

**107.** (Q648) Which of the following is a customer responsibility according to the AWS shared responsibility model?
- A. Apply security patches for Amazon S3 infrastructure devices.
- B. Provide physical security for AWS datacenters.
- C. Install operating system updates on Lambda@Edge.
- D. Implement multi-factor authentication (MFA) for IAM user accounts. ✅

---

