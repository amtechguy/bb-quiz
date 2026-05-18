**1.** A company stores 100 TB of data in its data center. The company wants to migrate the data to the AWS Cloud without using the internet. Which AWS service or resource will meet these requirements?

- A. Amazon Connect
- B. AWS DataSync
- C. AWS Snowball Edge ✅
- D. AWS VPN services

**Explanation:** AWS Snowball Edge is a physical data transfer device that moves large amounts of data to AWS without using the internet. DataSync and VPN both require internet connectivity.

---

**2.** Which AWS service helps assess the security and compliance of applications that are deployed on Amazon EC2 instances?

- A. AWS Security Hub
- B. Amazon Inspector ✅
- C. Amazon GuardDuty
- D. AWS Shield

**Explanation:** Amazon Inspector automatically assesses EC2 instances for software vulnerabilities and unintended network exposure, providing security and compliance findings.

---

**3.** A company wants to use Amazon EC2 instances to provide a static website to users all over the world. The company needs to minimize latency for the users. Which solution meets these requirements?

- A. Use Amazon ElastiCache as the database for the EC2 instances.
- B. Use EC2 instances in the same edge location and the same Availability Zone.
- C. Use Amazon CloudFront with the EC2 instances configured as the source. ✅
- D. Use EC2 instances in the same Availability Zone but in different AWS accounts.

**Explanation:** Amazon CloudFront caches content at edge locations worldwide, serving it from the location closest to each user to minimize latency.

---

**4.** Which of the following is one of the pillars of the AWS Well-Architected Framework?

- A. Efficiency and redundancy
- B. High availability
- C. Operational excellence ✅
- D. Business optimization

**Explanation:** The six pillars of the AWS Well-Architected Framework are: Operational Excellence, Security, Reliability, Performance Efficiency, Cost Optimization, and Sustainability.

---

**5.** A company wants to limit its employees' AWS access to a portfolio of predefined AWS resources. Which AWS solution should the company use to meet this requirement?

- A. AWS Config
- B. AWS software development kits (SDKs)
- C. AWS Service Catalog ✅
- D. AWS AppSync

**Explanation:** AWS Service Catalog allows organizations to create and manage approved portfolios of AWS resources that employees can deploy, enforcing governance and limiting access to predefined services.

---

**6.** A company wants to migrate a virtual server that runs Windows Server from an on-premises data center to AWS. The company wants to automatically convert the existing server to run natively on AWS infrastructure. Which AWS service will meet this requirement?

- A. AWS Application Discovery Service
- B. AWS Application Migration Service ✅
- C. AWS Config
- D. AWS DataSync

**Explanation:** AWS Application Migration Service (MGN) automatically converts on-premises servers to run natively on AWS, lifting and shifting workloads without requiring application changes.

---

**7.** Which AWS service or tool provides users with a graphical UI to manage AWS services?

- A. AWS Cloud Development Kit (AWS CDK)
- B. AWS CLI
- C. AWS Management Console ✅
- D. AWS SDKs

**Explanation:** The AWS Management Console is a browser-based graphical user interface for accessing and managing all AWS services.

---

**8.** Which component of the AWS global infrastructure does Amazon CloudFront use to speed up the delivery of content to users across the world?

- A. Amazon VPC
- B. Edge location ✅
- C. Local Zone
- D. AWS Outposts connection

**Explanation:** Amazon CloudFront uses a global network of edge locations to cache and deliver content closer to end users, reducing latency.

---

**9.** A company wants to host an application on Amazon EC2 instances. The company needs to bring its own license for its operating systems. To meet governance and compliance requirements, the application needs software licensing at the physical server level. Which EC2 instance purchasing option will meet these requirements?

- A. Reserved Instances
- B. Spot Instances
- C. On-Demand Instances
- D. Dedicated Hosts ✅

**Explanation:** Dedicated Hosts provide visibility into the physical server's sockets and cores, which is required by most BYOL licensing models that are tied to per-socket or per-core metrics.

---

**10.** A company is undergoing a security audit. The auditor needs to locate compliance-related information and must download AWS security and compliance documents including SOC reports. Which AWS service or group can provide these documents?

- A. AWS Abuse team
- B. AWS Artifact ✅
- C. AWS Support
- D. AWS Config

**Explanation:** AWS Artifact provides on-demand access to AWS compliance reports including SOC 1, SOC 2, SOC 3, PCI DSS, and ISO certifications.

---

**11.** A company is preparing to move its infrastructure to the AWS Cloud. The company needs to collect and assess on-premises server and application inventory. Which AWS service will meet these requirements?

- A. Amazon Connect
- B. AWS Migration Hub ✅
- C. Amazon QuickSight
- D. AWS Step Functions

**Explanation:** AWS Migration Hub provides a central location to collect, view, and track the status of on-premises server and application inventory during migration planning.

---

**12.** A company wants to migrate its on-premises relational databases to the AWS Cloud. The company wants to deploy Amazon RDS as close as possible to the company's current location. Which AWS service or resource will meet these requirements?

- A. Amazon Connect
- B. AWS Direct Connect
- C. Amazon Macie
- D. AWS Regions ✅

**Explanation:** AWS has Regions around the world. The company should choose the AWS Region geographically closest to their location when deploying Amazon RDS to minimize latency.

---

**13.** A company runs its application in the AWS Cloud. The company wants to review its AWS resources and receive recommendations about ways to optimize costs. Which AWS service or tool can the company use to meet these requirements?

- A. Amazon Inspector
- B. AWS Trusted Advisor ✅
- C. AWS Pricing Calculator
- D. AWS Budgets

**Explanation:** AWS Trusted Advisor analyzes your AWS environment and provides real-time recommendations across cost optimization, security, performance, fault tolerance, and service limits.

---

**14.** Which AWS service is a fully managed service that allows access to applications through a virtual interface (VIF)?

- A. Amazon AppStream 2.0 ✅
- B. Amazon EC2
- C. AWS Elastic Beanstalk
- D. AWS Lambda

**Explanation:** Amazon AppStream 2.0 is a fully managed application streaming service that provides users access to desktop applications through a virtual interface without needing to manage infrastructure.

---

**15.** A company is designing its AWS workloads so that components can be updated regularly and so that changes can be made in small, reversible increments. Which pillar of the AWS Well-Architected Framework does this design support?

- A. Security
- B. Performance efficiency
- C. Operational excellence ✅
- D. Reliability

**Explanation:** The Operational Excellence pillar includes the design principle of making frequent, small, reversible changes so that teams can iterate quickly and recover easily from errors.

---

**16.** Which AWS service can a company use to send SMS messages and email messages from applications?

- A. AWS Direct Connect
- B. Amazon Simple Email Service (Amazon SES)
- C. Amazon Simple Notification Service (Amazon SNS) ✅
- D. Amazon Simple Queue Service (Amazon SQS)

**Explanation:** Amazon SNS is a fully managed pub/sub messaging service that can send SMS text messages and email notifications from applications to end users.

---

**17.** A large company wants to track the combined AWS usage costs of all of its linked accounts. How can this be accomplished?

- A. Use AWS Trusted Advisor to generate customized summary reports.
- B. Use AWS Organizations to generate consolidated billing reports ✅
- C. Use AWS Budgets to set utilization targets and receive summary reports
- D. Use the AWS Control Tower dashboard to get a summary report of all linked account costs.

**Explanation:** AWS Organizations consolidated billing combines all member account charges into a single bill paid by the management account, giving visibility into total spending across all linked accounts.

---

**18.** A company wants to migrate its infrastructure to the AWS Cloud. The company needs to collect data for server configuration, utilization, and annual operating costs. Which AWS service will meet these requirements?

- A. AWS Compute Optimizer
- B. AWS Cost Explorer
- C. Migration Evaluator ✅
- D. AWS Pricing Calculator

**Explanation:** Migration Evaluator (formerly TSO Logic) collects on-premises infrastructure data including server configuration, utilization, and costs to provide a business case and projected savings for AWS migration.

---

**19.** A company wants to securely connect its on-premises VPCs to AWS services without exposing internal traffic to the public internet. Which AWS service or resource will meet these requirements?

- A. Amazon Connect
- B. Amazon Inspector
- C. An internet gateway
- D. AWS PrivateLink ✅

**Explanation:** AWS PrivateLink provides private connectivity between VPCs, AWS services, and on-premises applications without exposing traffic to the public internet.

---

**20.** A company wants to use a graph database to detect fraud patterns in real time. Which AWS service will meet this requirement?

- A. Amazon DynamoDB
- B. Amazon Neptune ✅
- C. Amazon RDS
- D. Amazon Timestream for LiveAnalytics

**Explanation:** Amazon Neptune is a fully managed graph database service optimized for storing and querying highly connected data, making it ideal for fraud detection use cases that analyze relationship patterns.

---

**21.** A company wants to use shell scripts to create and manage AWS resources. Which AWS service or tool will meet these requirements?

- A. AWS CLI ✅
- B. AWS Config
- C. Amazon Inspector
- D. AWS X-Ray

**Explanation:** The AWS Command Line Interface (CLI) allows users to interact with AWS services using shell scripts and commands, enabling automation and management of AWS resources programmatically.

---

**22.** A company is planning to migrate to the AWS Cloud and wants to become more responsive to customer inquiries and feedback. The company wants to focus on organizational transformation. Which task should the company perform according to the AWS CAF?

- A. Create new value propositions with new products and services.
- B. Use agile methods to rapidly iterate and evolve ✅
- C. Use a new data and analytics platform to create actionable insights.
- D. Migrate and modernize legacy infrastructure.

**Explanation:** AWS CAF's People perspective recommends using agile methods to rapidly iterate and evolve, enabling organizations to become more responsive and adaptive to customer needs.

---

**23.** A company is creating an Amazon EC2 instance. The company wants to control the incoming and outgoing network traffic at the EC2 instance level. Which AWS service or resource will meet this requirement?

- A. Amazon GuardDuty
- B. Amazon Inspector
- C. Security groups ✅
- D. AWS Shield

**Explanation:** Security groups act as a stateful virtual firewall at the EC2 instance level, controlling inbound and outbound traffic based on rules defined by port, protocol, and source/destination.

---

**24.** A company wants to identify unintended network accessibility and vulnerabilities on Amazon EC2 instances. Which AWS service can the company use to meet this requirement?

- A. Amazon Inspector ✅
- B. AWS Config
- C. AWS Trusted Advisor
- D. AWS Shield

**Explanation:** Amazon Inspector automatically discovers and scans EC2 instances for software vulnerabilities and unintended network accessibility, providing detailed security findings.

---

**25.** A company has deployed its application on AWS. The company wants to create financial reports for current and historical spending and forecast AWS service usage for the next year. Which AWS service or tool can the company use?

- A. AWS Trusted Advisor
- B. AWS Cost Explorer ✅
- C. AWS CloudTrail
- D. AWS Budgets

**Explanation:** AWS Cost Explorer provides interactive reports and graphs for current and historical AWS spending, and includes forecasting capabilities to predict future usage and costs.

---

**26.** Which AWS services allow users to monitor and retain records of account activities that include governance, compliance, and auditing? (Choose two.)

- A. Amazon CloudWatch ✅
- B. AWS CloudTrail ✅
- C. Amazon GuardDuty
- D. AWS Shield
- E. AWS WAF

**Explanation:** AWS CloudTrail records all API calls and account activity for governance and auditing. Amazon CloudWatch collects and retains logs and metrics for monitoring and operational compliance.

---

**27.** A company wants phone, email, and chat access to AWS support engineers. The company also wants the ability to get support for business-critical systems within 15 minutes. Which AWS Support plan meets these requirements?

- A. AWS Developer Support
- B. AWS Business Support
- C. AWS Enterprise Support ✅
- D. AWS Basic Support

**Explanation:** AWS Enterprise Support provides 24/7 phone, email, and chat access to senior engineers, and guarantees a 15-minute response time for business-critical system failures.

---

**28.** What is a characteristic of Convertible Reserved Instances?

- A. Users can exchange Convertible RIs for other Convertible RIs from a different instance family ✅
- B. Users can exchange Convertible RIs for other Convertible RIs in different AWS Regions.
- C. Users can sell and buy Convertible RIs on the AWS marketplace.
- D. Users can shorten the term of their Convertible RIs by merging them.

**Explanation:** Convertible Reserved Instances allow users to exchange them for other Convertible RIs with different instance families, operating systems, or tenancies, offering more flexibility than Standard RIs.

---

**29.** A company stores images of scanned financial invoices in Amazon S3. The company needs to identify and read total balance amounts from the invoices. Which AWS service will meet these requirements?

- A. Amazon Lex
- B. Amazon Polly
- C. Amazon Rekognition
- D. Amazon Textract ✅

**Explanation:** Amazon Textract uses machine learning to automatically extract text and structured data from scanned documents, including forms and tables, making it ideal for reading balance amounts from invoices.

---

**30.** A company wants to create multiple isolated networks in the same AWS account. Which AWS service or component will provide this functionality?

- A. AWS Transit Gateway
- B. Internet gateway
- C. Amazon VPC ✅
- D. Amazon EC2

**Explanation:** Amazon VPC allows you to create multiple logically isolated virtual networks within the same AWS account, each with its own IP address range, subnets, and network configuration.

---

**31.** A company needs to implement an AWS data warehouse solution that can manage petabytes of data. A reporting application will perform OLAP queries on the data. Which AWS service should the company use?

- A. Amazon Elastic File System (Amazon EFS)
- B. Amazon Redshift ✅
- C. Amazon RDS for MySQL
- D. Amazon DynamoDB

**Explanation:** Amazon Redshift is a fully managed petabyte-scale data warehouse service optimized for OLAP queries and complex analytics across large datasets.

---

**32.** A company is developing a web application that uses containers. The company needs a repository to store and control access to container images. Which AWS service will meet these requirements?

- A. Amazon Elastic Container Registry (Amazon ECR) ✅
- B. Amazon Elastic Kubernetes Service (Amazon EKS)
- C. Amazon Elastic Container Service (Amazon ECS)
- D. Amazon EC2

**Explanation:** Amazon ECR is a fully managed container image registry that makes it easy to store, manage, and deploy container images, with fine-grained access control via IAM policies.

---

**33.** A company has an environment that includes Amazon EC2 instances, Amazon Lightsail, and on-premises servers. The company wants to automate the security updates for its operating systems and applications with the LEAST operational effort. Which solution will meet these requirements?

- A. Use AWS Shield to identify and manage security events.
- B. Connect to each server by using a remote desktop connection. Run an update script.
- C. Use the AWS Systems Manager Patch Manager capability ✅
- D. Schedule Amazon GuardDuty to run on a nightly basis.

**Explanation:** AWS Systems Manager Patch Manager automates the process of patching managed instances across EC2, Lightsail, and on-premises servers from a central location with minimal operational overhead.

---

**34.** Which AWS service provides downloads of AWS security and compliance reports?

- A. AWS Artifact ✅
- B. AWS Certificate Manager (ACM)
- C. AWS Trusted Advisor
- D. Amazon Fraud Detector

**Explanation:** AWS Artifact is the go-to service for on-demand downloads of AWS compliance reports including SOC reports, PCI DSS, ISO certifications, and other third-party attestations.

---

**35.** Which AWS service provides managed DDoS protection?

- A. AWS Firewall Manager
- B. AWS Shield ✅
- C. Amazon GuardDuty
- D. Amazon Inspector

**Explanation:** AWS Shield is a managed DDoS protection service that safeguards applications running on AWS. Shield Standard is automatically included for all AWS customers at no additional cost.

---

**36.** A company needs a file-sharing service that supports SMB protocol. Which AWS service will meet this requirement?

- A. Amazon Aurora
- B. AWS Config
- C. AWS DataSync
- D. Amazon FSx for Windows File Server ✅

**Explanation:** Amazon FSx for Windows File Server provides fully managed Windows file shares built on Windows Server, natively supporting the SMB protocol for Windows-based workloads.

---

**37.** Which AWS services or tools can a company use to track its AWS costs? (Choose two.)

- A. AWS X-Ray
- B. AWS Cost and Usage Report ✅
- C. AWS CloudTrail
- D. Cost Explorer ✅
- E. AWS Pricing Calculator

**Explanation:** AWS Cost and Usage Report provides the most detailed billing data available. AWS Cost Explorer provides interactive charts and analysis of historical and forecasted costs. Both are core cost tracking tools.

---

**38.** A company wants to migrate its main application to Amazon EC2. The application must provide low latency to users in two different geographic locations and must have disaster recovery capabilities. How can these requirements be met?

- A. Deploy the application on an EC2 instance and set up EC2 automatic recovery.
- B. Deploy the application on multiple EC2 instances running in one Availability Zone.
- C. Deploy the application on EC2 instances in Multi-AZs in a single AWS Region.
- D. Deploy the application on EC2 instances in multiple AWS Regions. ✅

**Explanation:** Deploying across multiple AWS Regions ensures low latency for users in different geographic areas and provides disaster recovery capability if an entire Region becomes unavailable.

---

**39.** A company is using Amazon RDS. Which task is the company's responsibility, according to the AWS shared responsibility model?

- A. Apply encryption options for the database ✅
- B. Manage the underlying server hardware on which Amazon RDS runs.
- C. Apply patches to the underlying operating system.
- D. Apply minor patches to the database.

**Explanation:** Customers are responsible for enabling and configuring encryption options for their RDS databases. AWS manages the hardware, OS patching, and handles minor database patches.

---

**40.** An ecommerce company wants to design a highly available application that will be hosted on multiple Amazon EC2 instances. How should the company deploy the EC2 instances to meet these requirements?

- A. Across multiple edge locations
- B. Across multiple VPCs
- C. Across multiple Availability Zones ✅
- D. Across multiple AWS accounts

**Explanation:** Deploying EC2 instances across multiple Availability Zones ensures that if one AZ experiences an outage, the application remains available through instances in other AZs within the same Region.

---

**41.** Which component of the AWS global infrastructure does Amazon CloudFront use to deliver content to end users with low latency?

- A. Edge locations ✅
- B. AWS Regions
- C. Availability Zones
- D. AWS Direct Connect connections

**Explanation:** CloudFront uses a global network of edge locations to cache and serve content from the point nearest to each end user, dramatically reducing latency for content delivery.

---

**42.** A company runs a MySQL database in the company's on-premises data center. The company wants to run a copy of the database in the AWS Cloud. Which AWS service will meet this requirement?

- A. Amazon RDS ✅
- B. Amazon Neptune
- C. Amazon ElastiCache (Redis)
- D. Amazon DynamoDB

**Explanation:** Amazon RDS supports MySQL and provides a fully managed relational database service, handling provisioning, patching, backup, and recovery automatically.

---

**43.** Which tasks can companies perform by using AWS Billing and Cost Management? (Choose two.)

- A. Estimate the cost of a planned workload. ✅
- B. Generate alerts for costs that exceed defined thresholds. ✅
- C. Manage access to AWS services and resources.
- D. Estimate the costs of migrating data centers to the cloud
- E. Conduct AWS Well-Architected Framework reviews.

**Explanation:** AWS Billing and Cost Management includes the AWS Pricing Calculator for estimating planned workload costs and AWS Budgets for setting spending thresholds and generating alerts.

---

**44.** A company wants an Amazon EC2 instance to run an application continuously for one year without interruption. Which EC2 purchasing option will meet this requirement MOST cost-effectively?

- A. Dedicated Hosts
- B. On-Demand Instances
- C. Spot Instances
- D. Standard Reserved Instances ✅

**Explanation:** Standard Reserved Instances offer up to 72% savings over On-Demand for a 1-year commitment, making them the most cost-effective option for continuous, uninterruptible workloads.

---

**45.** Which AWS service or feature provides information about governance, monitoring, and risk auditing of AWS accounts?

- A. AWS CloudTrail ✅
- B. VPC Flow Logs
- C. Amazon CloudWatch
- D. AWS Trusted Advisor

**Explanation:** AWS CloudTrail records all API calls and account activity, providing a complete audit trail for governance, compliance, and risk auditing across AWS accounts.

---

**46.** A company wants to identify which AWS services a user has operated within a specified date range. Which AWS service or resource will meet this requirement?

- A. AWS Certificate Manager (ACM)
- B. Amazon GuardDuty
- C. AWS Identity and Access Management Access Analyzer ✅
- D. Amazon S3 ACLs

---

**47.** Which AWS services are examples of NoSQL databases? (Choose two.)

- A. Amazon DynamoDB ✅
- B. Amazon ElastiCache ✅
- C. Amazon Redshift
- D. Amazon Aurora
- E. Amazon RDS for MySQL

---

**48.** Which Amazon S3 storage class is the MOST cost-effective for long-term storage?

- A. S3 Glacier Deep Archive ✅
- B. S3 Standard
- C. S3 Standard-Infrequent Access (S3 Standard-IA)
- D. S3 One Zone-Infrequent Access (S3 One Zone-IA)

---

**49.** A company needs to quickly deploy an application to the AWS Cloud. The company wants to upload code to automatically create the application infrastructure. Which AWS service will meet these requirements?

- A. AWS AppSync
- B. AWS Config
- C. AWS Elastic Beanstalk ✅
- D. AWS Outposts

---

**50.** A company is creating a document that defines the operating system patch routine for all the company's systems. Which AWS resources should the company include in this document? (Choose two.)

- A. Amazon EC2 instances ✅
- B. AWS Lambda functions
- C. AWS Fargate tasks
- D. Amazon RDS instances ✅
- E. Amazon Elastic Container Service (Amazon ECS) instances

---

**51.** Where can AWS users review answers to frequently asked questions about security in the AWS Cloud?

- A. AWS Trusted Advisor
- B. AWS Knowledge Center ✅
- C. AWS Support Center
- D. AWS Artifact

---

**52.** A company runs business applications in an on-premises data center and in the AWS Cloud. The company needs a shared file system that can be available to both environments. Which AWS service meets these requirements?

- A. Amazon Elastic Block Store (Amazon EBS)
- B. Amazon S3
- C. Amazon ElastiCache
- D. Amazon Elastic File System (Amazon EFS) ✅

---

**53.** A retail company wants to ensure its website is protected from SQL injection attacks. The website uses an Application Load Balancer to distribute traffic to multiple Amazon EC2 instances. Which AWS service or feature can be used to create a custom rule that blocks SQL injection attacks?

- A. Security groups
- B. AWS WAF ✅
- C. Network ACLs
- D. AWS Shield

---

**54.** A company needs to provide users with a list of company-generated products based on AWS services and control access by provisioning a personalized portal for specific users. Which AWS service will meet these requirements?

- A. AWS AppSync
- B. Amazon Connect
- C. AWS Organizations
- D. AWS Service Catalog ✅

---

**55.** Which AWS service can be used to encrypt data at rest?

- A. Amazon GuardDuty
- B. AWS Shield
- C. AWS Security Hub
- D. AWS Key Management Service (AWS KMS) ✅

---

**56.** Which AWS service provides inbound and outbound network ACLs to restrict connectivity to Amazon EC2 instances?

- A. AWS Identity and Access Management (IAM)
- B. Amazon Connect
- C. Amazon VPC ✅
- D. Amazon API Gateway

---

**57.** Which AWS service should a company use to decouple large monolithic applications into smaller microservices components?

- A. AWS Direct Connect
- B. Amazon Lightsail
- C. Amazon Simple Queue Service (Amazon SQS) ✅
- D. Amazon CloudWatch

---

**58.** Which AWS service can provide recommendations for cost optimization?

- A. Amazon Inspector
- B. Amazon Detective
- C. AWS CloudTrail
- D. AWS Trusted Advisor ✅

---

**59.** A company wants to manage its infrastructure as code (IaC) in the AWS Cloud. Which AWS service will meet this requirement?

- A. AWS CloudFormation ✅
- B. AWS Elastic Beanstalk
- C. AWS Glue
- D. AWS Systems Manager

---

**60.** A newly created IAM user has no IAM policy attached. What will happen when the user logs in and attempts to view the AWS resources in the account?

- A. All AWS services will be read-only access by default.
- B. Access to all AWS resources will be denied. ✅
- C. Access to the AWS billing services will be allowed.
- D. Access to AWS resources will be allowed through the AWS CLI

---

**61.** A company that has an AWS Enterprise Support plan needs to protect its applications from DDoS attacks. The company requires access to the AWS DDoS Response Team (DRT) 24 hours a day, 7 days a week. Which AWS service will meet these requirements?

- A. AWS Shield Standard
- B. AWS Shield Advanced ✅
- C. AWS Firewall Manager
- D. AWS WAF

---

**62.** A company is using Amazon EC2 instances. Which tasks are the company's responsibility, according to the AWS shared responsibility model? (Choose two.)

- A. Maintain the network infrastructure.
- B. Patch the guest operating system ✅
- C. Configure a security group on deployed EC2 instances ✅
- D. Provide physical security for the underlying hardware of the EC2 instances.
- E. Manage the underlying hypervisor.

---

**63.** A company wants to connect existing VPCs and any new VPCs the company creates in the future to a separate set of VPCs. Which AWS service will meet this requirement?

- A. AWS Config
- B. Amazon Connect
- C. AWS Direct Connect
- D. AWS Transit Gateway ✅

---

**64.** An auditor requests certification details for a company's AWS hosted resources. How should the company respond to the auditor's request?

- A. Open an AWS Support ticket to request that the TAM respond and help the auditor.
- B. Open an AWS Support ticket to request auditor approval to conduct an onsite assessment.
- C. Explain that AWS does not need to be audited because the application is hosted in multiple AZs.
- D. Use AWS Artifact to download the applicable report for AWS security controls. Provide the report to the auditor. ✅

---

**65.** A company runs Amazon EC2 instances and an Amazon EFS file system on AWS and needs to centralize the data copies. Which AWS service will meet this requirement with the LEAST amount of operational effort?

- A. AWS Backup ✅
- B. AWS Config
- C. Amazon Inspector
- D. Amazon S3

---

**66.** A company needs to build a mobile app for iOS and Android on AWS. Which AWS service should the company use?

- A. Amazon SageMaker
- B. Amazon Elastic Kubernetes Service (Amazon EKS)
- C. AWS Amplify ✅
- D. AWS CodeBuild

---

**67.** A company needs to migrate its website from on premises to the AWS Cloud. The website must be hosted on hardware that is not shared with other companies. The company wants to use its existing per-socket, per-core software licenses. Which Amazon EC2 instance purchasing option will meet these requirements?

- A. Dedicated Instance
- B. Reserved Instance
- C. Dedicated Host ✅
- D. On-Demand Instance

---

**68.** A company's security policy requires a record of all changes made to Amazon EC2 security groups, including who made the change and when. Which AWS service will provide this information?

- A. AWS Lambda
- B. Amazon CloudWatch
- C. AWS WAF
- D. AWS CloudTrail ✅

---

**69.** Which of the following is an AWS best practice for using the AWS account root user credentials?

- A. Allow only the manager to use the account root user credentials for normal activities.
- B. Use the account root user credentials only for Amazon EC2 instances from the AWS Free Tier.
- C. Use the account root user credentials only when they alone must be used to perform a required function. ✅
- D. Use the account root user credentials only for the creation of private VPC subnets.

---

**70.** A company is running a globally-accessible application on AWS. The company wants to optimize the application's network traffic. Which AWS service will meet this requirement?

- A. AWS Auto Scaling
- B. AWS CloudFormation
- C. Amazon Connect
- D. AWS Global Accelerator ✅

---

**71.** A company wants to migrate its on-premises PostgreSQL database to a managed PostgreSQL database on AWS. Which AWS service will meet this requirement?

- A. Amazon DynamoDB
- B. Amazon Neptune
- C. Amazon RDS ✅
- D. Amazon Redshift

---

**72.** Which task is the shared responsibility of the customer and AWS under the AWS shared responsibility model?

- A. Installing hardware infrastructure
- B. Managing security ✅
- C. Managing guest operating systems
- D. Protecting the physical infrastructure that runs all services

---

**73.** Which Amazon RDS management task is the customer's responsibility under the AWS shared responsibility model?

- A. Configuring network access to Amazon RDS ✅
- B. Configuring physical security controls for Amazon RDS
- C. Managing Amazon RDS infrastructure
- D. Patching and updating Amazon RDS host operating systems

---

**74.** Which documentation does AWS Artifact provide?

- A. Amazon EC2 terms and conditions
- B. AWS ISO certifications ✅
- C. A history of a company's AWS spending
- D. A list of previous-generation Amazon EC2 instance types

---

**75.** A company plans to migrate to the AWS Cloud. The company must gather information about its on-premises applications, such as hostnames, IP addresses, and MAC addresses. Which AWS service will meet these requirements?

- A. AWS Application Discovery Service ✅
- B. AWS Application Migration Service
- C. AWS Database Migration Service (AWS DMS)
- D. AWS X-Ray

---

**76.** Which AWS service offers threat detection and continuously monitors for malicious activity and unauthorized behavior in AWS accounts?

- A. Amazon Macie
- B. AWS Config
- C. Amazon GuardDuty ✅
- D. Amazon Inspector

---

**77.** A company purchases Amazon EC2 Standard Reserved Instances to run a workload. After the workload is complete, the company no longer requires the Reserved Instances. Which solution will meet this requirement?

- A. Contact the AWS Support team to request the Standard Reserved Instances are transferred.
- B. Convert the Standard Reserved Instances to Compute Savings Plans.
- C. Create an Amazon Machine Image (AMI) of the Reserved Instances.
- D. Sell the Standard Reserved Instances in the Amazon EC2 Reserved Instance Marketplace ✅

---

**78.** A company needs to ensure that users around the world can access the company's application with low latency. Which advantage of the AWS Cloud will meet this requirement?

- A. Avoid data center costs
- B. Global infrastructure ✅
- C. Larger application leads to cost savings
- D. Pay-as-you-go pricing

---

**79.** A company is running its application in the AWS Cloud and wants to protect against a DDoS attack with near real-time visibility. Which AWS service will meet these requirements with the MOST features for DDoS protection?

- A. AWS Shield Advanced ✅
- B. AWS Shield
- C. Amazon GuardDuty
- D. Network ACLs

---

**80.** A company is developing a new web application. The company must give users the ability to log in to the application through social identity providers. Which AWS service will meet these requirements?

- A. AWS Directory Service
- B. Amazon Cognito ✅
- C. AWS Identity and Access Management (IAM)
- D. AWS IAM Identity Center

---

**81.** A company needs to collect and assess data for on-premises servers and applications before the company migrates its infrastructure to AWS. Which AWS service will meet these requirements?

- A. Amazon Connect
- B. AWS Migration Hub ✅
- C. Amazon QuickSight
- D. AWS Step Functions

---

**82.** A company is running applications on Amazon EC2 instances in the same AWS account for several different projects. The company wants to track infrastructure costs for each project with the least possible impact to existing infrastructure and no additional cost. What should the company do?

- A. Use a different EC2 instance type for each project.
- B. Publish project-specific custom Amazon CloudWatch metrics for each application.
- C. Deploy EC2 instances for each project in a separate AWS account.
- D. Use cost allocation tags with values that are specific to each project. ✅
