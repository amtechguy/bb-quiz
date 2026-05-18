**1.** How do customers benefit from Amazon's massive economies of scale?

- A. Periodic price reductions as the result of Amazon's operational efficiencies ✅
- B. New Amazon EC2 instance types providing the latest hardware
- C. The ability to scale up and down when needed
- D. Increased reliability in the underlying hardware of Amazon EC2 instances

**Explanation:** Amazon's massive scale allows it to achieve greater efficiencies and pass those savings to customers in the form of lower prices over time — a core benefit of cloud economies of scale.

---

**2.** Which AWS services can be used to gather information about AWS account activity? (Select TWO.)

- A. Amazon CloudFront
- B. AWS Cloud9
- C. AWS CloudTrail ✅
- D. AWS CloudHSM
- E. Amazon CloudWatch ✅

**Explanation:** AWS CloudTrail records API calls and account activity across your AWS infrastructure. Amazon CloudWatch collects monitoring data and logs, giving visibility into resource and application activity.

---

**3.** Which of the following common IT tasks can AWS cover to free up company IT resources? (Select TWO.)

- A. Patching databases software ✅
- B. Testing application releases
- C. Backing up databases ✅
- D. Creating database schema
- E. Running penetration tests

**Explanation:** With managed services like Amazon RDS, AWS handles database patching and automated backups, freeing customer IT teams to focus on higher-value work like schema design and application development.

---

**4.** In which scenario should Amazon EC2 Spot Instances be used?

- A. A company wants to move its main website to AWS from an on-premises web server.
- B. A company has a number of application services whose Service Level Agreement (SLA) requires 99.999% uptime.
- C. A company's heavily used legacy database is currently running on-premises.
- D. Interruptible jobs that are currently using On-Demand Instances. ✅

**Explanation:** Spot Instances are best for flexible, fault-tolerant, and interruptible workloads. They offer up to 90% savings over On-Demand but can be reclaimed by AWS with a 2-minute warning, making them unsuitable for critical or continuous workloads.

---

**5.** Which AWS feature should a customer leverage to achieve high availability of an application?

- A. AWS Direct Connect
- B. Availability Zones ✅
- C. Data centers
- D. Amazon Virtual Private Cloud (Amazon VPC)

**Explanation:** Deploying applications across multiple Availability Zones ensures that if one AZ experiences an outage, the application continues to run in the other AZs, achieving high availability.

---

**6.** Which is the minimum AWS Support plan that includes Infrastructure Event Management without additional costs?

- A. Enterprise ✅
- B. Business
- C. Developer
- D. Basic

**Explanation:** Infrastructure Event Management (IEM) is included at no extra charge only with the Enterprise Support plan. Business support customers can access IEM for an additional fee.

---

**7.** Which AWS service can serve a static website?

- A. Amazon S3 ✅
- B. Amazon Route 53
- C. Amazon QuickSight
- D. AWS X-Ray

**Explanation:** Amazon S3 supports static website hosting. You can configure an S3 bucket to serve HTML, CSS, JavaScript, and media files directly to web browsers without needing a web server.

---

**8.** How does AWS shorten the time to provision IT resources?

- A. It supplies an online IT ticketing platform for resource requests.
- B. It supports automatic code validation services.
- C. It provides the ability to programmatically provision existing resources. ✅
- D. It automates the resource request process from a company's IT vendor list.

**Explanation:** AWS APIs, SDKs, and tools like CloudFormation and the CLI allow resources to be provisioned programmatically in minutes, eliminating the weeks or months required to procure and set up on-premises hardware.

---

**9.** What can AWS edge locations be used for? (Select TWO.)

- A. Hosting applications
- B. Delivering content closer to users ✅
- C. Running NoSQL database caching services
- D. Reducing traffic on the server by caching responses ✅
- E. Sending notification messages to end users

**Explanation:** AWS edge locations are used by Amazon CloudFront to cache and deliver content (like images, videos, and web pages) closer to end users, reducing latency and origin server load.

---

**10.** Which of the following can limit Amazon Simple Storage Service (Amazon S3) bucket access to specific users?

- A. A public and private key-pair
- B. Amazon Inspector
- C. AWS Identity and Access Management (IAM) policies ✅
- D. Security Groups

**Explanation:** IAM policies and S3 bucket policies allow fine-grained control over who can access S3 buckets and objects. Security groups apply to EC2 instances, not S3.

---

**11.** A solution that is able to support growth in users, traffic, or data size with no drop in performance aligns with which cloud architecture principle?

- A. Think parallel
- B. Implement elasticity ✅
- C. Decouple your components
- D. Design for failure

**Explanation:** Elasticity is the ability to scale resources up or down automatically to handle changes in demand. An elastic system grows with traffic and shrinks when demand drops, maintaining performance without over-provisioning.

---

**12.** Which of the following tasks is the responsibility of AWS?

- A. Encrypting client-side data
- B. Configuring AWS Identity and Access Management (IAM) roles
- C. Securing the Amazon EC2 hypervisor ✅
- D. Setting user password policies

**Explanation:** Under the shared responsibility model, AWS is responsible for the security OF the cloud, including the hypervisor layer that underlies EC2 instances. Customers are responsible for configurations made on top of it.

---

**13.** One benefit of On-Demand Amazon Elastic Compute Cloud (Amazon EC2) pricing is:

- A. The ability to bid for a lower hourly cost.
- B. Paying a daily rate regardless of time used.
- C. Paying only for time used. ✅
- D. Pre-paying for instances and paying a lower hourly rate.

**Explanation:** On-Demand pricing means you pay for compute capacity by the second (minimum 60 seconds) with no long-term commitments or upfront payments. You only pay for what you actually use.

---

**14.** An administrator needs to rapidly deploy a popular IT solution and start using it immediately. Where can the administrator find assistance?

- A. AWS Well-Architected Framework documentation
- B. Amazon CloudFront
- C. AWS CodeCommit
- D. AWS Quick Start reference deployments ✅

**Explanation:** AWS Quick Starts are automated reference deployments built by AWS solutions architects and partners. They use CloudFormation templates to deploy popular technologies on AWS quickly and following best practices.

---

**15.** Which of the following services is in the category of AWS serverless platform?

- A. Amazon EMR
- B. Elastic Load Balancing
- C. AWS Lambda ✅
- D. AWS Mobile Hub

**Explanation:** AWS Lambda is a core serverless compute service. It runs code in response to events without requiring you to provision or manage servers, and you pay only for the compute time consumed.

---

**16.** Which service is not part of the AWS serverless platform?

- A. Amazon EC2 ✅
- B. Amazon S3
- C. Amazon Athena
- D. Amazon SQS

**Explanation:** Amazon EC2 requires you to provision, manage, and maintain virtual server instances, including the operating system. This makes it a traditional server-based service, unlike Lambda, S3, Athena, and SQS which are serverless.

---

**17.** Under the shared responsibility model, which of the following is a shared control between a customer and AWS?

- A. Physical controls
- B. Patch management ✅
- C. Zone security
- D. Data center auditing

**Explanation:** Patch management is a shared responsibility. AWS patches the underlying infrastructure and managed service components, while customers are responsible for patching their own operating systems and applications running on EC2.

---

**18.** What technology enables compute capacity to adjust as loads change?

- A. Load balancing
- B. Automatic failover
- C. Round robin
- D. Auto Scaling ✅

**Explanation:** AWS Auto Scaling monitors your application and automatically adjusts the number of EC2 instances (or other resources) in response to changing demand, ensuring you have the right capacity at the right time.

---

**19.** Which AWS services are defined as global instead of regional? (Select TWO.)

- A. Amazon Route 53 ✅
- B. Amazon EC2
- C. Amazon S3
- D. Amazon CloudFront ✅
- E. Amazon DynamoDB

**Explanation:** Amazon Route 53 (DNS) and Amazon CloudFront (CDN) are global services that operate across all AWS regions and edge locations. EC2, S3, and DynamoDB are regional services.

---

**20.** Which AWS service would you use to obtain compliance reports and certificates?

- A. AWS Artifact ✅
- B. AWS Lambda
- C. Amazon Inspector
- D. AWS Certificate Manager

**Explanation:** AWS Artifact is a self-service portal that provides on-demand access to AWS compliance reports such as SOC reports, PCI DSS attestations, and ISO certifications.

---

**21.** Under the shared responsibility model, which of the following tasks are the responsibility of the AWS customer? (Select TWO.)

- A. Ensuring that application data is encrypted at rest ✅
- B. Ensuring that AWS NTP servers are set to the correct time
- C. Ensuring that users have received security training in the use of AWS services ✅
- D. Ensuring that access to data centers is restricted
- E. Ensuring that hardware is disposed of properly

**Explanation:** Customers are responsible for encrypting their own data and for training their users on security awareness. Physical data center access, hardware disposal, and NTP servers are all AWS responsibilities.

---

**22.** Which AWS service can be used to manually launch instances based on resource requirements?

- A. Amazon EBS
- B. Amazon S3
- C. Amazon EC2 ✅
- D. Amazon ECS

**Explanation:** Amazon EC2 allows customers to launch virtual server instances of varying sizes and types based on their specific resource requirements, either manually via the console or programmatically.

---

**23.** A company is migrating an application that is running non-interruptible workloads for a three-year time frame. Which pricing construct would provide the MOST cost-effective solution?

- A. Amazon EC2 Spot Instances
- B. Amazon EC2 Dedicated Instances
- C. Amazon EC2 On-Demand Instances
- D. Amazon EC2 Reserved Instances ✅

**Explanation:** Reserved Instances offer up to 72% discount compared to On-Demand pricing in exchange for a 1 or 3-year commitment. For stable, non-interruptible workloads with a predictable duration, they provide the greatest cost savings.

---

**24.** The financial benefits of using AWS are: (Select TWO.)

- A. Reduced Total Cost of Ownership (TCO). ✅
- B. Increased capital expenditure (capex).
- C. Reduced operational expenditure (opex). ✅
- D. Deferred payment plans for startups.
- E. Business credit lines for startups.

**Explanation:** Moving to AWS reduces TCO by eliminating the need to purchase and maintain hardware. It also reduces operational costs through automation, managed services, and economies of scale.

---

**25.** Which of the following is entirely the responsibility of AWS, according to the AWS shared responsibility model?

- A. Patching of the guest operating system
- B. Security awareness and training
- C. Physical and environmental controls ✅
- D. Development of an IAM password policy

**Explanation:** AWS is solely responsible for the physical infrastructure, including data center security, environmental controls (power, cooling, fire suppression), and hardware maintenance. Customers are never responsible for these.

---

**26.** Which AWS service allows companies to connect an Amazon VPC to an on-premises data center? (Select TWO)

- A. AWS VPN ✅
- B. Amazon Redshift
- C. API Gateway
- D. Amazon Direct Connect ✅
- E. Amazon S3

**Explanation:** AWS VPN creates an encrypted tunnel over the public internet between your on-premises network and AWS. AWS Direct Connect provides a dedicated private physical connection, offering more consistent performance.

---

**27.** A company wants to reduce the physical compute footprint that developers use to run code. Which service would meet that need by enabling serverless architectures?

- A. Amazon Elastic Compute Cloud (Amazon EC2)
- B. AWS Lambda ✅
- C. Amazon DynamoDB
- D. AWS CodeCommit

**Explanation:** AWS Lambda is a serverless compute service that runs code without provisioning or managing servers. Developers simply upload their code and Lambda handles execution, scaling, and infrastructure management.

---

**28.** Which AWS service provides alerts when an AWS event may impact a company's AWS resources?

- A. AWS Personal Health Dashboard ✅
- B. AWS Service Health Dashboard
- C. AWS Trusted Advisor
- D. AWS Infrastructure Event Management

**Explanation:** The AWS Personal Health Dashboard provides personalized alerts and remediation guidance when AWS events affect your specific resources. The Service Health Dashboard shows general AWS service status without personalization.

---

**29.** Which of the following are categories of AWS Trusted Advisor? (Select TWO.)

- A. Fault Tolerance ✅
- B. Instance Usage
- C. Infrastructure
- D. Performance ✅
- E. Storage Capacity

**Explanation:** AWS Trusted Advisor is organized into five categories: Cost Optimization, Performance, Security, Fault Tolerance, and Service Limits. It provides real-time recommendations across all five areas.

---

**30.** Which of the following services falls under the responsibility of the customer to maintain operating system configuration, security patching, and networking?

- A. Amazon EC2 ✅
- B. Amazon ElastiCache
- C. AWS Fargate

**Explanation:** With Amazon EC2, customers are responsible for managing the guest operating system including updates, patching, and network configuration. Managed services like ElastiCache and Fargate abstract these responsibilities away.

---

**31.** A company will be moving from an on-premises data center to the AWS Cloud. What would be one financial difference after the move?

- A. Moving from variable operational expense (opex) to upfront capital expense (capex).
- B. Moving from upfront capital expense (capex) to variable capital expense (capex).
- C. Moving from upfront capital expense (capex) to variable operational expense (opex). ✅
- D. Elimination of upfront capital expense (capex) and elimination of variable operational expense (opex)

**Explanation:** On-premises requires large upfront capital investment in hardware. AWS shifts this to a variable operational expense model where you pay only for what you use, with no upfront hardware costs.

---

**32.** How should a customer quickly forecast the future costs for running a new web application?

- A. Amazon Aurora Backtrack
- B. Amazon CloudWatch Billing Alarms
- C. AWS Simple Monthly Calculator ✅
- D. AWS Cost and Usage report

**Explanation:** The AWS Simple Monthly Calculator (now the AWS Pricing Calculator) allows customers to estimate the monthly cost of AWS services for a planned architecture before deploying anything.

---

**33.** Which is the MINIMUM AWS Support plan that provides technical support through phone calls?

- A. Enterprise
- B. Business ✅
- C. Developer
- D. Basic

**Explanation:** The Business Support plan is the minimum tier that includes 24/7 phone, email, and chat access to Cloud Support Engineers. Developer support provides only business-hours email access.

---

**34.** Which AWS IAM feature is used to associate a set of permissions with multiple users?

- A. Multi-factor authentication
- B. Groups ✅
- C. Password policies
- D. Access keys

**Explanation:** IAM Groups allow you to attach IAM policies to a collection of users. All users in the group inherit those permissions, making it easy to manage access for teams without setting permissions individually.

---

**35.** Which of the following are benefits of the AWS Cloud? (Choose two.)

- A. Unlimited uptime
- B. Elasticity ✅
- C. Agility ✅
- D. Colocation
- E. Capital expenses

**Explanation:** Elasticity allows resources to scale with demand. Agility refers to the ability to quickly experiment, deploy, and innovate. These are two of the six core advantages of cloud computing defined by AWS.

---

**36.** Which of the following can a customer use to enable single sign-on (SSO) to the AWS Console?

- A. Amazon Connect
- B. AWS Directory Service ✅
- C. Amazon Pinpoint
- D. Amazon Rekognition

**Explanation:** AWS Directory Service integrates with Microsoft Active Directory and enables SSO so users can sign in to the AWS Management Console using their existing corporate credentials.

---

**37.** What are the multiple, isolated locations within an AWS Region that are connected by low-latency networks called?

- A. AWS Direct Connects
- B. Amazon VPCs
- C. Edge locations
- D. Availability Zones ✅

**Explanation:** Availability Zones (AZs) are physically separate data centers within an AWS Region, each with redundant power, networking, and connectivity, connected to each other via low-latency links.

---

**38.** Which of the following services provides on-demand access to AWS compliance reports?

- A. AWS IAM
- B. AWS Artifact ✅
- C. Amazon GuardDuty
- D. AWS KMS

**Explanation:** AWS Artifact is the go-to service for accessing AWS compliance documentation on demand, including SOC reports, PCI DSS reports, ISO certifications, and other third-party audit reports.

---

**39.** As part of the AWS shared responsibility model, which of the following operational controls do users fully inherit from AWS?

- A. Security management of data center ✅
- B. Patch management
- C. Configuration management
- D. User and access management

**Explanation:** Physical data center security is entirely AWS's responsibility. Customers fully inherit this control and never need to manage physical access, surveillance, or environmental security of AWS facilities.

---

**40.** When comparing AWS Cloud with on-premises Total Cost of Ownership, which expenses must be considered? (Choose two.)

- A. Software development
- B. Project management
- C. Storage hardware ✅
- D. Physical servers ✅
- E. Antivirus software license

**Explanation:** On-premises infrastructure requires purchasing physical servers and storage hardware, which represent significant capital expenditures that do not exist when using AWS cloud services.

---

**41.** Under the shared responsibility model, which of the following tasks are the responsibility of the customer? (Choose two.)

- A. Maintaining the underlying Amazon EC2 hardware.
- B. Managing the VPC network access control lists. ✅
- C. Encrypting data in transit and at rest. ✅
- D. Replacing failed hard disk drives.
- E. Deploying hardware in different Availability Zones.

**Explanation:** Customers are responsible for configuring VPC network ACLs to control traffic, and for encrypting their own data at rest and in transit. Physical hardware management and maintenance are AWS responsibilities.

---

**42.** Which scenarios represent the concept of elasticity on AWS? (Choose two.)

- A. Scaling the number of Amazon EC2 instances based on traffic. ✅
- B. Resizing Amazon RDS instances as business needs change. ✅
- C. Automatically directing traffic to less-utilized Amazon EC2 instances.
- D. Using AWS compliance documents to accelerate the compliance process.
- E. Having the ability to create and govern environments using code.

**Explanation:** Elasticity means the ability to scale resources up or down based on demand. Adding/removing EC2 instances based on traffic and resizing RDS to match business needs are both examples of elastic scaling.

---

**43.** When is it beneficial for a company to use a Spot Instance?

- A. When there is flexibility in when an application needs to run. ✅
- B. When there are mission-critical workloads.
- C. When dedicated capacity is needed.
- D. When an instance should not be stopped.

**Explanation:** Spot Instances are best for workloads with flexible timing that can tolerate interruptions, such as batch processing, big data analysis, or CI/CD jobs. They offer up to 90% savings over On-Demand pricing.

---

**44.** A company is considering moving its on-premises data center to AWS. What factors should be included in doing a Total Cost of Ownership (TCO) analysis? (Choose two.)

- A. Amazon EC2 instance availability
- B. Power consumption of the data center ✅
- C. Labor costs to replace old servers ✅
- D. Application developer time
- E. Database engine capacity

**Explanation:** A TCO analysis for on-premises vs. cloud must include on-premises costs like electricity for powering and cooling servers, and the labor costs for hardware maintenance and replacement — both of which are eliminated with AWS.

---

**45.** What function do security groups serve in relation to Amazon Elastic Compute Cloud (Amazon EC2) instance security?

- A. Act as a virtual firewall for the Amazon EC2 instance. ✅
- B. Secure AWS user accounts with AWS Identity and Access Management (IAM) policies.
- C. Provide DDoS protection with AWS Shield.
- D. Use Amazon CloudFront to protect the Amazon EC2 instance.

**Explanation:** Security groups act as a stateful virtual firewall for EC2 instances, controlling inbound and outbound traffic at the instance level based on rules you define by port, protocol, and source/destination.

---

**46.** Which disaster recovery scenario offers the lowest probability of downtime?

- A. Backup and restore
- B. Pilot light
- C. Warm standby
- D. Multi-site active-active ✅

**Explanation:** Multi-site active-active runs full workloads in multiple locations simultaneously, so if one site fails, traffic is instantly routed to another with near-zero downtime. It has the lowest RTO and RPO of all DR strategies.

---

**47.** A pharmaceutical company operates its infrastructure in a single AWS Region. The company has thousands of VPCs in various AWS accounts that it wants to interconnect. Which AWS service or feature should the company use to help simplify management and reduce operational costs?

- A. VPC endpoint
- B. VPC peering
- C. AWS Transit Gateway ✅
- D. AWS Direct Connect

**Explanation:** AWS Transit Gateway acts as a cloud router in a hub-and-spoke model, allowing thousands of VPCs and on-premises networks to connect through a single gateway, greatly simplifying management compared to complex VPC peering meshes.

---

**48.** A tech startup wants to protect its workloads running on AWS from SQL injection attacks. Which service can be used to achieve this?

- A. Security groups
- B. Network ACLs
- C. AWS WAF ✅
- D. IAM policy

**Explanation:** AWS WAF (Web Application Firewall) protects web applications from common web exploits like SQL injection and cross-site scripting (XSS). Security groups and NACLs operate at the network level and cannot inspect application-layer content.

---

**49.** Which cloud computing benefit does AWS demonstrate with its ability to offer lower variable costs as a result of high purchase volumes?

- A. Pay-as-you-go pricing
- B. High availability
- C. Global reach
- D. Economies of scale ✅

**Explanation:** Economies of scale refers to the cost advantages AWS gains from operating at massive scale, allowing it to purchase hardware and bandwidth in bulk and pass those lower costs on to customers through reduced pricing.

---

**50.** A company needs to deliver images and videos globally with minimal latency. Which AWS services can be used to accomplish this? (Choose 2)

- A. Amazon S3 ✅
- B. VPC
- C. Amazon EC2
- D. Amazon EBS
- E. Amazon CloudFront ✅

**Explanation:** Amazon S3 is ideal for storing large media files like images and videos durably and cost-effectively. Amazon CloudFront, a global CDN, then delivers that content from edge locations closest to each user, minimizing latency.

---

**51.** A company wants to connect to AWS over a private, low-latency connection from its remote office. What is the recommended method to meet these requirements?

- A. Create a VPN tunnel
- B. Use VPC peering to create a connection.
- C. Connect across the public internet
- D. Use AWS Direct Connect. ✅

**Explanation:** AWS Direct Connect establishes a dedicated private physical network connection between your premises and AWS, bypassing the public internet entirely. This provides consistent, low-latency performance and greater bandwidth reliability.
