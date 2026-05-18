# 📚 Amazon VPC — Virtual Private Cloud

> **Study Resources for this Topic:**
>
> - 📖 **Official AWS Docs:** [https://docs.aws.amazon.com/vpc/](https://docs.aws.amazon.com/vpc/)
> - 🎬 **YouTube Overview:** [https://www.youtube.com/watch?v=g2JOHLHh4rI](https://www.youtube.com/watch?v=g2JOHLHh4rI)
> - 🎓 **AWS Skill Builder (Free):** [AWS Cloud Practitioner Essentials](https://explore.skillbuilder.aws/learn/course/external/view/elearning/134/aws-cloud-practitioner-essentials)
>
> 💡 **Quick Tip:** Focus on: security groups vs Network ACLs, subnets, internet gateway, NAT gateway, VPC endpoints.

---

**1.** Question 889 Which AWS services make use of global edge locations? (Choose two.)
- A. AWS Fargate
- B. Amazon CloudFront ✅
- C. AWS Global Accelerator ✅
- D. AWS Wavelength
- E. Amazon VPC

---

**2.** Question 893 Which of the following acts as an instance-level firewall to control inbound and outbound access?
- A. Network access control list
- B. Security groups ✅
- C. AWS Trusted Advisor
- D. Virtual private gateways

---

**3.** Question 897 Which AWS tool or feature acts as a VPC firewall at the subnet level?
- A. Security group
- B. Network ACL ✅
- C. Traffic Mirroring
- D. Internet gateway

---

**4.** Question 904 Which AWS service or tool can be used to capture information about inbound and outbound traffic in an Amazon VPC?
- A. VPC Flow Logs ✅
- B. Amazon Inspector
- C. VPC endpoint services
- D. NAT gateway

---

**5.** Question 933 A large enterprise with multiple VPCs in several AWS Regions around the world needs to connect and centrally manage network connectivity between its VPCs. Which AWS service or feature meets these requirements?
- A. AWS Direct Connect
- B. AWS Transit Gateway ✅
- C. AWS Site-to-Site VPN
- D. VPC endpoints

---

**6.** Question 939 Which of the following are features of network ACLs as they are used in the AWS Cloud? (Choose two.)
- A. They are stateless. ✅
- B. They are stateful.
- C. They evaluate all rules before allowing traffic.
- D. They process rules in order, starting with the lowest numbered rule, when deciding whether to allow traffic. ✅
- E. They operate at the instance level.

---

**7.** Question 947 A company recently deployed an Amazon RDS instance in its VPC. The company needs to implement a stateful firewall to limit traffic to the private corporate network. Which AWS service or feature should the company use to limit network traffic directly to its RDS instance?
- A. Network ACLs
- B. Security groups ✅
- C. AWS WAF
- D. Amazon GuardDuty

---

**8.** Question 959 What is the scope of a VPC within the AWS network?
- A. A VPC can span all Availability Zones globally.
- B. A VPC must span at least two subnets in each AWS Region.
- C. A VPC must span at least two edge locations in each AWS Region.
- D. A VPC can span all Availability Zones within an AWS Region. ✅

---

**9.** Question 960 Which of the following are components of an AWS Site-to-Site VPN connection? (Choose two.)
- A. AWS Storage Gateway
- B. Virtual private gateway ✅
- C. NAT gateway
- D. Customer gateway ✅
- E. Internet gateway

---

**10.** Question 961 A company needs to establish a connection between two VPCs. The VPCs are located in two different AWS Regions. The company wants to use the existing infrastructure of the VPCs for this connection. Which AWS service or feature can be used to establish this connection?
- A. AWS Client VPN
- B. VPC peering ✅
- C. AWS Direct Connect
- D. VPC endpoints

---

**11.** Question 1275 Which of the following are features of network ACLs as they are used in the AWS Cloud? (Choose two.)
- A. They are stateless. ✅
- B. They are stateful.
- C. They evaluate all rules before allowing traffic.
- D. They process rules in order, starting with the lowest numbered rule, when deciding whether to allow traffic. ✅
- E. They operate at the instance level.

---

**12.** Question 1294 Which AWS service or feature gives users the ability to capture information about network traffic in a VPC?
- A. VPC Flow Logs ✅
- B. Amazon Inspector
- C. VPC route tables
- D. AWS CloudTrail

---

**13.** Question 1305 Which AWS services make use of global edge locations? (Choose two.)
- A. AWS Fargate
- B. Amazon CloudFront ✅
- C. AWS Global Accelerator ✅
- D. AWS Wavelength
- E. Amazon VPC

---

**14.** Question 1310 A company wants to establish a private network connection between AWS and its corporate network. Which AWS service or feature will meet this requirement?
- A. Amazon Connect
- B. Amazon Route 53
- C. AWS Direct Connect ✅
- D. VPC peering

---

**15.** Question 1311 Which AWS services or features give users the ability to create a network connection between two VPCs? (Choose two.)
- A. VPC endpoints
- B. Amazon Route 53
- C. VPC peering ✅
- D. AWS Direct Connect
- E. AWS Transit Gateway ✅

---

**16.** Question 1334 Which AWS service or component allows inbound traffic from the internet to access a VPC?
- A. Internet gateway ✅
- B. NAT gateway
- C. AWS WAF
- D. VPC peering

---

**17.** Question 417 Which AWS service or feature can a user configure to limit network access at the subnet level?
- A. AWS Shield
- B. AWS WAF
- C. Network ACL ✅
- D. Security group

---

**18.** Question 443 Which AWS service or feature gives users the ability to connect VPCs and on-premises networks to a central hub?
- A. Virtual private gateway
- B. AWS Transit Gateway ✅
- C. Internet gateway
- D. Customer gateway

---

**19.** Question 471 Which AWS service or feature requires an internet service provider (ISP) and a colocation facility to be implemented?
- A. AWS VPN
- B. Amazon Connect
- C. AWS Direct Connect ✅
- D. Internet gateway

---

**20.** Question 493 Which AWS tool or feature acts as a VPC firewall at the subnet level?
- A. Security group
- B. Network ACL ✅
- C. Traffic Mirroring
- D. Internet gateway

---

**21.** Question 516 Which component must be attached to a VPC to enable inbound internet access?
- A. NAT gateway
- B. VPC endpoint
- C. VPN connection
- D. Internet gateway ✅

---

**22.** Question 528 Which AWS service provides DNS resolution?
- A. Amazon CloudFront
- B. Amazon VPC
- C. Amazon Route 53 ✅
- D. AWS Direct Connect

---

**23.** Question 536 Which AWS service or feature provides a firewall at the subnet level within a VPC?
- A. Security group
- B. Network ACL ✅
- C. Elastic network interface
- D. AWS WAF

---

**24.** A company wants to securely connect its on-premises VPCs to AWS services without exposing internal traffic to the public internet. Which AWS service or resource will meet these requirements?

- A. Amazon Connect
- B. Amazon Inspector
- C. An internet gateway
- D. AWS PrivateLink ✅

**Explanation:** AWS PrivateLink provides private connectivity between VPCs, AWS services, and on-premises applications without exposing traffic to the public internet.

---

**25.** Which AWS service or feature provides information about governance, monitoring, and risk auditing of AWS accounts?

- A. AWS CloudTrail ✅
- B. VPC Flow Logs
- C. Amazon CloudWatch
- D. AWS Trusted Advisor

**Explanation:** AWS CloudTrail records all API calls and account activity, providing a complete audit trail for governance, compliance, and risk auditing across AWS accounts.

---

**26.** A company is running its application in the AWS Cloud and wants to protect against a DDoS attack with near real-time visibility. Which AWS service will meet these requirements with the MOST features for DDoS protection?

- A. AWS Shield Advanced ✅
- B. AWS Shield
- C. Amazon GuardDuty
- D. Network ACLs

---

**27.** Which AWS service allows companies to connect an Amazon VPC to an on-premises data center? (Select TWO)
- A. AWS VPN. ✅
- B. Amazon Redshift.
- C. API Gateway.
- D. Amazon Direct Connect. ✅
**Explanation:** AWS VPN creates an encrypted tunnel over the internet between your VPC and on-premises network. AWS Direct Connect provides a dedicated private network connection bypassing the internet entirely for more consistent performance.

---

**28.** Which AWS service identifies security groups that allow unrestricted access to a user's AWS resources?
- A. AWS Trusted Advisor. ✅
- B. Amazon Inspector.
- C. Amazon CloudWatch.
- D. AWS CloudTrail.
**Explanation:** AWS Trusted Advisor checks your security groups for rules that allow unrestricted access to specific ports and flags them as potential security risks.

---

**29.** Which AWS feature should a customer leverage to achieve high availability of an application?
- A. Snapshots
- B. Availability Zones. ✅
- C. Data centers.
- D. Amazon Virtual Private Cloud (Amazon VPC).
**Explanation:** Deploying your application across multiple Availability Zones ensures that if one AZ experiences a failure, your application continues running in the other AZs without interruption.

---

**30.** Which of the following features can be configured through the Amazon VPC Dashboard? (Select TWO)
- A. Elastic Load Balancing.
- B. Amazon Route 53.
- C. Subnets. ✅
- D. Security Groups. ✅
- E. Amazon CloudFront distributions.
**Explanation:** The VPC Dashboard lets you manage networking components like subnets, security groups, route tables, internet gateways, and NAT gateways. ELB, Route 53, and CloudFront are configured in their own dashboards.

---

**31.** Which component must be attached to a VPC to enable inbound Internet access?

- A. NAT gateway
- B. VPC endpoint
- C. VPN connection
- D. Internet gateway ✅

**Explanation:** An Internet Gateway is a horizontally scaled, redundant VPC component that allows communication between your VPC and the internet. It enables resources in public subnets to receive inbound connections from the internet.

---

**32.** Which AWS service or feature requires an internet service provider (ISP) and a colocation facility to be implemented?

- A. Internet gateway
- B. Amazon Connect
- C. AWS VPN
- D. AWS Direct Connect ✅

**Explanation:** AWS Direct Connect establishes a dedicated physical network connection between your premises and AWS. Setting it up requires working with an ISP and a Direct Connect location (colocation facility) to provision the physical circuit.

---

**33.** A company wants to track AWS resource configuration changes for compliance reasons. Which AWS feature can be used to meet this requirement?

- A. AWS Cost and Usage Report
- B. AWS Organizations service control policies (SCPs)
- C. AWS Config rules ✅
- D. VPC Flow Logs

**Explanation:** AWS Config rules continuously evaluate the configuration of your AWS resources against desired settings. They record configuration changes over time, making it easy to audit and demonstrate compliance with internal policies and regulatory standards.

---

**34.** Which AWS feature should a customer leverage to achieve high availability of an application?

- A. AWS Direct Connect
- B. Availability Zones ✅
- C. Data centers
- D. Amazon Virtual Private Cloud (Amazon VPC)

**Explanation:** Deploying applications across multiple Availability Zones ensures that if one AZ experiences an outage, the application continues to run in the other AZs, achieving high availability.

---

**35.** What are the multiple, isolated locations within an AWS Region that are connected by low-latency networks called?

- A. AWS Direct Connects
- B. Amazon VPCs
- C. Edge locations
- D. Availability Zones ✅

**Explanation:** Availability Zones (AZs) are physically separate data centers within an AWS Region, each with redundant power, networking, and connectivity, connected to each other via low-latency links.

---

**36.** A company wants to connect to AWS over a private, low-latency connection from its remote office. What is the recommended method to meet these requirements?

- A. Create a VPN tunnel
- B. Use VPC peering to create a connection.
- C. Connect across the public internet
- D. Use AWS Direct Connect. ✅

**Explanation:** AWS Direct Connect establishes a dedicated private physical network connection between your premises and AWS, bypassing the public internet entirely. This provides consistent, low-latency performance and greater bandwidth reliability.

---

**37.** Which AWS tool will identify security groups that grant unrestricted Internet access to a limited list of ports?

- A. AWS Organizations
- B. AWS Trusted Advisor ✅
- C. AWS Usage Report

**Explanation:** AWS Trusted Advisor includes security checks that identify security groups with rules allowing unrestricted access (0.0.0.0/0) to specific ports, helping you reduce your attack surface.

---

**38.** Which service would provide network connectivity in a hybrid architecture that includes the AWS Cloud?

- A. Amazon VPC
- B. AWS Direct Connect ✅
- C. AWS Directory Service

**Explanation:** AWS Direct Connect provides a dedicated private network connection between your on-premises environment and AWS, which is the core networking component needed to bridge a hybrid architecture between on-premises and cloud.

---

**39.** Which AWS service identifies security groups that allow unrestricted access to a user's AWS resources?

- A. AWS CloudTrail
- B. AWS Trusted Advisor ✅
- C. Amazon CloudWatch

**Explanation:** AWS Trusted Advisor includes security checks that detect security groups with inbound rules allowing unrestricted access (0.0.0.0/0) to sensitive ports, flagging them as potential security risks.

---

**40.** A company has developed an eCommerce web application in AWS. What should they do to ensure that the application has the highest level of availability?
- A. Deploy the application across multiple Availability Zones and Edge locations.
- B. Deploy the application across multiple Availability Zones and subnets.
- C. Deploy the application across multiple Regions and Availability Zones. ✅
- D. Deploy the application across multiple VPC’s and subnets.

---

**41.** How can you view the distribution of AWS spending in one of your AWS accounts?
- A. By using Amazon VPC console.
- B. By contacting the AWS Support team.
- C. By using AWS Cost Explorer. ✅
- D. By contacting the AWS Finance team.

---

**42.** Which of the following features can be configured through the Amazon Virtual Private Cloud (Amazon VPC) Dashboard? (Select TWO)
- A. Amazon CloudFront distributions.
- B. Amazon Route 53.
- C. Security Groups. ✅
- D. Subnets. ✅
- E. Elastic Load Balancing.

---

**43.** You are working on two projects that require completely different network configurations. Which AWS service or feature will allow you to isolate resources and network configurations?
- A. Internet gateways.
- B. Virtual Private Cloud. ✅
- C. Security Groups.
- D. Amazon CloudFront.

---

**44.** A company has business critical workloads hosted on AWS and they are unwilling to accept any downtime. Which of the following is a recommended best practice to protect their workloads in the event of an unexpected natural disaster?
- A. Replicate data across multiple Edge Locations worldwide and use Amazon CloudFront to perform automatic failover in the event of an outage.
- B. Deploy AWS resources across multiple Availability Zones within the same AWS Region.
- C. Create point-in-time backups in another subnet and recover this data when a disaster occurs.
- D. Deploy AWS resources to another AWS Region and implement an Active-Active disaster recovery strategy. ✅

---

**45.** What is the connectivity option that uses Internet Protocol Security (IPSec) to establish encrypted connectivity between an on-premises network and the AWS Cloud?
- A. Internet Gateway.
- B. AWS IQ.
- C. AWS Direct Connect.
- D. AWS Site-to-Site VPN. ✅

---

**46.** A company has hundreds of VPCs in multiple AWS Regions worldwide. What service does AWS offer to simplify the connection management among the VPCs?
- A. VPC Peering.
- B. AWS Transit Gateway. ✅
- C. Amazon Connect.
- D. Security Groups.

---

**47.** What is the main benefit of attaching security groups to an Amazon RDS instance?
- A. Manages user access and encryption keys.
- B. Controls what IP address ranges can connect to your database instance. ✅
- C. Deploys SSL/TLS certificates for use with your database instance.
- D. Distributes incoming traffic across multiple targets.

---

**48.** What does Amazon GuardDuty do to protect AWS accounts and workloads?
- A. Notifies AWS customers about abuse events once they are reported.
- B. Continuously monitors AWS infrastructure and helps detect threats such as attacker reconnaissance or account compromise. ✅
- C. Helps AWS customers identify the root cause of potential security issues.
- D. Checks security groups for rules that allow unrestricted access to AWS. resources.

---

**49.** Which AWS service or feature can be used to monitor CPU usage?
- A. AWS CloudTrail.
- B. VPC Flow Logs.
- C. Amazon CloudWatch. ✅
- D. AWS Config.

---

**50.** Which AWS service identifies security groups that allow unrestricted access to a user’s AWS resources?
- A. AWS Trusted Advisor. ✅
- B. Amazon Inspector.
- C. Amazon CloudWatch.
- D. AWS CloudTrail.

---

**51.** (Q1024) Which AWS service or tool can be used to set up a firewall to control traffic going into and coming out of an Amazon VPC subnet?
- A. Security group
- B. AWS WAF
- C. AWS Firewall Manager
- D. Network ACL ✅

---

**52.** (Q1027) Which AWS services make use of global edge locations? (Choose two.) a4
- A. AWS Fargate
- B. Amazon CloudFront ✅
- C. AWS Global Accelerator ✅
- D. AWS Wavelength
- E. Amazon VPC

---

**53.** (Q1034) Which AWS service or feature improves network performance by sending traffic through the AWS worldwide network infrastructure?
- A. Route table
- B. AWS Transit Gateway
- C. AWS Global Accelerator ✅
- D. Amazon VPC

---

**54.** (Q1046) A network engineer needs to build a hybrid cloud architecture connecting onpremises networks to the AWS Cloud using AWS Direct Connect. The company has a few VPCs in a single AWS Region and expects to increase the number of VPCs to hundreds over time. Which AWS service or feature should the engineer use to simplify and scale this connectivity as the VPCs increase in number?
- A. VPC endpoints
- B. AWS Transit Gateway ✅
- C. Amazon Route 53
- D. AWS Secrets Manager

---

**55.** (Q1051) A company wants to monitor for misconfigured security groups that are allowing unrestricted access to specific ports. Which AWS service will meet this requirement?
- A. AWS Trusted Advisor ✅
- B. Amazon CloudWatch
- C. Amazon GuardDuty
- D. AWS Health Dashboard

---

**56.** (Q1059) Which of the following services can be used to block network traffic to an instance? (Choose two.)
- A. Security groups ✅
- B. Amazon Virtual Private Cloud (Amazon VPC) flow logs
- C. Network ACLs ✅
- D. Amazon CloudWatch
- E. AWS CloudTrail

---

**57.** (Q1082) A company needs to block SQL injection attacks. Which AWS service or feature can meet this requirement?
- A. AWS WAF ✅
- B. AWS Shield
- C. Network ACLs
- D. Security groups

---

**58.** (Q1092) Which AWS service or feature allows a user to establish a dedicated network connection between a companys on-premises data center and the AWS Cloud?
- A. AWS Direct Connect ✅
- B. VPC peering
- C. AWS VPN
- D. Amazon Route 53

---

**59.** (Q1155) Which AWS services or features enable users to connect onpremises networks to a VPC? (Choose two.) . ne ]
- A. AWS VPN ✅
- B. Elastic Load Balancing
- C. AWS Direct Connect ✅
- D. VPC peering
- E. Amazon CloudFront

---

**60.** (Q1161) A company needs to centrally configure and manage Amazon VPC security groups across multiple AWS accounts within an organization in AWS Organizations. : Which AWS service should the company use to meet these requirements?
- A. AWS Firewall Manager ✅
- B. Amazon GuardDuty
- C. Amazon Detective
- D. AWS WAF

---

**61.** (Q1175) Which of the following acts as an instance-level firewall to control inbound and outbound access? h
- A. Network access control list
- B. Security groups ✅
- C. AWS Trusted Advisor
- D. Virtual private gateways

---

**62.** (Q1197) Which AWS service or tool can be used to capture information about inbound and outbound traffic in an Amazon VPC?
- A. VPC Flow Logs ✅
- B. Amazon Inspector
- C. VPC endpoint services
- D. NAT gateway

---

**63.** (Q436) Which statement is true about AWS global infrastructure?
- A. Availability Zones can span multiple AWS Regions.
- B. A VPC can have different subnets in different AWS Regions.
- C. AWS Regions consist of multiple Availability Zones. ✅
- D. A single subnet can span multiple Availability Zones.

**Explanation:** *(Add explanation here)*

---

**64.** (Q442) Which of the following services can be used to block network traffic to an instance? (Choose two.)
- A. Security groups ✅
- B. Amazon Virtual Private Cloud (Amazon VPC) flow logs
- C. Network ACLs ✅
- D. Amazon CloudWatch
- E. AWS CloudTrail

**Explanation:** *(Add explanation here)*

---

**65.** (Q456) A company wants to track AWS resource configuration changes for compliance reasons. Which AWS feature can be used to meet this requirement?
- A. AWS Cost and Usage Report
- B. AWS Organizations service control policies (SCPs)
- C. AWS Config rules ✅
- D. VPC Flow Logs

**Explanation:** *(Add explanation here)*

---

**66.** (Q464) A company wants to connect to AWS over a private, low-latency connection from its remote office. What is the recommended method to meet these requirements?
- A. Create a VPN tunnel
- B. Connect across the public internet
- C. Use VPC peering to create a connection.
- D. Use AWS Direct Connect. ✅

**Explanation:** *(Add explanation here)*

---

**67.** (Q472) Which AWS service or feature requires an internet service provider (ISP) and a colocation facility to be implemented?
- A. AWS VPN
- B. Amazon Connect
- C. AWS Direct Connect ✅
- D. Internet gateway

**Explanation:** *(Add explanation here)*

---

**68.** (Q477) Which of the following is the customer's responsibility when using Amazon RDS?
- A. Patching the operating system of underlying hardware
- B. Controlling traffic to and from the database through security groups ✅
- C. Running backups that enable point-in-time recovery of a DB Instance
- D. Replacing failed DB instances

**Explanation:** *(Add explanation here)*

---

**69.** (Q495) Which component must be attached to a VPC to enable inbound Internet access?
- A. NAT gateway
- B. VPC endpoint
- C. VPN connection
- D. Internet gateway ✅

**Explanation:** *(Add explanation here)*

---

**70.** (Q500) Which service provides a user the ability to warehouse data in the AWS Cloud?
- A. Amazon EFS
- B. Amazon Redshift ✅
- C. Amazon RDS
- D. Amazon VPC

**Explanation:** *(Add explanation here)*

---

**71.** (Q564) A user wants to transport data between AWS and an on-premises environment using a private network connection. Which AWS service or feature can be used to meet these requirements?
- A. NAT gateway
- B. AWS Direct Connect ✅
- C. Amazon VPC
- D. Internet gateway

**Explanation:** *(Add explanation here)*

---

**72.** (Q602) A company needs to block SQL injection attacks. Which AWS service or feature provides this functionality?
- A. AWS WAF ✅
- B. Network ACLs
- C. Security groups
- D. AWS Trusted Advisor

**Explanation:** *(Add explanation here)*

---

**73.** (Q611) Which AWS tool acts as a firewall to control traffic in and out of subnets within a VPC?
- A. Security group
- B. Route table
- C. VPC endpoint
- D. Network access control list (ACL) ✅

**Explanation:** *(Add explanation here)*

---

**74.** (Q638) A company uses a database that has a simple sign-up page to create users, and a basic login form to authenticate users so they can access the database. The company wants to give users the ability to store personal information, but user access must be controlled in a more secure and reliable way. Which AWS service or feature will meet these requirements?
- A. Security groups
- B. Amazon GuardDuty
- C. AWS Secrets Manager
- D. Amazon Cognito ✅

**Explanation:** *(Add explanation here)*

---

**75.** (Q574) A company with multiple accounts and teams wants to set up a new multi-account AWS environment. Which AWS service supports this requirement?
- A. AWS CloudFormation
- B. AWS Control Tower ✅
- C. AWS Config
- D. Amazon Virtual Private Cloud (Amazon VPC)

---

**76.** (Q581) Which AWS service or feature allows a company to have its own logically isolated section of the AWS Cloud? ,
- A. AWS VPN
- B. Availability Zones
- C. Amazon Virtual Private Cloud (Amazon VPC) ✅
- D. AWS Regions

---

**77.** (Q608) A company wants to set up a secure network connection from on premises to the AWS Cloud within | week. Which solution will meet these requirements?
- A. AWS Direct Connect
- B. Amazon VPC
- C. AWS Site-to-Site VPN ✅
- D. Edge location

---

**78.** (Q621) What is a benefit of using an Elastic Load Balancing (ELB) load balancer with applications running in the AWS Cloud?
- A. An ELB will automatically scale resources to meet capacity needs.
- B. An ELB can balance traffic across multiple compute resources. ✅
- C. An ELB can span multiple AWS Regions.
- D. An ELB can balance traffic between multiple internet gateways.

---

**79.** (Q630) Which AWS service can create a private network connection from on premises to the AWS Cloud?
- A. AWS Config
- B. Virtual Private Cloud (Amazon VPC)
- C. AWS Direct Connect ✅
- D. Amazon Route 53

---

**80.** (Q653) A company wants to use an AWS networking solution that can act as a centralized gateway between multiple VPCs and on-premises networks. Which AWS service or feature will meet this requirement?
- A. Gateway VPC endpoint
- B. AWS Direct Connect
- C. AWS Transit Gateway ✅
- D. AWS PrivateLink

---

**81.** (Q665) A company needs stateless network filtering for its VPC. Which AWS service, tool, or feature will meet this requirement?
- A. AWS PrivateLink
- B. Security group
- C. Network access control list (ACL) ✅
- D. AWS WAF

---

