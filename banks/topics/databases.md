# 📚 AWS Databases — RDS, DynamoDB, Aurora & more

> **Study Resources for this Topic:**
>
> - 📖 **Official AWS Docs:** [https://docs.aws.amazon.com/rds/](https://docs.aws.amazon.com/rds/)
> - 🎬 **YouTube Overview:** [https://www.youtube.com/watch?v=eMzCI7S1P9M](https://www.youtube.com/watch?v=eMzCI7S1P9M)
> - 🎓 **AWS Skill Builder (Free):** [AWS Cloud Practitioner Essentials](https://explore.skillbuilder.aws/learn/course/external/view/elearning/134/aws-cloud-practitioner-essentials)
>
> 💡 **Quick Tip:** Focus on: RDS (managed relational), DynamoDB (NoSQL), Aurora (MySQL/PostgreSQL-compatible), Redshift (data warehouse), Neptune (graph).

---

**1.** Which feature of Amazon Redshift improves query performance by caching the results of frequently run queries?
- A. Auto Scaling
- B. Redshift Spectrum
- C. Result caching ✅
- D. Materialized views

---

**2.** Question 957 A company is developing a mobile app that needs a high-performance NoSQL database. Which AWS services could the company use for this database? (Choose two.)
- A. Amazon Aurora
- B. Amazon RDS
- C. Amazon Redshift
- D. Amazon DocumentDB (with MongoDB compatibility) ✅
- E. Amazon DynamoDB ✅

---

**3.** Question 1235 A company needs to migrate a PostgreSQL database from on-premises to Amazon RDS. Which AWS service or tool should the company use to meet this requirement?
- A. Cloud Adoption Readiness Tool
- B. AWS Migration Hub
- C. AWS Database Migration Service (AWS DMS) ✅
- D. AWS Application Migration Service

---

**4.** Question 1265 A global company wants to use a managed security service for protection from SQL injection attacks. The service also must provide detailed logging information about access to the company's ecommerce applications. Which AWS service will meet these requirements?
- A. AWS Network Firewall
- B. Amazon RDS for SQL Server
- C. Amazon GuardDuty
- D. AWS WAF ✅

---

**5.** Question 1283 Which AWS Cloud benefit gives a company the ability to quickly deploy cloud resources to access compute, storage, and database infrastructures in a matter of minutes?
- A. Elasticity
- B. Cost savings
- C. Agility ✅
- D. Reliability

---

**6.** Question 1292 Which of the following is a fully managed graph database service on AWS?
- A. Amazon Aurora
- B. Amazon FSx
- C. Amazon DynamoDB
- D. Amazon Neptune ✅

---

**7.** Question 1300 A company wants to move its on-premises databases to managed cloud database services by using a simplified migration process. Which AWS service or tool can help the company meet this requirement?
- A. AWS Storage Gateway
- B. AWS Application Migration Service
- C. AWS DataSync
- D. AWS Database Migration Service (AWS DMS) ✅

---

**8.** Question 1317 A library wants to automate the classification of electronic books based on the contents of the books. Which AWS service should the library use to meet this requirement?
- A. Amazon Redshift
- B. Amazon CloudSearch
- C. Amazon Comprehend ✅
- D. Amazon Aurora

---

**9.** Question 1324 A company wants to use the AWS Cloud to deploy an application globally. Which architecture deployment model should the company use to meet this requirement?
- A. Multi-Region ✅
- B. Single-Region
- C. Multi-AZ
- D. Single-AZ

---

**10.** Question 1350 Which AWS service is a relational database compatible with MySQL and PostgreSQL?
- A. Amazon Redshift
- B. Amazon DynamoDB
- C. Amazon Aurora ✅
- D. Amazon Neptune

---

**11.** Question 1361 Which AWS service provides the ability to host a NoSQL database in the AWS Cloud?
- A. Amazon Aurora
- B. Amazon DynamoDB ✅
- C. Amazon RDS
- D. Amazon Redshift

---

**12.** Question 484 A company wants to run a graph query that provides credit card users' names, addresses, and transactions. The company wants the graph to show if the names, addresses, and transactions indicates possible fraud. Which AWS database service will meet these requirements?
- A. Amazon DocumentDB (with MongoDB compatibility)
- B. Amazon Timestream
- C. Amazon DynamoDB
- D. Amazon Neptune ✅

---

**13.** Question 488 A company needs to provide customer service by using voice calls and web chat features. Which AWS service should the company use to meet these requirements?
- A. Amazon Aurora
- B. Amazon Connect ✅
- C. Amazon WorkSpaces
- D. AWS Organizations

---

**14.** Question 499 A company runs MySQL database workloads on self-managed servers in an on-premises data center. The company wants to migrate the database workloads to an AWS managed service. Which migration strategy should the company use?
- A. Rehost
- B. Repurchase
- C. Refactor
- D. Replatform ✅

---

**15.** Question 518 A company is building an application that will receive millions of database queries each second. The company needs the data store for the application to scale to meet these needs. Which AWS service will meet this requirement?
- A. Amazon DynamoDB ✅
- B. AWS Cloud9
- C. Amazon ElastiCache for Memcached
- D. Amazon Neptune

---

**16.** Question 525 A company needs to deploy a PostgreSQL database into Amazon RDS. The database must be highly available and fault tolerant. Which AWS solution should the company use to meet these requirements?
- A. Amazon RDS with a single Availability Zone
- B. Amazon RDS snapshots
- C. Amazon RDS with multiple Availability Zones ✅
- D. AWS Database Migration Service (AWS DMS)

---

**17.** A company wants to migrate its on-premises relational databases to the AWS Cloud. The company wants to deploy Amazon RDS as close as possible to the company's current location. Which AWS service or resource will meet these requirements?

- A. Amazon Connect
- B. AWS Direct Connect
- C. Amazon Macie
- D. AWS Regions ✅

**Explanation:** AWS has Regions around the world. The company should choose the AWS Region geographically closest to their location when deploying Amazon RDS to minimize latency.

---

**18.** A company wants to use a graph database to detect fraud patterns in real time. Which AWS service will meet this requirement?

- A. Amazon DynamoDB
- B. Amazon Neptune ✅
- C. Amazon RDS
- D. Amazon Timestream for LiveAnalytics

**Explanation:** Amazon Neptune is a fully managed graph database service optimized for storing and querying highly connected data, making it ideal for fraud detection use cases that analyze relationship patterns.

---

**19.** A company needs a file-sharing service that supports SMB protocol. Which AWS service will meet this requirement?

- A. Amazon Aurora
- B. AWS Config
- C. AWS DataSync
- D. Amazon FSx for Windows File Server ✅

**Explanation:** Amazon FSx for Windows File Server provides fully managed Windows file shares built on Windows Server, natively supporting the SMB protocol for Windows-based workloads.

---

**20.** A company runs a MySQL database in the company's on-premises data center. The company wants to run a copy of the database in the AWS Cloud. Which AWS service will meet this requirement?

- A. Amazon RDS ✅
- B. Amazon Neptune
- C. Amazon ElastiCache (Redis)
- D. Amazon DynamoDB

**Explanation:** Amazon RDS supports MySQL and provides a fully managed relational database service, handling provisioning, patching, backup, and recovery automatically.

---

**21.** Which AWS services are examples of NoSQL databases? (Choose two.)

- A. Amazon DynamoDB ✅
- B. Amazon ElastiCache ✅
- C. Amazon Redshift
- D. Amazon Aurora
- E. Amazon RDS for MySQL

---

**22.** A company wants to migrate its on-premises PostgreSQL database to a managed PostgreSQL database on AWS. Which AWS service will meet this requirement?

- A. Amazon DynamoDB
- B. Amazon Neptune
- C. Amazon RDS ✅
- D. Amazon Redshift

---

**23.** A company plans to migrate to the AWS Cloud. The company must gather information about its on-premises applications, such as hostnames, IP addresses, and MAC addresses. Which AWS service will meet these requirements?

- A. AWS Application Discovery Service ✅
- B. AWS Application Migration Service
- C. AWS Database Migration Service (AWS DMS)
- D. AWS X-Ray

---

**24.** What is the benefit of using AWS managed services such as Amazon ElastiCache and Amazon RDS?
- A. They require the customer to monitor and replace failing instances.
- B. They have better performance than customer-managed services.
- C. They simplify patching and updating underlying OSs. ✅
- D. They do not require the customer to optimize instance type or size selections.
**Explanation:** AWS managed services handle routine tasks like OS patching, backups, and failover automatically, freeing customers to focus on their applications rather than infrastructure maintenance.

---

**25.** Which of the following is a fast and reliable Graph database service?
- A. Amazon Redshift.
- B. Amazon RDS.
- C. Amazon DynamoDB.
- D. Amazon Neptune. ✅
**Explanation:** Amazon Neptune is a fully managed graph database service optimized for storing and querying highly connected datasets such as social networks, recommendation engines, and fraud detection graphs.

---

**26.** Which AWS managed service is used to host databases?
- A. AWS Database Migration Service
- B. Amazon RDS. ✅
- C. AWS Glacier
- D. AWS EC2
**Explanation:** Amazon RDS is a fully managed relational database service that handles provisioning, patching, backups, and failover. It supports MySQL, PostgreSQL, Oracle, SQL Server, and Amazon Aurora.

---

**27.** A customer needs to run a relational database that easily scales. Which AWS service should they use?
- A. Amazon Aurora. ✅
- B. Amazon DynamoDB.
- C. Amazon ElastiCache.
- D. Amazon Quantum Ledger Database
**Explanation:** Amazon Aurora is a MySQL and PostgreSQL compatible relational database that scales automatically up to 128TB of storage and can handle thousands of transactions per second with high availability built in.

---

**28.** How can a user protect against AWS service disruptions if a natural disaster affects an entire geographic area?
- A. Deploy applications across multiple AWS Regions. ✅
- B. Use a hybrid cloud computing deployment model within the geographic area.
- C. Store application artifacts using AWS Artifact and replicate them across multiple AWS Regions.
- D. Deploy applications across multiple Availability Zones within an AWS Region.
**Explanation:** Natural disasters can affect an entire AWS Region. Deploying across multiple Regions ensures your application survives even a complete regional outage. Multi-AZ protects against data center failures but not full regional disasters.

---

**29.** What is the AWS database service that allows you to upload data structured in key-value format?

- A. Amazon Aurora.
- B. Amazon Redshift.
- C. Amazon RDS.
- D. AWS DynamoDB ✅

**Explanation:** Amazon DynamoDB is a fully managed NoSQL database service that supports key-value and document data structures, offering single-digit millisecond performance at any scale.

---

**30.** You work as an on-premises MySQL DBA. The work of database configuration, backups, patching, and DR can be time-consuming and repetitive. Your company has decided to migrate to the AWS Cloud. Which of the following can help save time on database maintenance so you can focus on data architecture and performance?

- A. Amazon Redshift.
- B. Amazon DynamoDB.
- C. Amazon CloudWatch.
- D. Amazon RDS. ✅

**Explanation:** Amazon RDS (Relational Database Service) is a managed service that automates time-consuming administration tasks like hardware provisioning, database setup, patching, and backups, freeing you to focus on your applications.

---

**31.** What does Amazon ElastiCache provide?

- A. An Ehcache compatible in-memory data store.
- B. An online software store that allows customers to launch pre-configured software with just few clicks.
- C. A domain name system in the cloud.
- D. In-memory caching for read-heavy applications. ✅

**Explanation:** Amazon ElastiCache is a fully managed in-memory caching service supporting Redis and Memcached. It improves application performance by retrieving data from fast, managed caches instead of slower disk-based databases.

---

**32.** Which AWS service provides the ability to host a NoSQL database in the AWS Cloud?

- A. Amazon Aurora
- B. Amazon DynamoDB ✅
- C. Amazon RDS
- D. Amazon Redshift

**Explanation:** Amazon DynamoDB is a fully managed, serverless NoSQL key-value and document database. It delivers single-digit millisecond performance at any scale and is designed for high-throughput applications.

---

**33.** What can AWS edge locations be used for? (Select TWO.)

- A. Hosting applications
- B. Delivering content closer to users ✅
- C. Running NoSQL database caching services
- D. Reducing traffic on the server by caching responses ✅
- E. Sending notification messages to end users

**Explanation:** AWS edge locations are used by Amazon CloudFront to cache and deliver content (like images, videos, and web pages) closer to end users, reducing latency and origin server load.

---

**34.** Which AWS service would a customer use with a static website to achieve lower latency and high transfer speeds?

- A. AWS Lambda
- B. Amazon DynamoDB Accelerator
- C. Amazon Route 53
- D. Amazon CloudFront ✅

**Explanation:** Amazon CloudFront is a global CDN that caches website content at edge locations worldwide, delivering it to users from the location closest to them — reducing latency and improving transfer speeds for static websites.

---

**35.** Which of the following are Database caching services provided by AWS? (Choose 2)

- A. Amazon Macie
- B. Amazon Elasticache ✅
- C. Amazon RDS
- D. DynamoDB Accelerator (DAX) ✅
- E. Amazon Simple Storage Service

**Explanation:** Amazon ElastiCache provides fully managed Redis and Memcached in-memory caching. DynamoDB Accelerator (DAX) is an in-memory cache specifically for DynamoDB that delivers microsecond response times. Both are purpose-built database caching services.

---

**36.** A company has decided to migrate its Oracle database to AWS. Which AWS service can help achieve this without negatively impacting the functionality of the source database?
- A. AWS OpsWorks.
- B. AWS Database Migration Service. ✅
- C. AWS Server Migration Service.
- D. AWS Application Discovery Service.

---

**37.** A company is deploying a new two-tier web application in AWS. Where should the most frequently accessed data be stored so that the application’s response time is optimal?
- A. AWS OpsWorks.
- B. AWS Storage Gateway.
- C. Amazon EBS volume.
- D. Amazon ElastiCache. ✅

---

**38.** Your company has a data store application that requires access to a NoSQL database. Which AWS database offering would meet this requirement?
- A. Amazon Aurora.
- B. Amazon DynamoDB. ✅
- C. Amazon Elastic Block Store.
- D. Amazon Redshift.

---

**39.** What does AWS provide to deploy popular technologies such as IBM MQ on AWS with the least amount of effort and time?
- A. Amazon Aurora.
- B. Amazon CloudWatch.
- C. AWS Quick Start reference deployments. ✅
- D. AWS OpsWorks.

---

**40.** Which AWS services should be used for read/write of constantly changing data? (Select TWO)
- A. Amazon Glacier.
- B. Amazon RDS. ✅
- C. AWS Snowball.
- D. Amazon Redshift.
- E. Amazon EFS. ✅

---

**41.** Which of the following is an AWS managed Domain Name System (DNS) web service?
- A. Amazon Route 53. ✅
- B. Amazon Neptune.
- C. Amazon SageMaker.
- D. Amazon Lightsail.

---

**42.** Which AWS service is a managed NoSQL database?
- A. Amazon Redshift.
- B. Amazon DynamoDB. ✅
- C. Amazon Aurora.
- D. Amazon RDS for ManaDB.

---

**43.** Which AWS service can be used to automatically scale an application up and down without making capacity planning decisions?
- A. Amazon AutoScaling. ✅
- B. Amazon Redshift.
- C. AWS CloudTrail.
- D. AWS Lambda.

---

**44.** Amazon Relational Database Service (Amazon RDS) offers which of the following benefits over traditional database management?
- A. AWS manages the data stored in Amazon RDS tables.
- B. AWS manages the maintenance of the operating system. ✅
- C. AWS automatically scales up instance types on demand.
- D. AWS manages the database type.

---

**45.** Which AWS managed service is used to host databases?
- A. AWS Batch.
- B. AWS Artifact.
- C. AWS Data Pipeline.
- D. Amazon RDS. ✅

---

**46.** A customer needs to run a MySQL database that easily scales. Which AWS service should they use?
- A. Amazon Aurora. ✅
- B. Amazon Redshift.
- C. Amazon DynamoDB.
- D. Amazon ElastiCache.

---

**47.** Which AWS service should be used for long-term, low-cost storage of data backups?
- A. Amazon RDS.
- B. Amazon Glacier. ✅
- C. AWS Snowball.
- D. AWS EBS.

---

**48.** What can AWS edge locations be used for? (Select TWO)
- A. Hosting applications.
- B. Delivering content closer to users. ✅
- C. Running NoSQL database caching services.
- D. Reducing traffic on the server by caching responses. ✅
- E. Sending notification messages to end users.

---

**49.** Which AWS service would a customer use with a static website to achieve tower latency and high transfer speeds?
- A. AWS Lambda.
- B. Amazon DynamoDB Accelerator.
- C. Amazon Route 53.
- D. Amazon CloudFront. ✅

---

**50.** What is the AWS database service that allows you to upload data structured in key-value format?
- A. Amazon DynamoDB. ✅
- B. Amazon Aurora.
- C. Amazon Redshift.
- D. Amazon RDS.

---

**51.** You work as an on-premises MySQL DBA. The work of database configuration, backups, patching, and DR can be time-consuming and repetitive. Your company has decided to migrate to the AWS Cloud. Which of the following can help save time on database maintenance so you can focus on data architecture and performance?
- A. Amazon RDS. ✅
- B. Amazon Redshift.
- C. Amazon DynamoDB.
- D. Amazon CloudWatch.

---

**52.** What does Amazon ElastiCache provide?
- A. In-memory caching for read-heavy applications. ✅
- B. An Ehcache compatible in-memory data store.
- C. An online software store that allows Customers to launch pre-configured software with just few clicks.
- D. A domain name system in the cloud.

---

**53.** A company has a large amount of structured data stored in their on-premises data center. They are planning to migrate all the data to AWS, what is the most appropriate AWS database option?
- A. Amazon DynamoDB.
- B. Amazon SNS.
- C. Amazon RDS. ✅
- D. Amazon ElastiCache.

---

**54.** Which of the following AWS services is designed with native Multi-AZ fault tolerance in mind? (Choose TWO)
- A. Amazon Redshift.
- B. AWS Snowball.
- C. Amazon Simple Storage Service. ✅
- D. Amazon EBS.
- E. Amazon DynamoDB. ✅

---

**55.** What are the Amazon RDS features that can be used to improve the availability of your database? (Choose TWO)
- A. AWS Regions.
- B. Multi-AZ Deployment. ✅
- C. Automatic patching.
- D. Read Replicas. ✅
- E. Edge Locations.

---

**56.** What does Amazon Elastic Beanstalk provide?
- A. A PaaS solution to automate application deployment. ✅
- B. A compute engine for Amazon ECS.
- C. A scalable file storage solution for use with AWS and on-premises servers.
- D. A NoSQL database service.

---

**57.** Which of the following AWS offerings is a MySQL-compatible relational database service that can scale capacity automatically based on demand?
- A. Amazon Neptune.
- B. Amazon Aurora. ✅
- C. Amazon RDS for SQL Server.
- D. Amazon RDS for PostgreSQL.

---

**58.** What are the benefits of using the Amazon Relational Database Service? (Choose TWO)
- A. Lower administrative burden. ✅
- B. Complete control over the underlying host.
- C. Resizable compute capacity. ✅
- D. Scales automatically to larger or smaller instance types.
- E. Supports the document and key-value data structure.

---

**59.** What is the AWS service that provides five times the performance of a standard MySQL database?
- A. Amazon Aurora. ✅
- B. Amazon Redshift.
- C. Amazon DynamoDB.
- D. Amazon Neptune.

---

**60.** For managed services like Amazon DynamoDB, which of the below is AWS responsible for? (Choose TWO)
- A. Protecting credentials.
- B. Logging access activity.
- C. Patching the database software. ✅
- D. Operating system maintenance. ✅
- E. Creating access policies.

---

**61.** Which of the following are factors in determining the appropriate database technology to use for a specific workload? (Choose TWO)
- A. Availability Zones.
- B. Data sovereignty.
- C. The number of reads and writes per second. ✅
- D. The nature of the queries. ✅
- E. Software bugs.

---

**62.** What are the benefits of using DynamoDB? (Choose TWO)
- A. Automatically scales to meet required throughput capacity. ✅
- B. Provides resizable instances to match the current demand.
- C. Supports both relational and non-relational data models.
- D. Offers extremely low (single-digit millisecond) latency. ✅
- E. Supports the most popular NoSQL database engines such as CouchDB and MongoDB.

---

**63.** Which of the following Amazon RDS features facilitates offloading of database read activity?
- A. Database Snapshots.
- B. Multi-AZ Deployments.
- C. Automated Backups.
- D. Read Replicas. ✅

---

**64.** You are running a financial services web application on AWS. The application uses a MySQL database to store the data. Which of the following AWS services would improve the performance of your application by allowing you to retrieve information from fast in-memory caches?
- A. Amazon EFS.
- B. Amazon Neptune.
- C. Amazon ElastiCache. ✅
- D. DAX.

---

**65.** Which AWS Service helps enterprises extend their on-premises storage to AWS in a cost-effective manner?
- A. AWS Data Pipeline.
- B. AWS Storage Gateway. ✅
- C. Amazon Aurora.
- D. Amazon EFS.

---

**66.** A customer is planning to migrate their Microsoft SQL Server databases to AWS. Which AWS Services can the customer use to run their Microsoft SQL Server database on AWS? (Choose TWO)
- A. AWS Fargate.
- B. Amazon Elastic Compute Cloud. ✅
- C. Amazon RDS. ✅
- D. AWS Database Migration service (DMS).
- E. AWS Lambda.

---

**67.** You need to migrate a large number of on-premises workloads to AWS. Which AWS service is the most appropriate?
- A. AWS File Transfer Acceleration.
- B. AWS Server Migration Service. ✅
- C. AWS Database Migration Service.
- D. AWS Application Discovery Service.

---

**68.** Which of the following is a feature of Amazon RDS that performs automatic failover when the primary database fails to respond?
- A. RDS Single-AZ.
- B. RDS Write Replica.
- C. RDS Snapshots.
- D. RDS Multi-AZ. ✅

---

**69.** Which of the following services provide real-time auditing for compliance and vulnerabilities? (Choose TWO)
- A. AWS Config. ✅
- B. Amazon Redshift.
- C. Amazon MQ.
- D. AWS Trusted Advisor. ✅
- E. Amazon Cognito.

---

**70.** For Amazon RDS databases, what does AWS perform on your behalf? (Choose TWO)
- A. Database setup. ✅
- B. Network traffic protection.
- C. Management of the operating system. ✅
- D. Access management.
- E. Management of firewall rules.

---

**71.** An organization needs to build a financial application that requires support for ACID transactions. Which AWS database service is most appropriate in this case?
- A. RedShift.
- B. RDS. ✅
- C. CloudHSM.
- D. DMS.

---

**72.** Amazon RDS supports multiple database engines to choose from. Which of the following is not one of them?
- A. PostgreSQL.
- B. Oracle.
- C. Microsoft SQL Server.
- D. Teradata. ✅

---

**73.** (Q1003) What type of database is Amazon DynamoDB?
- A. In-memory
- B. Relational
- C. Key-value ✅
- D. Graph

---

**74.** (Q1039) Which AWS service helps deliver highly available applications with fast failover for multi-Region and Multi-AZ architectures?
- A. AWS WAF
- B. AWS Global Accelerator ✅
- C. AWS Shield
- D. AWS Direct Connect

---

**75.** (Q1050) Which AWS service is a key-value database that provides sub-millisecond latency on a large scale?
- A. Amazon DynamoDB ✅
- B. Amazon Aurora
- C. Amazon DocumentDB (with MongoDB compatibility)
- D. Amazon Neptune

---

**76.** (Q1070) A company wants to migrate its on-premises relational databases to the AWS Cloud. The company wants to use infrastructure as close to its current geographical location as possible. Which AWS service or resource should the company use to select its Amazon RDS deployment area?
- A. Amazon Connect
- B. AWS Wavelength
- C. AWS Regions ✅
- D. AWS Direct Connect

---

**77.** (Q1153) A company plans to migrate to the AWS Cloud. The company is gathering information about its on-premises infrastructure and requires information such as the hostname, IP address, and MAC address. , Which AWS service will meet these requirements?
- A. AWS DataSync
- B. AWS Application Migration Service
- C. AWS Application Discovery Service ✅
- D. AWS Database Migration Service (AWS DMS)

---

**78.** (Q1156) A user needs to quickly deploy a nonrelational database on AWS. The user does not want to manage the underlying hardware or the database software. : Which AWS service can be used to accomplish this?
- A. Amazon RDS
- B. Amazon DynamoDB ✅
- C. Amazon Aurora
- D. Amazon Redshift

---

**79.** (Q1189) A company wants a time-series database service that makes it easier to store and analyze trillions of events each day. Which AWS service will meet this requirement? 5
- A. Amazon Neptune
- B. Amazon Timestream ✅
- C. Amazon Forecast
- D. Amazon DocumentDB (with MongoDB compatibility)

---

**80.** (Q1204) A company needs to migrate a PostgreSQL database from onpremises to Amazon RDS. Which AWS service or tool should the company use to meet this , requirement?
- A. Cloud Adoption Readiness Tool
- B. AWS Migration Hub
- C. AWS Database Migration Service (AWS DMS) ✅
- D. AWS Application Migration Service

---

**81.** (Q449) Which of the following IT tasks does AWS perform to offload a company's IT resource management responsibilities? (Choose two.)
- A. Configuring operating system firewalls
- B. Setting up access controls for data
- C. Backing up databases ✅
- D. Configuring database user accounts
- E. Installing operating systems ✅

**Explanation:** *(Add explanation here)*

---

**82.** (Q474) Which AWS service provides the ability to host a NoSQL database in the AWS Cloud?
- A. Amazon Aurora
- B. Amazon DynamoDB ✅
- C. Amazon RDS
- D. Amazon Redshift

**Explanation:** *(Add explanation here)*

---

**83.** (Q533) Which AWS service allows a user to provision a managed MySQL DB instance?
- A. Amazon DynamoDB
- B. Amazon Redshift
- C. Amazon RDS ✅
- D. AWS Database Migration Service (AWS DMS)

**Explanation:** *(Add explanation here)*

---

**84.** (Q536) Which AWS service stores graph data in the form of vertices and edges?
- A. Amazon DynamoDB
- B. Amazon RDS
- C. Amazon Quantum Ledger Database (Amazon QLDB)
- D. Amazon Neptune ✅

**Explanation:** *(Add explanation here)*

---

**85.** (Q547) Which of the following describes an AWS Region?
- A. Specific location within a geographic area that provides high availability ✅
- B. Set of data centers spanning multiple countries
- C. A global picture of a user's cloud computing environment
- D. A collection of databases that can be accessed from a specific geographic area only

**Explanation:** *(Add explanation here)*

---

**86.** (Q554) Which AWS database service providers in-memory data storage?
- A. Amazon DynamoDB
- B. Amazon ElastiCache ✅
- C. Amazon RDS
- D. Amazon Timestream

**Explanation:** *(Add explanation here)*

---

**87.** (Q612) A company is running a standard PostgreSQL database on premises. The company is migrating the database to the AWS Cloud and does not want to change the queries that access the database. The company must maximize the query performance. Which AWS service will meet these requirements?
- A. Amazon RDS for PostgreSQL
- B. Amazon Aurora PostgreSQL ✅
- C. Amazon DocumentDB (with MongoDB compatibility)
- D. Amazon DynamoDB

**Explanation:** *(Add explanation here)*

---

**88.** (Q632) Which databases are available on Amazon RDS? (Choose two.)
- A. Sybase
- B. Microsoft SQL Server ✅
- C. IBM Db2
- D. MongoDB
- E. PostgreSQL ✅

**Explanation:** *(Add explanation here)*

---

**89.** (Q645) Which service is an AWS in-memory data store service?
- A. Amazon Aurora
- B. Amazon RDS
- C. Amazon DynamoDB
- D. Amazon ElastiCache ✅

**Explanation:** *(Add explanation here)*

---

**90.** (Q561) Which recommendation can AWS Cost Explorer provide to help reduce cost?
- A. Use a specific database engine.
- B. Change the programming language for an application.
- C. Deploy a specific operating system.
- D. Terminate an idle instance. ✅

---

**91.** (Q586) A company needs an event history of which AWS resources the company has created. Which AWS service will provide this information?
- A. Amazon CloudWatch
- B. AWS CloudTrail ✅
- C. Amazon Aurora
- D. Amazon EventBridge

---

**92.** (Q588) Which AWS service provides a fully managed graph database for highly connected datasets?
- A. Amazon DynamoDB
- B. Amazon RDS
- C. Amazon Neptune ✅
- D. Amazon Aurora

---

**93.** (Q591) Which AWS service enables users to create copies of resources across AWS Regions?
- A. Amazon ElastiCache
- B. AWS CloudFormation ✅
- C. AWS CloudTrail
- D. AWS Systems Manager

---

**94.** (Q597) A company has a website on AWS. The company wants to deliver the website to a worldwide audience and provide low-latency response times for global users. Which AWS service will meet these requirements?
- A. AWS CloudFormation
- B. Amazon CloudFront ✅
- C. Amazon ElastiCache
- D. Amazon DynamoDB

---

**95.** (Q613) A company plans to perform a one-time migration of a large dataset with millions of files from its on-premises data center to the AWS Cloud. Which AWS service should the company use for the migration?
- A. AWS Database Migration Service (AWS DMS)
- B. AWS DataSync ✅
- C. AWS Migration Hub
- D. AWS Application Migration Service

---

**96.** (Q615) A company wants to develop an accessibility application that will convert text into audible speech. Which AWS service will meet this requirement?
- A. Amazon MQ
- B. Amazon Polly ✅
- C. Amazon Neptune
- D. Amazon Timestream

---

**97.** (Q623) A company wants to securely store Amazon RDS database credentials and automatically rotate user passwords periodically. Which AWS service or capability will meet these requirements?
- A. Amazon S83
- B. AWS Systems Manager Parameter Store
- C. AWS Secrets Manager ✅
- D. AWS CloudTrail

---

**98.** (Q626) A company plans to migrate to the AWS Cloud. The company wants to gather information about its on-premises data center. Which AWS service should the company use to meet these requirements?
- A. AWS Application Discovery Service ✅
- B. AWS DataSync
- C. AWS Storage Gateway
- D. AWS Database Migration Service (AWS DMS)

---

**99.** (Q661) A company wants to transfer a virtual Windows Server 2022 that is currently running in its own data Center to AWS. The company wants to automatically convert the existing server to run directly on AWSinfrastructure instead of visualized hardware. Which AWS service will meet these requirements?
- A. AWS DataSync
- B. AWS Database Migration Service (AWS DMS)
- C. AWS Application Discovery Service
- D. AWS Application Migration Service ✅

---

**100.** (Q662) Which AWS service is a fully managed NoSQL database service?
- A. Amazon RDS
- B. Amazon Redshift
- C. Amazon DynamoDB ✅
- D. Amazon Aurora

---

**101.** (Q667) A company wants to migrate its server-based applications to the AWS Cloud. The company wants to determine the total cost of ownership for its compute resources that will be hosted on the AWS,Cloud. Which combination of AWS services or tools will meet these requirements? (Choose two.)
- A. AWS Pricing Calculator ✅
- B. Migration Evaluator ✅
- C. AWS Support Center
- D. AWS Application Discovery Service
- E. AWS Database Migration Service (AWS DMS)

---

**102.** (Q672) A company wants to build graph queries for real-time fraud pattern detection. Which AWS service will meet this requirement?
- A. Amazon Neptune ✅
- B. Amazon DynamoDB
- C. Amazon Timestream
- D. Amazon Forecast

---

**103.** (Q696) Which AWS service supports MySQL database engines?
- A. Amazon Dynamo DB
- B. Amazon RDS ✅
- C. Amazon DocumentDB (with MongoDB compatibility)
- D. Amazon ElastiCache

---

