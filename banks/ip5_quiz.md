**1.** What time-savings advantage is offered with the use of Amazon Rekognition?

- A. Amazon Rekognition provides automatic watermarking of images.
- B. Amazon Rekognition provides automatic detection of objects appearing in pictures. ✅
- C. Amazon Rekognition provides the ability to resize millions of images automatically.

**Explanation:** Amazon Rekognition uses deep learning to automatically identify objects, people, text, scenes, and activities in images and videos, saving developers significant time compared to building custom image analysis solutions.

---

**2.** When comparing AWS with on-premises Total Cost of Ownership (TCO), what costs are included?

- A. Data center security ✅
- B. Business analysis
- C. Project management

**Explanation:** On-premises TCO includes physical costs like data center security, hardware, power, cooling, and facilities. Business analysis and project management are common to both environments and are not differentiating TCO factors.

---

**3.** According to the AWS shared responsibility model, what is AWS responsible for?

- A. Configuring Amazon VPC
- B. Managing application code
- C. Maintaining application traffic
- D. Providing Security for Data Centers ✅

**Explanation:** AWS is responsible for the security OF the cloud, which includes protecting the physical infrastructure — data centers, hardware, networking, and facilities. VPC configuration, application code, and traffic management are customer responsibilities.

---

**4.** Which service should be used to estimate the costs of running a new project on AWS?

- A. AWS TCO Calculator
- B. AWS Simple Monthly Calculator ✅
- C. AWS Cost Explorer API

**Explanation:** The AWS Simple Monthly Calculator (now the AWS Pricing Calculator) allows you to estimate the monthly cost of AWS services for a new project or architecture before you deploy anything.

---

**5.** Which AWS tool will identify security groups that grant unrestricted Internet access to a limited list of ports?

- A. AWS Organizations
- B. AWS Trusted Advisor ✅
- C. AWS Usage Report

**Explanation:** AWS Trusted Advisor includes security checks that identify security groups with rules allowing unrestricted access (0.0.0.0/0) to specific ports, helping you reduce your attack surface.

---

**6.** Which AWS service can be used to generate alerts based on an estimated monthly bill?

- A. AWS Config
- B. Amazon CloudWatch ✅
- C. AWS X-Ray

**Explanation:** Amazon CloudWatch can be configured with billing alarms that trigger when your estimated charges exceed a threshold you define, sending notifications via Amazon SNS.

---

**7.** Which Amazon EC2 pricing model offers the MOST significant discount when compared to On-Demand Instances?

- A. Partial Upfront Reserved Instances for a 1-year term
- B. All Upfront Reserved Instances for a 1-year term
- C. All Upfront Reserved Instances for a 3-year term ✅

**Explanation:** The greatest EC2 discount comes from All Upfront Reserved Instances with a 3-year term, which can save up to 72% compared to On-Demand pricing. Longer commitment plus full upfront payment yields the highest discount.

---

**8.** Which of the following is the responsibility of AWS?

- A. Setting up AWS Identity and Access Management (IAM) users and groups
- B. Physically destroying storage media at end of life ✅
- C. Patching guest operating systems

**Explanation:** AWS is responsible for decommissioning and destroying physical storage media at the end of its life, following industry standards. IAM configuration and guest OS patching are the customer's responsibility.

---

**9.** Which of the following is an advantage of using AWS?

- A. AWS audits user data.
- B. Data is automatically secure.
- C. There is no guessing on capacity needs. ✅

**Explanation:** One of the key advantages of AWS is the ability to provision exactly the capacity you need and scale it up or down on demand, eliminating the need to over-provision or under-provision based on guesses about future demand.

---

**10.** Which AWS service would a customer use with a static website to achieve lower latency and high transfer speeds?

- A. AWS Lambda
- B. Amazon DynamoDB Accelerator
- C. Amazon Route 53
- D. Amazon CloudFront ✅

**Explanation:** Amazon CloudFront is a global CDN that caches website content at edge locations worldwide, delivering it to users from the location closest to them — reducing latency and improving transfer speeds for static websites.

---

**11.** Which services manage and automate application deployments on AWS? (Choose two.)

- A. AWS Elastic Beanstalk ✅
- B. AWS CodeCommit
- C. AWS Data Pipeline
- D. AWS CodeDeploy ✅

**Explanation:** AWS Elastic Beanstalk automates deployment including provisioning, load balancing, and scaling. AWS CodeDeploy automates code deployments to EC2 instances, Lambda functions, and on-premises servers.

---

**12.** A user wants guidance on possible savings when migrating from on-premises to AWS. Which tool is suitable for this scenario?

- A. AWS Budgets
- B. Cost Explorer
- C. AWS Total Cost of Ownership (TCO) Calculator ✅

**Explanation:** The AWS TCO Calculator compares the cost of running workloads in on-premises data centers versus on AWS, helping organizations estimate potential savings when considering migration to the cloud.

---

**13.** Which principles are used to architect applications for reliability on the AWS Cloud? (Choose two.)

- A. Create IAM roles
- B. Use multiple Availability Zones ✅
- C. Implement security best practices
- D. Manage changes via documented processes
- E. Design for automated failure recovery ✅

**Explanation:** Reliability in the AWS Well-Architected Framework involves deploying across multiple Availability Zones to eliminate single points of failure and designing systems that automatically detect and recover from failures without manual intervention.

---

**14.** What tasks should a customer perform when that customer suspects an AWS account has been compromised? (Choose two.)

- A. Remove MFA tokens.
- B. Rotate passwords and access keys. ✅
- C. Move resources to a different AWS Region.
- D. Enforce stricter password policy for IAM Users ✅
- E. Delete S3 buckets

**Explanation:** When an account may be compromised, immediately rotate all credentials (passwords and access keys) to invalidate any stolen keys, and enforce stronger password requirements to prevent future unauthorized access.

---

**15.** What is an example of high availability in the AWS Cloud?

- A. Consulting AWS technical support at any time day or night
- B. Ensuring an application remains accessible even if a resource fails ✅
- C. Setting termination protection on EC2 Instances

**Explanation:** High availability means designing systems so they continue operating even when individual components fail. Deploying across multiple AZs ensures the application stays accessible even if one instance or AZ goes down.

---

**16.** Which AWS security service protects applications from distributed denial of service attacks with always-on detection and automatic inline mitigation?

- A. Amazon Inspector
- B. AWS Web Application Firewall (AWS WAF) ✅
- C. Elastic Load Balancing (ELB)

**Explanation:** AWS WAF (Web Application Firewall) helps protect web applications from common web exploits and DDoS attacks at the application layer. It works with CloudFront, ALB, and API Gateway to filter and monitor HTTP traffic.

---

**17.** A company wants to monitor the CPU usage of its Amazon EC2 resources. Which AWS service should the company use?

- A. AWS CloudTrail
- B. Amazon CloudWatch ✅
- C. AWS Cost and Usage report

**Explanation:** Amazon CloudWatch collects and tracks metrics including CPU utilization, network traffic, and disk I/O for EC2 instances. You can set alarms to notify you when metrics exceed defined thresholds.

---

**18.** What is an AWS Identity and Access Management (IAM) role?

- A. A user associated with an AWS resource
- B. A group associated with an AWS resource
- C. An entity that defines a set of permissions for use with an AWS resource ✅

**Explanation:** An IAM role is an AWS identity with permission policies that determine what the role can and cannot do in AWS. Unlike users, roles are not associated with a specific person and can be assumed by users, services, or applications that need temporary access.

---

**19.** What are the advantages of Reserved Instances? (Choose two.)

- A. They provide a discount over on-demand pricing. ✅
- B. They provide access to additional instance types.
- C. They provide additional networking capability.
- D. They lead to cost savings from using compute resources ✅

**Explanation:** Reserved Instances offer significant discounts (up to 72%) compared to On-Demand pricing in exchange for committing to a 1 or 3-year term, directly reducing the total cost of running compute workloads.

---

**20.** How do Amazon EC2 Auto Scaling groups help achieve high availability for a web application?

- A. They automatically add more instances across multiple AWS Regions based on global demand of the application.
- B. They automatically add or replace instances across multiple Availability Zones when the application needs it. ✅
- C. They enable the application's static content to reside closer to end users.

**Explanation:** EC2 Auto Scaling groups maintain the desired number of instances across multiple AZs, automatically launching replacements if an instance becomes unhealthy and adding capacity during demand spikes.

---

**21.** How can one AWS account use Reserved Instances from another AWS account?

- A. By using Amazon EC2 Dedicated Instances
- B. By using AWS Organizations consolidated billing ✅
- C. By using the AWS Cost Explorer tool

**Explanation:** When accounts are linked under AWS Organizations with consolidated billing, Reserved Instance discounts are shared across all member accounts. An unused Reserved Instance in one account can automatically apply its discount to matching usage in another account.

---

**22.** A customer runs an On-Demand Amazon Linux EC2 instance for 3 hours, 5 minutes, and 6 seconds. For how much time will the customer be billed?

- A. 3 hours
- B. 3 hours 5 minutes 6 Seconds ✅
- C. 3 hours 5 minutes
- D. 3 hours 6 minutes

**Explanation:** Amazon Linux EC2 On-Demand instances are billed per second with a minimum of 60 seconds. After the first minute, billing is exact to the second, so the customer pays for exactly 3 hours, 5 minutes, and 6 seconds.

---

**23.** Which of the following AWS services provide compute resources? (Choose two.)

- A. AWS Lambda ✅
- B. AWS CodeDeploy
- C. Amazon Elastic Container Service (Amazon ECS) ✅
- D. Amazon S3

**Explanation:** AWS Lambda provides serverless function-based compute. Amazon ECS is a container orchestration service that provides compute for containerized workloads. CodeDeploy is a deployment tool and S3 is object storage.

---

**24.** Which AWS service enables users to deploy infrastructure as code by automating the process of provisioning resources?

- A. Amazon GameLift
- B. AWS CloudFormation ✅
- C. AWS Data Pipeline

**Explanation:** AWS CloudFormation allows you to define your infrastructure in JSON or YAML templates and automatically provision and configure all required resources in the correct order, enabling repeatable, automated infrastructure deployment.

---

**25.** Which AWS services provide a way to extend an on-premises architecture to the AWS Cloud? (Choose two.)

- A. Amazon EBS
- B. AWS Direct Connect ✅
- C. Amazon CloudFront
- D. Storage Gateway ✅

**Explanation:** AWS Direct Connect provides a private dedicated network connection from on-premises to AWS. AWS Storage Gateway extends on-premises storage to the cloud, enabling hybrid architectures with seamless data movement between environments.

---

**26.** Which of the following allows users to provision a dedicated network connection from their internal network to AWS?

- A. AWS CloudHSM
- B. AWS Direct Connect ✅
- C. AWS VPN
- D. VPC

**Explanation:** AWS Direct Connect establishes a dedicated private physical connection between your internal network and AWS, bypassing the public internet. This provides more consistent network performance, lower latency, and reduced bandwidth costs.

---

**27.** Which services use AWS edge locations? (Choose two.)

- A. Amazon CloudFront ✅
- B. AWS Shield ✅
- C. Amazon EC2
- D. Amazon EBS

**Explanation:** Amazon CloudFront delivers cached content from edge locations worldwide. AWS Shield Standard is automatically applied at AWS edge locations to protect against DDoS attacks. EC2 and EBS are regional services that do not use edge locations.

---

**28.** Which service would provide network connectivity in a hybrid architecture that includes the AWS Cloud?

- A. Amazon VPC
- B. AWS Direct Connect ✅
- C. AWS Directory Service

**Explanation:** AWS Direct Connect provides a dedicated private network connection between your on-premises environment and AWS, which is the core networking component needed to bridge a hybrid architecture between on-premises and cloud.

---

**29.** Which tool can be used to compare the costs of running a web application in a traditional hosting environment to running it on AWS?

- A. AWS Cost Explorer
- B. AWS Budgets
- C. AWS Cost and Usage report
- D. AWS Pricing Calculator ✅

**Explanation:** The AWS Pricing Calculator (which replaced the TCO Calculator) helps estimate and compare the costs of running workloads on AWS versus traditional on-premises or hosting environments, making it ideal for migration cost analysis.

---

**30.** Under the shared responsibility model, which of the following areas are the customer's responsibility? (Choose two.)

- A. Firmware upgrades of network infrastructure
- B. Patching of operating systems ✅
- C. Patching of the underlying hypervisor
- D. Patching software applications installed on EC2 Instances ✅

**Explanation:** Customers are responsible for patching the guest operating systems and any software they install on EC2 instances. Firmware upgrades and hypervisor patching are AWS responsibilities as part of the underlying infrastructure.

---

**31.** Which service enables customers to audit and monitor changes in AWS resources?

- A. AWS Trusted Advisor
- B. Amazon GuardDuty
- C. Amazon Inspector
- D. AWS Config ✅

**Explanation:** AWS Config continuously records configuration changes to AWS resources and evaluates them against desired rules. It provides a detailed history of resource configurations for auditing, compliance, and troubleshooting.

---

**32.** Which AWS service identifies security groups that allow unrestricted access to a user's AWS resources?

- A. AWS CloudTrail
- B. AWS Trusted Advisor ✅
- C. Amazon CloudWatch

**Explanation:** AWS Trusted Advisor includes security checks that detect security groups with inbound rules allowing unrestricted access (0.0.0.0/0) to sensitive ports, flagging them as potential security risks.

---

**33.** According to the AWS shared responsibility model, who is responsible for configuration management?

- A. It is solely the responsibility of the customer.
- B. It is solely the responsibility of AWS.
- C. It is shared between AWS and the customer. ✅

**Explanation:** Configuration management is a shared responsibility. AWS configures and manages the underlying infrastructure components, while customers are responsible for configuring the services, operating systems, and applications they deploy.

---

**34.** Which AWS service is a content delivery network that securely delivers data, video, and applications to users globally with low latency and high speeds?

- A. AWS CloudFormation
- B. AWS Direct Connect
- C. Amazon CloudFront ✅

**Explanation:** Amazon CloudFront is AWS's global content delivery network (CDN). It distributes content through a worldwide network of edge locations, delivering data, videos, APIs, and applications to users with low latency and high transfer speeds.

---

**35.** Which benefit of the AWS Cloud supports matching the supply of resources with changing workload demands?

- A. Security
- B. Reliability
- C. Elasticity ✅

**Explanation:** Elasticity is the ability to automatically scale resources up or down to precisely match current demand. This ensures you always have the right amount of capacity — no more, no less — without manual intervention.

---

**36.** Which of the following are benefits of hosting infrastructure in the AWS Cloud? (Choose two.)

- A. There are no upfront commitments. ✅
- B. AWS manages all security in the cloud.
- C. Users have the ability to provision resources on demand. ✅
- D. Storage cost is for free

**Explanation:** AWS allows you to start using services with no upfront hardware investment, and you can provision resources on demand in minutes. AWS does not manage all security — customers are responsible for their portion under the shared responsibility model.

---

**37.** What AWS service would be used to centrally manage AWS access policies across multiple accounts?

- A. AWS Service Catalog
- B. AWS Config
- C. AWS Trusted Advisor
- D. AWS Organizations ✅

**Explanation:** AWS Organizations allows central governance of multiple AWS accounts. Using Service Control Policies (SCPs), you can set permission guardrails that apply across all accounts in your organization.

---

**38.** What is AWS Trusted Advisor?

- A. It is an AWS staff member who provides recommendations and best practices on how to use AWS.
- B. It is a network of AWS partners who provides recommendations and best practices on how to use AWS.
- C. It is an online tool with a set of automated checks that provides recommendations on cost optimization ✅

**Explanation:** AWS Trusted Advisor is an automated tool that analyzes your AWS environment and provides real-time recommendations across five categories: cost optimization, performance, security, fault tolerance, and service limits.

---

**39.** Which AWS service or feature allows a company to visualize, understand, and manage AWS costs and usage over time?

- A. AWS Budgets
- B. AWS Cost Explorer ✅
- C. AWS Organizations

**Explanation:** AWS Cost Explorer provides an interactive interface to visualize, understand, and manage your AWS costs and usage over time. It includes pre-built reports and allows you to filter and group costs by service, region, tag, and more.

---

**40.** Which AWS service offers on-demand access to AWS security and compliance reports?

- A. AWS CloudTrail
- B. AWS Artifact ✅
- C. AWS Health

**Explanation:** AWS Artifact is a self-service portal that provides on-demand access to AWS compliance documentation and security reports, including SOC reports, PCI DSS attestations, and ISO certifications.

---

**41.** What are the benefits of using the AWS Cloud for companies with customers in many countries around the world? (Choose two.)

- A. Companies can deploy applications in multiple AWS Regions to reduce latency. ✅
- B. Amazon Translate automatically translates third-party website interfaces into multiple languages.
- C. Amazon CloudFront has multiple edge locations around the world to reduce latency. ✅
- D. AWS is free of charge

**Explanation:** AWS's global infrastructure allows companies to deploy applications in Regions close to their users, and CloudFront's worldwide edge locations cache and serve content with low latency regardless of user location.

---

**42.** Which AWS service handles the deployment details of capacity provisioning, load balancing, Auto Scaling, and application health monitoring?

- A. AWS Config
- B. AWS Elastic Beanstalk ✅
- C. Amazon Route 53
- D. EC2 AutoScaling

**Explanation:** AWS Elastic Beanstalk is a PaaS that automatically handles all deployment infrastructure details including capacity provisioning, load balancing, auto-scaling, and health monitoring. Developers simply upload their application code.

---

**43.** Which AWS service provides inbound and outbound network ACLs to harden external connectivity to Amazon EC2?

- A. AWS IAM
- B. Amazon Connect
- C. Amazon VPC ✅
- D. Amazon EC2

**Explanation:** Amazon VPC includes Network Access Control Lists (NACLs) that act as stateless firewalls at the subnet level, controlling inbound and outbound traffic to protect EC2 instances from unauthorized network access.

---

**44.** When a company provisions web servers in multiple AWS Regions, what is being increased?

- A. Coupling
- B. Availability ✅
- C. Security
- D. Cost

**Explanation:** Deploying across multiple AWS Regions increases availability by ensuring the application continues to operate even if an entire Region experiences disruption. Users can be routed to the nearest healthy Region.

---

**45.** The pay-as-you-go pricing model for AWS services:

- A. Reduces capital expenditures. ✅
- B. Requires payment up front for AWS services.
- C. Is relevant only for Amazon EC2
- D. Gifts all AWS Services to Customers

**Explanation:** The pay-as-you-go model eliminates large upfront capital expenditures for hardware. Instead of buying servers, you pay only for the cloud resources you actually consume, shifting costs to operational expenditure.

---

**46.** Under the AWS shared responsibility model, AWS is responsible for which security-related tasks? (Choose 2)

- A. Lifecycle management of IAM credentials
- B. Physical security of global infrastructure ✅
- C. Encryption of Amazon EBS volumes
- D. Updating Security of Hypervisors and Host Hardware ✅

**Explanation:** AWS is responsible for the physical security of its global infrastructure and for maintaining the security of the hypervisor and underlying host hardware. IAM credential management and EBS encryption are customer responsibilities.

---

**47.** Which AWS service enables users to consolidate billing across multiple accounts?

- A. Amazon QuickSight
- B. AWS Organizations ✅
- C. AWS Budgets

**Explanation:** AWS Organizations provides consolidated billing, combining usage across all member accounts into a single bill paid by the management account, and enabling volume pricing discounts across the entire organization.

---

**48.** Which of the following are compute services provided by AWS? (Choose 3)

- A. Amazon Lightsail ✅
- B. Amazon EC2 ✅
- C. Amazon S3
- D. AWS Lambda ✅
- E. Amazon ECS

**Explanation:** Amazon Lightsail (virtual private servers), Amazon EC2 (virtual machines), and AWS Lambda (serverless functions) are all compute services. Amazon S3 is object storage, and Amazon ECS is a container orchestration platform that uses underlying compute.

---

**49.** Which of the following are storage services provided by AWS? (Choose 3)

- A. Amazon Simple Stored Service
- B. Amazon GroundStation
- C. Amazon EFS ✅
- D. Amazon Lex
- E. Amazon Simple Storage Service ✅
- F. Amazon EBS ✅

**Explanation:** Amazon EFS (Elastic File System), Amazon S3 (Simple Storage Service), and Amazon EBS (Elastic Block Store) are AWS's primary storage services. GroundStation is a satellite ground station service, and Lex is an AI chatbot service.

---

**50.** Which of the following are Database caching services provided by AWS? (Choose 2)

- A. Amazon Macie
- B. Amazon Elasticache ✅
- C. Amazon RDS
- D. DynamoDB Accelerator (DAX) ✅
- E. Amazon Simple Storage Service

**Explanation:** Amazon ElastiCache provides fully managed Redis and Memcached in-memory caching. DynamoDB Accelerator (DAX) is an in-memory cache specifically for DynamoDB that delivers microsecond response times. Both are purpose-built database caching services.
