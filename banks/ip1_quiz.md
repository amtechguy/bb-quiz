**1.** An administrator needs to rapidly deploy a popular IT solution and start using it immediately. Where can the administrator find assistance?
- A. AWS Well-Architected Framework documentation.
- B. Amazon CloudFront.
- C. AWS CodeCommit.
- D. AWS Quick Start reference deployments. ✅
**Explanation:** AWS Quick Start reference deployments are automated reference deployments for key workloads on the AWS Cloud. They help you deploy popular IT solutions on AWS quickly and easily.

---

**2.** What is one of the advantages of the Amazon Relational Database Service (Amazon RDS)?
- A. It simplifies relational database administration tasks ✅
- B. It provides 99.99999999999% reliability and durability
- C. It automatically scales databases for loads
- D. It enables users to dynamically adjust CPU and RAM resources
**Explanation:** Amazon RDS simplifies time-consuming database administration tasks such as backups, software patching, monitoring, scaling, and replication so you can focus on your applications.

---

**3.** Which of the following AWS Cloud services can be used to run a customer-managed relational database?
- A. Amazon EC2 ✅
- B. Amazon Route 53
- C. Amazon ElastiCache
- D. Amazon DynamoDB
**Explanation:** Amazon EC2 allows you to run any database software you choose on virtual servers you manage yourself, giving you full control over the database engine and configuration.

---

**4.** A user is planning to launch two additional Amazon EC2 instances to increase availability. Which action should the user take?
- A. Launch the instances across multiple Availability Zones in a single AWS Region. ✅
- B. Launch the instances as EC2 Reserved Instances in the same AWS Region and the same Availability Zone.
- C. Launch the instances in multiple AWS Regions but in the same Availability Zone.
- D. Launch the instances as EC2 Spot Instances in the same AWS Region but in different Availability Zones.
**Explanation:** Launching instances across multiple Availability Zones in the same Region protects your application from the failure of a single data center while keeping latency low between instances.

---

**5.** Which of the following can limit Amazon S3 bucket access to specific users?
- A. A public and private key-pair.
- B. Amazon Inspector.
- C. AWS Identity and Access Management (IAM) policies. ✅
- D. Security Groups.
**Explanation:** IAM policies control who can access your S3 buckets and what actions they can perform. You attach policies to users, groups, or roles to grant or restrict access.

---

**6.** Which AWS service allows companies to connect an Amazon VPC to an on-premises data center? (Select TWO)
- A. AWS VPN. ✅
- B. Amazon Redshift.
- C. API Gateway.
- D. Amazon Direct Connect. ✅
**Explanation:** AWS VPN creates an encrypted tunnel over the internet between your VPC and on-premises network. AWS Direct Connect provides a dedicated private network connection bypassing the internet entirely for more consistent performance.

---

**7.** Which AWS service or feature can be used to monitor CPU usage?
- A. AWS CloudTrail.
- B. VPC Flow Logs.
- C. Amazon CloudWatch. ✅
- D. Health Checks
**Explanation:** Amazon CloudWatch collects and tracks metrics including CPU utilization for EC2 instances. You can set alarms and automatically react to changes in your AWS resources.

---

**8.** Which task is AWS NOT responsible for in the shared responsibility model? (Select TWO)
- A. Granting access to individuals and services. ✅
- B. Ensuring datacenter security.
- C. Updating Amazon EC2 host firmware.
- D. Updating operating systems of user EC2 instances ✅
**Explanation:** Under the shared responsibility model, AWS manages the underlying infrastructure. Customers are responsible for managing access permissions and patching the operating systems running on their EC2 instances.

---

**9.** Which storage service can be used as a low-cost option for hosting static websites?
- A. Amazon Glacier.
- B. Amazon DynamoDB.
- C. Amazon Elastic File System (Amazon EFS).
- D. Amazon Simple Storage Service (Amazon S3). ✅
**Explanation:** Amazon S3 can host static websites directly. You enable static website hosting on a bucket, upload your HTML/CSS/JS files, and S3 serves them at very low cost with high durability.

---

**10.** According to the AWS shared responsibility model what is the sole responsibility of AWS?
- A. Application security.
- B. Edge location management. ✅
- C. Patch management.
- D. Client-side data.
**Explanation:** AWS is solely responsible for managing and maintaining its global infrastructure including edge locations. Customers never need to worry about the physical hardware or facilities that power AWS services.

---

**11.** Which of the following are pillars of the AWS Well-Architected Framework? (Select TWO)
- A. Multiple Availability Zones.
- B. Performance efficiency. ✅
- C. Cost Optimization ✅
- D. Operational Efficiency
- E. High availability.
**Explanation:** The six pillars of the AWS Well-Architected Framework are Operational Excellence, Security, Reliability, Performance Efficiency, Cost Optimization, and Sustainability.

---

**12.** Which AWS service identifies security groups that allow unrestricted access to a user's AWS resources?
- A. AWS Trusted Advisor. ✅
- B. Amazon Inspector.
- C. Amazon CloudWatch.
- D. AWS CloudTrail.
**Explanation:** AWS Trusted Advisor checks your security groups for rules that allow unrestricted access to specific ports and flags them as potential security risks.

---

**13.** Which design principles for cloud architecture are recommended when re-architecting a large monolithic application? (Select TWO)
- A. Use manual monitoring.
- B. Use fixed servers.
- C. Implement loose coupling. ✅
- D. Rely on individual components.
- E. Design for scalability. ✅
**Explanation:** Breaking a monolith into loosely coupled components means failures are isolated and each component can scale independently. Designing for scalability ensures the system handles growing demand without redesign.

---

**14.** When architecting cloud applications, which of the following is a key design principle?
- A. Use the largest instance possible.
- B. Provision capacity for peak load.
- C. Use the principle of least privilege. ✅
- D. Implement the layered security model.
**Explanation:** The principle of least privilege means granting only the minimum permissions needed to perform a task. This limits the blast radius if credentials are compromised.

---

**15.** A company has deployed several relational databases on Amazon EC2 instances. What is the MOST efficient way to apply monthly security patches?
- A. Connect to each database instance on a monthly basis and apply patches manually.
- B. Enable automate patching for the instances using the Amazon RDS console.
- C. In AWS Config, configure a rule for the instances and the required patch level.
- D. Use AWS Systems Manager to automate database patching according to a schedule. ✅
**Explanation:** AWS Systems Manager Patch Manager automates patching across your EC2 instances on a schedule you define, eliminating manual effort and reducing the risk of missed patches.

---

**16.** Which mechanism allows developers to access AWS services from application code?
- A. AWS Software Development Kit. ✅
- B. AWS Management Console.
- C. AWS CodePipeline.
- D. AWS Config.
**Explanation:** AWS SDKs provide language-specific APIs that let developers interact with AWS services directly from their application code in languages like Python, Java, JavaScript, and more.

---

**17.** Which AWS feature will reduce the customer's total cost of ownership (TCO)?
- A. Shared responsibility security model.
- B. Single tenancy.
- C. Elastic computing. ✅
- D. Distributed Architecture.
**Explanation:** Elastic computing lets you scale resources up and down based on demand, so you only pay for what you use. This eliminates the need to over-provision for peak loads, directly reducing TCO.

---

**18.** Which of the following is a benefit of using the AWS Cloud?
- A. Increased business agility ✅
- B. Inability to focus on revenue-generating activities.
- C. Control over cloud network hardware.
- D. Choice of specific cloud software vendors.
**Explanation:** AWS Cloud increases business agility by allowing companies to experiment quickly, deploy globally in minutes, and scale resources on demand without long procurement cycles.

---

**19.** Which of the following are categories of AWS Trusted Advisor? (Select TWO)
- A. Fault Tolerance. ✅
- B. Instance Usage.
- C. Infrastructure.
- D. Performance. ✅
- E. Storage Capacity.
**Explanation:** AWS Trusted Advisor checks fall into five categories: Cost Optimization, Performance, Security, Fault Tolerance, and Service Limits.

---

**20.** What is Amazon CloudWatch?
- A. A code repository with customizable build and team commit features.
- B. A metrics repository with customizable notification thresholds and channels. ✅
- C. A security configuration repository with threat analytics.
- D. A rule repository of a web application firewall with automated vulnerability prevention features.
**Explanation:** Amazon CloudWatch is a monitoring service that collects metrics and logs from AWS resources. You can set alarms and notifications based on thresholds you define.

---

**21.** Under the AWS shared responsibility model, which of the following are the customer's responsibility? (Select TWO)
- A. Patching operating system components for EC2 running PostgreSQL Databases ✅
- B. Encrypting data on the client-side. ✅
- C. Training the data center staff.
- D. Configuring Hardware firewall appliances
- E. Maintaining environmental controls within a data center.
**Explanation:** Customers are responsible for patching their EC2 operating systems and encrypting their own data. AWS handles the physical infrastructure including hardware firewalls, data center staff, and environmental controls.

---

**22.** Under the shared responsibility model, which of the following is a shared control? (Select TWO)
- A. Physical controls.
- B. Patch management. ✅
- C. Zone security.
- D. Data center auditing. ✅
**Explanation:** Patch management is shared because AWS patches infrastructure while customers patch their OS and applications. Auditing is shared because both AWS and customers maintain audit processes for their respective areas.

---

**23.** Which AWS service is used to pay AWS bills, and monitor usage and budget costs?
- A. AWS Billing and Cost Management. ✅
- B. Consolidated billing.
- C. Amazon CloudWatch.
- D. Amazon QuickSight.
**Explanation:** AWS Billing and Cost Management provides tools to pay your bills, monitor usage, and create budgets with alerts so you stay on top of your AWS spending.

---

**24.** How do customers benefit from Amazon's massive economies of scale?
- A. Periodic price reductions as the result of Amazon's operational efficiencies. ✅
- B. New Amazon EC2 instance types providing the latest hardware.
- C. The ability to scale up and down when needed.
- D. Increased reliability in the underlying hardware of Amazon EC2 instances.
**Explanation:** Because AWS aggregates usage from hundreds of thousands of customers, it achieves economies of scale that result in lower pay-as-you-go prices over time.

---

**25.** Which AWS feature allows a company to take advantage of usage tiers for services across multiple member accounts?
- A. Service control policies (SCPs).
- B. Consolidated billing. ✅
- C. All Upfront Reserved Instances.
- D. Organizational Units
**Explanation:** Consolidated billing combines usage from all accounts in an AWS Organization, allowing the company to reach higher usage tiers and receive volume discounts that individual accounts might not qualify for.

---

**26.** Which AWS services provide a way to extend an on-premises architecture to the AWS cloud? (Select TWO)
- A. Amazon EBS.
- B. Amazon Connect.
- C. AWS Storage Gateway ✅
- D. Amazon CloudFront.
- E. AWS Direct Connect. ✅
**Explanation:** AWS Storage Gateway connects on-premises environments to AWS cloud storage. AWS Direct Connect provides a dedicated private network link between your data center and AWS.

---

**27.** Which of the following services will automatically scale with an expected increase in web traffic?
- A. VPC
- B. Elastic Load Balancing. ✅
- C. Amazon EBS.
- D. AWS EC2
**Explanation:** Elastic Load Balancing automatically scales its request handling capacity in response to incoming traffic, distributing load across multiple targets without manual intervention.

---

**28.** Which service provides a virtually unlimited amount of online highly durable object storage?
- A. Amazon Redshift.
- B. Amazon Elastic File System (Amazon EFS).
- C. Amazon Elastic Container Service (Amazon ECS).
- D. Amazon S3. ✅
**Explanation:** Amazon S3 provides virtually unlimited object storage with 99.999999999% (11 nines) durability. There is no limit to the total amount of data you can store.

---

**29.** Which AWS feature should a customer leverage to achieve high availability of an application?
- A. Snapshots
- B. Availability Zones. ✅
- C. Data centers.
- D. Amazon Virtual Private Cloud (Amazon VPC).
**Explanation:** Deploying your application across multiple Availability Zones ensures that if one AZ experiences a failure, your application continues running in the other AZs without interruption.

---

**30.** Which AWS service or feature can enhance network security by blocking requests from a particular network for a web application? (Select TWO)
- A. AWS WAF. ✅
- B. AWS Trusted Advisor.
- C. AWS Direct Connect.
- D. AWS Organizations.
- E. Network ACLs. ✅
**Explanation:** AWS WAF lets you create rules to block requests from specific IP ranges at the application layer. Network ACLs act as a stateless firewall at the subnet level to block traffic from specific networks.

---

**31.** Which of the following is a cloud architectural design principle?
- A. Reliability and fault acceptance
- B. Loosely coupled components. ✅
- C. Build semi-monolithic systems.
- D. Use foundational services.
**Explanation:** Loose coupling reduces interdependencies between components so that a change or failure in one component does not cascade to others, improving resilience and scalability.

---

**32.** Which service enables risk auditing by continuously monitoring and logging account activity?
- A. Amazon CloudWatch.
- B. AWS CloudTrail. ✅
- C. AWS Config.
- D. AWS Health.
**Explanation:** AWS CloudTrail continuously records API calls and account activity across your AWS infrastructure, providing an audit trail for governance, compliance, and security analysis.

---

**33.** Where can AWS compliance and certification reports be downloaded?
- A. AWS Certificate Manager.
- B. AWS Secrets Manager
- C. AWS Artifact. ✅
- D. AWS Config
**Explanation:** AWS Artifact is a self-service portal that provides on-demand access to AWS compliance reports such as SOC, ISO, and PCI DSS certifications.

---

**34.** The financial benefits of using AWS are: (Select TWO)
- A. Reduced Total Cost of Ownership (TCO). ✅
- B. Increased capital expenditure (capex).
- C. Reduced operational expenditure (opex). ✅
- D. Deferred payment plans for startups.
- E. Business credit lines for startups.
**Explanation:** AWS reduces TCO by eliminating upfront hardware costs and reduces opex by replacing fixed infrastructure costs with variable pay-as-you-go pricing.

---

**35.** Which AWS service can serve as a target for a CloudFront distribution serving a static website?
- A. AWS X-Ray.
- B. Amazon Route 53.
- C. EBS Volume
- D. Amazon S3. ✅
**Explanation:** Amazon S3 is the most common origin for CloudFront distributions serving static websites. S3 hosts the files and CloudFront caches and delivers them globally with low latency.

---

**36.** What are the benefits of using the AWS Cloud for companies with customers in many countries? (Select TWO)
- A. Companies can deploy applications in multiple AWS Regions to reduce latency. ✅
- B. Amazon Translate automatically translates third-party website interfaces into multiple languages.
- C. Amazon CloudFront has multiple edge locations around the world to reduce latency. ✅
- D. Amazon Comprehend allows users to build applications that can respond to user requests in many languages.
- E. Elastic Load Balancing can distribute application web traffic to multiple AWS Regions around the world.
**Explanation:** Multiple AWS Regions allow you to deploy applications close to your global users. CloudFront's edge locations cache content worldwide, reducing latency for users regardless of their location.

---

**37.** Which of the following are main components of the AWS global infrastructure? (Select TWO)
- A. Resource groups.
- B. Points-of-presence ✅
- C. Security groups.
- D. Regions. ✅
- E. Datacenters.
**Explanation:** AWS global infrastructure consists of Regions, Availability Zones, and Points of Presence (edge locations). Regions are geographic areas and PoPs are used by CloudFront and Route 53 to deliver content with low latency.

---

**38.** What is the AWS customer responsible for according to the AWS shared responsibility model?
- A. Physical access controls.
- B. Data encryption. ✅
- C. Secure disposal of storage devices.
- D. Environmental risk management.
**Explanation:** Customers are responsible for encrypting their own data both at rest and in transit. AWS handles physical security, hardware disposal, and environmental controls in its data centers.

---

**39.** If each department within a company has its own AWS account, what is one way to enable consolidated billing?
- A. Use AWS Budgets on each account to pay only to budget.
- B. Contact AWS Support for a monthly bill.
- C. Create an AWS Organization from the payer account and invite the other accounts. ✅
- D. Put all invoices into one Amazon S3 bucket
**Explanation:** AWS Organizations lets you create a management account that consolidates billing for all member accounts. You send one invitation to each department account to join the organization.

---

**40.** What costs are included when comparing AWS TCO with on-premises TCO?
- A. Project management.
- B. Antivirus software licensing.
- C. Data center security. ✅
- D. Software development.
**Explanation:** On-premises TCO includes data center costs such as physical security, power, cooling, and hardware maintenance. These costs disappear when moving to AWS, making it a key comparison point.

---

**41.** What is the benefit of using AWS managed services such as Amazon ElastiCache and Amazon RDS?
- A. They require the customer to monitor and replace failing instances.
- B. They have better performance than customer-managed services.
- C. They simplify patching and updating underlying OSs. ✅
- D. They do not require the customer to optimize instance type or size selections.
**Explanation:** AWS managed services handle routine tasks like OS patching, backups, and failover automatically, freeing customers to focus on their applications rather than infrastructure maintenance.

---

**42.** Which services can be used across hybrid AWS Cloud architectures? (Select TWO)
- A. Storage Gateway ✅
- B. Amazon Macie
- C. Gateway Load Balancer.
- D. Auto Scaling.
- E. Virtual Private Network. ✅
**Explanation:** AWS Storage Gateway connects on-premises storage to the AWS cloud. AWS VPN creates encrypted tunnels between on-premises networks and AWS, both enabling hybrid architectures.

---

**43.** Which statement best describes Elastic Load Balancing?
- A. It translates a domain name into an IP address using DNS.
- B. It distributes incoming application traffic across one or more Amazon EC2 instances. ✅
- C. It collects metrics on connected Amazon EC2 instances.
- D. It automatically adjusts the number of Amazon EC2 instances to support incoming traffic.
**Explanation:** Elastic Load Balancing distributes incoming traffic across multiple targets such as EC2 instances, containers, and IP addresses, improving availability and fault tolerance.

---

**44.** Which of the following is a fast and reliable Graph database service?
- A. Amazon Redshift.
- B. Amazon RDS.
- C. Amazon DynamoDB.
- D. Amazon Neptune. ✅
**Explanation:** Amazon Neptune is a fully managed graph database service optimized for storing and querying highly connected datasets such as social networks, recommendation engines, and fraud detection graphs.

---

**45.** Which AWS service would you use to obtain compliance reports and certificates?
- A. AWS Artifact. ✅
- B. AWS Lambda.
- C. Amazon Inspector.
- D. AWS Certificate Manager.
**Explanation:** AWS Artifact provides on-demand access to AWS security and compliance reports and select online agreements, including SOC reports, ISO certifications, and PCI DSS documents.

---

**46.** Which AWS services are defined as global instead of regional? (Select TWO)
- A. Amazon Route 53. ✅
- B. Amazon EC2.
- C. Amazon S3.
- D. Amazon CloudFront. ✅
- E. Amazon DynamoDB.
**Explanation:** Amazon Route 53 and Amazon CloudFront operate globally across all AWS edge locations rather than being tied to a specific region. Most other AWS services are regional.

---

**47.** How would an AWS customer easily apply common access controls to a large set of users?
- A. Apply an IAM policy to an IAM group. ✅
- B. Apply an IAM policy to an IAM role.
- C. Apply the same IAM policy to all IAM users with access to the same workload.
- D. Apply an IAM policy to an Amazon Cognito user pool.
**Explanation:** IAM groups let you attach a single policy to multiple users at once. Any user added to the group automatically inherits the group's permissions, making access management much easier at scale.

---

**48.** A customer needs to determine TCO for a workload that requires physical isolation. Which hosting model should be used?
- A. Reserved Instances
- B. Dedicated Hosts ✅
- C. On-Demand Instances
- D. Spot Instances
**Explanation:** Dedicated Hosts provide physical servers dedicated entirely to your use, giving you full physical isolation from other AWS customers. This is required for certain compliance and licensing scenarios.

---

**49.** Which design principles are enabled by the AWS Cloud to improve the operation of workloads? (Select TWO)
- A. Loose coupling ✅
- B. Customized hardware
- C. Remove single points of failure ✅
- D. Minimize platform design
- E. Least privilege
**Explanation:** Loose coupling reduces dependencies between components so failures don't cascade. Removing single points of failure through redundancy and multi-AZ deployments ensures your workload stays available even when individual components fail.
