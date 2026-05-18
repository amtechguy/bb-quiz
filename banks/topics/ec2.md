# 📚 Amazon EC2 — Elastic Compute Cloud

> **Study Resources for this Topic:**
>
> - 📖 **Official AWS Docs:** [https://docs.aws.amazon.com/ec2/](https://docs.aws.amazon.com/ec2/)
> - 🎬 **YouTube Overview:** [https://www.youtube.com/watch?v=iHX-jtKIVNA](https://www.youtube.com/watch?v=iHX-jtKIVNA)
> - 🎓 **AWS Skill Builder (Free):** [AWS Cloud Practitioner Essentials](https://explore.skillbuilder.aws/learn/course/external/view/elearning/134/aws-cloud-practitioner-essentials)
>
> 💡 **Quick Tip:** Focus on: purchasing options (On-Demand, Reserved, Spot, Dedicated), Auto Scaling, and instance types.

---

**1.** A company needs to collect and process real-time streaming data from thousands of sources. Which AWS service should the company use?
- A. Amazon SQS
- B. Amazon Kinesis Data Streams ✅
- C. Amazon S3
- D. AWS Batch

---

**2.** Which AWS service automatically loads streaming data into Amazon S3, Amazon Redshift, and other destinations?
- A. Amazon Kinesis Data Streams
- B. Amazon Kinesis Data Firehose ✅
- C. Amazon SQS
- D. AWS DataSync

---

**3.** What is the primary use case for Amazon Redshift?
- A. Transactional database workloads (OLTP)
- B. Real-time streaming analytics
- C. Analytical query workloads on large datasets (OLAP) ✅
- D. NoSQL document storage

---

**4.** Which AWS service provides fully managed Apache Kafka for real-time streaming data pipelines?
- A. Amazon SQS
- B. Amazon Kinesis Data Streams
- C. Amazon Managed Streaming for Apache Kafka (Amazon MSK) ✅
- D. AWS Glue

---

**5.** Which AWS service enables near-real-time analytics on streaming data using SQL queries?
- A. Amazon Athena
- B. Amazon Kinesis Data Analytics ✅
- C. Amazon Redshift
- D. AWS Glue

---

**6.** A company needs to continuously capture and load streaming data into Amazon S3 for later analysis. Which AWS service provides the MOST operationally efficient solution?
- A. Amazon SQS
- B. Amazon Kinesis Data Firehose ✅
- C. AWS DataSync
- D. Amazon SNS

---

**7.** Which AWS service can a company use to detect anomalies in streaming data in real time?
- A. Amazon CloudWatch
- B. Amazon Kinesis Data Analytics ✅
- C. AWS Glue
- D. Amazon Redshift

---

**8.** A company wants to store and analyze streaming data from web application clickstreams. Which AWS service should the company use?
- A. Amazon SQS
- B. Amazon Kinesis Data Firehose ✅
- C. AWS Batch
- D. Amazon RDS

---

**9.** A company wants to set up an end-to-end analytics pipeline that includes data ingestion, transformation, cataloging, and visualization. Which combination of AWS services should the company use? (Choose two.)
- A. AWS Glue ✅
- B. Amazon EC2
- C. Amazon QuickSight ✅
- D. Amazon SQS
- E. AWS CloudFormation

---

**10.** Question 877 A retail company has recently migrated its website to AWS. The company wants to ensure that it is protected from SQL injection attacks. The website uses an Application Load Balancer to distribute traffic to multiple Amazon EC2 instances. Which AWS service or feature can be used to create a custom rule that blocks SQL injection attacks?
- A. Security groups
- B. AWS WAF ✅
- C. Network ACLs
- D. AWS Shield

---

**11.** Question 880 Which type of AWS storage is ephemeral and is deleted when an Amazon EC2 instance is stopped or terminated?
- A. Amazon Elastic Block Store (Amazon EBS)
- B. Amazon EC2 Instance store ✅
- C. Amazon Elastic File System (Amazon EFS)
- D. Amazon S3

---

**12.** Question 882 A company hosts an application on an Amazon EC2 instance. The EC2 instance needs to access several AWS resources, including Amazon S3 and Amazon DynamoDB. What is the MOST operationally efficient solution to delegate permissions?
- A. Create an IAM role with the required permissions. Attach the role to the EC2 instance. ✅
- B. Create an IAM user and use its access key and secret access key in the application.
- C. Create an IAM user and use its access key and secret access key to create a CLI profile in the EC2 instance
- D. Create an IAM role with the required permissions. Attach the role to the administrative IAM user.

---

**13.** Question 884 What is the purpose of having an internet gateway within a VPC?
- A. To create a VPN connection to the VPC
- B. To allow communication between the VPC and the internet ✅
- C. To impose bandwidth constraints on internet traffic
- D. To load balance traffic from the internet across Amazon EC2 instances

---

**14.** Question 894 A company has a workload that will run continuously for 1 year. The workload cannot tolerate service interruptions. Which Amazon EC2 purchasing option will be MOST cost-effective?
- A. All Upfront Reserved Instances ✅
- B. Partial Upfront Reserved Instances
- C. Dedicated Instances
- D. On-Demand Instances

---

**15.** Question 905 A company wants to ensure that two Amazon EC2 instances are in separate data centers with minimal communication latency between the data centers. How can the company meet this requirement?
- A. Place the EC2 instances in two separate AWS Regions connected with a VPC peering connection. ✅
- B. Place the EC2 instances in two separate Availability Zones within the same AWS Region.
- C. Place one EC2 instance on premises and the other in an AWS Region. Then connect them by using an AWS
- D. Place both EC2 instances in a placement group for dedicated bandwidth.

---

**16.** Question 906 In which situations should a company create an IAM user instead of an IAM role? (Choose two.)
- A. When an application that runs on Amazon EC2 instances requires access to other AWS services
- B. When the company creates AWS access credentials for individuals ✅
- C. When the company creates an application that runs on a mobile phone that makes requests to AWS
- D. When the company needs to add users to IAM groups ✅
- E. When users are authenticated in the corporate network and want to be able to use AWS without having to sign

---

**17.** Question 909 A retail company needs to build a highly available architecture for a new ecommerce platform. The company is using only AWS services that replicate data across multiple Availability Zones. Which AWS services should the company use to meet this requirement? (Choose two.)
- A. Amazon EC2
- B. Amazon Elastic Block Store (Amazon EBS)
- C. Amazon Aurora ✅
- D. Amazon DynamoDB ✅
- E. Amazon Redshift

---

**18.** Question 916 Which of the following are benefits of Amazon EC2 Auto Scaling? (Choose two.)
- A. Improved health and availability of applications ✅
- B. Reduced network latency
- C. Optimized performance and costs ✅
- D. Automated snapshots of data
- E. Cross-Region Replication

---

**19.** Question 917 A company has several departments. Each department has its own AWS accounts for its applications. The company wants all AWS costs on a single invoice to simplify payment, but the company wants to know the costs that each department is incurring. Which AWS tool or feature will provide this functionality?
- A. AWS Cost and Usage Reports
- B. Consolidated billing ✅
- C. Savings Plans
- D. AWS Budgets

---

**20.** Question 924 A company wants to implement threat detection on its AWS infrastructure. However, the company does not want to deploy additional software. Which AWS service should the company use to meet these requirements?
- A. Amazon VPC
- B. Amazon EC2
- C. Amazon GuardDuty ✅
- D. AWS Direct Connect

---

**21.** Question 926 A company needs to install an application in a Docker container. Which AWS service eliminates the need to provision and manage the container hosts?
- A. AWS Fargate ✅
- B. Amazon FSx for Windows File Server
- C. Amazon Elastic Container Service (Amazon ECS)
- D. Amazon EC2

---

**22.** Question 935 Which AWS service should be used to monitor Amazon EC2 instances for CPU and network utilization?
- A. Amazon Inspector
- B. AWS CloudTrail
- C. Amazon CloudWatch ✅
- D. AWS Config

---

**23.** Question 948 A company has a single Amazon EC2 instance. The company wants to adopt a highly available architecture. What can the company do to meet this requirement?
- A. Scale vertically to a larger EC2 instance size.
- B. Scale horizontally across multiple Availability Zones. ✅
- C. Purchase an EC2 Dedicated Instance.
- D. Change the EC2 instance family to a compute optimized instance.

---

**24.** Question 956 A company has a database server that is always running. The company hosts the server on Amazon EC2 instances. The instance sizes are suitable for the workload. The workload will run for 1 year. Which EC2 instance purchasing option will meet these requirements MOST cost-effectively?
- A. Standard Reserved Instances ✅
- B. On-Demand Instances
- C. Spot Instances
- D. Convertible Reserved Instances

---

**25.** Question 958 A company needs to simultaneously process hundreds of requests from different users. Which combination of AWS services should the company use to build an operationally efficient solution?
- A. Amazon Simple Queue Service (Amazon SQS) and AWS Lambda ✅
- B. AWS Data Pipeline and Amazon EC2
- C. Amazon Kinesis and Amazon Athena
- D. AWS Amplify and AWS AppSync

---

**26.** Question 964 A user needs to determine whether an Amazon EC2 instance's security groups were modified in the last month. How can the user see if a change was made?
- A. Use Amazon EC2 to see if the security group was changed.
- B. Use AWS Identity and Access Management (IAM) to see which user or role changed the security group.
- C. Use AWS CloudTrail to see if the security group was changed. ✅
- D. Use Amazon CloudWatch to see if the security group was changed.

---

**27.** Question 966 Which AWS service or feature acts as a firewall for Amazon EC2 instances?
- A. Network ACL
- B. Elastic network interface
- C. Amazon VPC
- D. Security group ✅

---

**28.** Question 968 A company wants to review its monthly costs of using Amazon EC2 and Amazon RDS for the past year. Which AWS service or tool provides this information?
- A. AWS Trusted Advisor
- B. Cost Explorer ✅
- C. Amazon Forecast
- D. Amazon CloudWatch

---

**29.** Question 969 A company wants to migrate a critical application to AWS. The application has a short runtime. The application is invoked by changes in data or by shifts in system state. The company needs a compute solution that maximizes operational efficiency and minimizes the cost of running the application. Which AWS solution should the company use to meet these requirements?
- A. Amazon EC2 On-Demand Instances
- B. AWS Lambda ✅
- C. Amazon EC2 Reserved Instances
- D. Amazon EC2 Spot Instances

---

**30.** Question 972 A company is launching an ecommerce application that must always be available. The application will run on Amazon EC2 instances continuously for the next 12 months. What is the MOST cost-effective instance purchasing option that meets these requirements?
- A. Spot Instances
- B. Savings Plans ✅
- C. Dedicated Hosts
- D. On-Demand Instances

---

**31.** Question 976 Which documentation does AWS Artifact provide?
- A. Amazon EC2 terms and conditions
- B. AWS ISO certifications ✅
- C. A history of a company's AWS spending
- D. A list of previous-generation Amazon EC2 instance types

---

**32.** Question 982 A large company has multiple departments. Each department has its own AWS account. Each department has purchased Amazon EC2 Reserved Instances. Some departments do not use all the Reserved Instances that they purchased, and other departments need more Reserved Instances than they purchased. The company needs to manage the AWS accounts for all the departments so that the departments can share the Reserved Instances. Which AWS service or tool should the company use to meet these requirements?
- A. AWS Systems Manager
- B. Cost Explorer
- C. AWS Trusted Advisor
- D. AWS Organizations ✅

---

**33.** Question 985 Which AWS services or features provide disaster recovery solutions for Amazon EC2 instances? (Choose two.)
- A. Reserved Instances
- B. EC2 Amazon Machine Images (AMIs) ✅
- C. Amazon Elastic Block Store (Amazon EBS) snapshots ✅
- D. AWS Shield
- E. Amazon GuardDuty

---

**34.** Question 987 A user is comparing purchase options for an application that runs on Amazon EC2 and Amazon RDS. The application cannot sustain any interruption. The application experiences a predictable amount of usage, including some seasonal spikes that last only a few weeks at a time. It is not possible to modify the application. Which purchase option meets these requirements MOST cost-effectively?
- A. Review the AWS Marketplace and buy Partial Upfront Reserved Instances to cover the predicted and seasonal
- B. Buy Reserved Instances for the predicted amount of usage throughout the year. Allow any seasonal usage to ✅
- C. Buy Reserved Instances for the predicted amount of usage throughout the year. Allow any seasonal usage to ✅
- D. Buy Reserved Instances to cover all potential usage that results from the seasonal usage.

---

**35.** Question 1214 Which of the following describes some of the core functionality of Amazon S3?
- A. Amazon S3 is a high-performance block storage service that is designed for use with Amazon EC2.
- B. Amazon S3 is an object storage service that provides high-level performance, security, scalability, and data ✅
- C. Amazon S3 is a fully managed, highly reliable, and scalable file storage system that is accessible over the
- D. Amazon S3 is a scalable, fully managed elastic NFS for use with AWS Cloud services and on-premises

---

**36.** Question 1216 A company wants to create templates that the company can reuse to deploy multiple AWS resources. Which AWS service or feature can the company use to meet this requirement?
- A. AWS Marketplace
- B. Amazon Machine Image (AMI)
- C. AWS CloudFormation ✅
- D. AWS OpsWorks

---

**37.** Question 1217 A company wants to migrate its database to a managed AWS service that is compatible with PostgreSQL. Which AWS services will meet these requirements? (Choose two.)
- A. Amazon Athena
- B. Amazon RDS ✅
- C. Amazon EC2
- D. Amazon DynamoDB
- E. Amazon Aurora ✅

---

**38.** Question 1225 A user has a stateful workload that will run on Amazon EC2 for the next 3 years. What is the MOST cost-effective pricing model for this workload?
- A. On-Demand Instances
- B. Reserved Instances ✅
- C. Dedicated Instances
- D. Spot Instances

---

**39.** Question 1228 A company often does not use all of its current Amazon EC2 capacity to run stateless workloads. The company wants to optimize its EC2 costs. Which EC2 instance type will meet these requirements?
- A. Spot Instances ✅
- B. Dedicated Instances
- C. Reserved Instances
- D. On-Demand Instances

---

**40.** Question 1229 A company wants to store and retrieve files in Amazon S3 for its existing on-premises applications by using industry-standard file system protocols. Which AWS service will meet these requirements?
- A. AWS DataSync
- B. AWS Snowball Edge
- C. Amazon S3 File Gateway ✅
- D. AWS Transfer Family

---

**41.** Question 1236 What can a user accomplish using AWS CloudTrail?
- A. Generate an IAM user credentials report.
- B. Record API calls made to AWS services. ✅
- C. Assess the compliance of AWS resource configurations with policies and guidelines.
- D. Ensure that Amazon EC2 instances are patched with the latest security updates.

---

**42.** Question 1237 A company is planning to host its workloads on AWS. Which AWS service requires the company to update and patch the guest operating system?
- A. Amazon DynamoDB
- B. Amazon S3
- C. Amazon EC2 ✅
- D. Amazon Aurora

---

**43.** Question 1238 A company is migrating its workloads to the AWS Cloud. The company must retain full control of patch management for the guest operating systems that host its applications. Which AWS service should the company use to meet these requirements?
- A. Amazon DynamoDB
- B. Amazon EC2 ✅
- C. AWS Lambda
- D. Amazon RDS

---

**44.** Question 1240 A company wants to migrate its PostgreSQL database to AWS. The company does not use the database frequently. Which AWS service or resource will meet these requirements with the LEAST management overhead?
- A. PostgreSQL on Amazon EC2
- B. Amazon RDS for PostgreSQL
- C. Amazon Aurora PostgreSQL-Compatible Edition
- D. Amazon Aurora Serverless ✅

---

**45.** Question 1241 A company wants to create a globally accessible ecommerce platform for its customers. The company wants to use a highly available and scalable DNS web service to connect users to the platform. Which AWS service will meet these requirements?
- A. Amazon EC2
- B. Amazon VPC
- C. Amazon Route 53 ✅
- D. Amazon RDS

---

**46.** Question 1248 Which Amazon EC2 pricing model provides the MOST cost savings for an always-up, right-sized database server running for a project that will last 1 year?
- A. On-Demand Instances
- B. Convertible Reserved Instances
- C. Spot Instances
- D. Standard Reserved Instances ✅

---

**47.** Question 1252 A company wants to receive alerts to monitor its overall operating costs for its AWS public cloud infrastructure. Which AWS offering will meet these requirements?
- A. Amazon EventBridge
- B. Compute Savings Plans
- C. AWS Budgets ✅
- D. Migration Evaluator

---

**48.** Question 1254 A company wants to run a simulation for 3 years without interruptions. Which Amazon EC2 instance purchasing option will meet these requirements MOST cost-effectively?
- A. Spot Instances
- B. Reserved Instances ✅
- C. Dedicated Hosts
- D. On-Demand Instances

---

**49.** Question 1257 A company wants to use Amazon EC2 instances to provide a static website to users all over the world. The company needs to minimize latency for the users. Which solution meets these requirements?
- A. Use EC2 instances in multiple edge locations.
- B. Use EC2 instances in the same Availability Zone but in different AWS Regions.
- C. Use Amazon CloudFront with the EC2 instances configured as the source. ✅
- D. Use EC2 instances in the same Availability Zone but in different AWS accounts.

---

**50.** Question 1258 A team of researchers is going to collect data at remote locations around the world. Many locations do not have internet connectivity. The team needs to capture the data in the field, and transfer it to the AWS Cloud later. Which AWS service will support these requirements?
- A. AWS Outposts
- B. AWS Transfer Family
- C. AWS Snow Family ✅
- D. AWS Migration Hub

---

**51.** Question 1260 A company has decided to adopt Amazon EC2 infrastructure and wants to scale various stateless services for short-term usage. Which EC2 pricing model is MOST cost-efficient to meet these requirements?
- A. Spot Instances ✅
- B. On-Demand Instances
- C. Reserved Instances
- D. Dedicated Hosts

---

**52.** Question 1273 Which task can a company perform by using security groups in the AWS Cloud?
- A. Allow access to an Amazon EC2 instance through only a specific port. ✅
- B. Deny access to malicious IP addresses at a subnet level.
- C. Protect data that is cached by Amazon CloudFront.
- D. Apply a stateless firewall to an Amazon EC2 instance.

---

**53.** Question 1274 A company plans to run a compute-intensive workload that uses graphics processing units (GPUs). Which Amazon EC2 instance type should the company use?
- A. Accelerated computing ✅
- B. Compute optimized
- C. Storage optimized
- D. General purpose

---

**54.** Question 1282 A company needs to run a pre-installed third-party firewall on an Amazon EC2 instance. Which AWS service or feature can provide this solution?
- A. Network ACLs
- B. Security groups
- C. AWS Marketplace ✅
- D. AWS Trusted Advisor

---

**55.** Question 1286 An Amazon EC2 instance previously used for development is inaccessible and no longer appears in the AWS Management Console. Which AWS service should be used to determine what action made this EC2 instance inaccessible?
- A. Amazon CloudWatch Logs
- B. AWS Security Hub
- C. Amazon Inspector
- D. AWS CloudTrail ✅

---

**56.** Question 1289 A development team wants to deploy multiple test environments for an application in a fast, repeatable manner. Which AWS service should the team use?
- A. Amazon EC2
- B. AWS CloudFormation ✅
- C. Amazon QuickSight
- D. Amazon Elastic Container Service (Amazon ECS)

---

**57.** Question 1295 Which type of AWS storage is ephemeral and is deleted when an Amazon EC2 instance is stopped or terminated?
- A. Amazon Elastic Block Store (Amazon EBS)
- B. Amazon EC2 instance store ✅
- C. Amazon Elastic File System (Amazon EFS)
- D. Amazon S3

---

**58.** Question 1296 A company wants to provide access to Windows file shares in AWS from its on-premises workloads. The company does not want to provision any additional infrastructure or applications in its data center. Which AWS service will meet these requirements?
- A. Amazon FSx File Gateway ✅
- B. AWS DataSync
- C. Amazon S3
- D. AWS Snow Family

---

**59.** Question 1298 An ecommerce company wants to use Amazon EC2 Auto Scaling to add and remove EC2 instances based on CPU utilization. Which AWS service or feature can initiate an Amazon EC2 Auto Scaling action to achieve this goal?
- A. Amazon Simple Queue Service (Amazon SQS)
- B. Amazon Simple Notification Service (Amazon SNS)
- C. AWS Systems Manager
- D. Amazon CloudWatch alarm ✅

---

**60.** Question 1302 A company has been storing monthly reports in an Amazon S3 bucket. The company exports the report data into comma-separated values (.csv) files. A developer wants to write a simple query that can read all of these files and generate a summary report. Which AWS service or feature should the developer use to meet these requirements with the LEAST amount of operational overhead?
- A. Amazon S3 Select
- B. Amazon Athena ✅
- C. Amazon Redshift
- D. Amazon EC2

---

**61.** Question 1306 A user needs a relational database but does not have the resources to manage the hardware, resiliency, and replication. Which AWS service option meets the user's requirements?
- A. Run MySQL on Amazon Elastic Container Service (Amazon ECS).
- B. Run MySQL on Amazon EC2.
- C. Choose Amazon RDS for MySQL. ✅
- D. Choose Amazon ElastiCache for Redis.

---

**62.** Question 1307 A company needs to deploy applications in the AWS Cloud as quickly as possible. The company also needs to minimize the complexity that is related to the management of AWS resources. Which AWS service should the company use to meet these requirements?
- A. AWS Config
- B. AWS Elastic Beanstalk ✅
- C. Amazon EC2
- D. Amazon Personalize

---

**63.** Question 1313 A company wants to use application stacks to run a workload in the AWS Cloud. The company wants to use pre-configured instances. Which AWS service will meet these requirements?
- A. Amazon Lightsail ✅
- B. Amazon Athena
- C. AWS Outposts
- D. Amazon EC2

---

**64.** Question 1314 Which AWS services are supported by Savings Plans? (Choose two.)
- A. Amazon EC2 ✅
- B. Amazon RDS
- C. Amazon SageMaker ✅
- D. Amazon Redshift
- E. Amazon DynamoDB

---

**65.** Question 1323 A company created an Amazon EC2 instance. The company wants to control the incoming and outgoing network traffic at the instance level. Which AWS resource or service will meet this requirement?
- A. AWS Shield
- B. Security groups ✅
- C. Network Access Analyzer
- D. VPC endpoints

---

**66.** Question 1328 A company launched an Amazon EC2 instance with the latest Amazon Linux 2 Amazon Machine Image (AMI). Which actions can a system administrator take to connect to the EC2 instance? (Choose two.)
- A. Use Amazon EC2 Instance Connect. ✅
- B. Use a Remote Desktop Protocol (RDP) connection.
- C. Use AWS Batch.
- D. Use AWS Systems Manager Session Manager. ✅
- E. Use Amazon Connect.

---

**67.** Question 1330 Which task requires a user to sign in as the AWS account root user?
- A. The deletion of IAM users
- B. The deletion of an AWS account ✅
- C. The creation of an organization in AWS Organizations
- D. The deletion of Amazon EC2 instances

---

**68.** Question 1332 A company needs Amazon EC2 instances for a workload that can tolerate interruptions. Which EC2 instance purchasing option meets this requirement with the LARGEST discount compared to On-Demand prices?
- A. Spot Instances ✅
- B. Convertible Reserved Instances
- C. Standard Reserved Instances
- D. Dedicated Hosts

---

**69.** Question 1340 In which ways does the AWS Cloud offer lower total cost of ownership (TCO) of computing resources than on-premises data centers? (Choose two.)
- A. AWS replaces upfront capital expenditures with pay-as-you-go costs. ✅
- B. AWS is designed for high availability, which eliminates user downtime.
- C. AWS eliminates the need for on-premises IT staff.
- D. AWS uses economies of scale to continually reduce prices. ✅
- E. AWS offers a single pricing model for Amazon EC2 instances.

---

**70.** Question 1342 Which of the following AWS services are serverless? (Choose two.)
- A. AWS Outposts
- B. Amazon EC2
- C. Amazon Elastic Kubernetes Service (Amazon EKS)
- D. AWS Fargate ✅
- E. AWS Lambda ✅

---

**71.** Question 1343 When a user wants to utilize their existing per-socket, per-core, or per-virtual machine software licenses for a Microsoft Windows server running on AWS, which Amazon EC2 instance type is required?
- A. Spot Instances
- B. Dedicated Instances
- C. Dedicated Hosts ✅
- D. Reserved Instances

---

**72.** Question 1344 A solutions architect needs to maintain a fleet of Amazon EC2 instances so that any impaired instances are replaced with new ones. Which AWS service should the solutions architect use?
- A. Amazon Elastic Container Service (Amazon ECS)
- B. Amazon GuardDuty
- C. AWS Shield
- D. AWS Auto Scaling ✅

---

**73.** Question 1346 What does Amazon CloudFront provide?
- A. Automatic scaling for all resources to power an application from a single unified interface
- B. Secure delivery of data, videos, applications, and APIs to users globally with low latency ✅
- C. Ability to directly manage traffic globally through a variety of routing types, including latency-based routing, geo
- D. Automatic distribution of incoming application traffic across multiple targets, such as Amazon EC2 instances,

---

**74.** Question 1353 Which AWS service makes it easier to monitor and troubleshoot application logs and cloud resources?
- A. Amazon EC2
- B. AWS Identity and Access Management (IAM)
- C. Amazon CloudWatch ✅
- D. AWS CloudTrail

---

**75.** Question 1354 Which AWS service uses AWS Compute Optimizer to provide sizing recommendations based on workload metrics?
- A. Amazon EC2 ✅
- B. Amazon RDS
- C. Amazon Lightsail
- D. AWS Step Functions

---

**76.** Question 1357 A company is in the early stages of planning a migration to AWS. The company wants to obtain the monthly predicted total AWS cost of ownership for future Amazon EC2 instances and associated storage. Which AWS service or tool should the company use to meet these requirements?
- A. AWS Pricing Calculator ✅
- B. AWS Compute Optimizer
- C. AWS Trusted Advisor
- D. AWS Application Migration Service

---

**77.** Question 1358 A company is migrating to the AWS Cloud and plans to run experimental workloads for 3 to 6 months on AWS. Which pricing model will meet these requirements?
- A. Use Savings Plans for a 3-year term.
- B. Use Dedicated Hosts.
- C. Buy Reserved Instances.
- D. Use On-Demand Instances. ✅

---

**78.** Question 411 Which feature of Amazon RDS provides the ability to automatically create a primary database instance and to synchronously replicate data to an instance in another Availability Zone?
- A. Read replicas
- B. Blue/green deployment
- C. Multi-AZ deployment ✅
- D. Reserved Instances

---

**79.** Question 413 A company runs many Amazon EC2 instances in its VPC. The company wants to use a native AWS security resource to control network traffic between certain EC2 instances. Which AWS service or feature will meet this requirement?
- A. Network ACLs
- B. AWS WAF
- C. Amazon GuardDuty
- D. Security groups ✅

---

**80.** Question 425 Which AWS service or resource can a company use to deploy AWS WAF rules?
- A. Amazon EC2
- B. Application Load Balancer ✅
- C. AWS Trusted Advisor
- D. Network Load Balancer

---

**81.** Question 426 A company hosts its website on Amazon EC2 instances. The company needs to ensure that the website reaches a global audience and provides minimum latency to users. Which AWS service should the company use to meet these requirements?
- A. Amazon Route 53
- B. Amazon CloudFront ✅
- C. Elastic Load Balancing
- D. AWS Lambda

---

**82.** Question 429 A company is running a reporting web server application on Amazon EC2 instances. The application runs once every week and once again at the end of the month. The EC2 instances can be shut down when they are not in use. What is the MOST cost-effective billing model for this use case?
- A. Standard Reserved Instances
- B. Convertible Reserved Instances
- C. On-Demand Capacity Reservations
- D. On-Demand Instances ✅

---

**83.** Question 431 A company is moving its development and test environments to AWS to increase agility and reduce cost. Because these are not production workloads and the servers are not fully utilized, occasional unavailability is acceptable. What is the MOST cost-effective Amazon EC2 pricing model that will meet these requirements?
- A. Reserved Instances
- B. On-Demand Instances
- C. Spot Instances ✅
- D. Dedicated Hosts

---

**84.** Question 440 A company wants to migrate a company's on-premises container infrastructure to the AWS Cloud. The company wants to prevent unplanned administration and operation cost and adapt to a serverless architecture. Which AWS service will meet these requirements?
- A. Amazon Connect
- B. AWS Fargate ✅
- C. Amazon Lightsail
- D. Amazon EC2

---

**85.** Question 441 A company wants its Amazon EC2 instances to be in different locations but share the same geographic area. The company also wants to use multiple power grids and independent networking connectivity for the EC2 instances. Which solution meets these requirements?
- A. Use EC2 instances in multiple edge locations in the same AWS Region.
- B. Use EC2 instances in multiple Availability Zones in the same AWS Region. ✅
- C. Use EC2 instances in multiple Amazon Connect locations in the same AWS Region.
- D. Use EC2 instances in multiple AWS Artifact locations in the same AWS Region.

---

**86.** Question 442 An ecommerce company has deployed a new web application on Amazon EC2 instances. The company wants to distribute incoming HTTP traffic evenly across all running instances. Which AWS service or resource will meet this requirement?
- A. Amazon EC2 Auto Scaling
- B. Application Load Balancer ✅
- C. Gateway Load Balancer
- D. Network Load Balancer

---

**87.** Question 444 A company wants to run CPU-intensive workload across multiple Amazon EC2 instances. Which EC2 instance type should the company use to meet this requirement?
- A. General purpose instances
- B. Compute optimized instances ✅
- C. Memory optimized instances
- D. Storage optimized instances

---

**88.** Question 462 A company wants to use Amazon EC2 instances for a stable production workload that will run for 1 year. Which instance purchasing option meets these requirements MOST cost-effectively?
- A. Dedicated Hosts
- B. Reserved Instances ✅
- C. On-Demand Instances
- D. Spot Instances

---

**89.** Question 463 A company wants to log in securely to Linux Amazon EC2 instances. How can the company accomplish this goal?
- A. Use SSH keys. ✅
- B. Use a VPN.
- C. Use end-to-end encryption.
- D. Use Amazon Route 53.

---

**90.** Question 465 A company wants a solution that will automatically adjust the number of Amazon EC2 instances that are being used based on the current load. Which AWS service will meet these requirements?
- A. Dedicated Hosts
- B. Placement groups
- C. Auto Scaling groups ✅
- D. Reserved Instances

---

**91.** Question 467 A company plans to migrate its custom marketing application and order-processing application to AWS. The company needs to deploy the applications on different types of instances with various configurations of CPU, memory, storage, and networking capacity. Which AWS service should the company use to meet these requirements?
- A. AWS Lambda
- B. Amazon Cognito
- C. Amazon Athena
- D. Amazon EC2 ✅

---

**92.** Question 469 Which AWS services can host PostgreSQL databases? (Choose two.)
- A. Amazon S3
- B. Amazon Aurora ✅
- C. Amazon EC2 ✅
- D. Amazon OpenSearch Service
- E. Amazon Elastic File System (Amazon EFS)

---

**93.** Question 472 A company wants its Amazon EC2 instances to operate in a highly available environment, even if there is a natural disaster in a particular geographic area. Which solution achieves this goal?
- A. Use EC2 instances in multiple AWS Regions. ✅
- B. Use EC2 instances in multiple edge locations.
- C. Use EC2 instances in the same Availability Zone but in different AWS Regions.
- D. Use Amazon CloudFront with the EC2 instances configured as the source.

---

**94.** Question 473 Which AWS service allows for file sharing between multiple Amazon EC2 instances?
- A. AWS Direct Connect
- B. AWS Snowball Edge
- C. AWS Backup
- D. Amazon Elastic File System (Amazon EFS) ✅

---

**95.** Question 482 Which of the following are AWS best practice recommendations for the use of AWS Identity and Access Management (IAM)? (Choose two.)
- A. Use the AWS account root user for daily access.
- B. Use access keys and secret access keys on Amazon EC2.
- C. Rotate credentials on a regular basis. ✅
- D. Create a shared set of access keys for system administrators.
- E. Configure multi-factor authentication (MFA). ✅

---

**96.** Question 494 A company runs an application on AWS that performs batch jobs. The application is fault-tolerant and can handle interruptions. The company wants to optimize the cost to run the application. Which AWS offering will meet these requirements?
- A. Amazon Macie
- B. Amazon Neptune
- C. Amazon EC2 Spot Instances ✅
- D. Amazon EC2 On-Demand Instances

---

**97.** Question 502 A user wants to invoke an AWS Lambda function when an Amazon EC2 instance enters the "stopping" state. Which AWS service is appropriate for this use case?
- A. Amazon EventBridge ✅
- B. AWS Config
- C. Amazon Simple Notification Service (Amazon SNS)
- D. AWS CloudFormation

---

**98.** Question 508 A company wants to rightsize its Amazon EC2 instances. Which configuration change will meet this requirement with the LEAST operational overhead?
- A. Add EC2 instances in another Availability Zone.
- B. Change the size and type of the EC2 instances based on utilization. ✅
- C. Convert the payment method from On-Demand to Savings Plans.
- D. Reprovision the EC2 instances with a larger instance type.

---

**99.** Question 513 A systems administrator wants to monitor the CPU utilization of a company's Amazon EC2 instances. Which AWS service can provide this information?
- A. AWS Config
- B. AWS Trusted Advisor
- C. AWS CloudTrail
- D. Amazon CloudWatch ✅

---

**100.** Question 515 An independent software vendor wants to deliver and share its custom Amazon Machine Images (AMIs) to prospective customers. Which AWS service will meet these requirements?
- A. AWS Marketplace ✅
- B. AWS Data Exchange
- C. Amazon EC2
- D. AWS Organizations

---

**101.** Question 521 A company's application is running on Amazon EC2 instances. The company is planning a partial migration to a serverless architecture in the next year and wants to pay for resources up front. Which AWS purchasing option will optimize the company's costs?
- A. Convertible Reserved Instances
- B. Spot Instances
- C. EC2 Instance Savings Plans ✅
- D. Compute Savings Plan

---

**102.** Question 524 A company has batch workloads that need to run for short periods of time on Amazon EC2. The workloads can handle interruptions and can start again from where they ended. What is the MOST cost-effective EC2 instance purchasing option to meet these requirements?
- A. Reserved Instances
- B. Spot Instances ✅
- C. Dedicated Instances
- D. On-Demand Instances

---

**103.** Question 530 An ecommerce company plans to move its data center workload to the AWS Cloud to support highly dynamic usage patterns. Which benefits make the AWS Cloud cost-effective for the migration of this type of workload? (Choose two.)
- A. Reliability
- B. Security
- C. Elasticity ✅
- D. Pay-as-you-go resource ✅
- E. High availability

---

**104.** Question 531 When designing AWS workloads to be operational even when there are component failures, what is an AWS best practice?
- A. Perform quarterly disaster recovery tests.
- B. Place the main component on the us-east-1 Region.
- C. Design for automatic failover to healthy resources. ✅
- D. Design workloads to fit on a single Amazon EC2 instance.

---

**105.** Question 538 A company needs to host a web server on Amazon EC2 instances for at least 1 year. The web server cannot tolerate interruption. Which EC2 instance purchasing option will meet these requirements MOST cost-effectively?
- A. On-Demand Instances
- B. Partial Upfront Reserved Instances ✅
- C. Spot Instances
- D. No Upfront Reserved Instances

---

**106.** Question 542 An ecommerce company wants to distribute traffic between the Amazon EC2 instances that host its website. Which AWS service or resource will meet these requirements?
- A. Application Load Balancer ✅
- B. AWS WAF
- C. AWS CloudHSM
- D. AWS Direct Connect

---

**107.** Question 546 A company is hosting a web application on Amazon EC2 instances. The company wants to implement custom conditions to filter and control inbound web traffic. Which AWS service will meet these requirements?
- A. Amazon GuardDuty
- B. AWS WAF ✅
- C. Amazon Macie
- D. AWS Shield

---

**108.** Question 548 A company has temporary workload that is also variable. The company needs to use Amazon EC2 instances for the workload. The EC2 instances need to handle short bursts of work that cannot stop before finishing. Which purchase option will meet these requirements?
- A. Spot Instances
- B. On-Demand Instances ✅
- C. Savings Plan
- D. Reserved Instances

---

**109.** Which AWS service helps assess the security and compliance of applications that are deployed on Amazon EC2 instances?

- A. AWS Security Hub
- B. Amazon Inspector ✅
- C. Amazon GuardDuty
- D. AWS Shield

**Explanation:** Amazon Inspector automatically assesses EC2 instances for software vulnerabilities and unintended network exposure, providing security and compliance findings.

---

**110.** A company wants to use Amazon EC2 instances to provide a static website to users all over the world. The company needs to minimize latency for the users. Which solution meets these requirements?

- A. Use Amazon ElastiCache as the database for the EC2 instances.
- B. Use EC2 instances in the same edge location and the same Availability Zone.
- C. Use Amazon CloudFront with the EC2 instances configured as the source. ✅
- D. Use EC2 instances in the same Availability Zone but in different AWS accounts.

**Explanation:** Amazon CloudFront caches content at edge locations worldwide, serving it from the location closest to each user to minimize latency.

---

**111.** A company wants to host an application on Amazon EC2 instances. The company needs to bring its own license for its operating systems. To meet governance and compliance requirements, the application needs software licensing at the physical server level. Which EC2 instance purchasing option will meet these requirements?

- A. Reserved Instances
- B. Spot Instances
- C. On-Demand Instances
- D. Dedicated Hosts ✅

**Explanation:** Dedicated Hosts provide visibility into the physical server's sockets and cores, which is required by most BYOL licensing models that are tied to per-socket or per-core metrics.

---

**112.** Which AWS service is a fully managed service that allows access to applications through a virtual interface (VIF)?

- A. Amazon AppStream 2.0 ✅
- B. Amazon EC2
- C. AWS Elastic Beanstalk
- D. AWS Lambda

**Explanation:** Amazon AppStream 2.0 is a fully managed application streaming service that provides users access to desktop applications through a virtual interface without needing to manage infrastructure.

---

**113.** A company is creating an Amazon EC2 instance. The company wants to control the incoming and outgoing network traffic at the EC2 instance level. Which AWS service or resource will meet this requirement?

- A. Amazon GuardDuty
- B. Amazon Inspector
- C. Security groups ✅
- D. AWS Shield

**Explanation:** Security groups act as a stateful virtual firewall at the EC2 instance level, controlling inbound and outbound traffic based on rules defined by port, protocol, and source/destination.

---

**114.** A company wants to identify unintended network accessibility and vulnerabilities on Amazon EC2 instances. Which AWS service can the company use to meet this requirement?

- A. Amazon Inspector ✅
- B. AWS Config
- C. AWS Trusted Advisor
- D. AWS Shield

**Explanation:** Amazon Inspector automatically discovers and scans EC2 instances for software vulnerabilities and unintended network accessibility, providing detailed security findings.

---

**115.** What is a characteristic of Convertible Reserved Instances?

- A. Users can exchange Convertible RIs for other Convertible RIs from a different instance family ✅
- B. Users can exchange Convertible RIs for other Convertible RIs in different AWS Regions.
- C. Users can sell and buy Convertible RIs on the AWS marketplace.
- D. Users can shorten the term of their Convertible RIs by merging them.

**Explanation:** Convertible Reserved Instances allow users to exchange them for other Convertible RIs with different instance families, operating systems, or tenancies, offering more flexibility than Standard RIs.

---

**116.** A company wants to create multiple isolated networks in the same AWS account. Which AWS service or component will provide this functionality?

- A. AWS Transit Gateway
- B. Internet gateway
- C. Amazon VPC ✅
- D. Amazon EC2

**Explanation:** Amazon VPC allows you to create multiple logically isolated virtual networks within the same AWS account, each with its own IP address range, subnets, and network configuration.

---

**117.** A company is developing a web application that uses containers. The company needs a repository to store and control access to container images. Which AWS service will meet these requirements?

- A. Amazon Elastic Container Registry (Amazon ECR) ✅
- B. Amazon Elastic Kubernetes Service (Amazon EKS)
- C. Amazon Elastic Container Service (Amazon ECS)
- D. Amazon EC2

**Explanation:** Amazon ECR is a fully managed container image registry that makes it easy to store, manage, and deploy container images, with fine-grained access control via IAM policies.

---

**118.** A company has an environment that includes Amazon EC2 instances, Amazon Lightsail, and on-premises servers. The company wants to automate the security updates for its operating systems and applications with the LEAST operational effort. Which solution will meet these requirements?

- A. Use AWS Shield to identify and manage security events.
- B. Connect to each server by using a remote desktop connection. Run an update script.
- C. Use the AWS Systems Manager Patch Manager capability ✅
- D. Schedule Amazon GuardDuty to run on a nightly basis.

**Explanation:** AWS Systems Manager Patch Manager automates the process of patching managed instances across EC2, Lightsail, and on-premises servers from a central location with minimal operational overhead.

---

**119.** A company wants to migrate its main application to Amazon EC2. The application must provide low latency to users in two different geographic locations and must have disaster recovery capabilities. How can these requirements be met?

- A. Deploy the application on an EC2 instance and set up EC2 automatic recovery.
- B. Deploy the application on multiple EC2 instances running in one Availability Zone.
- C. Deploy the application on EC2 instances in Multi-AZs in a single AWS Region.
- D. Deploy the application on EC2 instances in multiple AWS Regions. ✅

**Explanation:** Deploying across multiple AWS Regions ensures low latency for users in different geographic areas and provides disaster recovery capability if an entire Region becomes unavailable.

---

**120.** An ecommerce company wants to design a highly available application that will be hosted on multiple Amazon EC2 instances. How should the company deploy the EC2 instances to meet these requirements?

- A. Across multiple edge locations
- B. Across multiple VPCs
- C. Across multiple Availability Zones ✅
- D. Across multiple AWS accounts

**Explanation:** Deploying EC2 instances across multiple Availability Zones ensures that if one AZ experiences an outage, the application remains available through instances in other AZs within the same Region.

---

**121.** A company wants an Amazon EC2 instance to run an application continuously for one year without interruption. Which EC2 purchasing option will meet this requirement MOST cost-effectively?

- A. Dedicated Hosts
- B. On-Demand Instances
- C. Spot Instances
- D. Standard Reserved Instances ✅

**Explanation:** Standard Reserved Instances offer up to 72% savings over On-Demand for a 1-year commitment, making them the most cost-effective option for continuous, uninterruptible workloads.

---

**122.** A company is creating a document that defines the operating system patch routine for all the company's systems. Which AWS resources should the company include in this document? (Choose two.)

- A. Amazon EC2 instances ✅
- B. AWS Lambda functions
- C. AWS Fargate tasks
- D. Amazon RDS instances ✅
- E. Amazon Elastic Container Service (Amazon ECS) instances

---

**123.** A retail company wants to ensure its website is protected from SQL injection attacks. The website uses an Application Load Balancer to distribute traffic to multiple Amazon EC2 instances. Which AWS service or feature can be used to create a custom rule that blocks SQL injection attacks?

- A. Security groups
- B. AWS WAF ✅
- C. Network ACLs
- D. AWS Shield

---

**124.** Which AWS service provides inbound and outbound network ACLs to restrict connectivity to Amazon EC2 instances?

- A. AWS Identity and Access Management (IAM)
- B. Amazon Connect
- C. Amazon VPC ✅
- D. Amazon API Gateway

---

**125.** A company runs Amazon EC2 instances and an Amazon EFS file system on AWS and needs to centralize the data copies. Which AWS service will meet this requirement with the LEAST amount of operational effort?

- A. AWS Backup ✅
- B. AWS Config
- C. Amazon Inspector
- D. Amazon S3

---

**126.** A company needs to migrate its website from on premises to the AWS Cloud. The website must be hosted on hardware that is not shared with other companies. The company wants to use its existing per-socket, per-core software licenses. Which Amazon EC2 instance purchasing option will meet these requirements?

- A. Dedicated Instance
- B. Reserved Instance
- C. Dedicated Host ✅
- D. On-Demand Instance

---

**127.** A company's security policy requires a record of all changes made to Amazon EC2 security groups, including who made the change and when. Which AWS service will provide this information?

- A. AWS Lambda
- B. Amazon CloudWatch
- C. AWS WAF
- D. AWS CloudTrail ✅

---

**128.** Which of the following is an AWS best practice for using the AWS account root user credentials?

- A. Allow only the manager to use the account root user credentials for normal activities.
- B. Use the account root user credentials only for Amazon EC2 instances from the AWS Free Tier.
- C. Use the account root user credentials only when they alone must be used to perform a required function. ✅
- D. Use the account root user credentials only for the creation of private VPC subnets.

---

**129.** Which documentation does AWS Artifact provide?

- A. Amazon EC2 terms and conditions
- B. AWS ISO certifications ✅
- C. A history of a company's AWS spending
- D. A list of previous-generation Amazon EC2 instance types

---

**130.** A company purchases Amazon EC2 Standard Reserved Instances to run a workload. After the workload is complete, the company no longer requires the Reserved Instances. Which solution will meet this requirement?

- A. Contact the AWS Support team to request the Standard Reserved Instances are transferred.
- B. Convert the Standard Reserved Instances to Compute Savings Plans.
- C. Create an Amazon Machine Image (AMI) of the Reserved Instances.
- D. Sell the Standard Reserved Instances in the Amazon EC2 Reserved Instance Marketplace ✅

---

**131.** A company is running applications on Amazon EC2 instances in the same AWS account for several different projects. The company wants to track infrastructure costs for each project with the least possible impact to existing infrastructure and no additional cost. What should the company do?

- A. Use a different EC2 instance type for each project.
- B. Publish project-specific custom Amazon CloudWatch metrics for each application.
- C. Deploy EC2 instances for each project in a separate AWS account.
- D. Use cost allocation tags with values that are specific to each project. ✅

---

**132.** What is one of the advantages of the Amazon Relational Database Service (Amazon RDS)?
- A. It simplifies relational database administration tasks ✅
- B. It provides 99.99999999999% reliability and durability
- C. It automatically scales databases for loads
- D. It enables users to dynamically adjust CPU and RAM resources
**Explanation:** Amazon RDS simplifies time-consuming database administration tasks such as backups, software patching, monitoring, scaling, and replication so you can focus on your applications.

---

**133.** Which of the following AWS Cloud services can be used to run a customer-managed relational database?
- A. Amazon EC2 ✅
- B. Amazon Route 53
- C. Amazon ElastiCache
- D. Amazon DynamoDB
**Explanation:** Amazon EC2 allows you to run any database software you choose on virtual servers you manage yourself, giving you full control over the database engine and configuration.

---

**134.** A user is planning to launch two additional Amazon EC2 instances to increase availability. Which action should the user take?
- A. Launch the instances across multiple Availability Zones in a single AWS Region. ✅
- B. Launch the instances as EC2 Reserved Instances in the same AWS Region and the same Availability Zone.
- C. Launch the instances in multiple AWS Regions but in the same Availability Zone.
- D. Launch the instances as EC2 Spot Instances in the same AWS Region but in different Availability Zones.
**Explanation:** Launching instances across multiple Availability Zones in the same Region protects your application from the failure of a single data center while keeping latency low between instances.

---

**135.** Which AWS service or feature can be used to monitor CPU usage?
- A. AWS CloudTrail.
- B. VPC Flow Logs.
- C. Amazon CloudWatch. ✅
- D. Health Checks
**Explanation:** Amazon CloudWatch collects and tracks metrics including CPU utilization for EC2 instances. You can set alarms and automatically react to changes in your AWS resources.

---

**136.** A company has deployed several relational databases on Amazon EC2 instances. What is the MOST efficient way to apply monthly security patches?
- A. Connect to each database instance on a monthly basis and apply patches manually.
- B. Enable automate patching for the instances using the Amazon RDS console.
- C. In AWS Config, configure a rule for the instances and the required patch level.
- D. Use AWS Systems Manager to automate database patching according to a schedule. ✅
**Explanation:** AWS Systems Manager Patch Manager automates patching across your EC2 instances on a schedule you define, eliminating manual effort and reducing the risk of missed patches.

---

**137.** How do customers benefit from Amazon's massive economies of scale?
- A. Periodic price reductions as the result of Amazon's operational efficiencies. ✅
- B. New Amazon EC2 instance types providing the latest hardware.
- C. The ability to scale up and down when needed.
- D. Increased reliability in the underlying hardware of Amazon EC2 instances.
**Explanation:** Because AWS aggregates usage from hundreds of thousands of customers, it achieves economies of scale that result in lower pay-as-you-go prices over time.

---

**138.** Which AWS feature allows a company to take advantage of usage tiers for services across multiple member accounts?
- A. Service control policies (SCPs).
- B. Consolidated billing. ✅
- C. All Upfront Reserved Instances.
- D. Organizational Units
**Explanation:** Consolidated billing combines usage from all accounts in an AWS Organization, allowing the company to reach higher usage tiers and receive volume discounts that individual accounts might not qualify for.

---

**139.** Which statement best describes Elastic Load Balancing?
- A. It translates a domain name into an IP address using DNS.
- B. It distributes incoming application traffic across one or more Amazon EC2 instances. ✅
- C. It collects metrics on connected Amazon EC2 instances.
- D. It automatically adjusts the number of Amazon EC2 instances to support incoming traffic.
**Explanation:** Elastic Load Balancing distributes incoming traffic across multiple targets such as EC2 instances, containers, and IP addresses, improving availability and fault tolerance.

---

**140.** Which AWS services are defined as global instead of regional? (Select TWO)
- A. Amazon Route 53. ✅
- B. Amazon EC2.
- C. Amazon S3.
- D. Amazon CloudFront. ✅
- E. Amazon DynamoDB.
**Explanation:** Amazon Route 53 and Amazon CloudFront operate globally across all AWS edge locations rather than being tied to a specific region. Most other AWS services are regional.

---

**141.** A customer needs to determine TCO for a workload that requires physical isolation. Which hosting model should be used?
- A. Reserved Instances
- B. Dedicated Hosts ✅
- C. On-Demand Instances
- D. Spot Instances
**Explanation:** Dedicated Hosts provide physical servers dedicated entirely to your use, giving you full physical isolation from other AWS customers. This is required for certain compliance and licensing scenarios.

---

**142.** What is the lowest-cost, durable storage option for retaining database backups for immediate retrieval?
- A. Amazon EBS.
- B. Amazon Glacier.
- C. Amazon S3. ✅
- D. Amazon EFS
- E. Amazon EC2 Instance Store.
**Explanation:** Amazon S3 offers low-cost durable object storage with immediate retrieval. Glacier is cheaper but has retrieval delays. EBS and EFS are more expensive block and file storage options not suited for backup archiving.

---

**143.** Which of the following is a shared control between the customer and AWS?
- A. Configuration of an Amazon EC2 instance.
- B. Awareness. ✅
- C. Environmental controls of physical AWS data centers.
- D. Providing a key for Amazon S3 client-side encryption.
**Explanation:** Awareness and training is a shared control — AWS trains its employees on security while customers are responsible for training their own staff on AWS security best practices.

---

**144.** Which type of AWS storage is ephemeral and is deleted when an instance is stopped or terminated?
- A. Amazon S3.
- B. Amazon EBS.
- C. Amazon EFS.
- D. Amazon EC2 instance store. ✅
**Explanation:** EC2 instance store provides temporary block storage physically attached to the host computer. This storage is lost when the instance stops, hibernates, or terminates. Use EBS for persistent storage.

---

**145.** Which Amazon EC2 pricing model allows customers to use existing server-bound software licenses?
- A. Dedicated Hosts. ✅
- B. Spot Instances.
- C. On-Demand Instances.
- D. Reserved Instances.
**Explanation:** Dedicated Hosts provide physical servers dedicated to your use, allowing you to use your existing per-socket, per-core, or per-VM software licenses that require physical server binding.

---

**146.** When performing a cost analysis that supports physical isolation of a customer workload, which compute hosting model should be accounted for in the TCO?
- A. On-Demand Instances
- B. No Upfront Reserved Instances
- C. Dedicated Hosts ✅
- D. Reserved Instances
**Explanation:** Dedicated Hosts provide physical server isolation for compliance and licensing requirements. They cost more than shared instances and must be accounted for separately in TCO calculations.

---

**147.** Which Amazon EC2 instance pricing model can provide discounts of up to 90%?
- A. Reserved Instances.
- B. On-Demand.
- C. Dedicated Hosts.
- D. Spot Instances. ✅
**Explanation:** Spot Instances use spare AWS capacity and can offer discounts of up to 90% compared to On-Demand prices. The trade-off is that AWS can reclaim them with a two-minute warning when capacity is needed elsewhere.

---

**148.** Which of the following AWS services can be used to serve large amounts of online video content with the lowest possible latency? (Select TWO)
- A. AppStream 2.0
- B. Amazon Glacier.
- C. Amazon S3. ✅
- D. Amazon Elastic File System (EFS).
- E. Amazon CloudFront. ✅
**Explanation:** Amazon S3 stores video files durably and cost-effectively. Amazon CloudFront delivers that content from edge locations close to viewers worldwide, minimizing latency for video streaming.

---

**149.** In which scenario should Amazon EC2 Spot Instances be used?
- A. A company has a number of infrequent interruptible jobs that are currently using On-Demand Instances. ✅
- B. A company has a number of application services whose SLA requires 99.999% uptime.
- C. A company wants to move its main website to AWS from an on-premises web server.
- D. A company's heavily used legacy database is currently running on-premises.
**Explanation:** Spot Instances are ideal for workloads that are flexible about when they run and can tolerate interruptions, such as batch processing, data analysis, or background jobs that run infrequently.

---

**150.** An engineer wants to deploy AWS Infrastructure as code using a programming language he is familiar with. Which service can be used?
- A. Amazon S3
- B. Amazon CloudFormation
- C. Amazon CloudFront
- D. Cloud Development Kit ✅
**Explanation:** AWS Cloud Development Kit (CDK) lets developers define cloud infrastructure using familiar programming languages like Python, TypeScript, Java, and C#, which are then synthesized into CloudFormation templates.

---

**151.** Which of the following is NOT correct regarding Amazon EC2 On-demand instances?

- A. The on-demand instances follow the AWS pay-as-you-go pricing model.
- B. With on-demand instances no longer-term commitments or upfront payments are needed.
- C. When using on-demand Linux instances you pay a start-up fee when launching a new instance for the first time. ✅
- D. You can spin up on-demand instance whenever you require them.

**Explanation:** There is no start-up fee for On-Demand Linux instances. You simply pay for the compute capacity you use per second (with a minimum of 60 seconds), with no upfront costs or commitments.

---

**152.** What is the AWS service that provides a virtual network dedicated to your AWS account?

- A. AWS Subnets.
- B. AWS Dedicated Hosts.
- C. Amazon VPC. ✅
- D. AWS VPN.

**Explanation:** Amazon VPC (Virtual Private Cloud) lets you provision a logically isolated section of the AWS Cloud where you can launch AWS resources in a virtual network that you define and control.

---

**153.** Which of the following AWS services can be used as a compute resource? (Choose TWO)

- A. Amazon CloudWatch.
- B. Amazon S3.
- C. Amazon EC2. ✅
- D. AWS Lambda. ✅
- E. Amazon VPC.

**Explanation:** Amazon EC2 provides resizable virtual server capacity. AWS Lambda is a serverless compute service that runs code in response to events. Both are core AWS compute services.

---

**154.** Which of the following EC2 instance purchasing options supports the Bring Your Own License (BYOL) model for almost every BYOL scenario?

- A. Dedicated Hosts. ✅
- B. On-demand Instances.
- C. Reserved Instances.
- D. Dedicated Instances.

**Explanation:** Dedicated Hosts provide you with a physical server fully dedicated to your use, giving you visibility into the number of sockets and physical cores. This is required by most BYOL licensing agreements that are tied to per-socket or per-core metrics.

---

**155.** Which pricing model would result in maximum Amazon Elastic Compute Cloud (Amazon EC2) savings for a database server that must be online for one year?

- A. Spot Instance
- B. On-Demand Instance
- C. Partial Upfront Reserved Instance ✅
- D. No Upfront Reserved Instance

**Explanation:** For workloads running continuously for one year, Reserved Instances offer significant savings over On-Demand. Partial Upfront Reserved Instances provide greater discounts than No Upfront, and Spot Instances are unsuitable as they can be interrupted.

---

**156.** A company has a MySQL database running on a single Amazon EC2 instance. The company now requires higher availability in the event of an outage. Which set of tasks would meet this requirement?

- A. Add an Application Load Balancer in front of the EC2 instance
- B. Configure EC2 Auto Recovery to move the instance to another Availability Zone
- C. Migrate to Amazon RDS and enable Multi-AZ ✅
- D. Enable termination protection for the EC2 instance to avoid outages

**Explanation:** Amazon RDS Multi-AZ deployments provide enhanced availability by automatically provisioning a synchronous standby replica in a different Availability Zone, with automatic failover in case of an outage.

---

**157.** A user has limited knowledge of AWS services, but wants to quickly deploy a scalable Node.js application in the AWS Cloud. Which service should be used to deploy the application?

- A. AWS CloudFormation
- B. AWS Elastic Beanstalk ✅
- C. Amazon EC2
- D. AWS OpsWorks

**Explanation:** AWS Elastic Beanstalk is the easiest way to deploy and scale web applications. You simply upload your code and Elastic Beanstalk automatically handles capacity provisioning, load balancing, auto-scaling, and monitoring.

---

**158.** What are the advantages of deploying an application with Amazon EC2 instances in multiple Availability Zones? (Choose two.)

- A. Preventing a single point of failure ✅
- B. Reducing the operational costs of the application
- C. Allowing the application to serve cross-region users with low latency
- D. Increasing the availability of the application ✅
- E. Increasing the load of the application

**Explanation:** Deploying across multiple AZs eliminates single points of failure at the infrastructure level and ensures the application remains available even if one AZ experiences an outage, significantly increasing overall availability.

---

**159.** A workload on AWS will run for the foreseeable future by using a consistent number of Amazon EC2 instances. What pricing model will minimize cost while ensuring that compute resources remain available?

- A. Dedicated Hosts
- B. On-Demand Instances
- C. Spot Instances
- D. Reserved Instances ✅

**Explanation:** Reserved Instances provide up to 72% discount compared to On-Demand pricing in exchange for a 1 or 3-year commitment. For stable, predictable workloads running long-term, they offer the best cost savings while guaranteeing capacity.

---

**160.** Which AWS service allows customers to purchase unused Amazon EC2 capacity at an often discounted rate?

- A. Reserved Instances
- B. On-Demand Instances
- C. Spot Instances ✅
- D. Dedicated Instances

**Explanation:** EC2 Spot Instances let you take advantage of unused EC2 capacity in the AWS cloud at up to 90% off On-Demand prices. They are ideal for flexible, fault-tolerant workloads that can tolerate interruptions.

---

**161.** Which AWS services offer compute capabilities? (Choose two.)

- A. Amazon Macie
- B. Amazon EC2 ✅
- C. Amazon Elastic Block Store (Amazon EBS)
- D. AWS Lambda ✅
- E. Amazon Cognito

**Explanation:** Amazon EC2 provides virtual server compute capacity. AWS Lambda is a serverless compute service that executes code in response to events. Both are fundamental AWS compute services.

---

**162.** A company is expecting a short-term spike in internet traffic for its application. During the traffic increase, the application cannot be interrupted. The company also needs to minimize cost and maximize flexibility. Which Amazon EC2 instance type should the company use to meet these requirements?

- A. Spot Instances
- B. Reserved Instances
- C. Dedicated Hosts
- D. On-Demand Instances ✅

**Explanation:** On-Demand Instances are ideal for short-term, unpredictable workloads that cannot be interrupted. They provide maximum flexibility with no long-term commitments, and you pay only for the compute time you actually use.

---

**163.** How do customers benefit from Amazon's massive economies of scale?

- A. Periodic price reductions as the result of Amazon's operational efficiencies ✅
- B. New Amazon EC2 instance types providing the latest hardware
- C. The ability to scale up and down when needed
- D. Increased reliability in the underlying hardware of Amazon EC2 instances

**Explanation:** Amazon's massive scale allows it to achieve greater efficiencies and pass those savings to customers in the form of lower prices over time — a core benefit of cloud economies of scale.

---

**164.** In which scenario should Amazon EC2 Spot Instances be used?

- A. A company wants to move its main website to AWS from an on-premises web server.
- B. A company has a number of application services whose Service Level Agreement (SLA) requires 99.999% uptime.
- C. A company's heavily used legacy database is currently running on-premises.
- D. Interruptible jobs that are currently using On-Demand Instances. ✅

**Explanation:** Spot Instances are best for flexible, fault-tolerant, and interruptible workloads. They offer up to 90% savings over On-Demand but can be reclaimed by AWS with a 2-minute warning, making them unsuitable for critical or continuous workloads.

---

**165.** Which of the following can limit Amazon Simple Storage Service (Amazon S3) bucket access to specific users?

- A. A public and private key-pair
- B. Amazon Inspector
- C. AWS Identity and Access Management (IAM) policies ✅
- D. Security Groups

**Explanation:** IAM policies and S3 bucket policies allow fine-grained control over who can access S3 buckets and objects. Security groups apply to EC2 instances, not S3.

---

**166.** One benefit of On-Demand Amazon Elastic Compute Cloud (Amazon EC2) pricing is:

- A. The ability to bid for a lower hourly cost.
- B. Paying a daily rate regardless of time used.
- C. Paying only for time used. ✅
- D. Pre-paying for instances and paying a lower hourly rate.

**Explanation:** On-Demand pricing means you pay for compute capacity by the second (minimum 60 seconds) with no long-term commitments or upfront payments. You only pay for what you actually use.

---

**167.** Which service is not part of the AWS serverless platform?

- A. Amazon EC2 ✅
- B. Amazon S3
- C. Amazon Athena
- D. Amazon SQS

**Explanation:** Amazon EC2 requires you to provision, manage, and maintain virtual server instances, including the operating system. This makes it a traditional server-based service, unlike Lambda, S3, Athena, and SQS which are serverless.

---

**168.** What technology enables compute capacity to adjust as loads change?

- A. Load balancing
- B. Automatic failover
- C. Round robin
- D. Auto Scaling ✅

**Explanation:** AWS Auto Scaling monitors your application and automatically adjusts the number of EC2 instances (or other resources) in response to changing demand, ensuring you have the right capacity at the right time.

---

**169.** Which AWS services are defined as global instead of regional? (Select TWO.)

- A. Amazon Route 53 ✅
- B. Amazon EC2
- C. Amazon S3
- D. Amazon CloudFront ✅
- E. Amazon DynamoDB

**Explanation:** Amazon Route 53 (DNS) and Amazon CloudFront (CDN) are global services that operate across all AWS regions and edge locations. EC2, S3, and DynamoDB are regional services.

---

**170.** Which AWS service can be used to manually launch instances based on resource requirements?

- A. Amazon EBS
- B. Amazon S3
- C. Amazon EC2 ✅
- D. Amazon ECS

**Explanation:** Amazon EC2 allows customers to launch virtual server instances of varying sizes and types based on their specific resource requirements, either manually via the console or programmatically.

---

**171.** A company is migrating an application that is running non-interruptible workloads for a three-year time frame. Which pricing construct would provide the MOST cost-effective solution?

- A. Amazon EC2 Spot Instances
- B. Amazon EC2 Dedicated Instances
- C. Amazon EC2 On-Demand Instances
- D. Amazon EC2 Reserved Instances ✅

**Explanation:** Reserved Instances offer up to 72% discount compared to On-Demand pricing in exchange for a 1 or 3-year commitment. For stable, non-interruptible workloads with a predictable duration, they provide the greatest cost savings.

---

**172.** A company wants to reduce the physical compute footprint that developers use to run code. Which service would meet that need by enabling serverless architectures?

- A. Amazon Elastic Compute Cloud (Amazon EC2)
- B. AWS Lambda ✅
- C. Amazon DynamoDB
- D. AWS CodeCommit

**Explanation:** AWS Lambda is a serverless compute service that runs code without provisioning or managing servers. Developers simply upload their code and Lambda handles execution, scaling, and infrastructure management.

---

**173.** Which of the following services falls under the responsibility of the customer to maintain operating system configuration, security patching, and networking?

- A. Amazon EC2 ✅
- B. Amazon ElastiCache
- C. AWS Fargate

**Explanation:** With Amazon EC2, customers are responsible for managing the guest operating system including updates, patching, and network configuration. Managed services like ElastiCache and Fargate abstract these responsibilities away.

---

**174.** Which scenarios represent the concept of elasticity on AWS? (Choose two.)

- A. Scaling the number of Amazon EC2 instances based on traffic. ✅
- B. Resizing Amazon RDS instances as business needs change. ✅
- C. Automatically directing traffic to less-utilized Amazon EC2 instances.
- D. Using AWS compliance documents to accelerate the compliance process.
- E. Having the ability to create and govern environments using code.

**Explanation:** Elasticity means the ability to scale resources up or down based on demand. Adding/removing EC2 instances based on traffic and resizing RDS to match business needs are both examples of elastic scaling.

---

**175.** When is it beneficial for a company to use a Spot Instance?

- A. When there is flexibility in when an application needs to run. ✅
- B. When there are mission-critical workloads.
- C. When dedicated capacity is needed.
- D. When an instance should not be stopped.

**Explanation:** Spot Instances are best for workloads with flexible timing that can tolerate interruptions, such as batch processing, big data analysis, or CI/CD jobs. They offer up to 90% savings over On-Demand pricing.

---

**176.** A company is considering moving its on-premises data center to AWS. What factors should be included in doing a Total Cost of Ownership (TCO) analysis? (Choose two.)

- A. Amazon EC2 instance availability
- B. Power consumption of the data center ✅
- C. Labor costs to replace old servers ✅
- D. Application developer time
- E. Database engine capacity

**Explanation:** A TCO analysis for on-premises vs. cloud must include on-premises costs like electricity for powering and cooling servers, and the labor costs for hardware maintenance and replacement — both of which are eliminated with AWS.

---

**177.** What function do security groups serve in relation to Amazon Elastic Compute Cloud (Amazon EC2) instance security?

- A. Act as a virtual firewall for the Amazon EC2 instance. ✅
- B. Secure AWS user accounts with AWS Identity and Access Management (IAM) policies.
- C. Provide DDoS protection with AWS Shield.
- D. Use Amazon CloudFront to protect the Amazon EC2 instance.

**Explanation:** Security groups act as a stateful virtual firewall for EC2 instances, controlling inbound and outbound traffic at the instance level based on rules you define by port, protocol, and source/destination.

---

**178.** A company needs to deliver images and videos globally with minimal latency. Which AWS services can be used to accomplish this? (Choose 2)

- A. Amazon S3 ✅
- B. VPC
- C. Amazon EC2
- D. Amazon EBS
- E. Amazon CloudFront ✅

**Explanation:** Amazon S3 is ideal for storing large media files like images and videos durably and cost-effectively. Amazon CloudFront, a global CDN, then delivers that content from edge locations closest to each user, minimizing latency.

---

**179.** Which Amazon EC2 pricing model offers the MOST significant discount when compared to On-Demand Instances?

- A. Partial Upfront Reserved Instances for a 1-year term
- B. All Upfront Reserved Instances for a 1-year term
- C. All Upfront Reserved Instances for a 3-year term ✅

**Explanation:** The greatest EC2 discount comes from All Upfront Reserved Instances with a 3-year term, which can save up to 72% compared to On-Demand pricing. Longer commitment plus full upfront payment yields the highest discount.

---

**180.** Which services manage and automate application deployments on AWS? (Choose two.)

- A. AWS Elastic Beanstalk ✅
- B. AWS CodeCommit
- C. AWS Data Pipeline
- D. AWS CodeDeploy ✅

**Explanation:** AWS Elastic Beanstalk automates deployment including provisioning, load balancing, and scaling. AWS CodeDeploy automates code deployments to EC2 instances, Lambda functions, and on-premises servers.

---

**181.** What is an example of high availability in the AWS Cloud?

- A. Consulting AWS technical support at any time day or night
- B. Ensuring an application remains accessible even if a resource fails ✅
- C. Setting termination protection on EC2 Instances

**Explanation:** High availability means designing systems so they continue operating even when individual components fail. Deploying across multiple AZs ensures the application stays accessible even if one instance or AZ goes down.

---

**182.** A company wants to monitor the CPU usage of its Amazon EC2 resources. Which AWS service should the company use?

- A. AWS CloudTrail
- B. Amazon CloudWatch ✅
- C. AWS Cost and Usage report

**Explanation:** Amazon CloudWatch collects and tracks metrics including CPU utilization, network traffic, and disk I/O for EC2 instances. You can set alarms to notify you when metrics exceed defined thresholds.

---

**183.** What are the advantages of Reserved Instances? (Choose two.)

- A. They provide a discount over on-demand pricing. ✅
- B. They provide access to additional instance types.
- C. They provide additional networking capability.
- D. They lead to cost savings from using compute resources ✅

**Explanation:** Reserved Instances offer significant discounts (up to 72%) compared to On-Demand pricing in exchange for committing to a 1 or 3-year term, directly reducing the total cost of running compute workloads.

---

**184.** How do Amazon EC2 Auto Scaling groups help achieve high availability for a web application?

- A. They automatically add more instances across multiple AWS Regions based on global demand of the application.
- B. They automatically add or replace instances across multiple Availability Zones when the application needs it. ✅
- C. They enable the application's static content to reside closer to end users.

**Explanation:** EC2 Auto Scaling groups maintain the desired number of instances across multiple AZs, automatically launching replacements if an instance becomes unhealthy and adding capacity during demand spikes.

---

**185.** How can one AWS account use Reserved Instances from another AWS account?

- A. By using Amazon EC2 Dedicated Instances
- B. By using AWS Organizations consolidated billing ✅
- C. By using the AWS Cost Explorer tool

**Explanation:** When accounts are linked under AWS Organizations with consolidated billing, Reserved Instance discounts are shared across all member accounts. An unused Reserved Instance in one account can automatically apply its discount to matching usage in another account.

---

**186.** A customer runs an On-Demand Amazon Linux EC2 instance for 3 hours, 5 minutes, and 6 seconds. For how much time will the customer be billed?

- A. 3 hours
- B. 3 hours 5 minutes 6 Seconds ✅
- C. 3 hours 5 minutes
- D. 3 hours 6 minutes

**Explanation:** Amazon Linux EC2 On-Demand instances are billed per second with a minimum of 60 seconds. After the first minute, billing is exact to the second, so the customer pays for exactly 3 hours, 5 minutes, and 6 seconds.

---

**187.** Which services use AWS edge locations? (Choose two.)

- A. Amazon CloudFront ✅
- B. AWS Shield ✅
- C. Amazon EC2
- D. Amazon EBS

**Explanation:** Amazon CloudFront delivers cached content from edge locations worldwide. AWS Shield Standard is automatically applied at AWS edge locations to protect against DDoS attacks. EC2 and EBS are regional services that do not use edge locations.

---

**188.** Which AWS service provides inbound and outbound network ACLs to harden external connectivity to Amazon EC2?

- A. AWS IAM
- B. Amazon Connect
- C. Amazon VPC ✅
- D. Amazon EC2

**Explanation:** Amazon VPC includes Network Access Control Lists (NACLs) that act as stateless firewalls at the subnet level, controlling inbound and outbound traffic to protect EC2 instances from unauthorized network access.

---

**189.** The pay-as-you-go pricing model for AWS services:

- A. Reduces capital expenditures. ✅
- B. Requires payment up front for AWS services.
- C. Is relevant only for Amazon EC2
- D. Gifts all AWS Services to Customers

**Explanation:** The pay-as-you-go model eliminates large upfront capital expenditures for hardware. Instead of buying servers, you pay only for the cloud resources you actually consume, shifting costs to operational expenditure.

---

**190.** Which of the following are compute services provided by AWS? (Choose 3)

- A. Amazon Lightsail ✅
- B. Amazon EC2 ✅
- C. Amazon S3
- D. AWS Lambda ✅
- E. Amazon ECS

**Explanation:** Amazon Lightsail (virtual private servers), Amazon EC2 (virtual machines), and AWS Lambda (serverless functions) are all compute services. Amazon S3 is object storage, and Amazon ECS is a container orchestration platform that uses underlying compute.

---

**191.** Which of the following is an example of horizontal scaling in the AWS Cloud?
- A. Replacing an existing EC2 instance with a larger, more powerful one.
- B. Increasing the compute capacity of a single EC2 instance to address the growing demands of an application.
- C. Adding more RAM capacity to an EC2 instance.
- D. Adding more EC2 instances of the same size to handle an increase in traffic. ✅

---

**192.** You have noticed that several critical Amazon EC2 instances have been terminated. Which of the following AWS services would help you determine who took this action?
- A. Amazon Inspector.
- B. AWS CloudTrail. ✅
- C. AWS Trusted Advisor.
- D. EC2 Instance Usage Report.

---

**193.** You have set up consolidated billing for several AWS accounts. One of the accounts has purchased a number of reserved instances for 3 years. Which of the following is true regarding this scenario?
- A. The Reserved Instance discounts can only be shared with the master account.
- B. All accounts can receive the hourly cost benefit of the Reserved Instances. ✅
- C. The purchased instances will have better performance than On-demand instances.
- D. There are no cost benefits from using consolidated billing; It is for informational purposes only.

---

**194.** A Japanese company hosts their applications on Amazon EC2 instances in the Tokyo Region. The company has opened new branches in the United States, and the US users are complaining of high latency. What can the company do to reduce latency for the users in the US while minimizing costs?
- A. Applying the Amazon Connect latency-based routing policy.
- B. Registering a new US domain name to serve the users in the US.
- C. Building a new data center in the US and implementing a hybrid model.
- D. Deploying new Amazon EC2 instances in a Region located in the US. ✅

---

**195.** Adjusting compute capacity dynamically to reduce cost is an implementation of which AWS cloud best practice?
- A. Build security in every layer.
- B. Parallelize tasks.
- C. Implement elasticity. ✅
- D. Adopt monolithic architecture.

---

**196.** Which of the following helps a customer view the Amazon EC2 billing activity for the past month?
- A. AWS Budgets.
- B. AWS Pricing Calculator.
- C. AWS Systems Manager.
- D. AWS Cost & Usage Reports. ✅

---

**197.** You want to run a questionnaire application for only one day (without interruption), which Amazon EC2 purchase option should you use?
- A. Reserved instances.
- B. Spot instances.
- C. Dedicated instances.
- D. On-demand instances. ✅

---

**198.** You are working on a project that involves creating thumbnails of millions of images. Consistent uptime is not an issue, and continuous processing is not required. Which EC2 buying option would be the most cost-effective?
- A. Reserved Instances.
- B. On-demand Instances.
- C. Dedicated Instances.
- D. Spot Instances. ✅

---

**199.** In order to implement best practices when dealing with a “Single Point of Failure,” you should attempt to build as much automation as possible in both detecting and reacting to failure. Which of the following AWS services would help? (Choose TWO)
- A. ELB. ✅
- B. Auto Scaling. ✅
- C. Amazon Athen.
- D. ECR.
- E. Amazon EC2.

---

**200.** A developer is planning to build a two-tier web application that has a MySQL database layer. Which of the following AWS database services would provide automated backups for the application?
- A. A MySQL database installed on an EC2 instance.
- B. Amazon Aurora. ✅
- C. Amazon DynamoDB.
- D. Amazon Neptune.

---

**201.** You have deployed your application on multiple Amazon EC2 instances. Your customers complain that sometimes they can’t reach your application. Which AWS service allows you to monitor the performance of your EC2 instances to assist in troubleshooting these issues?
- A. AWS Lambda.
- B. AWS Config.
- C. Amazon CloudWatch. ✅
- D. AWS CloudTrail.

---

**202.** An organization has decided to purchase an Amazon EC2 Reserved Instance (RI) for three years in order to reduce costs. It is possible that the application workloads could change during the reservation period. What is the EC2 Reserved Instance (RI) type that will allow the company to exchange the purchased reserved instance for another reserved instance with higher computing power if they need to?
- A. Elastic RI.
- B. Premium RI.
- C. Standard RI.
- D. Convertible RI. ✅

---

**203.** Which of the following Reserved Instance (RI) pricing models provides the highest average savings compared to On-Demand pricing?
- A. One-year, No Upfront, Standard RI pricing.
- B. One-year, All Upfront, Convertible RI pricing.
- C. Three-year, All Upfront, Standard RI pricing. ✅
- D. Three-year, No Upfront, Convertible RI pricing.

---

**204.** Which of the following is an AWS-managed compute service?
- A. Amazon SWF.
- B. Amazon EC2.
- C. AWS Lambda. ✅
- D. Amazon Aurora.

---

**205.** A company wants to reduce the physical compute footprint that developers use to run code. Which service would meet that need by enabling serverless architectures?
- A. Amazon Elastic Compute Cloud (Amazon EC2).
- B. AWS Lambda. ✅
- C. Amazon DynamoDB.
- D. AWS CodeCommit.

---

**206.** Which Amazon EC2 pricing model offers the MOST significant discount when compared to OnDemand Instances?
- A. A Partial Upfront Reserved Instances for a 1-year term.
- B. All Upfront Reserved instances for a 1 year form.
- C. All Upfront Reserved Instances for a 3 year term. ✅
- D. No Upfront Reserved Instances for a 3 year term.

---

**207.** A user must meet compliance and software licensing requirements that state a workload must be hosted on a physical server. When Amazon EC2 instance pricing option will meet these requirements?
- A. Dedicated Hosts. ✅
- B. Dedicated Instances.
- C. Spot Instances.
- D. Reserved Instances.

---

**208.** Which of the Reserved Instance (RI) pricing models can change the attributes of the RI as long as the exchange results in the creation of RIs of equal or greater value?
- A. Dedicated RIs.
- B. Scheduled RIs.
- C. Convertible RIs. ✅
- D. Standard RIs.

---

**209.** Which service is best for storing common database query results, which helps to alleviate database access load?
- A. Amazon Machine Learning.
- B. Amazon SQS.
- C. Amazon ElastiCache. ✅
- D. Amazon EC2 Instance Store.

---

**210.** When should a company consider using Amazon EC2 Spot Instances? (Select TWO)
- A. For non-production applications. ✅
- B. For stateful workloads.
- C. For applications that cannot have interruptions.
- D. For fault-tolerant flexible applications. ✅
- E. For sensitive database applications.

---

**211.** A company wants to focus on business activities instead of managing compute and capacity. Which AWS service can be used to automatically add or remove Amazon EC2 instances based on demand?
- A. Elastic Load Balancer.
- B. Amazon EC2 Auto Scaling. ✅
- C. Amazon Route 53.
- D. Amazon CloudFront.

---

**212.** Access keys in AWS Identity and Access Management (IM1) are used to:
- A. Log in to the AWS Management Console.
- B. Make programmatic calls to AWS from AWS APIs. ✅
- C. Log in to Amazon EC2 instances.
- D. Authenticate to AWS CodeCommit repositories.

---

**213.** Web servers running on Amazon EC2 access a legacy application running in a corporate data center. What term would describe this model?
- A. Cloud-native.
- B. Partner network.
- C. Hybrid architecture. ✅
- D. Infrastructure as a service.

---

**214.** Which AWS services can host a Microsoft SQL Server database? (Select TWO)
- A. Amazon EC2. ✅
- B. Amazon Relational Database Service (Amazon RDS). ✅
- C. Amazon Aurora.
- D. Amazon Redshift.
- E. Amazon S3.

---

**215.** What is the lowest-cost, durable storage option for retaining database backups for immediate retrieval?
- A. Amazon S3. ✅
- B. Amazon Glacier.
- C. Amazon EBS.
- D. Amazon EC2 Instance Store.

---

**216.** Which of the following is a shared control between the customer and AWS?
- A. Providing a key for Amazon S3 client-side encryption.
- B. Configuration of an Amazon EC2 instance.
- C. Environmental controls of physical AWS data centers.
- D. Awareness. ✅

---

**217.** Which type of AWS storage is ephemeral and is deleted when an instance is stopped Of terminated?
- A. Amazon EBS.
- B. Amazon EC2 instance store. ✅
- C. Amazon EFS.
- D. Amazon S3.

---

**218.** Which services are parts of the AWS serverless platform?
- A. Amazon EC2, Amazon S3, Amazon Athena.
- B. Amazon Kinesis, Amazon SQS, Amazon EMR.
- C. AWS Step Functions, Amazon DynamoDB, Amazon SNS. ✅
- D. Amazon Athena, Amazon Cognito, Amazon EC2.

---

**219.** Which of the following Amazon EC2 pricing models allow customers to use existing server-bound software licenses?
- A. Spot Instances.
- B. Reserved Instances.
- C. Dedicated Hosts. ✅
- D. On-Demand Instances.

---

**220.** When performing a cost analysis that supports physical isolation of a customer workload, which compute hosting model should be accounted for in the Total Cost of Ownership (TCO)?
- A. Dedicated Hosts ✅
- B. Reserved Instances
- C. On-Demand Instances
- D. No Upfront Reserved Instances

---

**221.** Which Amazon EC2 instance pricing model can provide discounts of up to 90%?
- A. Reserved Instances.
- B. On-Demand.
- C. Dedicated Hosts.
- D. Spot Instances. ✅

---

**222.** In which scenario should Amazon EC2 Spot Instances be used?
- A. A company wants to move its main website to AWS from an on-premises web server.
- B. A company has a number of application services whose Service Level Agreement (SLA) requires 99.999% uptime.
- C. A company’s heavily used legacy database is currently running on-premises.
- D. A company has a number of infrequent, interruptible jobs that are currently using On-Demand Instances. ✅

---

**223.** One benefit of On-Demand Amazon Elastic Compute Cloud (Amazon EC2) pricing is:
- A. The ability to bid for a lower hourly cost.
- B. Paying a daily rate regardless of time used.
- C. Paying only for time used. ✅
- D. Pre-paying for instances and paying a lower hourly rate.

---

**224.** A characteristic of edge locations is that they:
- A. Host Amazon EC2 instances closer to users.
- B. Help lower latency and improve performance for users. ✅
- C. Cache frequently changing data without reaching the origin server.
- D. Refresh data changes daily.

---

**225.** A company is migrating an application that is running non-interruptible workloads for a three-year time frame. Which pricing construct would provide the MOST cost-effective solution?
- A. Amazon EC2 Spot Instances.
- B. Amazon EC2 Dedicated Instances.
- C. Amazon EC2 On-Demand Instances.
- D. Amazon EC2 Reserved Instances. ✅

---

**226.** How can one AWS account use Reserved Instances from another AWS account?
- A. By using Amazon EC2 Dedicated Instances.
- B. By using AWS Organizations consolidated billing. ✅
- C. By using the AWS Cost Explorer tool.
- D. By using AWS Budgets.

---

**227.** Which of the following services falls under the responsibility of the customer to maintain operating system configuration, security patching, and networking?
- A. Amazon RDS.
- B. Amazon EC2. ✅
- C. Amazon ElastiCache.
- D. AWS Fargate.

---

**228.** Which Amazon EC2 pricing model adjusts based on supply and demand of EC2 instances?
- A. On-Demand Instances.
- B. Reserved Instances.
- C. Spot Instances. ✅
- D. Convertible Reserved Instances.

---

**229.** A Cloud Practitioner must determine if any security groups in an AWS account have been provisioned to allow unrestricted access for specific ports. What is the SIMPLEST way to do this?
- A. Review the inbound rules for each security group in the Amazon EC2 management console to check for port 0.0.0.0/0.
- B. Run AWS Trusted Advisor and review the findings. ✅
- C. Open the AWS IAM console and check the inbound rule filters for open access.
- D. In AWS Config, create a custom rule that invokes an AWS Lambda function to review firewall rules for inbound access.

---

**230.** Which of the following services have Distributed Denial of Service (DDoS) mitigation features? (Select TWO)
- A. AWS WAF. ✅
- B. Amazon DynamoDB.
- C. Amazon EC2.
- D. Amazon CloudFront. ✅
- E. Amazon Inspector.

---

**231.** Which of the following AWS features enables a user to launch a pre-configured Amazon Elastic Compute Cloud (Amazon EC2) instance?
- A. Amazon Elastic Block Store (Amazon EBS).
- B. Amazon Machine Image. ✅
- C. Amazon EC2 Systems Manager.
- D. Amazon AppStream 2.0.

---

**232.** How do Amazon EC2 Auto Scaling groups help achieve high availability for a web application?
- A. They automatically add more instances across multiple AWS Regions based on global demand of the application.
- B. They automatically add or replace instances across multiple Availability Zones when the application needs it. ✅
- C. They enable the application’s stalk: content to reside closer to end users.
- D. They are able to distribute incoming requests across a tier of web server instances.

---

**233.** Which of the following tasks is the responsibility of AWS?
- A. Encrypting client-side data.
- B. Configuring AWS Identity and Access Management (IAM) roles.
- C. Securing the Amazon EC2 hypervisor. ✅
- D. Setting user password policies.

---

**234.** A company is considering using AWS for a self-hosted database that requires a nightly shutdown for maintenance and cost-saving purposes. Which service should the company use?
- A. Amazon Redshift.
- B. Amazon DynamoDB.
- C. Amazon Elastic Compute Cloud (Amazon EC2) with Amazon EC2 instance store.
- D. Amazon EC2 with Amazon Elastic Block Store (Amazon EBS). ✅

---

**235.** Which of the following is NOT correct regarding Amazon EC2 On-demand instances?
- A. You have to pay a start-up fee when launching a new instance for the first time. ✅
- B. The on-demand instances follow the AWS pay-as-you-go pricing model.
- C. With on-demand instances, no longer-term commitments or upfront payments are needed.
- D. When using on-demand Linux instances, you are charged per second based on an hourly rate.

---

**236.** According to the AWS Acceptable Use Policy, which of the following statements is true regarding penetration testing of EC2 instances?
- A. Penetration testing is not allowed in AWS.
- B. Penetration testing is performed automatically by AWS to determine vulnerabilities in your AWS infrastructure.
- C. Penetration testing can be performed by the customer on their own instances without prior authorization from AWS. ✅
- D. The AWS customers are only allowed to perform penetration testing on services managed by AWS.

---

**237.** What is the AWS service that provides a virtual network dedicated to your AWS account?
- A. AWS VPN.
- B. AWS Subnets.
- C. AWS Dedicated Hosts.
- D. Amazon VPC. ✅

---

**238.** Which of the following AWS services can be used as a compute resource? (Choose TWO)
- A. Amazon VPC.
- B. Amazon CloudWatch.
- C. Amazon S3.
- D. Amazon EC2. ✅
- E. AWS Lambda. ✅

---

**239.** Which of the following EC2 instance purchasing options supports the Bring Your Own License (BYOL) model for almost every BYOL scenario?
- A. Dedicated Instances.
- B. Dedicated Hosts. ✅
- C. On-demand Instances.
- D. Reserved Instances.

---

**240.** What is the AWS service that provides you the highest level of control over the underlying virtual infrastructure?
- A. Amazon Redshift.
- B. Amazon DynamoDB.
- C. Amazon EC2. ✅
- D. Amazon RDS.

---

**241.** In your on-premises environment, you can create as many virtual servers as you need from a single template. What can you use to perform the same in AWS?
- A. IAM.
- B. An internet gateway.
- C. EBS Snapshot.
- D. AMI. ✅

---

**242.** What are two advantages of using Cloud Computing over using traditional data centers? (Choose TWO)
- A. Reserved Compute capacity.
- B. Eliminating Single Points of Failure (SPOFs). ✅
- C. Distributed infrastructure. ✅
- D. Virtualized compute resources.
- E. Dedicated hosting.

---

**243.** Which of the following services allows you to run containerized applications on a cluster of EC2 instances?
- A. Amazon ECS. ✅
- B. AWS Data Pipeline.
- C. AWS Cloud9.
- D. AWS Personal Health Dashboard.

---

**244.** What are the AWS services/features that can help you maintain a highly available and fault-tolerant architecture in AWS? (Choose TWO)
- A. AWS Direct Connect.
- B. Amazon EC2 Auto Scaling. ✅
- C. Elastic Load Balancer. ✅
- D. CloudFormation.
- E. Network ACLs.

---

**245.** Which of the following activities may help reduce your AWS monthly costs?
- A. Enabling Amazon EC2 Auto Scaling for all of your workloads. ✅
- B. Using the AWS Network Load Balancer (NLB) to load balance the incoming HTTP requests.
- C. Removing all of your Cost Allocation Tags.
- D. Deploying your AWS resources across multiple Availability Zones.

---

**246.** Which of the following AWS security features is associated with an EC2 instance and functions to filter incoming traffic requests?
- A. AWS X-Ray.
- B. Network ACL.
- C. Security Groups. ✅
- D. VPC Flow logs.

---

**247.** What is the AWS serverless service that allows you to run your applications without any administrative burden?
- A. Amazon LightSail.
- B. AWS Lambda. ✅
- C. Amazon RDS instances.
- D. Amazon EC2 instances.

---

**248.** Jessica is managing an e-commerce web application in AWS. The application is hosted on six EC2 instances. One day, three of the instances crashed; but none of her customers were affected. What has Jessica done correctly in this scenario?
- A. She has properly built an elastic system.
- B. She has properly built a fault tolerant system. ✅
- C. She has properly built an encrypted system.
- D. She has properly built a scalable system.

---

**249.** Which of the following describes the payment model that AWS makes available for customers that can commit to using Amazon EC2 over a one or 3-year term to reduce their total computing costs?
- A. Pay less as AWS grows.
- B. Pay as you go.
- C. Pay less by using more.
- D. Save when you reserve. ✅

---

**250.** Sarah has deployed an application in the Northern California (us-west-1) region. After examining the application’s traffic, she notices that about 30% of the traffic is coming from Asia. What can she do to reduce latency for the users in Asia?
- A. Replicate the current resources across multiple Availability Zones within the same region.
- B. Migrate the application to a hosting provider in Asia.
- C. Recreate the website content.
- D. Create a CDN using CloudFront, so that content is cached at Edge Locations close to and in Asia. ✅

---

**251.** Using Amazon EC2 falls under which of the following cloud computing models?
- A. Iaas & SaaS.
- B. IaaS. ✅
- C. SaaS.
- D. PaaS.

---

**252.** Amazon Glacier is an Amazon S3 storage class that is suitable for storing [...] & [...]. (Choose TWO)
- A. Active archives. ✅
- B. Dynamic websites’ assets.
- C. Long-term analytic data. ✅
- D. Active databases.
- E. Cached data.

---

**253.** What is the AWS service that performs automated network assessments of Amazon EC2 instances to check for vulnerabilities?
- A. Amazon Kinesis.
- B. Security groups.
- C. Amazon Inspector. ✅
- D. AWS Network Access Control Lists.

---

**254.** A company needs to host a database in Amazon RDS for at least three years. Which of the following options would be the most cost-effective solution?
- A. Reserved instances     - No Upfront.
- B. Reserved instances     - Partial Upfront. ✅
- C. On-Demand instances.
- D. Spot Instances.

---

**255.** Savings Plans are available for which of the following AWS compute services? (Choose TWO)
- A. AWS Batch.
- B. AWS Outposts.
- C. Amazon Lightsail.
- D. Amazon EC2. ✅
- E. AWS Lambda. ✅

---

**256.** A company has deployed a new web application on multiple Amazon EC2 instances. Which of the following should they use to ensure that the incoming HTTP traffic is distributed evenly across the instances?
- A. AWS EC2 Auto Recovery.
- B. AWS Auto Scaling.
- C. AWS Network Load Balancer.
- D. AWS Application Load Balancer. ✅

---

**257.** Which of the following can help protect your EC2 instances from DDoS attacks? (Choose TWO)
- A. AWS CloudHSM.
- B. Security Groups. ✅
- C. AWS Batch.
- D. AWS IAM.
- E. Network Access Control Lists (Network ACLs). ✅

---

**258.** How are AWS customers billed for Linux-based Amazon EC2 usage?
- A. EC2 instances will be billed on one second increments, with a minimum of one minute. ✅
- B. EC2 instances will be billed on one hour increments, with a minimum of one day.
- C. EC2 instances will be billed on one minute increments, with a minimum of one hour.
- D. EC2 instances will be billed on one day increments, with a minimum of one month.

---

**259.** Which of the following will impact the price paid for an EC2 instance? (Choose TWO)
- A. Instance type. ✅
- B. The Availability Zone where the instance is provisioned. ✅
- C. Load balancing.
- D. Number of buckets.
- E. Number of private IPs.

---

**260.** A customer spent a lot of time configuring a newly deployed Amazon EC2 instance. After the workload increases, the customer decides to provision another EC2 instance with an identical configuration. How can the customer achieve this?
- A. By creating an AWS Config template from the old instance and launching a new instance from it.
- B. By creating an EBS Snapshot of the old instance.
- C. By installing Aurora on EC2 and launching a new instance from it.
- D. By creating an AMI from the old instance and launching a new instance from it. ✅

---

**261.** A company has developed a media transcoding application in AWS. The application is designed to recover quickly from hardware failures. Which one of the following types of instance would be the most cost-effective choice to use?
- A. Reserved instances.
- B. Spot Instances. ✅
- C. On-Demand instances.
- D. Dedicated instances.

---

**262.** What is one benefit and one drawback of buying a reserved EC2 instance? (Select TWO)
- A. Instances can be shut down by AWS at any time with no notification.
- B. Reserved instances require at least a one-year pricing commitment. ✅
- C. There is no additional charge for using dedicated instances.
- D. Reserved instances provide a significant discount compared to on-demand instances. ✅
- E. Reserved instances are best suited for periodic workloads.

---

**263.** What is the most cost-effective purchasing option for running a set of EC2 instances that must always be available for a period of two months?
- A. On-Demand Instances. ✅
- B. Spot Instances.
- C. Reserved Instances     - All Upfront.
- D. Reserved Instances     - No Upfront.

---

**264.** Which of the following AWS services scale automatically without your intervention? (Choose TWO)
- A. Amazon EC2.
- B. Amazon S3. ✅
- C. AWS Lambda. ✅
- D. Amazon EMR.
- E. Amazon EBS.

---

**265.** A company is planning to migrate an application from Amazon EC2 to AWS Lambda to use a serverless architecture. Which of the following will be the responsibility of AWS after migration? (Choose TWO)
- A. Application management.
- B. Capacity management. ✅
- C. Access control.
- D. Operating system maintenance. ✅
- E. Data management.

---

**266.** A company needs to migrate their website from on-premises to AWS. Security is a major concern for them, so they need to host their website on hardware that is NOT shared with other AWS customers. Which of the following EC2 instance options meets this requirement?
- A. On-demand instances.
- B. Spot instances.
- C. Dedicated instances. ✅
- D. Reserved instances.

---

**267.** How can AWS customers track and avoid over-spending on underutilized reserved instances?
- A. Customers can add all AWS accounts to an AWS Organization, enable Consolidated Billing, and turn off Reserved Instance sharing.
- B. Customers can use Amazon Neptune to track and analyze their usage patterns, detect underutilized reserved instances, and then sell them on the Amazon EC2 Reserved Instance Marketplace.
- C. Customers can use the AWS Budgets service to track the reserved instances usage and set up alert notifications when their utilization drops below the threshold that they define. ✅
- D. Customers can use Amazon CloudTrail to automatically check for unused reservations and get recommendations to reduce their bill.

---

**268.** What does AWS Service Catalog provide?
- A. It enables customers to quickly find descriptions and use cases for AWS services.
- B. It enables customers to explore the different catalogs of AWS services.
- C. It simplifies organizing and governing commonly deployed IT services. ✅
- D. It allows developers to deploy infrastructure on AWS using familiar programming languages.

---

**269.** A company is trying to analyze the costs applied to their AWS account recently. Which of the following provides them the most granular data about their AWS costs and usage?
- A. Amazon Machine Image.
- B. AWS Cost Explorer.
- C. AWS Cost & Usage Report. ✅
- D. Amazon CloudWatch.

---

**270.** Which of the below are responsibilities of the customer when using Amazon EC2? (Choose TWO)
- A. Protecting sensitive data. ✅
- B. Patching of the underlying infrastructure.
- C. Setup and operation of managed databases.
- D. Maintaining consistent hardware components.
- E. Installing and configuring third-party software. ✅

---

**271.** Which of the following is NOT a characteristic of Amazon Elastic Compute Cloud (Amazon EC2)?
- A. Amazon EC2 is considered a Serverless Web Service. ✅
- B. Amazon EC2 eliminates the need to invest in hardware upfront.
- C. Amazon EC2 can launch as many or as few virtual servers as needed.
- D. Amazon EC2 offers scalable computing.

---

**272.** What is the AWS Compute service that executes code only when triggered by events?
- A. AWS Lambda. ✅
- B. Amazon CloudWatch.
- C. AWS Transit Gateway.
- D. Amazon EC2.

---

**273.** Both AWS and traditional IT distributors provide a wide range of virtual servers to meet their customers’ requirements. What is the name of these virtual servers in AWS?
- A. Amazon EBS Snapshots.
- B. Amazon VPC.
- C. AWS Managed Servers.
- D. Amazon EC2 Instances. ✅

---

**274.** One of the major advantages of using AWS is cost savings. What does AWS provide to reduce the cost of running Amazon EC2 instances?
- A. Low monthly instance maintenance costs.
- B. Low-cost instance tagging.
- C. Per-second instance billing. ✅
- D. Low instance start-up fees.

---

**275.** You decide to buy a reserved instance for a term of one year. Which option provides the largest total discount?
- A. All up-front reservation. ✅
- B. All reserved instance payment options provide the same discount level.
- C. Partial up-front reservation.
- D. No up-front reservation.

---

**276.** A company has a web application that is hosted on a single EC2 instance and is approaching 100 percent CPU Utilization during peak loads. Rather than scaling the server vertically, the company has decided to deploy three Amazon EC2 instances in parallel and to distribute traffic across the three servers. What AWS Service should the company use to distribute the traffic evenly?
- A. AWS Global Accelerator.
- B. AWS Application Load Balancer (ALB). ✅
- C. Amazon CloudFront.
- D. Transit VPC.

---

**277.** Which of the following approaches will help you eliminate human error and automate the process of creating and updating your AWS environment?
- A. Use Software test automation tools.
- B. Use AWS CodeDeploy to build and automate your AWS environment.
- C. Use code to provision and operate your AWS infrastructure. ✅
- D. Migrate all of your applications to a dedicated host.

---

**278.** What are the advantages of using Auto Scaling Groups for EC2 instances?
- A. Auto Scaling Groups caches the most recent responses at global edge locations to reduce latency and improve performance.
- B. Auto Scaling Groups scales EC2 instances in multiple Availability Zones to increase application availability and fault tolerance. ✅
- C. Auto Scaling Groups scales EC2 instances across multiple regions to reduce latency for global users.
- D. Auto Scaling Groups distributes application traffic across multiple Availability Zones to enhance performance.

---

**279.** Which of the following is NOT a factor when estimating the costs of Amazon EC2? (Choose TWO)
- A. The amount of time the instances will be running.
- B. Number of security groups. ✅
- C. Allocated Elastic IP Addresses.
- D. Number of Hosted Zones. ✅
- E. Number of instances.

---

**280.** Which of the following AWS offerings are serverless services? (Choose TWO)
- A. Amazon EC2.
- B. AWS Lambda. ✅
- C. Amazon DynamoDB. ✅
- D. Amazon EMR.
- E. Amazon RDS.

---

**281.** Which AWS Service provides integration with Chef to automate the configuration of EC2 instances?
- A. AWS Config.
- B. AWS OpsWorks. ✅
- C. AutoScaling.
- D. AWS CloudFormation.

---

**282.** A company is migrating a web application to AWS. The application’s compute capacity is continually utilized throughout the year. Which of the below options offers the company the most cost-effective solution?
- A. On-demand Instances.
- B. Dedicated Hosts.
- C. Spot Instances.
- D. Reserved Instances. ✅

---

**283.** When granting permissions to applications running on Amazon EC2 instances, which of the following is considered best practice?
- A. Generate new IAM access keys every time you delegate permissions.
- B. Store the required AWS credentials directly within the application code.
- C. Use temporary security credentials (IAM roles) instead of long-term access keys. ✅
- D. Do nothing; Applications that run on Amazon EC2 instances do not need permission to interact with other AWS services or resources.

---

**284.** According to best practices, which of the below options is best suited for processing a large number of binary files?
- A. Vertically scaling EC2 instances.
- B. Running RDS instances in parallel.
- C. Vertically scaling RDS instances.
- D. Running EC2 instances in parallel. ✅

---

**285.** Which AWS Service offers an NFS file system that can be mounted concurrently from multiple EC2 instances?
- A. Amazon Elastic File System. ✅
- B. Amazon Simple Storage Service.
- C. Amazon Elastic Block Store.
- D. AWS Storage Gateway.

---

**286.** Which AWS Service can perform health checks on Amazon EC2 instances?
- A. AWS CloudFormation.
- B. Amazon Route 53. ✅
- C. Amazon Chime.
- D. Amazon Aurora.

---

**287.** Which of the following are examples of AWS-managed databases? (Choose TWO)
- A. Amazon Neptune. ✅
- B. Amazon CloudSearch.
- C. Microsoft SQL Server on Amazon EC2.
- D. MySQL on Amazon EC2.
- E. Amazon RDS for MySQL. ✅

---

**288.** A company’s AWS workflow requires that it periodically perform large-scale image and video processing jobs. The customer is seeking to minimize cost and has stated that the amount of time it takes to process these jobs is not critical, but that cost minimization is the most important factor in designing the solution. Which EC2 instance class is best suited for this processing?
- A. EC2 On-Demand Instances.
- B. EC2 Reserved Instances     - No Upfront.
- C. EC2 Spot Instances. ✅
- D. EC2 Reserved Instances     - All Upfront.

---

**289.** Which statement is true in relation to the security of Amazon EC2?
- A. You should use instance store volumes to store login data.
- B. You should regularly patch the operating system and applications on your EC2 instances. ✅
- C. You should deploy critical components of your application in the Availability Zone that you trust.
- D. You can track all API calls using Amazon Athena.

---

**290.** You are using several on-demand EC2 Instances to run your development environment. What is the best way to reduce your charges when these instances are not in use?
- A. Deleting all EBS volumes attached to the instances.
- B. You cannot minimize charges for on-demand instances.
- C. Terminating the instances.
- D. Stopping the instances. ✅

---

**291.** Which of the following is an available option when purchasing Amazon EC2 instances?
- A. The ability to bid to get the lowest possible prices.
- B. The ability to register EC2 instances to get volume discounts on every hour the instances are running.
- C. The ability to buy Dedicated Instances for up to 90% discount.
- D. The ability to pay upfront to get lower hourly costs. ✅

---

**292.** A company experiences fluctuations in traffic patterns to their e-commerce website when running flash sales. What service can help the company dynamically match the required compute capacity to handle spikes in traffic during flash sales?
- A. AWS Auto Scaling. ✅
- B. Amazon Elastic Compute Cloud.
- C. Amazon Elastic File System.
- D. Amazon ElastiCache.

---

**293.** Which of the following AWS services uses Puppet to automate how EC2 instances are configured?
- A. AWS OpsWorks. ✅
- B. AWS CloudFormation.
- C. AWS Quick Starts.
- D. AWS CloudTrail.

---

**294.** Which of the following are valid Amazon EC2 Reserved Instance types? (Choose TWO)
- A. Convertible. ✅
- B. Expedited.
- C. Bulk.
- D. Spot.
- E. Standard. ✅

---

**295.** You manage a blog on AWS that has different environments: development, testing, and production. What can you use to create a custom console for each environment to view and manage your resources easily?
- A. AWS Resource Groups. ✅
- B. AWS Placement Groups.
- C. AWS Management Console.
- D. AWS Tag Editor.

---

**296.** Which AWS service collects metrics from running EC2 instances?
- A. Amazon Inspector.
- B. Amazon CloudWatch. ✅
- C. AWS CloudFormation.
- D. AWS CloudTrail.

---

**297.** Which of the following compute resources are serverless? (Choose TWO)
- A. Amazon EC2.
- B. AWS Fargate. ✅
- C. AWS Lambda. ✅
- D. Amazon ECS.
- E. Amazon EMR.

---

**298.** For compliance and regulatory purposes, a government agency requires that their applications must run on hardware that is dedicated to them only. How can you meet this requirement?
- A. Use EC2 Dedicated Hosts. ✅
- B. Use EC2 Reserved Instances.
- C. Use EC2 Spot Instances.
- D. Use EC2 On-demand Instances.

---

**299.** The owner of an E-Commerce application notices that the compute capacity requirements vary heavily from time to time. What makes AWS more economical than traditional data centers for this type of application?
- A. AWS allows customers to launch powerful EC2 instances to handle spikes in load.
- B. AWS allows customers to pay upfront to get bigger discounts.
- C. AWS allows customers to launch and terminate EC2 instances based on demand. ✅
- D. AWS allows customers to choose cheaper types of EC2 instances that best fit their needs.

---

**300.** For new AWS customers, what is the EASIEST way to launch a simple WordPress website on AWS?
- A. Run WordPress on an Amazon Lightsail instance. ✅
- B. Install WordPress on an Amazon EC2 instance.
- C. Use the Amazon S3 Web hosting feature.
- D. Host the website directly on AWS Cloud Development Kit (AWS CDK).

---

**301.** Which of the following services allows you to install and run custom relational database software?
- A. Amazon EC2. ✅
- B. Amazon Cognito.
- C. Amazon RDS.
- D. Amazon Inspector.

---

**302.** Your application requirements for CPU and RAM are changing in an unpredictable way. Which service can be used to dynamically adjust these resources based on load?
- A. Auto Scaling. ✅
- B. ELB.
- C. Amazon Route53.
- D. Amazon Elastic Container Service.

---

**303.** You have been tasked with auditing the security of your VPC. As part of this process, you need to start by analyzing what inbound and outbound traffic is allowed on your EC2 instances. What two parts of the VPC do you need to check to accomplish this task?
- A. Network ACLs and Traffic Manager.
- B. Network ACLs and Subnets.
- C. Security Groups and Internet Gateways.
- D. Security Groups and Network ACLs. ✅

---

**304.** Amazon EC2 instances are conceptually very similar to traditional servers. However, using Amazon EC2 server instances in the same manner as traditional hardware server instances is only a starting point. What are the main benefits of using the AWS EC2 instances instead of traditional servers? (Choose TWO)
- A. Improves Fault-Tolerance. ✅
- B. Provides your business with a seamless remote accessibility.
- C. Prevents unauthorized users from getting into your network.
- D. Provides automatic data backups.
- E. Can be scaled manually in a shorter period of time. ✅

---

**305.** A company is running a large web application that needs to always be available. The application tends to slow down when CPU usage is greater than 60%. How can they track when CPU usage goes above 60% for any of the EC2 Instances in their account?
- A. Use CloudFront to monitor the CPU usage.
- B. Set the AWS Config CPU threshold to 60% to receive a notification when EC2 usage exceeds that value.
- C. Use CloudWatch Alarms to monitor the CPU and alert when the CPU usage is >= 60%. ✅
- D. Use SNS to monitor the utilization of the server.

---

**306.** What is the recommended storage option when hosting an often-changing database on an Amazon EC2 instance?
- A. Amazon EBS. ✅
- B. Amazon RDS.
- C. You can't run a database inside an Amazon EC2 instance.
- D. Amazon DynamoDB.

---

**307.** What factors determine how you are charged when using AWS Lambda? (Choose TWO)
- A. Storage consumed.
- B. Number of requests to your functions. ✅
- C. Number of volumes.
- D. Placement groups.
- E. Compute time consumed. ✅

---

**308.** What should you consider when storing data in Amazon Glacier?
- A. Amazon Glacier only accepts data in a compressed format.
- B. Glacier can only be used to store frequently accessed data and data archives.
- C. Amazon Glacier does not provide immediate retrieval of data. ✅
- D. Attach Glacier to an EC2 Instance to be able to store data.

---

**309.** Engineers are wasting a lot of time and effort managing batch computing software in traditional data centers. Which of the following AWS services allows them to easily run thousands of batch computing jobs?
- A. Amazon EC2.
- B. AWS Batch. ✅
- C. Lambda@Edge.
- D. AWS Fargate.

---

**310.** How can you increase your application’s fault-tolerance while it is being hosted in AWS?
- A. Deploy your application across multiple EC2 instances.
- B. Deploy your application across multiple Availability Zones. ✅
- C. Host your application on one powerful EC2 instance type instead of multiple smaller instances.
- D. Deploy the underlying application resources across multiple subnets.

---

**311.** A company needs to host a big data application on AWS using EC2 instances. Which of the following AWS Storage services would they choose to automatically get high throughput to multiple compute nodes?
- A. Amazon Elastic Block Store.
- B. AWS Storage Gateway.
- C. Amazon Elastic File System. ✅
- D. S3.

---

**312.** What are the benefits of the AWS Marketplace service? (Choose TWO)
- A. Protects customers by performing periodic security checks on listed products.
- B. Per-second billing.
- C. Provides cheaper options for purchasing Amazon EC2 on-demand instances.
- D. Provides flexible pricing options that suit most customer needs. ✅
- E. Provides software solutions that run on AWS or any other Cloud vendor. ✅

---

**313.** You are planning to launch an advertising campaign over the coming weekend to promote a new digital product. It is expected that there will be heavy spikes in load during the campaign period, and you can’t afford any downtime. You need additional compute resources to handle the additional load. What is the most cost-effective EC2 instance purchasing option for this job?
- A. Savings Plans.
- B. Spot Instances.
- C. Reserved Instances.
- D. On-Demand Instances. ✅

---

**314.** The elasticity of the AWS Cloud enables customers to save costs when compared to traditional hosting providers. What can AWS customers do to benefit from the elasticity of the AWS Cloud? (Choose TWO)
- A. Deploy your resources across multiple Availability Zones.
- B. Use Amazon EC2 Auto Scaling. ✅
- C. Deploy your resources in another region.
- D. Use Elastic Load Balancing.
- E. Use Serverless Computing whenever possible. ✅

---

**315.** What are some of the benefits of using On-Demand EC2 instances? (Choose TWO)
- A. They provide free capacity when testing your new applications.
- B. They are cheaper than all other EC2 options.
- C. They remove the need to buy “safety net” capacity to handle periodic traffic spikes. ✅
- D. They only require 1-2 days for setup and configuration.
- E. You can increase or decrease your compute capacity depending on the demands of your application. ✅

---

**316.** Which AWS service delivers data, videos, applications, and APIs to users globally with low latency and high transfer speeds?
- A. Amazon Route 53.
- B. Amazon Connect.
- C. Amazon CloudFront. ✅
- D. Amazon EC2.

---

**317.** A user is planning to launch two additional Amazon EC2 instances to increase availability. Which action should the user take?
- A. Launch the instances across multiple Availability Zones in a single AWS Region. ✅
- B. Launch the instances as EC2 Reserved Instances in the same AWS Region and the same Availability Zone.
- C. Launch the instances in multiple AWS Regions but in the same Availability Zone.
- D. Launch the instances as EC2 Spot Instances in the same AWS Region but in different Availability Zones.

---

**318.** A company has deployed several relational databases on Amazon EC2 instances. Every month the database software vendor releases new security patches that need to be applied to the databases. What is the MOST efficient way to apply the security patches?
- A. Connect to each database instance on a monthly basis and download and apply the necessary security patches from the vendor.
- B. Enable automate patching for the instances using the Amazon RDS console.
- C. In AWS Config. configure a rule for the instances and the required patch level.
- D. Use AWS Systems Manager to automate database patching according to a schedule. ✅

---

**319.** How do customers benefit from Amazon’s massive economies of scale?
- A. Periodic price reductions as the result of Amazon’s operational efficiencies. ✅
- B. New Amazon EC2 instance types providing the latest hardware.
- C. The ability to scale up and down when needed.
- D. Increased reliability in the underlying hardware of Amazon EC2 instances.

---

**320.** Which of the following are main components of the AWS global infrastructure? (Select TWO)
- A. Resource groups.
- B. Availability Zones. ✅
- C. Security groups.
- D. Regions. ✅
- E. Amazon Machine Images (AMIS).

---

**321.** Which AWS services are defined as global instead of regional? (Select TWO)
- A. Amazon Route 53. ✅
- B. Amazon EC2.
- C. Amazon S3.
- D. Amazon CloudFront. ✅
- E. Amazon DynamoDB.

---

**322.** (Q993) Which Amazon EC2 pricing model is the MOST cost efficient for an uninterruptible workload that runs once a year for 24 hours? y? ~ 4 _=
- A. On-Demand Instances ✅
- B. Reserved Instances
- C. Spot Instances
- D. Dedicated Instances

---

**323.** (Q994) A company has a compute workload that is steady, predictable, and uninterruptible.Which nae EC2 instance purchasing options meet these requirements MOST cost-effectively? (Choose two.
- A. On-Demand Instances
- B. Reserved Instances ✅
- C. Spot Instances
- D. Saving Plans ✅
- E. Dedicated Hosts

---

**324.** (Q998) A company has multiple AWS accounts that include compute workloads that cannot be interrupted. The company wants to obtain billing discounts that are based on the companys use of AWS services.Which AWS feature or purchasing option will meet these requirements?
- A. Resource tagging
- B. Consolidated billing ✅
- C. Pay-as-you-go pricing
- D. Spot Instances

---

**325.** (Q1004) In which scenario should Amazon EC2 Spot Instances be used? requires 99.999% uptime.
- A. A company wants to move its main website to AWS from an on-premises web server.
- B. A company has a number of application services whose Service Level Agreement (SLA)
- C. A company's heavily used legacy database is currently running on-premises.
- D. A company has a number of infrequent, interruptible jobs that are currently using OnDemand Instances. ✅

---

**326.** (Q1005) Which fully managed AWS service assists with the creation, testing, and management of custom Amazon EC2 images?
- A. EC2 Image Builder ✅
- B. Amazon Machine Image (AMI)
- C. AWS Launch Wizard
- D. AWS Elastic Beanstalk

---

**327.** (Q1009) A company has an uninterruptible application that runs on Amazon EC2 instances. The application constantly processes a backlog of files in an Amazon Simple Queue Service (Amazon SQS) queue. This usage is expected to continue to grow for years. What is the MOST cost-effective EC2 instance purchasing model to meet these requirements?
- A. Spot Instances
- B. On-Demand Instances
- C. Savings Plans ✅
- D. Dedicated Hosts

---

**328.** (Q1013) A user wants to allow applications running on an Amazon EC2 instance to make calls to other AWS services. The access granted must be secure. Which AWS service or feature should be used?
- A. Security groups
- B. AWS Firewall Manager
- C. IAM roles ✅
- D. IAM user SSH keys

---

**329.** (Q1014) A company has multiple AWS accounts that include compute workloads that cannot be interrupted. The company wants to obtain billing discounts that are based on the companys use of AWS services. Which AWS feature or purchasing option will meet these requirements?
- A. Resource tagging
- B. Consolidated billing ✅
- C. Pay-as-you-go pricing
- D. Spot Instances

---

**330.** (Q1016) Which AWS tool gives users the ability to plan their service usage, service costs, and instance reservations, and also allows them to set custom alerts when their costs or usage exceed established thresholds?
- A. Cost Explorer
- B. AWS Budgets ✅
- C. AWS Cost and Usage Report
- D. Reserved Instance reporting

---

**331.** (Q1021) Which task is the responsibility of AWS when using AWS services?
- A. Management of IAM user permissions
- B. Creation of security group rules for outbound access
- C. Maintenance of physical and environmental controls ✅
- D. Application of Amazon EC2 operating system patches

---

**332.** (Q1030) In which situations should a company create an IAM user instead of an IAM role? (Choose two.) services requests to AWS without having to sign in a second time Ta ey
- A. When an application that runs on Amazon EC2 instances requires access to other AWS
- B. When the company creates AWS access credentials for individuals ✅
- C. When the company creates an application that runs on a mobile phone that makes
- D. When the company needs to add users to IAM groups ✅
- E. When users are authenticated in the corporate network and want to be able to use AWS

---

**333.** (Q1032) According to security best practices, how should an Amazon EC2 instance be given access to an Amazon S3 bucket? the file. the keys, then upload the file.
- A. Hard code an IAM users secret key and access key directly in the application, and upload
- B. B. Store the IAM users secret key and access key in a text file on the EC2 instance, read
- C. C. Have the EC2 instance assume a role to obtain the privileges to upload the file. ✅
- D. D. Modify the S3 bucket policy so that any service can upload to it at any time.

---

**334.** (Q1047) A company needs to install an application in a Docker container. Which AWS service eliminates the need to provision and manage the container hosts?
- A. AWS Fargate ✅
- B. Amazon FSx for Windows File Server
- C. Amazon Elastic Container Service (Amazon ECS)
- D. Amazon EC2

---

**335.** (Q1048) Which AWS services or features provide disaster recovery solutions for Amazon EC2 instances? (Choose two.)
- A. EC2 Reserved Instances
- B. EC2 Amazon Machine Images (AMIs) ✅
- C. Amazon Elastic Block Store (Amazon EBS) snapshots ✅
- D. AWS Shield
- E. Amazon GuardDuty

---

**336.** (Q1049) A company is deploying a machine learning (ML) research project that will require a lot of compute power over several months. The ML processing jobs do not need to run at specific times. Which Amazon EC2 instance purchasing option will meet these requirements at the lowest cost?
- A. On-Demand Instances
- B. Spot Instances ✅
- C. Reserved Instances
- D. Dedicated Instances

---

**337.** (Q1056) Which AWS service can identify when an Amazon EC2 instance was terminated?
- A. AWS Identity and Access Management (IAM)
- B. AWS CloudTrail ✅
- C. AWS Compute Optimizer
- D. Amazon EventBridge

---

**338.** (Q1057) A company has a test AWS environment. A company is planning on testing an application within AWS. The application testing can be interrupted and does not need to run continuously. Which Amazon EC2 purchasing option will meet these requirements MOST cost-effectively?
- A. On-Demand Instances
- B. Dedicated Instances
- C. Spot Instances ✅
- D. Reserved Instances

---

**339.** (Q1069) A company wants to make an upfront commitment for continued use of its production Amazon EC2 instances in exchange for a reduced overall cost. Which pricing options meet these requirements with the LOWEST cost? (Choose two.)
- A. Spot Instances
- B. On-Demand Instances
- C. Reserved Instances ✅
- D. Savings Plans ✅
- E. Dedicated Hosts

---

**340.** (Q1079) Elasticity in the AWS Cloud refers to which of the following? (Choose two.) ams
- A. How quickly an Amazon EC2 instance can be restarted
- B. The ability to rightsize resources as demand shifts ✅
- C. The maximum amount of RAM an Amazon EC2 instance can use
- D. The pay-as-you-go billing model
- E. How easily resources can be procured when they are needed ✅

---

**341.** (Q1080) A company runs thousands of simultaneous simulations using AWS Batch. Each simulation is stateless, is fault tolerant, and runs for up to 3 hours. Which pricing model enables the company to optimize costs and meet these requirements?
- A. Reserved Instances
- B. Spot Instances ✅
- C. On-Demand Instances
- D. Dedicated Instances

---

**342.** (Q1095) What is the purpose of having an internet gateway within a VPC?
- A. To create a VPN connection to the VPC
- B. To allow communication between the VPC and the internet ✅
- C. To impose bandwidth constraints on internet traffic
- D. To load balance traffic from the internet across Amazon EC2 instances

---

**343.** (Q1096) A developer wants to deploy an application quickly on AWS without manually creating the required resources. Which AWS service will meet these requirements?
- A. Amazon EC2
- B. AWS Elastic Beanstalk ✅
- C. AWS CodeBuild
- D. Amazon Personalize

---

**344.** (Q1099) An online gaming company needs to choose a purchasing option to run its Amazon EC2 instances for 1 year. The web traffic is consistent, and any increases in traffic are predictable. The EC2 instances must be online and available without any disruption. Which EC2 instance purchasing option will meet these requirements MOST cost-effectively?
- A. On-Demand Instances
- B. Reserved Instances ✅
- C. Spot Instances
- D. Spot Fleet

---

**345.** (Q1103) n e-learning platform needs to run an application for 2 months each year. The application will be deployed on Amazon EC2 instances. Any application downtime during those 2 months must be avoided. Which EC2 purchasing option will meet these requirements MOST cost-effectively?
- A. Reserved Instances
- B. Dedicated Hosts
- C. Spot Instances
- D. On-Demand Instances ✅

---

**346.** (Q1104) Which AWS services or tools can identify rightsizing opportunities for Amazon EC2 instances? (Choose two.) eT
- A. AWS Cost Explorer ✅
- B. AWS Billing Conductor
- C. Amazon CodeGuru
- D. Amazon SageMaker
- E. AWS Compute Optimizer ✅

---

**347.** (Q1110) A company is running and managing its own Docker environment on Amazon EC2 instances. The company wants an alternative to help manage cluster size, scheduling, and environment maintenance. Which AWS service meets these requirements?
- A. AWS Lambda
- B. Amazon RDS
- C. AWS Fargate ✅
- D. Amazon Athena

---

**348.** (Q1111) A company wants to run a NoSQL database on Amazon EC2 instances. Which task is the responsibility of AWS in this scenario?
- A. Update the guest operating system of the EC2 instances.
- B. Maintain high availability at the database layer.
- C. Patch the physical infrastructure that hosts the EC2 instances. ✅
- D. Configure the security group firewall.

---

**349.** (Q1113) A company has deployed applications on Amazon EC2 instances. The company needs to assess application vulnerabilities and must identify infrastructure deployments that do not meet best practices. Which AWS service can the company use to meet these requirements?
- A. AWS Trusted Advisor
- B. Amazon Inspector ✅
- C. AWS Config
- D. Amazon GuardDuty

---

**350.** (Q1114) A company has a centralized group of users with large file storage requirements that have exceeded the space available on premises. The company wants to extend its file storage capabilities for this group while retaining the performance benefit of sharing content locally. What is the MOST operationally efficient AWS solution for this scenario? mounting utility. workstation to the file gateway. WorkDocs account for each user. Provisioned IOPS volume. Share the EBS volume directly with the users.
- A. Create an Amazon $3 bucket for each user. Mount each bucket by using an $3 file system
- B. Configure and deploy an AWS Storage Gateway file gateway. Connect each users ✅
- C. Move each users working environment to Amazon WorkSpaces. Set up an Amazon
- D. Deploy an Amazon EC2 instance and attach an Amazon Elastic Block Store (Amazon EBS)

---

**351.** (Q1126) A company wants to run its workload on Amazon EC2 instances for more than 1 year. This workload will run continuously. Which option offers a discounted hourly rate compared to the hourly rate of On-Demand Instances?
- A. AWS Graviton processor
- B. Dedicated Hosts
- C. EC2 Instance Savings Plans ✅
- D. Amazon EC2 Auto Scaling instances

---

**352.** (Q1132) A company needs to continuously run an experimental workload on an Amazon EC2 instance and stop the instance after 12 hours. Which instance purchasing option will meet this requirement MOST costeffectively?
- A. On-Demand Instances ✅
- B. Reserved Instances
- C. Spot Instances
- D. Dedicated Instances

---

**353.** (Q1135) A company wants its Amazon EC2 instances to operate in a highly available environment, even if there is a natural disaster in a particular geographic area. 7 Which approach will achieve this goal?
- A. Use EC2 instances in multiple AWS Regions. ✅
- B. Use EC2 instances in multiple Amazon CloudFront locations.
- C. Use EC2 instances in multiple edge locations.
- D. Use EC2 instances in AWS Local Zones.

---

**354.** (Q1143) A company plans to migrate its application to AWS and run the application on Amazon EC2 instances. The application will have continuous usage for 1 year. . Which EC2 instance purchasing option will meet these requirements MOST cost-effectively?
- A. Reserved Instances ✅
- B. Spot Instances
- C. On-Demand Instances
- D. Dedicated Hosts

---

**355.** (Q1152) Which AWS service enables users to check for vulnerabilities on Amazon EC2 instances by using predefined assessment templates?
- A. AWS WAF
- B. AWS Trusted Advisor
- C. Amazon Inspector ✅
- D. AWS Shield

---

**356.** (Q1157) Which actions are examples of a companys effort to rightsize its AWS resources to control cloud costs? (Choose two.) h NoSQL datasets. patterns. infrequently to lower-cost storage tiers.
- A. Switch from Amazon RDS to Amazon DynamoDB to accommodate
- B. Base the selection of Amazon EC2 instance types on past utilization ✅
- C. Use Amazon S3 Lifecycle policies to move objects that users access ✅
- D. Use Multi-AZ deployments for Amazon RDS.
- E. Replace existing Amazon EC2 instances with AWS Elastic Beanstalk.

---

**357.** (Q1160) A user has limited knowledge of AWS services, but wants to quickly deploy a scalable Node.js application in the AWS Cloud. Which service should be used to deploy the application? .
- A. AWS CloudFormation
- B. AWS Elastic Beanstalk ✅
- C. Amazon EC2
- D. AWS OpsWorks

---

**358.** (Q1163) A company has an Amazon EC2 instance in a private subnet. The company wants to initiate a connection to the internet to pull operating system updates while preventing traffic from the internet from accessing the EC2 instance. Which AWS managed service allows this?
- A. VPC endpoint
- B. NAT gateway ✅
- C. Amazon PrivateLink
- D. VPC peering

---

**359.** (Q1171) Which of the following is a way to use Amazon EC2 Auto Scaling groups to scale capacity in the AWS Cloud? h demand. demand.
- A. Scale the number of EC2 instances in or out automatically, based on ✅
- B. Use serverless EC2 instances.
- C. Scale the size of EC2 instances up or down automatically, based on
- D. Transfer unused CPU resources between EC2 instances.

---

**360.** (Q1174) Which Amazon EC2 instance pricing model can provide discounts of up to 90%?
- A. Reserved Instances
- B. On-Demand
- C. Dedicated Hosts
- D. Spot Instances ✅

---

**361.** (Q1181) A customer runs an On-Demand Amazon Linux EC2 instance for 3 hours, 5 minutes, and 6 seconds. For how much time will the customer be billed? A
- A. 3 hours, 5 minutes
- B. 3 hours, 5 minutes, and 6 seconds ✅
- C. 3 hours, 6 minutes
- D. 4 hours

---

**362.** (Q1195) A company wants to automatically add and remove Amazon EC2 instances. The company wants the EC2 instances to adjust to varying workloads dynamically. . Which service or feature will meet these requirements?
- A. Amazon DynamoDB
- B. Amazon EC2 Spot Instances
- C. AWS Snow Family
- D. Amazon EC2 Auto Scaling ✅

---

**363.** (Q1198) Which AWS service or feature can a company use to apply security rules to specific Amazon EC2 instances?
- A. Network ACLs ,
- B. Security groups ✅
- C. AWS Trusted Advisor
- D. AWS WAF

---

**364.** (Q1201) A company hosts an application on multiple Amazon EC2 instances. The application uses Amazon Simple Notification Service (Amazon SNS) to send messages. 5 Which AWS service or feature will give the application permission to access required AWS services?
- A. AWS Certificate Manager (ACM)
- B. IAM roles ✅
- C. AWS Security Hub
- D. Amazon GuardDuty

---

**365.** (Q1206) A company wants to migrate its PostgreSQL database to AWS. The company does not use the database frequently. Which AWS service or resource will meet these requirements with the LEAST management overhead?
- A. PostgreSQL on Amazon EC2
- B. Amazon RDS for PostgreSQL
- C. Amazon Aurora PostgreSQL-Compatible Edition
- D. Amazon Aurora Serverless ✅

---

**366.** (Q428) Using AWS Identity and Access Management (IAM), what can be attached to an Amazon EC2 instance to make service requests?
- A. Group
- B. Role ✅
- C. Policy
- D. Access key

**Explanation:** *(Add explanation here)*

---

**367.** (Q437) A company wants to securely access an Amazon S3 bucket from an Amazon EC2 instance without accessing the internet. What should the company use to accomplish this goal?
- A. VPN connection
- B. Internet gateway
- C. VPC endpoint ✅
- D. NAT gateway

**Explanation:** *(Add explanation here)*

---

**368.** (Q448) According to security best practices, how should an Amazon EC2 instance be given access to an Amazon S3 bucket? file. then upload the file.
- A. Hard code an IAM user's secret key and access key directly in the application, and upload the
- B. Store the IAM user's secret key and access key in a text file on the EC2 instance, read the keys,
- C. Have the EC2 instance assume a role to obtain the privileges to upload the file. ✅
- D. Modify the S3 bucket policy so that any service can upload to it at any time.

**Explanation:** *(Add explanation here)*

---

**369.** (Q451) How can AWS enable a company to control expenses as an application's usage changes unpredictably?
- A. AWS will refund the cost difference if a customer moves to larger servers.
- B. The application can be built to scale up or down automatically as resources are needed ✅
- C. Spot instances will automatically be used if the price is lower than on-demand instances.
- D. Amazon CloudWatch will automatically predict what resources are needed.

**Explanation:** *(Add explanation here)*

---

**370.** (Q457) A company is expecting a short-term spike in internet traffic for its application. During the traffic increase, the application cannot be interrupted. The company also needs to minimize cost and maximize flexibility. Which Amazon EC2 instance type should the company use to meet these requirements?
- A. On-Demand Instances ✅
- B. Spot Instances
- C. Reserved Instances
- D. Dedicated Hosts

**Explanation:** *(Add explanation here)*

---

**371.** (Q460) A company is running a self-managed Oracle database directly on Amazon EC2 for its steadystate database. The company wants to reduce compute costs. Which option should the company use to maximize savings over a 3-year term?
- A. EC2 Dedicated Instances
- B. EC2 Spot Instances
- C. EC2 Reserved Instances ✅
- D. EC2 On-Demand Instances

**Explanation:** *(Add explanation here)*

---

**372.** (Q461) How should a web application be deployed to ensure high availability in the AWS Cloud? Zone.
- A. Deploy multiple instances of the application in multiple Availability Zones. ✅
- B. Deploy multiple instances of the application in a single Availability Zone.
- C. Deploy the application to a compute-optimized Amazon EC2 instance in a single Availability
- D. Deploy the application in one Amazon EC2 instance in an Auto Scaling group.

**Explanation:** *(Add explanation here)*

---

**373.** (Q471) Which AWS services offer compute capabilities? (Choose two.)
- A. Amazon EC2 ✅
- B. Amazon S3
- C. Amazon Elastic Block Store (Amazon EBS)
- D. Amazon Cognito
- E. AWS Lambda ✅

**Explanation:** *(Add explanation here)*

---

**374.** (Q473) Which AWS service allows customers to purchase unused Amazon EC2 capacity at an often discounted rate?
- A. Reserved Instances
- B. On-Demand Instances
- C. Dedicated Instances
- D. Spot Instances ✅

**Explanation:** *(Add explanation here)*

---

**375.** (Q479) A workload on AWS will run for the foreseeable future by using a consistent number of Amazon EC2 instances. What pricing model will minimize cost while ensuring that compute resources remain available?
- A. Dedicated Hosts
- B. On-Demand Instances
- C. Spot Instances
- D. Reserved Instances ✅

**Explanation:** *(Add explanation here)*

---

**376.** (Q480) What are the advantages of deploying an application with Amazon EC2 instances in multiple Availability Zones? (Choose two.)
- A. Preventing a single point of failure ✅
- B. Reducing the operational costs of the application
- C. Allowing the application to serve cross-region users with low latency
- D. Increasing the availability of the application ✅
- E. Increasing the load of the application

**Explanation:** *(Add explanation here)*

---

**377.** (Q486) A user has limited knowledge of AWS services, but wants to quickly deploy a scalable Node.js application in the AWS Cloud. Which service should be used to deploy the application?
- A. AWS CloudFormation
- B. AWS Elastic Beanstalk ✅
- C. Amazon EC2
- D. AWS OpsWorks

**Explanation:** *(Add explanation here)*

---

**378.** (Q488) AnyCompany recently purchased Example Corp. Both companies use AWS resources, and AnyCompany wants a single aggregated bill. Which option allows AnyCompany to receive a single bill? manager to link the accounts and consolidate billing. bills be combined. account to Example Corp. AnyCompany AWS account.
- A. Example Corp. must submit a request to its AWS solutions architect or AWS technical account
- B. AnyCompany must create a new support case in the AWS Support Center requesting that both
- C. Send an invitation to join the organization from AnyCompany's AWS Organizations master ✅
- D. Migrate the Example Corp. VPCs, Amazon EC2 instances, and other resources into the

**Explanation:** *(Add explanation here)*

---

**379.** (Q493) A company has a MySQL database running on a single Amazon EC2 instance. The company now requires higher availability in the event of an outage. Which set of tasks would meet this requirement?
- A. Add an Application Load Balancer in front of the EC2 instance
- B. Configure EC2 Auto Recovery to move the instance to another Availability Zone
- C. Migrate to Amazon RDS and enable Multi-AZ ✅
- D. Enable termination protection for the EC2 instance to avoid outages

**Explanation:** *(Add explanation here)*

---

**380.** (Q504) A cloud practitioner needs an Amazon EC2 instance to launch and run for 7 hours without interruptions. What is the most suitable and cost-effective option for this task?
- A. On-Demand Instance ✅
- B. Reserved Instance
- C. Dedicated Host
- D. Spot Instance

**Explanation:** *(Add explanation here)*

---

**381.** (Q505) A user has a stateful workload that will run on Amazon EC2 for the next 3 years. What is the MOST cost-effective pricing model for this workload?
- A. On-Demand Instances
- B. Reserved Instances ✅
- C. Dedicated Instances
- D. Spot Instances

**Explanation:** *(Add explanation here)*

---

**382.** (Q510) Which are benefits of using Amazon RDS over Amazon EC2 when running relational databases on AWS? (Choose two.)
- A. Automated backups ✅
- B. Schema management
- C. Indexing of tables
- D. Software patching ✅
- E. Extract, transform, and load (ETL) management

**Explanation:** *(Add explanation here)*

---

**383.** (Q513) What is a characteristic of Convertible Reserved Instances (RIs)?
- A. Users can exchange Convertible RIs for other Convertible RIs from a different instance family. ✅
- B. Users can exchange Convertible RIs for other Convertible RIs in different AWS Regions.
- C. Users can sell and buy Convertible RIs on the AWS Marketplace.
- D. Users can shorten the term of their Convertible RIs by merging them with other Convertible RIs.

**Explanation:** *(Add explanation here)*

---

**384.** (Q519) A company is piloting a new customer-facing application on Amazon Elastic Compute Cloud (Amazon EC2) for one month. What pricing model is appropriate?
- A. Reserved Instances
- B. Spot Instances
- C. On-Demand Instances ✅
- D. Dedicated Hosts

**Explanation:** *(Add explanation here)*

---

**385.** (Q537) When designing AWS workloads to be operational even when there are component failures, what is an AWS best practice?
- A. Perform quarterly disaster recovery tests.
- B. Place the main component on the us-east-1 Region.
- C. Design for automatic failover to healthy resources. ✅
- D. Design workloads to fit on a single Amazon EC2 instance.

**Explanation:** *(Add explanation here)*

---

**386.** (Q545) A company is designing a web application that will run on Amazon EC2 instances. Which AWS services and features will improve availability and reduce the impact of failures for this application? (Choose two.) different AWS Region
- A. Amazon EC2 Auto Scaling for the EC2 instances ✅
- B. VPC subnet ACLs to check the health of a service
- C. Resources that are distributed across multiple Availability Zones ✅
- D. Configuration of AWS Server Migration Service (AWS SMS) to move the EC2 instances to a
- E. Resources that are distributed across multiple AWS points of presence

**Explanation:** *(Add explanation here)*

---

**387.** (Q546) Which fully managed AWS service assists with the creation, testing, and management of custom Amazon EC2 images?
- A. EC2 Image Builder ✅
- B. Amazon Machine Image (AMI)
- C. AWS Launch Wizard
- D. AWS Elastic Beanstalk

**Explanation:** *(Add explanation here)*

---

**388.** (Q549) A company has been storing monthly reports in an Amazon S3 bucket. The company exports the report data into comma-separated values (.csv) files. A developer wants to write a simple query that can read all of these files and generate a summary report. Which AWS service or feature should the developer use to meet these requirements with the LEAST amount of operational overhead?
- A. Amazon S3 Select
- B. Amazon Athena ✅
- C. Amazon Redshift
- D. Amazon EC2

**Explanation:** *(Add explanation here)*

---

**389.** (Q569) A company has multiple departments. The company must charge each department for its exact AWS Cloud usage, including data transfer costs. How can the company determine these costs by department?
- A. Use one AWS account for each department. ✅
- B. Use cost allocation tags on services that are used the most often.
- C. Use AWS Trusted Advisor.
- D. Use Savings Plans.

**Explanation:** *(Add explanation here)*

---

**390.** (Q570) An ecommerce company has Amazon EC2 instances running as web servers. There is a predictable pattern of peak traffic load that occurs two times each day, always at the same time. The EC2 instances are idle for the remainder of the day. What is the MOST cost-effective way to manage these resources while maintaining fault tolerance?
- A. Use an Auto Scaling group to scale resources in and out based on demand. ✅
- B. Purchase Reserved Instances to ensure peak capacity at all times.
- C. Write a cron job to stop the EC2 instances when the traffic demand is low.
- D. Write a script to vertically scale the EC2 instances during peak traffic demand.

**Explanation:** *(Add explanation here)*

---

**391.** (Q580) An application that is hosted on Amazon EC2 has a steady and consistent workload. The application will operate for at least 1 year. What is the MOST cost-effective instance purchasing option to meet these requirements?
- A. Spot Instances
- B. Reserved Instances ✅
- C. On-Demand Instances
- D. Dedicated Hosts

**Explanation:** *(Add explanation here)*

---

**392.** (Q583) A company moves its infrastructure from on premises to the AWS Cloud. The company can now provision additional Amazon EC2 instances whenever the instances are required. With this ability, the company can launch new marketing campaigns in 3 days instead of 3 weeks. Which benefit of the AWS Cloud does this scenario demonstrate?
- A. Cost savings
- B. Improved operational resilience
- C. Increased business agility ✅
- D. Enhanced security

**Explanation:** *(Add explanation here)*

---

**393.** (Q584) A company wants to design a reliable web application that is hosted on Amazon EC2. Which approach will achieve this goal?
- A. Launch large EC2 instances in the same Availability Zone
- B. Spread EC2 instances across more than one security group
- C. Spread EC2 instances across more than one Availability Zone. ✅
- D. Use an Amazon Machine Image (AMI) from AWS Marketplace.

**Explanation:** *(Add explanation here)*

---

**394.** (Q588) A large retail company wants to use an AWS service to process clickstream data from the company's ecommerce website. The company wants to collect and analyze the streaming data in real time. Which AWS service meets these requirements?
- A. Amazon Kinesis ✅
- B. Amazon Athena
- C. Amazon CloudFront
- D. AWS Data Exchange

**Explanation:** *(Add explanation here)*

---

**395.** (Q590) A company is developing an application that the company will host on Amazon EC2 instances. The application must be available 24 hours a day, 7 days a week. The company needs a scalable, highly available cloud architecture to support the application. Which guidelines should the company apply in its design to meet these requirements? (Choose two.)
- A. Use EC2 Spot Instances
- B. Use Multi-AZ deployments. ✅
- C. Use Auto Scaling groups ✅
- D. Use AWS Backup.
- E. Use EC2 Reserved Instances.

**Explanation:** *(Add explanation here)*

---

**396.** (Q593) A company wants to build a data analytics application that uses Amazon Redshift. The company needs a cost estimate for its future Amazon Redshift usage. Which AWS tool will provide a high-level cost estimation?
- A. AWS Budgets
- B. AWS Pricing Calculator ✅
- C. AWS Cost Explorer
- D. Savings Plans

**Explanation:** *(Add explanation here)*

---

**397.** (Q597) Which actions are examples of a company's effort to rightsize its AWS resources to control cloud costs? (Choose two.) storage tiers.
- A. Switch from Amazon RDS to Amazon DynamoDB to accommodate NoSQL datasets.
- B. Base the selection of Amazon EC2 instance types on past utilization patterns. ✅
- C. Use Amazon S3 Lifecycle policies to move objects that users access infrequently to lower-cost ✅
- D. Use Multi-AZ deployments for Amazon RDS.
- E. Replace existing Amazon EC2 instances with AWS Elastic Beanstalk.

**Explanation:** *(Add explanation here)*

---

**398.** (Q603) A company wants its Amazon EC2 instances to operate in a highly available environment, even if there is a natural disaster in a particular geographic area. Which solution achieves this goal?
- A. Use EC2 instances in a single Availability Zone
- B. Use EC2 instances in multiple AWS Regions ✅
- C. Use EC2 instances in multiple edge locations.
- D. Use Amazon CloudFront with the EC2 instances configured as the source.

**Explanation:** *(Add explanation here)*

---

**399.** (Q605) A company needs to apply security rules to specific Amazon EC2 instances. Which AWS service or feature provides this functionality?
- A. AWS WAF
- B. Network ACLs
- C. Amazon VPC
- D. Security groups ✅

**Explanation:** *(Add explanation here)*

---

**400.** (Q606) A company wants to run Amazon EC2 instances in locations that are near the company's global users. Which aspect of the AWS environment will support this requirement?
- A. Availability Zone
- B. Edge locations
- C. AWS Regions ✅
- D. Regional edge caches

**Explanation:** *(Add explanation here)*

---

**401.** (Q607) A company's project team needs to simultaneously mount a file system on multiple Amazon EC2 Linux instances. The file system also will be shared across multiple Availability Zones. Which AWS service will meet these requirements?
- A. Amazon Elastic File System (Amazon EFS) ✅
- B. Amazon S3
- C. Amazon Elastic Block Store (Amazon EBS)
- D. Amazon FSx for Windows File Server

**Explanation:** *(Add explanation here)*

---

**402.** (Q622) A company has stopped all of its Amazon EC2 instances but monthly billing charges continue to occur.What could be causing this? (Choose two.)
- A. Amazon Elastic Block Store (Amazon EBS) storage charges ✅
- B. Operating system charges
- C. Hardware charges
- D. Elastic IP charges ✅
- E. Input/output (I/O) charges

**Explanation:** *(Add explanation here)*

---

**403.** (Q626) Which Reserved Instance (RI) provides the HIGHEST average cost savings compared to an On-Demand Instance?
- A. 1-year, No Upfront, Standard RI
- B. 1-year, All Upfront, Convertible RI
- C. 3-year, All Upfront, Standard RI ✅
- D. 3-year, No Upfront, Convertible RI

**Explanation:** *(Add explanation here)*

---

**404.** (Q627) Elasticity in the AWS Cloud refers to which of the following? (Choose two.)
- A. How quickly an Amazon EC2 instance can be restarted
- B. The ability to rightsize resources as demand shifts ✅
- C. The maximum amount of RAM an Amazon EC2 Instance can use
- D. The pay-as-you-go billing model
- E. How easily resources can be procured when they are needed ✅

**Explanation:** *(Add explanation here)*

---

**405.** (Q630) Which AWS service allows for file sharing between multiple Amazon EC2 instances?
- A. AWS Direct Connect
- B. AWS Snowball Edge
- C. AWS Backup
- D. Amazon Elastic File System (Amazon EFS) ✅

**Explanation:** *(Add explanation here)*

---

**406.** (Q631) A company is running and managing its own Docker environment on Amazon EC2 instances. The company wants an alternative to help manage cluster size, scheduling, and environment maintenance. Which AWS service meets these requirements?
- A. AWS Lambda
- B. Amazon RDS
- C. AWS Fargate ✅
- D. Amazon Athena

**Explanation:** *(Add explanation here)*

---

**407.** (Q637) A company's system administrator discovers that someone logged in to the company's AWS account during the weekend and terminated an Amazon EC2 instance. Which AWS service should the system administrator use to identify who made this change?
- A. Amazon Inspector
- B. Amazon Pinpoint
- C. AWS CloudTrail ✅
- D. AWS Trusted Advisor

**Explanation:** *(Add explanation here)*

---

**408.** (Q639) A company is running multiple workloads in the AWS Cloud and recently began investigating ways to reduce costs. The company is already running fault-tolerant workloads on Amazon EC2 that perform periodic checkpoints in case of an outage. Which AWS service or pricing model can provide the GREATEST cost savings?
- A. Capacity Reservations
- B. Amazon Lightsail
- C. Spot Instances ✅
- D. Dedicated Hosts

**Explanation:** *(Add explanation here)*

---

**409.** (Q642) A company needs to perform data processing once a week that typically takes about 5 hours to complete. Which AWS service should the company use for this workload?
- A. AWS Lambda
- B. Amazon EC2 ✅
- C. AWS CodeDeploy
- D. AWS Wavelength

**Explanation:** *(Add explanation here)*

---

**410.** (Q551) A company uses Amazon RDS for a product database. The company wants to ensure the database is highly available. Which feature of Amazon RDS will meet this requirement?
- A. Read replicas
- B. Blue/green deployment
- C. Multi-AZ deployment ✅
- D. Reserved Instances

---

**411.** (Q554) A company needs a firewall that will control network connections to and from a single Amazon EC2 instance. This firewall will not control network connections to and from other instances that are in the same subnet. Which AWS service or feature can the company use to meet these requirements?
- A. Network ACL
- B. AWS WAF
- C. Route table
- D. Security group ✅

---

**412.** (Q555) A company is planning to use the Amazon EC2 instances as web servers. Customers from around the world will use the web servers. Most customers will use the web servers only during certain hours of the day. How should the company deploy the EC2 instances to achieve the LOWEST operational cost?
- A. In multiple Availability Zones
- B. In an Auto Scaling group ✅
- C. In a placement group
- D. In private subnets

---

**413.** (Q557) A company uses Amazon EC2 instances to run its application. The application needs to be available and running continuously for three or more years. What type of EC2 instance should the company purchase for a discount on the EC2 pricing?
- A. Reserved Instances ✅
- B. Spot Instances
- C. On-Demand Instances
- D. EC2 Fleet

---

**414.** (Q560) A company needs to use AWS technology to deploy a static website. Which solution meets this requirement with the LEAST amount of operational overhead?
- A. Deploy the website on Amazon EC2.
- B. Host the website on AWS Elastic Beanstalk.
- C. Deploy the website with Amazon Lightsail.
- D. Host the website on Amazon S3. ✅

---

**415.** (Q564) Which Amazon EC2 Reserved Instances term commitment will give users the MOST cost savings?
- A. 1 year
- B. 2 years
- C. 3 years ✅
- D. 5 years

---

**416.** (Q565) A company is running big data analytics and massive parallel computations on its AWS test and development servers. The company can tolerate occasional downtime. What is the MOST cost-effective Amazon EC2 purchasing option for the company to use?
- A. On-Demand Instances
- B. Spot Instances ✅
- C. Reserved Instances
- D. Savings Plans

---

**417.** (Q566) A company runs Amazon EC2 instances in a research lab. The instances run for 3 hours each week and cannot be interrupted. What is the MOST cost-effective instance purchasing option to meet these requirements?
- A. Compute Savings Plan
- B. On-Demand Instances ✅
- C. Convertible Reserved Instances
- D. Spot Instances

---

**418.** (Q569) A company will run a predictable compute workload on Amazon EC2 instances for the next 3 years. The workload is critical for the company. The company wants to optimize costs to run the workload. Which solution will meet these requirements?
- A. Spot Instances
- B. Dedicated Hosts
- C. Savings Plans ✅
- D. On-Demand Instances

---

**419.** (Q573) A company has migrated its workload to the AWS Cloud. The company wants to optimize existing Amazon EC2 resources. Which AWS services or tools provide this functionality? (Choose two.)
- A. AWS Elastic Beanstalk
- B. AWS Cost Explorer ✅
- C. Amazon Detective
- D. AWS Compute Optimizer ✅
- E. AWS Billing Conductor

---

**420.** (Q578) A company needs to purchase Amazon EC2 instances to support an application that will run continuously for more than 1 year. Which EC2 instance purchasing option meets these requirements MOST cost-effectively?
- A. Dedicated Instances
- B. Spot Instances
- C. Reserved Instances ✅
- D. On-Demand Instances

---

**421.** (Q589) A company's cloud environment includes Amazon EC2 instances and Application Load Balancers. The company wants to improve protections for its cloud resources against DDoS attacks. The company also wants to have real-time visibility into any DDoS attacks. Which AWS service will meet these requirements?
- A. AWS Shield Standard
- B. AWS Firewall Manager
- C. AWS Shield Advanced ✅
- D. Amazon GuardDuty

---

**422.** (Q590) A company wants to update its online data processing application by implementing containerbased services that run for 4 hours at a time. The company does not want to provision or manage server instances. Which AWS service will meet these requirements? Cc. Amazon EC2
- A. AWS Lambda
- B. AWS Fargate ✅
- D. AWS Elastic Beanstalk

---

**423.** (Q593) A user needs to perform a one-time backup of an Amazon Elastic Block Store (Amazon EBS) volume that is attached to an Amazon EC2 instance. What is the MOST operationally efficient way to perform this backup? Direct Connect.
- A. Attach another EBS volume to the EC2 instance, and copy the contents.
- B. Copy the EBS volume to a server that is running outside AWS and is connected with AWS
- C. Create an EBS snapshot of the volume. ✅
- D. Create a custom script to copy the EBS file contents to Amazon S3.

---

**424.** (Q599) Which AWS service or feature can be used to monitor for potential disk write spikes on a system that is running on Amazon EC2?
- A. AWS CloudTrail
- B. AWS Health Dashboard
- C. AWS Trusted Advisor
- D. Amazon CloudWatch ✅

---

**425.** (Q600) A company has applications that control on-premises factory equipment. Which AWS service should the company use to run these applications with the LEAST latency? Cc. AWS Lambda
- A. AWS Outposts ✅
- B. Amazon EC2
- D. AWS Fargate

---

**426.** (Q604) Which VPC component can a company use to set up a virtual firewall at the Amazon EC2 instance level?
- A. Network ACL
- B. Security group ✅
- C. Route table
- D. NAT gateway

---

**427.** (Q614) Which AWS network services or features allow CIDR block notation when providing an IP address range? (Choose two.)
- A. Security groups ✅
- B. Amazon Machine Image (AMI)
- C. Network access control list (network ACL) ✅
- D. AWS Budgets
- E. Amazon Elastic Block Store (Amazon EBS)

---

**428.** (Q634) A company has a workload that will run continuously for 1 year. The workload cannot tolerate service interruptions. Which Amazon EC2 purchasing option will be MOST cost-effective?
- A. All Upfront Reserved Instances ✅
- B. Partial Upfront Reserved Instances
- C. Dedicated Instances
- D. On-Demand Instances

---

**429.** (Q637) A company wants to track the monthly cost and usage of all Amazon EC2 instances in a specific AWS environment. Which AWS service or tool will meet these requirements?
- A. AWS Cost Anomaly Detection
- B. AWS Budgets ✅
- C. AWS Compute Optimizer
- D. AWS Trusted Advisor

---

**430.** (Q639) A company wants a cost-effective option when running its applications in an Amazon EC2 instance for short time periods. The applications can be interrupted. Which EC2 instance type will meet these requirements?
- A. Spot Instances ✅
- B. On-Demand Instances
- C. Reserved Instances
- D. Dedicated Instances

---

**431.** (Q644) A company wants to securely access an Amazon S3 bucket from an Amazon EC2 instance without accessing the internet. What should the company use to accomplish this goal?
- A. VPN connection
- B. Internet gateway
- C. VPC endpoint ✅
- D. NAT gateway

---

**432.** (Q645) A company wants an AWS service that can automate software deployment in Amazon EC2 instances and on-premises instances. Which AWS service will meet this requirement?
- A. AWS CodeCommit
- B. AWS CodeBuild
- C. AWS CodeDeploy ✅
- D. AWS CodePipeline

---

**433.** (Q646) Which AWS services are serverless? (Choose two.)
- A. AWS Fargate ✅
- B. Amazon Managed Streaming for Apache Kafka
- C. Amazon EMR
- D. Amazon S83 ✅
- E. Amazon EC2

---

**434.** (Q651) A company needs to run some of its workloads on premises to comply with regulatory guidelines, The company wants to use the AWS Cloud to run workloads that are not required to be on premises#The company also wants to be able to use the same API calls for the on-premises workloads and the cloud workloads. Which AWS service or feature should the company use to meet these requirements?
- A. Dedicated Hosts
- B. AWS Outposts ✅
- C. Availability Zones
- D. AWS Wavelength

---

**435.** (Q652) What is the recommended use case for Amazon EC2 On-Demand Instances? period of time
- A. A steady-state workload that requires a particular EC2 instance configuration for a long
- B. A workload that can be interrupted for a project that requires the lowest possible cost
- C. An unpredictable workload that does not require a long-term commitment ✅
- D. A workload that is expected to run for longer than 1 year

---

**436.** (Q656) In which situations should a company create an IAM user instead of an IAM role? services requests to AWS without having to sign in a second time
- A. When an application that runs on Amazon EC2 instances requires access to other AWS
- B. When the company creates AWS access credentials for individuals ✅
- C. When the company creates an application that runs on a mobile phone that makes
- D. When the company needs to add users to IAM groups ✅
- E. When users are authenticated in the corporate network and want to be able to use AWS

---

**437.** (Q657) A company hosts a web application on AWS. The company has improved the availability of its,application by provisioning multiple Amazon EC2 instances. The company wants to distribute its traffic aeross.the EC2 instances while providing a single point of contact to the web clients. Which AWS service can distribute the traffic to multiple EC2 instances as targets?
- A. VPC endpoints
- B. Application Load Balancer ✅
- C. NAT gateway
- D. Internet gateway

---

**438.** (Q664) A company wants to migrate its on-premises SQL Server database to the AWS Cloud. The company-wants AWS to handle the day-to-day administration of the database. Which AWS service will meet the company's requirements?
- A. Amazon EC2 for Microsoft SQL Server
- B. Amazon DynamoDB
- C. Amazon RDS ✅
- D. Amazon Aurora

---

**439.** (Q668) A company has data lakes designed for high performance computing (HPC) workloads. Which Amazon EC2 instance type should the company use to meet these requirements?
- A. General purpose instances
- B. Compute optimized instances ✅
- C. Memory optimized instances
- D. Storage optimized instances

---

**440.** (Q674) A company wants to deploy a web application as a containerized application. The company wants to Use a managed service that can automatically create container images from source code and deploy the containerized application. Which AWS service will meet these requirements?
- A. AWS Elastic Beanstalk
- B. Amazon Elastic Container Service (Amazon ECS)
- C. AWS App Runner ✅
- D. Amazon EC2

---

**441.** (Q675) A company has moved all its infrastructure to the AWS Cloud. To plan ahead for each quartersthe finance team wants to track the cost and usage data of all resources from previous months. The financeteam_wants to automatically generate reports that contains the data. Which AWS service or feature should the finance team use to meet these requirements?
- A. Amazon Detective
- B. AWS Pricing Calculator
- C. AWS Budgets ✅
- D. AWS Savings Plans

---

**442.** (Q677) A company wants to migrate critical on-premises production systems to Amazon EC2 instances. The production instances will be used for at least 3 years. The company wants a pricing option thatywillminimize cost. Which solution will meet these requirements?
- A. On-Demand Instances
- B. Reserved Instances ✅
- C. Spot Instances
- D. AWS Free Tier

---

**443.** (Q680) A company has multiple SQL-based databases located in a data center. The company needs tounigrate all database servers to the AWS Cloud to reduce the cost of operating physical servers. Which AWS service or resource will meet these requirements with the LEAST operattonaljoverhead?
- A. Amazon EC2 instances
- B. Amazon RDS ✅
- C. Amazon DynamoDB
- D. OpenSearch

---

**444.** (Q684) A company needs to run an application on Amazon EC2 instances without interruption. Which EC2 instance purchasing option will meet this requirement MOST cost-effectively?
- A. Standard Reserved Instances ✅
- B. Convertible Reserved Instances
- C. On-Demand Instances
- D. Spot Instances

---

**445.** (Q686) A company plans to migrate its application from on premises to the AWS Cloud. The company.needs to gather usage and configuration data for the application components. Which AWS service will meet these requirements?
- A. AWS Database Migration Service (AWS DMS)
- B. AWS Transfer Family
- C. AWS Application Discovery Service ✅
- D. AWS Global Accelerator

---

**446.** (Q689) Which type of workload should a company run on Amazon EC2 Spot Instances? period. of time
- A. A steady-state workload that requires a particular EC2 instance configuration for a long
- B. A workload that can be interrupted and can control costs ✅
- C. A steady-state workload that does not require a long-term commitment
- D. A workload that cannot be interrupted and can control costs

---

**447.** (Q691) For which use case are Amazon EC2 On-Demand Instances MOST cost-effective?
- A. Compute-intensive video transcoding that can be restarted if necessary
- B. An instance in continual use for 1 month to conduct quality assurance tests ✅
- C. An instance that runs a web server that will run for 1 year
- D. An instance that runs a database that will run for 3 years

---

**448.** (Q693) Which AWS offering can analyze a companys AWS environment to discover security vulnerabilities on Amazon EC2 instances?
- A. Amazon Inspector ✅
- B. Amazon Macie
- C. AWS Shield Standard
- D. Security groups

---

**449.** (Q694) A company plans to onboard new employees that will be working remotely. The company needs to'set up Windows virtual desktops to create a working environment for the new employees. The employes.must be able access the working environment from anywhere and by using their computer or a web browser: Which AWS service or feature will meet these requirements?
- A. Dedicated Hosts
- B. AWS Global Accelerator
- C. Amazon Workspaces ✅
- D. Amazon CloudFront

---

**450.** (Q697) A company purchased Amazon EC2 Standard Reserved Instances (RIs) for a workload in the AWS Cloud. The company needs to move part of the workload to an instance family that does not match theinstance family of these Standard RIs. How can the company take advantage of the Standard RIs that it no longer needs?
- A. Contact the AWS Support team, and ask the team to sell the Standard RIs
- B. Sell the Standard RIs on the Amazon EC2 Reserved Instance Marketplace ✅
- C. Sell the Standard RIs as a third-party seller on the AWS Marketplace
- D. Convert the Standard RIs to Savings Plans

---

