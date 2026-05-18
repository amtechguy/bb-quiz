**1.** A global company with a large number of AWS accounts is seeking a way in which they can centrally manage billing and security policies across all accounts. Which AWS Service will assist them in meeting these goals?

- A. AWS Trusted Advisor.
- B. IAM User Groups.
- C. AWS Config.
- D. AWS Organizations ✅

**Explanation:** AWS Organizations allows you to centrally manage multiple AWS accounts, consolidate billing, and apply Service Control Policies (SCPs) to enforce security and compliance across all accounts.

---

**2.** Which service provides object-level storage in AWS?

- A. Amazon Instance Store.
- B. Amazon EFS.
- C. Amazon S3. ✅
- D. Amazon EBS

**Explanation:** Amazon S3 (Simple Storage Service) is AWS's object storage service, designed to store and retrieve any amount of data as objects within buckets.

---

**3.** A company is concerned that they are spending money on underutilized compute resources in AWS. Which AWS feature will help ensure that their applications are automatically adding/removing EC2 compute capacity to closely match the required demand?

- A. AWS Budgets.
- B. AWS Auto Scaling. ✅
- C. AWS Cost Explorer.
- D. Elastic Load Balancer

**Explanation:** AWS Auto Scaling monitors your applications and automatically adjusts EC2 capacity to maintain steady, predictable performance at the lowest possible cost.

---

**4.** Which S3 storage class is best for data with unpredictable access patterns?

- A. Amazon S3 Glacier Flexible Retrieval.
- B. Amazon S3 Standard.
- C. Amazon S3 Standard-Infrequent Access.
- D. S3 Intelligent Tiering ✅

**Explanation:** S3 Intelligent-Tiering automatically moves objects between access tiers based on changing access patterns, making it ideal when access patterns are unknown or unpredictable.

---

**5.** What is the AWS database service that allows you to upload data structured in key-value format?

- A. Amazon Aurora.
- B. Amazon Redshift.
- C. Amazon RDS.
- D. AWS DynamoDB ✅

**Explanation:** Amazon DynamoDB is a fully managed NoSQL database service that supports key-value and document data structures, offering single-digit millisecond performance at any scale.

---

**6.** Which of the following is NOT correct regarding Amazon EC2 On-demand instances?

- A. The on-demand instances follow the AWS pay-as-you-go pricing model.
- B. With on-demand instances no longer-term commitments or upfront payments are needed.
- C. When using on-demand Linux instances you pay a start-up fee when launching a new instance for the first time. ✅
- D. You can spin up on-demand instance whenever you require them.

**Explanation:** There is no start-up fee for On-Demand Linux instances. You simply pay for the compute capacity you use per second (with a minimum of 60 seconds), with no upfront costs or commitments.

---

**7.** A company has moved to AWS recently. Which of the following AWS Services will help ensure that they have the proper security settings? (Choose TWO)

- A. Amazon Inspector. ✅
- B. Amazon SNS.
- C. Amazon CloudWatch.
- D. Concierge Support Team.
- E. AWS Trusted Advisor. ✅

**Explanation:** Amazon Inspector automatically assesses applications for vulnerabilities and deviations from best practices. AWS Trusted Advisor provides real-time guidance to help provision resources following AWS security best practices.

---

**8.** What is the AWS feature that provides an additional level of security above the default authentication mechanism of usernames and passwords?

- A. Email verification.
- B. AWS KMS.
- C. AWS MFA. ✅
- D. CloudHSM

**Explanation:** AWS Multi-Factor Authentication (MFA) adds an extra layer of protection on top of your username and password by requiring a second form of authentication, such as a one-time code from a hardware or virtual device.

---

**9.** A company is introducing a new product to their customers, and is expecting a surge in traffic to their web application. As part of their Enterprise Support plan, which of the following provides the company with architectural and scaling guidance?

- A. AWS Health Dashboard.
- B. Infrastructure Event Management. ✅
- C. AWS Support Concierge Service.
- D. AWS Knowledge Center.

**Explanation:** Infrastructure Event Management (IEM) is an AWS Enterprise Support feature that provides architectural and scaling guidance before, during, and after significant events such as product launches or peak traffic periods.

---

**10.** You work as an on-premises MySQL DBA. The work of database configuration, backups, patching, and DR can be time-consuming and repetitive. Your company has decided to migrate to the AWS Cloud. Which of the following can help save time on database maintenance so you can focus on data architecture and performance?

- A. Amazon Redshift.
- B. Amazon DynamoDB.
- C. Amazon CloudWatch.
- D. Amazon RDS. ✅

**Explanation:** Amazon RDS (Relational Database Service) is a managed service that automates time-consuming administration tasks like hardware provisioning, database setup, patching, and backups, freeing you to focus on your applications.

---

**11.** Which of the below is a best-practice when designing solutions on AWS?

- A. Use AWS reservations to reduce costs when testing your production environment.
- B. Use IAM users to grant temporary access to services or applications
- C. Provision a large compute capacity to handle any spikes in load
- D. Invest heavily in architecting your environment ✅

**Explanation:** AWS recommends investing in good architecture upfront. The AWS Well-Architected Framework emphasizes designing resilient, efficient, and cost-effective systems rather than retrofitting architecture later.

---

**12.** Which service is used to ensure that messages between software components are not lost if one or more components fail?

- A. Amazon SES.
- B. AWS Direct Connect.
- C. Amazon Connect.
- D. Amazon SQS. ✅

**Explanation:** Amazon SQS (Simple Queue Service) is a fully managed message queuing service that decouples and scales microservices, distributed systems, and serverless applications, ensuring messages are not lost if a component fails.

---

**13.** The principle "design for failure and nothing will fail" is very important when designing your AWS Cloud architecture. Which of the following would help adhere to this principle? (Choose TWO)

- A. Availability Zones. ✅
- B. Elastic Load Balancing. ✅
- C. Penetration testing.
- D. Vertical Scaling.
- E. Multi-factor authentication.

**Explanation:** Deploying across multiple Availability Zones eliminates single points of failure at the infrastructure level. Elastic Load Balancing distributes traffic across healthy instances, automatically routing around failures.

---

**14.** What is the AWS service that provides a virtual network dedicated to your AWS account?

- A. AWS Subnets.
- B. AWS Dedicated Hosts.
- C. Amazon VPC. ✅
- D. AWS VPN.

**Explanation:** Amazon VPC (Virtual Private Cloud) lets you provision a logically isolated section of the AWS Cloud where you can launch AWS resources in a virtual network that you define and control.

---

**15.** According to the AWS Shared responsibility model, which of the following are the responsibility of the customer? (Choose TWO)

- A. Protecting the confidentiality of data in transit in Amazon S3. ✅
- B. Controlling physical access to AWS Regions.
- C. Ensuring that the underlying EC2 host is configured properly.
- D. Patching applications installed on Amazon EC2. ✅
- E. Managing environmental events of AWS data centers.

**Explanation:** Customers are responsible for security IN the cloud: encrypting data in transit, managing their own applications, and patching OS and software on EC2 instances. AWS is responsible for the physical infrastructure.

---

**16.** Which of the following AWS services can be used as a compute resource? (Choose TWO)

- A. Amazon CloudWatch.
- B. Amazon S3.
- C. Amazon EC2. ✅
- D. AWS Lambda. ✅
- E. Amazon VPC.

**Explanation:** Amazon EC2 provides resizable virtual server capacity. AWS Lambda is a serverless compute service that runs code in response to events. Both are core AWS compute services.

---

**17.** Your company is designing a new application that will store and retrieve photos and videos. Which of the following services should you recommend as the underlying storage mechanism?

- A. Amazon SQS.
- B. Amazon S3. ✅
- C. Amazon Instance store.
- D. Amazon EBS.

**Explanation:** Amazon S3 is the ideal service for storing and retrieving any amount of unstructured data such as photos and videos. It offers durability, scalability, and built-in media hosting features.

---

**18.** Which of the following is equivalent to a user name and password and is used to authenticate your programmatic access to AWS services and APIs?

- A. Key pairs.
- B. Access Keys. ✅
- C. MFA.
- D. Instance Password.
- E. Encryption Keys

**Explanation:** AWS Access Keys consist of an Access Key ID and a Secret Access Key. They are used to authenticate programmatic requests to AWS APIs via the CLI, SDKs, and direct API calls.

---

**19.** What does Amazon ElastiCache provide?

- A. An Ehcache compatible in-memory data store.
- B. An online software store that allows customers to launch pre-configured software with just few clicks.
- C. A domain name system in the cloud.
- D. In-memory caching for read-heavy applications. ✅

**Explanation:** Amazon ElastiCache is a fully managed in-memory caching service supporting Redis and Memcached. It improves application performance by retrieving data from fast, managed caches instead of slower disk-based databases.

---

**20.** What is the AWS service that enables you to manage all of your AWS accounts from a single master account?

- A. AWS Trusted Advisor.
- B. AWS Organizations. ✅
- C. Amazon Config.
- D. AWS WAF.

**Explanation:** AWS Organizations allows you to consolidate multiple AWS accounts into an organization that you create and centrally manage, including consolidated billing and policy-based management.

---

**21.** Which of the following EC2 instance purchasing options supports the Bring Your Own License (BYOL) model for almost every BYOL scenario?

- A. Dedicated Hosts. ✅
- B. On-demand Instances.
- C. Reserved Instances.
- D. Dedicated Instances.

**Explanation:** Dedicated Hosts provide you with a physical server fully dedicated to your use, giving you visibility into the number of sockets and physical cores. This is required by most BYOL licensing agreements that are tied to per-socket or per-core metrics.

---

**22.** Which of the following is one of the benefits of moving infrastructure from an on-premises data center to AWS?

- A. Automatic data protection.
- B. Reduced Capital Expenditure (CapEx). ✅
- C. AWS holds responsibility for managing customer applications.
- D. Free support for all enterprise customers.

**Explanation:** Moving to AWS shifts spending from capital expenditure (buying hardware) to operational expenditure (paying for what you use). This eliminates large upfront investments and allows you to scale costs with your business.

---

**23.** Which of the following are important design principles you should adopt when designing systems on AWS? (Choose TWO)

- A. Always choose to pay as you go.
- B. Treat servers as fixed resources.
- C. Automate wherever possible. ✅
- D. Remove single points of failure. ✅
- E. Always use Global Services in your architecture rather than Regional Services.

**Explanation:** AWS Well-Architected best practices include automating manual processes to reduce human error and increase consistency, and designing for resilience by eliminating single points of failure through redundancy.

---

**24.** A user is planning to migrate an application workload to the AWS Cloud. Which control becomes the responsibility of AWS once the migration is complete?

- A. Patching the guest operating system
- B. Maintaining physical and environmental controls ✅
- C. Protecting communications and maintaining zone security
- D. Patching specific applications

**Explanation:** Under the AWS Shared Responsibility Model, AWS is always responsible for the physical infrastructure including data center security, environmental controls (power, cooling), and hardware maintenance.

---

**25.** Which services can be used to deploy applications on AWS? (Choose two.)

- A. AWS Elastic Beanstalk ✅
- B. AWS Config
- C. AWS OpsWorks ✅
- D. AWS Application Discovery Service
- E. Amazon Kinesis

**Explanation:** AWS Elastic Beanstalk is a PaaS that automatically handles deployment, capacity provisioning, and scaling. AWS OpsWorks is a configuration management service using Chef and Puppet to automate application deployment.

---

**26.** Which AWS service can be used to provide an on-demand, cloud-based contact center?

- A. AWS Direct Connect
- B. Amazon Connect ✅
- C. AWS Support Center
- D. AWS Managed Services

**Explanation:** Amazon Connect is an easy-to-use omnichannel cloud contact center that helps companies provide superior customer service at lower cost, with no upfront payments or long-term commitments.

---

**27.** What tool enables customers without an AWS account to estimate costs for almost all AWS services?

- A. Cost Explorer
- B. TCO Calculator
- C. AWS Budgets
- D. AWS Pricing Calculator ✅

**Explanation:** The AWS Pricing Calculator is a free web-based tool that lets anyone — including those without an AWS account — estimate the cost of AWS services for their specific use case and architecture.

---

**28.** Which component must be attached to a VPC to enable inbound Internet access?

- A. NAT gateway
- B. VPC endpoint
- C. VPN connection
- D. Internet gateway ✅

**Explanation:** An Internet Gateway is a horizontally scaled, redundant VPC component that allows communication between your VPC and the internet. It enables resources in public subnets to receive inbound connections from the internet.

---

**29.** Which pricing model would result in maximum Amazon Elastic Compute Cloud (Amazon EC2) savings for a database server that must be online for one year?

- A. Spot Instance
- B. On-Demand Instance
- C. Partial Upfront Reserved Instance ✅
- D. No Upfront Reserved Instance

**Explanation:** For workloads running continuously for one year, Reserved Instances offer significant savings over On-Demand. Partial Upfront Reserved Instances provide greater discounts than No Upfront, and Spot Instances are unsuitable as they can be interrupted.

---

**30.** A company has a MySQL database running on a single Amazon EC2 instance. The company now requires higher availability in the event of an outage. Which set of tasks would meet this requirement?

- A. Add an Application Load Balancer in front of the EC2 instance
- B. Configure EC2 Auto Recovery to move the instance to another Availability Zone
- C. Migrate to Amazon RDS and enable Multi-AZ ✅
- D. Enable termination protection for the EC2 instance to avoid outages

**Explanation:** Amazon RDS Multi-AZ deployments provide enhanced availability by automatically provisioning a synchronous standby replica in a different Availability Zone, with automatic failover in case of an outage.

---

**31.** A company wants to ensure that AWS Management Console users are meeting password complexity requirements. How can the company configure password complexity?

- A. Using an AWS IAM user policy
- B. Using an AWS Organizations service control policy (SCP)
- C. Using an AWS IAM account password policy ✅
- D. Using an AWS Security Hub managed insight

**Explanation:** IAM account password policies allow administrators to enforce password requirements for all IAM users, including minimum length, character types, expiration, and reuse restrictions.

---

**32.** A company is building an application that requires the ability to send, store, and receive messages between application components. The company has another requirement to process messages in first-in, first-out (FIFO) order. Which AWS service should the company use?

- A. AWS Step Functions
- B. Amazon Simple Notification Service (Amazon SNS)
- C. Amazon Kinesis Data Streams
- D. Amazon Simple Queue Service (Amazon SQS) ✅

**Explanation:** Amazon SQS FIFO queues are designed to ensure that messages are processed exactly once, in the exact order they are sent, making it the right choice for applications requiring strict FIFO message ordering.

---

**33.** AnyCompany recently purchased Example Corp. Both companies use AWS resources, and AnyCompany wants a single aggregated bill. Which option allows AnyCompany to receive a single bill?

- A. Example Corp. must submit a request to its AWS solutions architect or AWS technical account manager to link the accounts and consolidate billing.
- B. AnyCompany must create a new support case in the AWS Support Center requesting that both bills be combined.
- C. Send an invitation to join the organization from AnyCompany's AWS Organizations master account to Example Corp. ✅
- D. Migrate the Example Corp. VPCs, Amazon EC2 instances, and other resources into the AnyCompany AWS account.

**Explanation:** AWS Organizations enables consolidated billing by inviting existing AWS accounts to join your organization. The management (master) account receives a single bill covering all member accounts.

---

**34.** Which tool can be used to create alerts when the actual or forecasted cost of AWS services exceeds a certain threshold?

- A. Cost Explorer
- B. AWS Budgets ✅
- C. AWS Cost and Usage Report
- D. AWS CloudTrail

**Explanation:** AWS Budgets allows you to set custom cost and usage budgets and receive alerts via email or SNS when your actual or forecasted costs exceed your defined thresholds.

---

**35.** A user has limited knowledge of AWS services, but wants to quickly deploy a scalable Node.js application in the AWS Cloud. Which service should be used to deploy the application?

- A. AWS CloudFormation
- B. AWS Elastic Beanstalk ✅
- C. Amazon EC2
- D. AWS OpsWorks

**Explanation:** AWS Elastic Beanstalk is the easiest way to deploy and scale web applications. You simply upload your code and Elastic Beanstalk automatically handles capacity provisioning, load balancing, auto-scaling, and monitoring.

---

**36.** Which AWS Trusted Advisor check is available to all AWS users?

- A. Core checks ✅
- B. All checks
- C. Fault tolerance checks
- D. Cost optimization checks

**Explanation:** All AWS customers get access to the core Trusted Advisor checks (7 security checks and service limit checks) regardless of support plan. Full access to all checks requires Business or Enterprise Support.

---

**37.** A web developer is concerned that a DDoS attack could target an application. Which AWS services or features can help protect against such an attack? (Choose two.)

- A. AWS Shield ✅
- B. AWS CloudTrail
- C. Amazon CloudFront ✅
- D. AWS Support Center
- E. AWS Service Health Dashboard

**Explanation:** AWS Shield is a managed DDoS protection service that safeguards AWS applications. Amazon CloudFront helps mitigate DDoS attacks by distributing traffic across edge locations and absorbing attack traffic.

---

**38.** Which AWS service gives users on-demand, self-service access to AWS compliance control reports?

- A. AWS Config
- B. Amazon GuardDuty
- C. AWS Trusted Advisor
- D. AWS Artifact ✅

**Explanation:** AWS Artifact is a self-service audit artifact retrieval portal that provides customers with on-demand access to AWS compliance documentation, such as SOC reports, PCI DSS reports, and ISO certifications.

---

**39.** A company wants to provide one of its employees with access to Amazon RDS. The company also wants to limit the interaction to only the AWS CLI and AWS software development kits (SDKs). Which combination of actions should the company take to meet these requirements while following the principles of least privilege? (Choose two.)

- A. Create an IAM user and provide AWS Management Console access only.
- B. Create an IAM user and provide programmatic access only. ✅
- C. Create an IAM role and provide AWS Management Console access only.
- D. Create an IAM policy with administrator access and attach it to the IAM user.
- E. Create an IAM policy with Amazon RDS access and attach it to the IAM user. ✅

**Explanation:** Programmatic access (access keys) enables CLI and SDK access without Console access. Attaching a policy with only RDS permissions follows least privilege by granting only the minimum permissions required.

---

**40.** A company has a compliance requirement to record and evaluate configuration changes, as well as perform remediation actions on AWS resources. Which AWS service should the company use?

- A. AWS Config ✅
- B. AWS Secrets Manager
- C. AWS CloudTrail
- D. AWS Trusted Advisor

**Explanation:** AWS Config continuously monitors and records AWS resource configurations, evaluates them against desired rules, and can trigger automatic remediation actions through AWS Systems Manager when configurations drift.

---

**41.** What are the advantages of deploying an application with Amazon EC2 instances in multiple Availability Zones? (Choose two.)

- A. Preventing a single point of failure ✅
- B. Reducing the operational costs of the application
- C. Allowing the application to serve cross-region users with low latency
- D. Increasing the availability of the application ✅
- E. Increasing the load of the application

**Explanation:** Deploying across multiple AZs eliminates single points of failure at the infrastructure level and ensures the application remains available even if one AZ experiences an outage, significantly increasing overall availability.

---

**42.** A workload on AWS will run for the foreseeable future by using a consistent number of Amazon EC2 instances. What pricing model will minimize cost while ensuring that compute resources remain available?

- A. Dedicated Hosts
- B. On-Demand Instances
- C. Spot Instances
- D. Reserved Instances ✅

**Explanation:** Reserved Instances provide up to 72% discount compared to On-Demand pricing in exchange for a 1 or 3-year commitment. For stable, predictable workloads running long-term, they offer the best cost savings while guaranteeing capacity.

---

**43.** Which of the following is the customer's responsibility when using Amazon RDS?

- A. Patching the operating system of underlying hardware
- B. Controlling traffic to and from the database through security groups ✅
- C. Running backups that enable point-in-time recovery of a DB instance
- D. Replacing failed DB instances

**Explanation:** Under the shared responsibility model for RDS, AWS manages the underlying infrastructure, OS patching, backups, and hardware replacement. Customers are responsible for network access controls such as configuring security groups.

---

**44.** What is the customer's responsibility when using AWS Lambda?

- A. Operating system configuration
- B. Application management ✅
- C. Platform management
- D. Code encryption

**Explanation:** With AWS Lambda, AWS manages the infrastructure, OS, runtime, and scaling. The customer is responsible for the application code itself — its logic, dependencies, and correct functioning.

---

**45.** A company wants to be notified when its AWS Cloud costs or usage exceed defined thresholds. Which AWS service will support these requirements?

- A. Amazon Macie
- B. Cost Explorer
- C. AWS Budgets ✅
- D. AWS CloudTrail

**Explanation:** AWS Budgets lets you set custom budgets and configure alerts to be sent via email or Amazon SNS when your actual or forecasted costs and usage exceed your defined thresholds.

---

**46.** Which AWS service provides the ability to host a NoSQL database in the AWS Cloud?

- A. Amazon Aurora
- B. Amazon DynamoDB ✅
- C. Amazon RDS
- D. Amazon Redshift

**Explanation:** Amazon DynamoDB is a fully managed, serverless NoSQL key-value and document database. It delivers single-digit millisecond performance at any scale and is designed for high-throughput applications.

---

**47.** Which AWS service allows customers to purchase unused Amazon EC2 capacity at an often discounted rate?

- A. Reserved Instances
- B. On-Demand Instances
- C. Spot Instances ✅
- D. Dedicated Instances

**Explanation:** EC2 Spot Instances let you take advantage of unused EC2 capacity in the AWS cloud at up to 90% off On-Demand prices. They are ideal for flexible, fault-tolerant workloads that can tolerate interruptions.

---

**48.** Which AWS service or feature requires an internet service provider (ISP) and a colocation facility to be implemented?

- A. Internet gateway
- B. Amazon Connect
- C. AWS VPN
- D. AWS Direct Connect ✅

**Explanation:** AWS Direct Connect establishes a dedicated physical network connection between your premises and AWS. Setting it up requires working with an ISP and a Direct Connect location (colocation facility) to provision the physical circuit.

---

**49.** Which AWS services offer compute capabilities? (Choose two.)

- A. Amazon Macie
- B. Amazon EC2 ✅
- C. Amazon Elastic Block Store (Amazon EBS)
- D. AWS Lambda ✅
- E. Amazon Cognito

**Explanation:** Amazon EC2 provides virtual server compute capacity. AWS Lambda is a serverless compute service that executes code in response to events. Both are fundamental AWS compute services.

---

**50.** Which AWS service can be used to privately store and manage versions of source code?

- A. AWS CodeCommit ✅
- B. AWS CodeStar
- C. AWS CodeBuild
- D. AWS CodePipeline

**Explanation:** AWS CodeCommit is a fully managed, private source control service that hosts secure Git repositories, allowing teams to store and version control code without needing to manage their own source control infrastructure.

---

**51.** Which AWS service should a cloud practitioner use to identify security vulnerabilities of an AWS account?

- A. AWS Secrets Manager
- B. Amazon Cognito
- C. AWS Trusted Advisor ✅
- D. Amazon Macie

**Explanation:** AWS Trusted Advisor inspects your AWS environment and provides real-time recommendations across security, cost optimization, performance, and fault tolerance — including checks for open S3 buckets, unrestricted security groups, and missing MFA.

---

**52.** What are the benefits of consolidated billing for AWS Cloud services? (Choose two.)

- A. Volume discounts ✅
- B. A minimal additional fee for use
- C. Installment payment options
- D. One bill for multiple accounts ✅
- E. Custom cost and usage budget creation

**Explanation:** AWS Organizations consolidated billing combines usage across all accounts to qualify for volume pricing discounts, and delivers a single bill to the management account covering all member accounts for simplified financial management.

---

**53.** A company is expecting a short-term spike in internet traffic for its application. During the traffic increase, the application cannot be interrupted. The company also needs to minimize cost and maximize flexibility. Which Amazon EC2 instance type should the company use to meet these requirements?

- A. Spot Instances
- B. Reserved Instances
- C. Dedicated Hosts
- D. On-Demand Instances ✅

**Explanation:** On-Demand Instances are ideal for short-term, unpredictable workloads that cannot be interrupted. They provide maximum flexibility with no long-term commitments, and you pay only for the compute time you actually use.

---

**54.** A company wants to track AWS resource configuration changes for compliance reasons. Which AWS feature can be used to meet this requirement?

- A. AWS Cost and Usage Report
- B. AWS Organizations service control policies (SCPs)
- C. AWS Config rules ✅
- D. VPC Flow Logs

**Explanation:** AWS Config rules continuously evaluate the configuration of your AWS resources against desired settings. They record configuration changes over time, making it easy to audit and demonstrate compliance with internal policies and regulatory standards.
