# 📚 Amazon CloudFront & Global Infrastructure

> **Study Resources for this Topic:**
>
> - 📖 **Official AWS Docs:** [https://docs.aws.amazon.com/cloudfront/](https://docs.aws.amazon.com/cloudfront/)
> - 🎬 **YouTube Overview:** [https://www.youtube.com/watch?v=AT-nHW3_SVI](https://www.youtube.com/watch?v=AT-nHW3_SVI)
> - 🎓 **AWS Skill Builder (Free):** [AWS Cloud Practitioner Essentials](https://explore.skillbuilder.aws/learn/course/external/view/elearning/134/aws-cloud-practitioner-essentials)
>
> 💡 **Quick Tip:** CloudFront uses edge locations to cache content. Global Accelerator routes traffic over AWS backbone. Route 53 is DNS.

---

**1.** Question 911 Service control policies (SCPs) manage permissions for which of the following?
- A. Availability Zones
- B. AWS Regions
- C. AWS Organizations ✅
- D. Edge locations

---

**2.** Question 922 A company wants to migrate its applications from its on-premises data center to a VPC in the AWS Cloud. These applications will need to access on-premises resources. Which actions will meet these requirements? (Choose two.)
- A. Use AWS Service Catalog to identify a list of on-premises resources that can be migrated.
- B. Create a VPN connection between an on-premises device and a virtual private gateway in the VPC. ✅
- C. Use an Amazon CloudFront distribution and configure it to accelerate content delivery close to the on-premises
- D. Set up an AWS Direct Connect connection between the on-premises data center and AWS. ✅
- E. Use Amazon CloudFront to restrict access to static web content provided through the on-premises web servers.

---

**3.** Question 1338 A company needs to connect its on-premises data center to the AWS Cloud. The company needs a dedicated, low-latency connection with consistent network performance. Which AWS service will meet these requirements?
- A. AWS Global Accelerator
- B. Amazon CloudFront
- C. AWS Direct Connect ✅
- D. AWS Managed VPN

---

**4.** Question 1352 Which benefit of cloud computing gives a company the ability to deploy applications to users all over the world through a network of AWS Regions, Availability Zones, and edge locations?
- A. Economy of scale
- B. Global reach ✅
- C. Agility
- D. High availability

---

**5.** Question 445 A company is connecting multiple VPCs and on-premises networks. The company needs to use an AWS service as a cloud router to simplify peering relationships. Which AWS service can the company use to meet this requirement?
- A. AWS Direct Connect
- B. AWS Transit Gateway ✅
- C. Amazon Connect
- D. Amazon Route 53

---

**6.** Question 466 A company is building AWS architecture to deliver real-time data feeds from an on-premises data center into an application that runs on AWS. The company needs a consistent network connection with minimal latency. What should the company use to connect the application and the data center to meet these requirements?
- A. AWS Direct Connect ✅
- B. Public internet
- C. AWS VPN
- D. Amazon Connect

---

**7.** Question 527 Which statements accurately describe the relationships among components of AWS global infrastructure? (Choose two.)
- A. There are more AWS Regions than Availability Zones.
- B. There are more edge locations than AWS Regions. ✅
- C. An edge location is an Availability Zone.
- D. There are more AWS Regions than edge locations.
- E. There are more Availability Zones than AWS Regions. ✅

---

**8.** Question 547 A company wants to maintain bandwidth throughput and provide a more consistent network experience than public internet-based connections. Which AWS service should the company choose?
- A. AWS VPN
- B. AWS Direct Connect ✅
- C. Amazon Connect
- D. Amazon CloudFront

---

**9.** Which component of the AWS global infrastructure does Amazon CloudFront use to deliver content to end users with low latency?

- A. Edge locations ✅
- B. AWS Regions
- C. Availability Zones
- D. AWS Direct Connect connections

**Explanation:** CloudFront uses a global network of edge locations to cache and serve content from the point nearest to each end user, dramatically reducing latency for content delivery.

---

**10.** A company is running a globally-accessible application on AWS. The company wants to optimize the application's network traffic. Which AWS service will meet this requirement?

- A. AWS Auto Scaling
- B. AWS CloudFormation
- C. Amazon Connect
- D. AWS Global Accelerator ✅

---

**11.** What is an advantage of deploying an application across multiple Availability Zones?
- A. The application will have higher availability because it can withstand a service disruption in one Availability Zone. ✅
- B. There is a lower risk of service failure if a natural disaster causes a service disruption in a given AWS Region.
- C. There will be better coverage as Availability Zones are geographically distant and can serve a wider area.
- D. There will be decreased application latency that will improve the user experience.
**Explanation:** Multiple AZs within a Region are isolated from each other's failures. If one AZ goes down your application keeps running in the others, achieving high availability without the cost of multi-Region deployment.

---

**12.** Which AWS service is a content delivery network that securely delivers data, video, and applications to users globally with low latency and high speeds?

- A. AWS CloudFormation
- B. AWS Direct Connect
- C. Amazon CloudFront ✅

**Explanation:** Amazon CloudFront is AWS's global content delivery network (CDN). It distributes content through a worldwide network of edge locations, delivering data, videos, APIs, and applications to users with low latency and high transfer speeds.

---

**13.** What are the benefits of using the AWS Cloud for companies with customers in many countries around the world? (Choose two.)

- A. Companies can deploy applications in multiple AWS Regions to reduce latency. ✅
- B. Amazon Translate automatically translates third-party website interfaces into multiple languages.
- C. Amazon CloudFront has multiple edge locations around the world to reduce latency. ✅
- D. AWS is free of charge

**Explanation:** AWS's global infrastructure allows companies to deploy applications in Regions close to their users, and CloudFront's worldwide edge locations cache and serve content with low latency regardless of user location.

---

**14.** What does Amazon CloudFront use to distribute content to global users with low latency?
- A. AWS Global Accelerator.
- B. AWS Regions.
- C. AWS Edge Locations. ✅
- D. AWS Availability Zones.

---

**15.** Which of the following can be described as a global content delivery network (CDN) service?
- A. AWS VPN.
- B. AWS Direct Connect.
- C. AWS Regions.
- D. Amazon CloudFront. ✅

---

**16.** Which of the following is a correct relationship between regions, Availability Zones, and edge locations?
- A. Data centers contain regions.
- B. Regions contain Availability Zones. ✅
- C. Availability Zones contain edge locations.
- D. Edge locations contain regions.

---

**17.** What is an advantage of deploying an application across multiple Availability Zones?
- A. There is a lower risk of service failure if a natural disaster causes a service disruption in a given AWS Region.
- B. The application will have higher availability because it can withstand a service disruption in one Availability Zone. ✅
- C. There will be better coverage as Availability Zones are geographical^ distant and can serve a wider area.
- D. There will be decreased application latency that will improve the user experience.

---

**18.** Which feature of the AWS Cloud will support an international company’s requirement for low latency to all of its customers?
- A. Fault tolerance.
- B. Global reach. ✅
- C. Pay-as-you-go pricing.
- D. High availability.

---

**19.** AWS has created a large number of Edge Locations as part of its Global Infrastructure. Which of the following is NOT a benefit of using Edge Locations?
- A. Edge locations are used by CloudFront to cache the most recent responses.
- B. Edge locations are used by CloudFront to improve your end users’ experience when uploading files.
- C. Edge locations are used by CloudFront to distribute traffic across multiple instances to reduce latency. ✅
- D. Edge locations are used by CloudFront to distribute content to global users with low latency.

---

**20.** Your application has recently experienced significant global growth, and international users are complaining of high latency. What is the AWS characteristic that can help improve your international users’ experience?
- A. Elasticity.
- B. Global reach. ✅
- C. Data durability.
- D. High availability.

---

**21.** A developer needs to set up an SSL security certificate for a client's eCommerce website in order to use the HTTPS protocol. Which of the following AWS services can be used to deploy the required SSL server certificates? (Choose TWO)
- A. Amazon Route 53. ✅
- B. AWS ACM. ✅
- C. AWS Directory Service.
- D. AWS Identity & Access Management.
- E. AWS Data Pipeline.

---

**22.** Which statement best describes the concept of an AWS region?
- A. An AWS Region is a geographical location with a collection of Edge locations.
- B. An AWS Region is a virtual network dedicated only to a single AWS customer.
- C. An AWS Region is a geographical location with a collection of Availability Zones. ✅
- D. An AWS Region represents the country where the AWS infrastructure exist.

---

**23.** Availability Zones within a Region are connected over low-latency links. Which of the following is a benefit of these links?
- A. Create private connection to your data center.
- B. Achieve global high availability.
- C. Automate the process of provisioning new compute resources.
- D. Make synchronous replication of your data possible. ✅

---

**24.** You want to create a backup of your data in another geographical location. Where should you create this backup?
- A. In another Edge location.
- B. In another Region. ✅
- C. In another VPC.
- D. In another Availability Zone.

---

**25.** Which service can you use to route traffic to the endpoint that provides the best application performance for your users worldwide?
- A. AWS Global Accelerator. ✅
- B. AWS Data Pipeline.
- C. AWS DAX Accelerator.
- D. AWS Transfer Acceleration.

---

**26.** Which of the below options are use cases of the Amazon Route 53 service? (Choose TWO)
- A. Point-to-point connectivity between an on-premises data center and AWS.
- B. Detects configuration changes in the AWS environment.
- C. DNS configuration and management. ✅
- D. Manages global application traffic through a variety of routing types. ✅
- E. Provides infrastructure security optimization recommendations.

---

**27.** For some services, AWS automatically replicates data across multiple Availability Zones to provide fault tolerance in the event of a server failure or Availability Zone outage. Select TWO services that automatically replicate data across Availability Zones.
- A. Instance Store.
- B. S3. ✅
- C. DynamoDB. ✅
- D. Amazon Route 53.
- E. AWS VPN.

---

**28.** Which AWS service can be used to route end users to the nearest AWS Region to reduce latency?
- A. Amazon Cognito.
- B. AWS Systems Manager.
- C. AWS Cloud9.
- D. Amazon Route 53. ✅

---

**29.** (Q1035) Which AWS service enables companies to deploy an application close to end users?
- A. Amazon CloudFront ✅
- B. AWS Auto Scaling
- C. AWS AppSync
- D. Amazon Route 53

---

**30.** (Q433) A media company wants to distribute video content to millions of users worldwide over the internet. The company wants to use the AWS global network backbone to distribute cached content with low latency and high data transfer speeds. Which AWS service will meet these requirements?
- A. Amazon CloudFront ✅
- B. AWS Global Accelerator
- C. AWS Direct Connect
- D. Amazon Connect

**Explanation:** *(Add explanation here)*

---

**31.** (Q445) A company wants to test mobile apps on a variety of popular mobile devices. Which AWS service should the company use to achieve this goal?
- A. AWS IoT Core
- B. AWS Wavelength
- C. AWS Device Farm ✅
- D. AWS Direct Connect

**Explanation:** *(Add explanation here)*

---

**32.** (Q468) A company wants to ensure its infrastructure is designed for fault tolerance and business continuity in the event of an environmental disruption. Which AWS infrastructure component should the company replicate across?
- A. Edge locations
- B. Availability Zones
- C. Regions ✅
- D. Amazon Route 53

**Explanation:** *(Add explanation here)*

---

**33.** (Q516) A company plans to run its IT infrastructure in the AWS Cloud. The infrastructure must be highly available. The company also must minimize the network latency between servers. Which deployment scenario will meet these requirements?
- A. Deploy in multiple Availability Zones in multiple AWS Regions.
- B. Deploy in one Availability Zone in one AWS Region
- C. Deploy in multiple AWS Regions. Deploy in one Availability Zone in each Region.
- D. Deploy in multiple Availability Zones in one AWS Region. ✅

**Explanation:** *(Add explanation here)*

---

**34.** (Q616) A company needs to set up dedicated network connectivity between its onpremises data center and the AWS Cloud. The network cannot use the public internet. Which AWS service or feature will meet these requirements?
- A. AWS Transit Gateway
- B. AWS VPN
- C. Amazon CloudFront
- D. AWS Direct Connect ✅

---

**35.** (Q663) A company deployed an application in multiple AWS Regions around the world. The company, wants to improve the applications performance and availability. Which AWS service will meet these requirements?
- A. AWS Global Accelerator ✅
- B. Amazon DataZone
- C. AWS Cloud Map
- D. AWS Auto Scaling

---

**36.** (Q688) A company wants to provide low latency to its users around the world. Which feature of the AWS Cloud meet this requirement?
- A. Global infrastructure ✅
- B. Pay as-you-go pricing
- C. Managed services
- D. Economy of scale

---

