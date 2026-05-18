**1.** How can a company reduce its Total Cost of Ownership (TCO) using AWS?
- A. By having no operational expenditures.
- B. By having no responsibility for third-party license costs.
- C. By minimizing large capital expenditures. ✅
- D. By having AWS manage applications.
**Explanation:** AWS reduces TCO primarily by eliminating large upfront capital expenditures on hardware. Instead of buying servers, you pay only for what you use, converting capex to opex.

---

**2.** Which options does AWS make available for customers who want to learn about security in the cloud in an instructor-led setting? (Select TWO)
- A. AWS Online Tech Talks.
- B. AWS Classroom Training. ✅
- C. AWS Forums.
- D. AWS Trusted Advisor.
- E. AWS Blog. ✅
**Explanation:** AWS offers instructor-led classroom training through AWS Training and Certification. AWS Blog also provides educational security content. Forums and Tech Talks are self-service rather than instructor-led.

---

**3.** Which of the following will enhance the security of access to the AWS Management Console? (Select TWO)
- A. Security groups.
- B. AWS Certificate Manager.
- C. AWS Secrets Manager.
- D. Password policies. ✅
- E. AWS Multi-Factor Authentication (AWS MFA). ✅
**Explanation:** Strong password policies ensure users create complex passwords that are hard to guess. MFA adds a second layer of verification beyond just a password, significantly reducing the risk of unauthorized access.

---

**4.** Which of the following features can be configured through the Amazon VPC Dashboard? (Select TWO)
- A. Elastic Load Balancing.
- B. Amazon Route 53.
- C. Subnets. ✅
- D. Security Groups. ✅
- E. Amazon CloudFront distributions.
**Explanation:** The VPC Dashboard lets you manage networking components like subnets, security groups, route tables, internet gateways, and NAT gateways. ELB, Route 53, and CloudFront are configured in their own dashboards.

---

**5.** For which auditing process does AWS have sole responsibility?
- A. Zone Security
- B. Amazon S3 bucket policies.
- C. Physical security. ✅
- D. AWS CloudTrail Logs.
**Explanation:** AWS has sole responsibility for the physical security of its data centers. Customers never have access to AWS facilities. S3 bucket policies and CloudTrail logs are the customer's responsibility to configure and review.

---

**6.** Which of the following are advantages of AWS consolidated billing? (Select TWO)
- A. A fixed discount on the monthly bill.
- B. Potential volume discounts as usage in all accounts is combined. ✅
- C. Service limits increasing by default in all accounts.
- D. The ability to receive one bill for multiple accounts. ✅
**Explanation:** Consolidated billing combines usage across all accounts so you can reach higher volume tiers and receive discounts. It also simplifies payment by generating a single invoice for all accounts in the organization.

---

**7.** Which of the following common IT tasks can AWS cover to free up company IT resources? (Select TWO)
- A. Patching databases software. ✅
- B. Backing up databases. ✅
- C. Creating database schema.
- D. Testing application releases.
- E. Running penetration tests.
**Explanation:** AWS managed database services like RDS handle patching and backups automatically. Schema design and application testing remain the customer's responsibility as they are application-level concerns.

---

**8.** A company wants to expand from one AWS Region into a second AWS Region. What does the company need to do to start supporting the new Region?
- A. Download the AWS Management Console for the new Region.
- B. Begin deploying resources in the second Region. ✅
- C. Move an Availability Zone to the new Region.
- D. Contact an AWS Account Manager to sign a new contract.
**Explanation:** AWS Regions are available to all customers by default. You simply start deploying resources in the new Region through the console, CLI, or API. No special contracts or downloads are required.

---

**9.** Why is it beneficial to use Elastic Load Balancers with applications?
- A. They automatically adjust capacity and are provided at no charge to users.
- B. Balancers do not provide a single point of failure
- C. They allow for the conversion of traffic to data
- D. They are capable of handling constant changes in network traffic patterns. ✅
**Explanation:** Elastic Load Balancing distributes incoming traffic across multiple targets and handles traffic pattern changes automatically, improving fault tolerance and availability of your application.

---

**10.** Which is the MINIMUM AWS Support plan that allows for one-hour target response time for support cases?
- A. Basic
- B. Enterprise.
- C. Business. ✅
- D. Developer
**Explanation:** AWS Business Support provides a one-hour response time for urgent support cases where your production system is down. Developer Support only offers 12-hour response times for general guidance.

---

**11.** What is the lowest-cost, durable storage option for retaining database backups for immediate retrieval?
- A. Amazon EBS.
- B. Amazon Glacier.
- C. Amazon S3. ✅
- D. Amazon EFS
- E. Amazon EC2 Instance Store.
**Explanation:** Amazon S3 offers low-cost durable object storage with immediate retrieval. Glacier is cheaper but has retrieval delays. EBS and EFS are more expensive block and file storage options not suited for backup archiving.

---

**12.** What AWS team assists customers with accelerating cloud adoption through paid engagements in specialty practice areas?
- A. AWS Enterprise Support.
- B. AWS Technical Account Managers.
- C. AWS Concierge Services
- D. AWS Professional Services. ✅
- E. AWS Solutions Architects.
**Explanation:** AWS Professional Services is a global team that helps customers achieve their desired business outcomes through paid engagements, working alongside customers and partners to accelerate cloud adoption.

---

**13.** A company needs 24/7 phone email and chat access with a response time of less than 1 hour if a production system has a service interruption. Which AWS Support plan meets these requirements at the LOWEST cost?
- A. Basic.
- B. Business. ✅
- C. Enterprise.
- D. Developer.
**Explanation:** AWS Business Support provides 24/7 phone, email, and chat access with a one-hour response time for production system outages. Enterprise offers faster response but at a higher cost, making Business the lowest-cost option that meets these requirements.

---

**14.** If a customer needs to audit the change management of AWS resources, which of the following AWS services should the customer NOT use?
- A. AWS Trusted Advisor. ✅
- B. AWS Config.
- C. Amazon CloudWatch.
- D. Amazon CloudTrail
**Explanation:** AWS Trusted Advisor provides best practice recommendations but does not track resource changes. AWS Config, CloudWatch, and CloudTrail all provide change tracking and audit capabilities for AWS resources.

---

**15.** How does AWS Trusted Advisor provide guidance to users of the AWS Cloud? (Select TWO)
- A. It detects potential security vulnerabilities caused by permissions settings on account resources. ✅
- B. It provides a list of cost optimization recommendations based on current AWS usage. ✅
- C. It automatically corrects potential security issues caused by permissions settings on account resources.
- D. It provides proactive alerting whenever an Amazon EC2 instance has been compromised.
- E. It identifies software vulnerabilities in applications running on AWS.
**Explanation:** Trusted Advisor analyzes your AWS environment and provides recommendations across cost optimization, security, performance, fault tolerance, and service limits. It identifies issues but does not automatically fix them.

---

**16.** Which AWS managed service is used to host databases?
- A. AWS Database Migration Service
- B. Amazon RDS. ✅
- C. AWS Glacier
- D. AWS EC2
**Explanation:** Amazon RDS is a fully managed relational database service that handles provisioning, patching, backups, and failover. It supports MySQL, PostgreSQL, Oracle, SQL Server, and Amazon Aurora.

---

**17.** Which IAM entity is associated with an access key ID and secret access key when using AWS CLI?
- A. IAM user. ✅
- B. IAM group.
- C. IAM policy.
- D. IAM role.
**Explanation:** Access keys consist of an access key ID and secret access key and are associated with IAM users for programmatic access via the CLI or API. Roles use temporary credentials and groups cannot have access keys.

---

**18.** Under the shared responsibility model, which of the following is the customer NOT responsible for? (Select TWO)
- A. Ensuring that data is encrypted at rest.
- B. Ensuring that firmware is updated on hardware devices. ✅
- C. Ensuring Lambda functions are written with correct syntax.
- D. Ensuring that network cables are category six or higher. ✅
**Explanation:** AWS is solely responsible for maintaining physical hardware including firmware updates and physical network infrastructure like cables. Customers are responsible for their data encryption and application code.

---

**19.** Which AWS service provides a simple and scalable shared file storage solution for Linux-based AWS and on-premises servers?
- A. Amazon FSx
- B. Amazon EBS.
- C. Amazon EFS. ✅
- D. Amazon S3.
**Explanation:** Amazon EFS provides a fully managed NFS file system that can be mounted simultaneously by multiple Linux instances both in AWS and on-premises, making it ideal for shared file storage workloads.

---

**20.** What credential components are required to gain programmatic access to an AWS account? (Select TWO)
- A. A user ID.
- B. A secret access key. ✅
- C. A secondary key.
- D. An access key ID. ✅
- E. A primary key.
**Explanation:** Programmatic access to AWS requires both an access key ID which identifies the user and a secret access key which acts as the password. Together they authenticate API and CLI requests.

---

**21.** Which of the following is a shared control between the customer and AWS?
- A. Configuration of an Amazon EC2 instance.
- B. Awareness. ✅
- C. Environmental controls of physical AWS data centers.
- D. Providing a key for Amazon S3 client-side encryption.
**Explanation:** Awareness and training is a shared control — AWS trains its employees on security while customers are responsible for training their own staff on AWS security best practices.

---

**22.** Which type of AWS storage is ephemeral and is deleted when an instance is stopped or terminated?
- A. Amazon S3.
- B. Amazon EBS.
- C. Amazon EFS.
- D. Amazon EC2 instance store. ✅
**Explanation:** EC2 instance store provides temporary block storage physically attached to the host computer. This storage is lost when the instance stops, hibernates, or terminates. Use EBS for persistent storage.

---

**23.** Which of the following is an advantage of consolidated billing on AWS?
- A. Shared access permissions.
- B. Eliminates the need for tagging.
- C. Volume pricing qualification. ✅
- D. Multiple bills per account.
**Explanation:** Consolidated billing combines usage from all accounts in an organization, which can qualify the organization for volume pricing tiers and discounts that individual accounts might not reach on their own.

---

**24.** Which Amazon EC2 pricing model allows customers to use existing server-bound software licenses?
- A. Dedicated Hosts. ✅
- B. Spot Instances.
- C. On-Demand Instances.
- D. Reserved Instances.
**Explanation:** Dedicated Hosts provide physical servers dedicated to your use, allowing you to use your existing per-socket, per-core, or per-VM software licenses that require physical server binding.

---

**25.** Which of the following security measures protect access to an AWS account? (Select TWO)
- A. Grant least privilege access to IAM users. ✅
- B. Create one IAM user and share with many developers and users.
- C. Enable Amazon CloudFront.
- D. Enable AWS CloudTrail.
- E. Activate multi-factor authentication (MFA) for privileged users. ✅
**Explanation:** Least privilege ensures users only have the permissions they need, limiting damage if credentials are compromised. MFA adds a second authentication factor making unauthorized access much harder even if a password is stolen.

---

**26.** Which AWS service provides the ability to manage infrastructure as code?
- A. AWS Direct Connect.
- B. AWS CodePipeline.
- C. AWS CloudFormation. ✅
- D. AWS CodeDeploy.
**Explanation:** AWS CloudFormation lets you model and provision AWS infrastructure using JSON or YAML templates, enabling you to treat infrastructure as code with version control, repeatability, and automation.

---

**27.** What is an advantage of deploying an application across multiple Availability Zones?
- A. The application will have higher availability because it can withstand a service disruption in one Availability Zone. ✅
- B. There is a lower risk of service failure if a natural disaster causes a service disruption in a given AWS Region.
- C. There will be better coverage as Availability Zones are geographically distant and can serve a wider area.
- D. There will be decreased application latency that will improve the user experience.
**Explanation:** Multiple AZs within a Region are isolated from each other's failures. If one AZ goes down your application keeps running in the others, achieving high availability without the cost of multi-Region deployment.

---

**28.** A customer needs to run a relational database that easily scales. Which AWS service should they use?
- A. Amazon Aurora. ✅
- B. Amazon DynamoDB.
- C. Amazon ElastiCache.
- D. Amazon Quantum Ledger Database
**Explanation:** Amazon Aurora is a MySQL and PostgreSQL compatible relational database that scales automatically up to 128TB of storage and can handle thousands of transactions per second with high availability built in.

---

**29.** Which of the following is NOT an AWS Cloud architecture design principle? (Select TWO)
- A. Implement loose coupling.
- B. Implement layered security model
- C. Anticipate failure
- D. Implement vertical scaling. ✅
- E. Implement single points of failure. ✅
**Explanation:** AWS architecture principles favor horizontal scaling over vertical scaling and designing to eliminate single points of failure. Loose coupling, layered security, and designing for failure are all recommended principles.

---

**30.** AWS Enterprise Support users have access to which service or feature not available to other AWS Support plans?
- A. AWS Trusted Advisor.
- B. AWS Support case.
- C. Amazon Connect.
- D. Concierge team. ✅
**Explanation:** The AWS Concierge team is exclusively available to Enterprise Support customers. They assist with billing and account inquiries and help navigate AWS resources and escalations.

---

**31.** A company will be moving from an on-premises data center to the AWS Cloud. What would be one financial difference after the move?
- A. Moving from upfront capital expense (capex) to variable operational expense (opex). ✅
- B. Elimination of upfront capital expense (capex) and elimination of variable operational expense (opex).
- C. Moving from upfront capital expense (capex) to variable capital expense (capex).
- D. Moving from variable operational expense (opex) to upfront capital expense (capex).
**Explanation:** On-premises requires large upfront hardware purchases (capex). AWS uses a pay-as-you-go model where you pay only for what you consume each month (opex), eliminating the need for large capital investments.

---

**32.** When performing a cost analysis that supports physical isolation of a customer workload, which compute hosting model should be accounted for in the TCO?
- A. On-Demand Instances
- B. No Upfront Reserved Instances
- C. Dedicated Hosts ✅
- D. Reserved Instances
**Explanation:** Dedicated Hosts provide physical server isolation for compliance and licensing requirements. They cost more than shared instances and must be accounted for separately in TCO calculations.

---

**33.** Which AWS service should be used for long-term, lowest-cost storage of data backups?
- A. Amazon RDS.
- B. AWS EBS.
- C. Amazon Glacier
- D. Amazon Glacier Deep Archive ✅
- E. AWS Snowball.
**Explanation:** Amazon S3 Glacier Deep Archive is the lowest-cost storage class in AWS, designed for data that is rarely accessed and can tolerate retrieval times of 12 hours. It is ideal for long-term backup archiving.

---

**34.** Which is the MINIMUM AWS Support plan that provides technical support through phone calls?
- A. Basic.
- B. Enterprise.
- C. Business. ✅
- D. Developer.
**Explanation:** AWS Business Support is the minimum plan that includes 24/7 phone access to Cloud Support Engineers. Developer Support only offers email access during business hours.

---

**35.** Which Amazon EC2 instance pricing model can provide discounts of up to 90%?
- A. Reserved Instances.
- B. On-Demand.
- C. Dedicated Hosts.
- D. Spot Instances. ✅
**Explanation:** Spot Instances use spare AWS capacity and can offer discounts of up to 90% compared to On-Demand prices. The trade-off is that AWS can reclaim them with a two-minute warning when capacity is needed elsewhere.

---

**36.** Which of the following AWS services can be used to serve large amounts of online video content with the lowest possible latency? (Select TWO)
- A. AppStream 2.0
- B. Amazon Glacier.
- C. Amazon S3. ✅
- D. Amazon Elastic File System (EFS).
- E. Amazon CloudFront. ✅
**Explanation:** Amazon S3 stores video files durably and cost-effectively. Amazon CloudFront delivers that content from edge locations close to viewers worldwide, minimizing latency for video streaming.

---

**37.** What can AWS edge locations be used for? (Select TWO)
- A. Delivering content closer to users. ✅
- B. Reducing traffic on the server by caching responses. ✅
- C. Hosting applications.
- D. Running NoSQL database caching services.
- E. Sending notification messages to end users.
**Explanation:** AWS edge locations are used by CloudFront to cache content close to end users for low-latency delivery. Caching at the edge reduces the number of requests that need to go back to the origin server.

---

**38.** Which AWS tool or service provides detailed reports on estimated cost savings after migration?
- A. AWS Total Cost of Ownership (TCO) Calculator. ✅
- B. AWS Migration Hub.
- C. Cost Explorer.
- D. AWS Budgets.
- E. Pricing Calculator
**Explanation:** The AWS TCO Calculator helps you compare the cost of running your applications on-premises versus on AWS, providing detailed reports on estimated savings to justify migration decisions.

---

**39.** Which AWS service provides a customized view of the health of specific AWS services that power a customer's workloads?
- A. Amazon CloudWatch.
- B. AWS Service Health Dashboard.
- C. AWS Personal Health Dashboard. ✅
- D. AWS X-Ray.
**Explanation:** AWS Personal Health Dashboard gives you a personalized view of AWS service health events that may affect your specific resources, unlike the Service Health Dashboard which shows general AWS-wide status.

---

**40.** One of the advantages to moving infrastructure from an on-premises data center to the AWS Cloud is:
- A. It allows the business to leave servers unpatched.
- B. It allows the business to focus on business activities. ✅
- C. It allows the business to eliminate IT bills.
- D. It allows the business to put a server in each customer's data center.
**Explanation:** By offloading infrastructure management to AWS, businesses free up their IT teams to focus on innovation and revenue-generating activities rather than maintaining physical hardware.

---

**41.** How can an AWS user with an AWS Basic Support plan obtain technical assistance from AWS? (Select TWO)
- A. AWS Discussion Forums. ✅
- B. AWS Trusted Advisor. ✅
- C. AWS Senior Support Engineers.
- D. AWS Technical Account Managers.
**Explanation:** Basic Support includes access to AWS Discussion Forums where the community can help answer questions, and the core AWS Trusted Advisor checks. Phone and engineer support require paid support plans.

---

**42.** How can a user protect against AWS service disruptions if a natural disaster affects an entire geographic area?
- A. Deploy applications across multiple AWS Regions. ✅
- B. Use a hybrid cloud computing deployment model within the geographic area.
- C. Store application artifacts using AWS Artifact and replicate them across multiple AWS Regions.
- D. Deploy applications across multiple Availability Zones within an AWS Region.
**Explanation:** Natural disasters can affect an entire AWS Region. Deploying across multiple Regions ensures your application survives even a complete regional outage. Multi-AZ protects against data center failures but not full regional disasters.

---

**43.** Which activity is a customer responsibility in the AWS Cloud according to the AWS shared responsibility model?
- A. Patching and fixing flaws within the AWS Cloud infrastructure.
- B. Ensuring network connectivity from AWS to the internet.
- C. Ensuring the physical security of cloud data centers.
- D. Ensuring Amazon EBS volumes are backed up. ✅
**Explanation:** Backing up EBS volumes is the customer's responsibility. AWS provides the tools like snapshots but customers must configure and manage their own backup strategy. AWS handles physical infrastructure and network connectivity.

---

**44.** In which scenario should Amazon EC2 Spot Instances be used?
- A. A company has a number of infrequent interruptible jobs that are currently using On-Demand Instances. ✅
- B. A company has a number of application services whose SLA requires 99.999% uptime.
- C. A company wants to move its main website to AWS from an on-premises web server.
- D. A company's heavily used legacy database is currently running on-premises.
**Explanation:** Spot Instances are ideal for workloads that are flexible about when they run and can tolerate interruptions, such as batch processing, data analysis, or background jobs that run infrequently.

---

**45.** A customer is deploying a new application and needs to choose an AWS Region. Which factors could influence the decision? (Select TWO)
- A. Reduced latency to users. ✅
- B. Cooling costs in hotter climates.
- C. Proximity to the customer's office for on-site visits.
- D. Data sovereignty compliance. ✅
- E. The application's presentation in the local language.
**Explanation:** Choosing a Region close to your users reduces latency. Data sovereignty laws may require data to stay within certain geographic boundaries. Cooling costs and office proximity are not relevant AWS Region selection factors.

---

**46.** Which AWS service provides alerts when an AWS event may impact a company's AWS resources?
- A. AWS Service Health Dashboard.
- B. AWS Personal Health Dashboard. ✅
- C. AWS Infrastructure Event Management.
- D. AWS Trusted Advisor.
**Explanation:** AWS Personal Health Dashboard proactively notifies you about AWS events that may affect your specific resources with actionable information and guidance to help you plan for scheduled changes.

---

**47.** Which disaster recovery scenario offers the lowest probability of downtime?
- A. Warm standby.
- B. Pilot light.
- C. Multi-site active-active. ✅
- D. Backup and restore.
**Explanation:** Multi-site active-active runs your workload simultaneously in multiple sites. Traffic is distributed across all sites so if one fails the others continue without any downtime. It is the most expensive but offers the lowest RTO.

---

**48.** Which service's PRIMARY purpose is software version control?
- A. AWS Code Artifact.
- B. Amazon CodeStar.
- C. Amazon Cognito.
- D. AWS CodeCommit. ✅
**Explanation:** AWS CodeCommit is a fully managed source control service that hosts secure Git repositories, making it the primary AWS service for software version control.

---

**49.** How can a customer increase security to AWS account logins? (Select TWO)
- A. Use Session Manager
- B. Enable AWS Organizations
- C. Enable Multi-Factor Authentication (MFA) ✅
- D. Configure a strong password policy ✅
- E. Use Amazon Cognito to manage access
- F. Configure AWS Certificate Manager
**Explanation:** MFA requires a second form of verification beyond a password, making unauthorized access much harder. Strong password policies enforce complexity and rotation requirements to reduce the risk of password-based attacks.

---

**50.** An engineer wants to deploy AWS Infrastructure as code using a programming language he is familiar with. Which service can be used?
- A. Amazon S3
- B. Amazon CloudFormation
- C. Amazon CloudFront
- D. Cloud Development Kit ✅
**Explanation:** AWS Cloud Development Kit (CDK) lets developers define cloud infrastructure using familiar programming languages like Python, TypeScript, Java, and C#, which are then synthesized into CloudFormation templates.
