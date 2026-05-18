# 📚 AWS Storage Services

> **Study Resources for this Topic:**
>
> - 📖 **Official AWS Docs:** [https://aws.amazon.com/products/storage/](https://aws.amazon.com/products/storage/)
> - 🎬 **YouTube Overview:** [https://www.youtube.com/watch?v=6vNC_BCqFmI](https://www.youtube.com/watch?v=6vNC_BCqFmI)
> - 🎓 **AWS Skill Builder (Free):** [AWS Cloud Practitioner Essentials](https://explore.skillbuilder.aws/learn/course/external/view/elearning/134/aws-cloud-practitioner-essentials)
>
> 💡 **Quick Tip:** EBS (block, EC2 attached), EFS (shared file NFS), FSx (Windows SMB), Storage Gateway (hybrid), Snowball/Snowmobile (physical data transfer).

---

**1.** Question 888 Which AWS service is used to provide encryption for Amazon EBS?
- A. AWS Certificate Manager
- B. AWS Systems Manager
- C. AWS KMS ✅
- D. AWS Config

---

**2.** Question 908 A company has a fleet of cargo ships. The cargo ships have sensors that collect data at sea, where there is intermittent or no internet connectivity. The company needs to collect, format, and process the data at sea and move the data to AWS later. Which AWS service should the company use to meet these requirements?
- A. AWS IoT Core
- B. Amazon Lightsail
- C. AWS Storage Gateway
- D. AWS Snowball Edge ✅

---

**3.** Question 1251 A company wants to migrate petabytes of data from its on-premises data center to AWS. The company does not want to use an internet connection to perform the migration. Which AWS service will meet these requirements?
- A. AWS DataSync
- B. Amazon Connect
- C. AWS Snowmobile ✅
- D. AWS Direct Connect

---

**4.** Question 1288 A company wants to migrate unstructured data to AWS. The data needs to be securely moved with inflight encryption and end-to-end data validation. Which AWS service will meet these requirements?
- A. AWS Application Migration Service
- B. Amazon Elastic File System (Amazon EFS)
- C. AWS DataSync ✅
- D. AWS Migration Hub

---

**5.** Question 1290 A company wants to quickly implement a continuous integration/continuous delivery (CI/CD) pipeline. Which AWS service will meet this requirement?
- A. AWS Config
- B. Amazon Cognito
- C. AWS DataSync
- D. AWS CodeStar ✅

---

**6.** Question 1301 A company needs a fully managed file server that natively supports Microsoft workloads and file systems. The file server must also support the SMB protocol. Which AWS service should the company use to meet these requirements?
- A. Amazon Elastic File System (Amazon EFS)
- B. Amazon FSx for Lustre
- C. Amazon FSx for Windows File Server ✅
- D. Amazon Elastic Block Store (Amazon EBS)

---

**7.** Question 1345 Which AWS service provides on-premises applications with low-latency access to data that is stored in the AWS Cloud?
- A. Amazon CloudFront
- B. AWS Storage Gateway ✅
- C. AWS Backup
- D. AWS DataSync

---

**8.** Question 470 Which AWS service can generate information that can be used by external auditors?
- A. Amazon Cognito
- B. Amazon FSx
- C. AWS Config ✅
- D. Amazon Inspector

---

**9.** A company stores 100 TB of data in its data center. The company wants to migrate the data to the AWS Cloud without using the internet. Which AWS service or resource will meet these requirements?

- A. Amazon Connect
- B. AWS DataSync
- C. AWS Snowball Edge ✅
- D. AWS VPN services

**Explanation:** AWS Snowball Edge is a physical data transfer device that moves large amounts of data to AWS without using the internet. DataSync and VPN both require internet connectivity.

---

**10.** A company wants to migrate a virtual server that runs Windows Server from an on-premises data center to AWS. The company wants to automatically convert the existing server to run natively on AWS infrastructure. Which AWS service will meet this requirement?

- A. AWS Application Discovery Service
- B. AWS Application Migration Service ✅
- C. AWS Config
- D. AWS DataSync

**Explanation:** AWS Application Migration Service (MGN) automatically converts on-premises servers to run natively on AWS, lifting and shifting workloads without requiring application changes.

---

**11.** Which AWS services provide a way to extend an on-premises architecture to the AWS cloud? (Select TWO)
- A. Amazon EBS.
- B. Amazon Connect.
- C. AWS Storage Gateway ✅
- D. Amazon CloudFront.
- E. AWS Direct Connect. ✅
**Explanation:** AWS Storage Gateway connects on-premises environments to AWS cloud storage. AWS Direct Connect provides a dedicated private network link between your data center and AWS.

---

**12.** Which of the following services will automatically scale with an expected increase in web traffic?
- A. VPC
- B. Elastic Load Balancing. ✅
- C. Amazon EBS.
- D. AWS EC2
**Explanation:** Elastic Load Balancing automatically scales its request handling capacity in response to incoming traffic, distributing load across multiple targets without manual intervention.

---

**13.** Which services can be used across hybrid AWS Cloud architectures? (Select TWO)
- A. Storage Gateway ✅
- B. Amazon Macie
- C. Gateway Load Balancer.
- D. Auto Scaling.
- E. Virtual Private Network. ✅
**Explanation:** AWS Storage Gateway connects on-premises storage to the AWS cloud. AWS VPN creates encrypted tunnels between on-premises networks and AWS, both enabling hybrid architectures.

---

**14.** Which AWS services provide a way to extend an on-premises architecture to the AWS Cloud? (Choose two.)

- A. Amazon EBS
- B. AWS Direct Connect ✅
- C. Amazon CloudFront
- D. Storage Gateway ✅

**Explanation:** AWS Direct Connect provides a private dedicated network connection from on-premises to AWS. AWS Storage Gateway extends on-premises storage to the cloud, enabling hybrid architectures with seamless data movement between environments.

---

**15.** What does AWS Snowball provide? (Choose TWO)
- A. Built-in computing capabilities that allow customers to process data locally. ✅
- B. A catalog of third-party software solutions that customers need to build solutions and run their businesses.
- C. A hybrid cloud storage between on-premises environments and the AWS Cloud.
- D. An Exabyte-scale data transfer service that allows you to move extremely large amounts of data to AWS.
- E. Secure transfer of large amounts of data into and out of the AWS. ✅

---

**16.** Which service provides a hybrid storage service that enables on-premises applications to seamlessly use cloud storage?
- A. Amazon Glacier
- B. AWS Snowball
- C. AWS Storage Gateway ✅
- D. Amazon Elastic Block Storage (Amazon EBS)

---

**17.** Which AWS services provide a way to extend an on-premises architecture to the AWS Cloud? (Select TWO)
- A. Amazon EBS.
- B. AWS Direct Connect. ✅
- C. Amazon CloudFront.
- D. AWS Storage Gateway. ✅
- E. Amazon Connect.

---

**18.** Which AWS Service can be used to establish a dedicated, private network connection between AWS and your datacenter?
- A. AWS Direct Connect. ✅
- B. Amazon CloudFront.
- C. AWS Snowball.
- D. Amazon Route 53.

---

**19.** Which AWS service can be used to store and reliably deliver messages across distributed systems?
- A. Amazon Simple Queue Service. ✅
- B. AWS Storage Gateway.
- C. Amazon Simple Email Service.
- D. Amazon Simple Storage Service.

---

**20.** Which of the following AWS Services helps with planning application migration to the AWS Cloud?
- A. AWS Snowball Migration Service.
- B. AWS Application Discovery Service. ✅
- C. AWS DMS.
- D. AWS Migration Hub.

---

**21.** A company is building an online cloud storage platform. They need a storage service that can scale capacity automatically, while minimizing cost. Which AWS storage service should the company use to meet these requirements?
- A. Amazon Simple Storage Service. ✅
- B. Amazon Elastic Block Store.
- C. Amazon Elastic Container Service.
- D. AWS Storage Gateway.

---

**22.** Which of the following are factors should be considered for Amazon EBS pricing? (Choose TWO)
- A. The size of volumes provisioned per month. ✅
- B. The compute capacity you consume.
- C. The amount of data you have stored in snapshots. ✅
- D. The compute time you consume.
- E. The number of Snowball storage devices you request.

---

**23.** A media company has an application that requires the transfer of large data sets to and from AWS every day. This data is business critical and should be transferred over a consistent connection. Which AWS service should the company use?
- A. AWS Direct Connect. ✅
- B. Amazon Comprehend.
- C. AWS Snowmobile.
- D. AWS VPN.

---

**24.** You want to transfer 200 Terabytes of data from on-premises locations to the AWS Cloud, which of the following can do the job in a cost-effective way?
- A. AWS Snowmobile.
- B. AWS Import/Export.
- C. AWS DMS.
- D. AWS Snowball. ✅

---

**25.** You have just finished writing your application code. Which service can be used to automate the deployment and scaling of your application?
- A. Amazon Simple Storage Service.
- B. AWS Elastic Beanstalk. ✅
- C. AWS CodeCommit.
- D. Amazon Elastic File System.

---

**26.** What is the benefit of Amazon EBS volumes being automatically replicated within the same availability zone?
- A. Elasticity.
- B. Durability. ✅
- C. Traceability.
- D. Accessibility.

---

**27.** Which of the following AWS services integrates with AWS Shield and AWS Web Application Firewall (AWS WAF) to protect against network and application layer DDoS attacks?
- A. Amazon EFS.
- B. AWS Secrets Manager.
- C. AWS Systems Manager.
- D. Amazon CloudFront. ✅

---

**28.** (Q1043) Which AWS service is used to provide encryption for Amazon EBS? Cc. AWS KMS
- A. AWS Certificate Manager
- B. AWS Systems Manager
- D. AWS Config

---

**29.** (Q1093) Which option is a physical location of the AWS global infrastructure?
- A. AWS DataSync
- B. AWS Region ✅
- C. Amazon Connect
- D. AWS Organizations

---

**30.** (Q1168) A company is planning to move data backups to the AWS Cloud. The company needs to replace on-premises storage with storage that is cloud-based but locally cached. : Which AWS service meets these requirements? me ae
- A. AWS Storage Gateway ✅
- B. AWS Snowcone
- C. AWS Backup
- D. Amazon Elastic File System (Amazon EFS)

---

**31.** (Q1183) Who enables encryption of data at rest for Amazon Elastic Block Store (Amazon EBS)?
- A. AWS Support
- B. AWS customers ✅
- C. AWS Key Management Service (AWS KMS)
- D. AWS Trusted Advisor

---

**32.** (Q1200) A company has a fleet of cargo ships. The cargo ships have sensors that collect data at sea, where there is intermittent or no internet connectivity. The company needs to collect, format, and process the data at sea and move the data to AWS later. Which AWS service should the company use to meet these requirements?
- A. AWS loT Core
- B. Amazon Lightsail
- C. AWS Storage Gateway
- D. AWS Snowball Edge ✅

---

**33.** (Q427) A company previously lost data that was stored in an on-premises data center. To protect against future loss of data, the company wants to use AWS to automatically launch thousands of its machines in a fully provisioned state in minutes, in a format that supports data restoration. Which AWS service should the company use to meet these requirements?
- A. AWS Direct Connect
- B. AWS Storage Gateway
- C. CloudEndure Disaster Recovery ✅
- D. AWS Backup

**Explanation:** *(Add explanation here)*

---

**34.** (Q434) A company is planning to move data backups to the AWS Cloud. The company needs to replace on-premises storage with storage that is cloud-based but locally cached. Which AWS service meets these requirements?
- A. AWS Storage Gateway ✅
- B. AWS Snowcone
- C. AWS Backup
- D. Amazon Elastic File System (Amazon EFS)

**Explanation:** *(Add explanation here)*

---

**35.** (Q559) Which AWS services or resources can a company use directly on its on-premises servers? (Choose two.)
- A. AWS OpsWorks ✅
- B. AWS CloudFormation
- C. AWS Storage Gateway ✅
- D. Application Load Balancer
- E. Amazon Cognito

**Explanation:** *(Add explanation here)*

---

**36.** (Q592) Which AWS service should a company use to create a serverless workflow?
- A. Amazon Connect
- B. AWS Lambda
- C. AWS Step Functions ✅
- D. Amazon Elastic Block Store (Amazon EBS)
- E. AWS CodeBuild

**Explanation:** *(Add explanation here)*

---

**37.** (Q576) Which AWS service helps users plan and track their server and application inventory migration data to AWS?
- A. Amazon CloudWatch
- B. AWS DataSync
- C. AWS Migration Hub ✅
- D. AWS Application Migration Service

---

**38.** (Q685) A company wants a fully managed service that centralizes and automates data protection across AWS services and hybrid workloads. Which AWS service will meet these requirements?
- A. AWS Artifact
- B. AWS Backup ✅
- C. AWS Batch
- D. AWS Shield

---

