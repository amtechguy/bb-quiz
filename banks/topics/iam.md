# 📚 AWS IAM — Identity and Access Management

> **Study Resources for this Topic:**
>
> - 📖 **Official AWS Docs:** [https://docs.aws.amazon.com/iam/](https://docs.aws.amazon.com/iam/)
> - 🎬 **YouTube Overview:** [https://www.youtube.com/watch?v=SXSqhTn2DuE](https://www.youtube.com/watch?v=SXSqhTn2DuE)
> - 🎓 **AWS Skill Builder (Free):** [AWS Cloud Practitioner Essentials](https://explore.skillbuilder.aws/learn/course/external/view/elearning/134/aws-cloud-practitioner-essentials)
>
> 💡 **Quick Tip:** Focus on: users, roles, groups, policies, MFA, least privilege principle, root user best practices.

---

**1.** Which AWS service provides a fully managed Jupyter notebook environment for data scientists to build ML models?
- A. Amazon SageMaker Studio ✅
- B. Amazon EMR
- C. AWS Glue
- D. Amazon Athena

---

**2.** A company wants to analyze the sentiment of social media posts about its brand in real time. Which AWS service should the company use?
- A. Amazon Rekognition
- B. Amazon Comprehend ✅
- C. Amazon Textract
- D. Amazon Translate

---

**3.** Which AWS service helps companies govern access to data in a data lake, including fine-grained permissions?
- A. AWS IAM
- B. AWS Lake Formation ✅
- C. AWS Config
- D. Amazon Macie

---

**4.** A company wants to make its data lake searchable and accessible to analysts using standard SQL. Which AWS service should the company use?
- A. Amazon QuickSight
- B. Amazon Athena ✅
- C. Amazon OpenSearch Service
- D. AWS Glue

---

**5.** A company wants to build machine learning-powered forecasts using historical time-series data without needing ML expertise. Which AWS service will meet this requirement?
- A. Amazon SageMaker
- B. Amazon Forecast ✅
- C. Amazon Comprehend
- D. Amazon Kinesis

---

**6.** Question 881 Which of the following is a characteristic of the AWS account root user?
- A. The root user is the only user that can be configured with multi-factor authentication (MFA).
- B. The root user is the only user that can access the AWS Management Console.
- C. The root user is the first sign-in identity that is available when an AWS account is created. ✅
- D. The root user has a password that cannot be changed.

---

**7.** Question 886 A pharmaceutical company operates its infrastructure in a single AWS Region. The company has thousands of VPCs in a various AWS accounts that it wants to interconnect. Which AWS service or feature should the company use to help simplify management and reduce operational costs?
- A. VPC endpoint
- B. AWS Direct Connect
- C. AWS Transit Gateway ✅
- D. VPC peering

---

**8.** Question 890 A company is operating several factories where it builds products. The company needs the ability to process data, store data, and run applications with local system interdependencies that require low latency. Which AWS service should the company use to meet these requirements?
- A. AWS IoT Greengrass
- B. AWS Lambda
- C. AWS Outposts ✅
- D. AWS Snowball Edge

---

**9.** Question 900 Which AWS service supports a hybrid architecture that gives users the ability to extend AWS infrastructure, AWS services, APIs, and tools to data centers, co-location environments, or on-premises facilities?
- A. AWS Snowmobile
- B. AWS Local Zones
- C. AWS Outposts ✅
- D. AWS Fargate

---

**10.** Question 921 A manufacturing company has a critical application that runs at a remote site that has a slow internet connection. The company wants to migrate the workload to AWS. The application is sensitive to latency and interruptions in connectivity. The company wants a solution that can host this application with minimum latency. Which AWS service or feature should the company use to meet these requirements?
- A. Availability Zones
- B. AWS Local Zones
- C. AWS Wavelength
- D. AWS Outposts ✅

---

**11.** Question 925 Which AWS service uses edge locations?
- A. Amazon Aurora
- B. AWS Global Accelerator ✅
- C. Amazon Connect
- D. AWS Outposts

---

**12.** Question 927 Which AWS service or feature checks access policies and offers actionable recommendations to help users set secure and functional policies?
- A. AWS Systems Manager
- B. AWS IAM Access Analyzer ✅
- C. AWS Trusted Advisor
- D. Amazon GuardDuty

---

**13.** Question 942 A company needs to graphically visualize AWS billing and usage over time. The company also needs information about its AWS monthly costs. Which AWS Billing and Cost Management tool provides this data in a graphical format?
- A. AWS Bills
- B. Cost Explorer ✅
- C. AWS Cost and Usage Report
- D. AWS Budgets

---

**14.** Question 951 A global media company uses AWS Organizations to manage multiple AWS accounts. Which AWS service or feature can the company use to limit the access to AWS services for member accounts?
- A. AWS Identity and Access Management (IAM)
- B. Service control policies (SCPs) ✅
- C. Organizational units (OUs)
- D. Access control lists (ACLs)

---

**15.** Question 967 How does the AWS Cloud pricing model differ from the traditional on-premises storage pricing model?
- A. AWS resources do not incur costs
- B. There are no infrastructure operating costs
- C. There are no upfront cost commitments ✅
- D. There are no software licensing costs

---

**16.** Question 983 Which component of the AWS global infrastructure is made up of one or more discrete data centers that have redundant power, networking, and connectivity?
- A. AWS Region
- B. Availability Zone ✅
- C. Edge location
- D. AWS Outposts

---

**17.** Question 1208 Which option is an environment that consists of one or more data centers?
- A. Amazon CloudFront
- B. Availability Zone ✅
- C. VPC
- D. AWS Outposts

---

**18.** Question 1213 Which action will help increase security in the AWS Cloud?
- A. Enable programmatic access for all IAM users.
- B. Use IAM users instead of IAM roles to delegate permissions.
- C. Rotate access keys on a reoccurring basis. ✅
- D. Use inline policies instead of customer managed policies.

---

**19.** Question 1220 A company needs to organize its resources and track AWS costs on a detailed level. The company needs to categorize costs by business department, environment, and application. Which solution will meet these requirements?
- A. Access the AWS Cost Management console to organize resources, set an AWS budget, and receive
- B. Use tags to organize the resources. Activate cost allocation tags to track AWS costs on a detailed level. ✅
- C. Create Amazon CloudWatch dashboards to visually organize and track costs individually.
- D. Access the AWS Billing and Cost Management dashboard to organize and track resource consumption on a

---

**20.** Question 1222 A company wants a customized assessment of its current on-premises environment. The company wants to understand its projected running costs in the AWS Cloud. Which AWS service or tool will meet these requirements?
- A. AWS Trusted Advisor
- B. Amazon Inspector
- C. AWS Control Tower
- D. Migration Evaluator ✅

---

**21.** Question 1224 A company hosts a large amount of data in AWS. The company wants to identify if any of the data should be considered sensitive. Which AWS service will meet the requirement?
- A. Amazon Inspector
- B. Amazon Macie ✅
- C. AWS Identity and Access Management (IAM)
- D. Amazon CloudWatch

---

**22.** Question 1233 A company wants to integrate its online shopping website with social media login credentials. Which AWS service can the company use to make this integration?
- A. AWS Directory Service
- B. AWS Identity and Access Management (IAM)
- C. Amazon Cognito ✅
- D. AWS IAM Identity Center (AWS Single Sign-On)

---

**23.** Question 1264 A developer wants AWS users to access AWS services by using temporary security credentials. Which AWS service or feature should the developer use to provide these credentials?
- A. IAM policies
- B. IAM user groups
- C. AWS Security Token Service (AWS STS) ✅
- D. AWS IAM Identity Center (AWS Single Sign-On)

---

**24.** Question 1267 A company wants to verify if multi-factor authentication (MFA) is enabled for all users within its AWS accounts. Which AWS service or resource will meet this requirement?
- A. AWS Cost and Usage Report
- B. IAM credential reports ✅
- C. AWS Artifact
- D. Amazon CloudFront reports

---

**25.** Question 1272 An external auditor has requested that a company provide a list of all its IAM users, including the status of users' credentials and access keys. What is the SIMPLEST way to provide this information?
- A. Create an IAM user account for the auditor, granting the auditor administrator permissions.
- B. Take a screenshot of each user's page in the AWS Management Console, then provide the screenshots to the
- C. Download the IAM credential report, then provide the report to the auditor. ✅
- D. Download the AWS Trusted Advisor report, then provide the report to the auditor.

---

**26.** Question 1280 A company has a managed IAM policy that does not grant the necessary permissions for users to accomplish required tasks. How can this be resolved?
- A. Enable AWS Shield Advanced.
- B. Create a custom IAM policy. ✅
- C. Use a third-party web application firewall (WAF) managed rule from the AWS Marketplace.
- D. Use AWS Key Management Service (AWS KMS) to create a customer-managed key.

---

**27.** Question 1291 Which AWS Cloud deployment model uses AWS Outposts as part of the application deployment infrastructure?
- A. On-premises
- B. Serverless
- C. Cloud-native
- D. Hybrid ✅

---

**28.** Question 1320 A company wants to generate a list of IAM users. The company also wants to view the status of various credentials that are associated with the users, such as password, access keys, and multi-factor authentication (MFA) devices. Which AWS service or feature will meet these requirements?
- A. IAM credential report ✅
- B. AWS IAM Identity Center (AWS Single Sign-On)
- C. AWS Identity and Access Management Access Analyzer
- D. AWS Cost and Usage Report

---

**29.** Question 1326 A company is migrating its applications from on-premises to the AWS Cloud. The company wants to ensure that the applications are assigned only the minimum permissions that are needed to perform all operations. Which AWS service will meet these requirements?
- A. AWS Identity and Access Management (IAM) ✅
- B. Amazon CloudWatch
- C. Amazon Macie
- D. Amazon GuardDuty

---

**30.** Question 1335 Which AWS service can companies use to create infrastructure from code?
- A. Amazon Elastic Kubernetes Service (Amazon EKS)
- B. AWS Outposts
- C. AWS CodePipeline
- D. AWS CloudFormation ✅

---

**31.** Question 1341 A company wants to deploy some of its resources in the AWS Cloud. To meet regulatory requirements, the data must remain local and on premises. There must be low latency between AWS and the company resources. Which AWS service or feature can be used to meet these requirements?
- A. AWS Local Zones
- B. Availability Zones
- C. AWS Outposts ✅
- D. AWS Wavelength Zones

---

**32.** Question 1362 Which of the following is a characteristic of the AWS account root user?
- A. The root user is the only user that can be configured with multi-factor authentication (MFA).
- B. The root user is the only user that can access the AWS Management Console.
- C. The root user is the first sign-in identity that is available when an AWS account is created. ✅
- D. The root user has a password that cannot be changed.

---

**33.** Question 409 Which task is the responsibility of a company that is using Amazon RDS?
- A. Provision the underlying infrastructure.
- B. Create IAM policies to control administrative access to the service. ✅
- C. Install the cables to connect the hardware for compute and storage.
- D. Install and patch the RDS operating system.

---

**34.** Question 410 Which of the following is an advantage that the AWS Cloud provides to users?
- A. Users eliminate the need to guess about infrastructure capacity requirements. ✅
- B. Users decrease their variable costs by maintaining sole ownership of IT hardware.
- C. Users maintain control of underlying IT infrastructure hardware.
- D. Users maintain control of operating systems for managed services.

---

**35.** Question 412 A company needs to check for IAM access keys that have not been rotated recently. Which AWS service should the company use to meet this requirement?
- A. AWS WAF
- B. AWS Shield
- C. Amazon Cognito
- D. AWS Trusted Advisor ✅

---

**36.** Question 428 A company wants to provide one of its employees with access to Amazon RDS. The company also wants to limit the interaction to only the AWS CLI and AWS software development kits (SDKs). Which combination of actions should the company take to meet these requirements while following the principles of least privilege? (Choose two.)
- A. Create an IAM user and provide AWS Management Console access only.
- B. Create an IAM user and provide programmatic access only.
- C. Create an IAM role and provide AWS Management Console access only.
- D. Create an IAM policy with administrator access and attach it to the IAM user. ✅
- E. Create an IAM policy with Amazon RDS access and attach it to the IAM user. ✅

---

**37.** Question 433 A company wants to organize its users so that the company can grant permissions to the users as a group. Which AWS service or tool can the company use to meet this requirement?
- A. Security groups
- B. AWS Identity and Access Management (IAM)
- C. Resource groups ✅
- D. AWS Security Hub

---

**38.** Question 447 Which action should a company take to improve security in its AWS account?
- A. Require multi-factor authentication (MFA) for privileged users. ✅
- B. Remove the root user account.
- C. Create an access key for the AWS account root user.
- D. Create an access key for each privileged user.

---

**39.** Question 448 Which of the following are ways to improve security on AWS? (Choose two.)
- A. Using AWS Artifact
- B. Granting the broadest permissions to all IAM roles
- C. Running application code with AWS Cloud
- D. Enabling multi-factor authentication (MFA) with Amazon Cognito ✅
- E. Using AWS Trusted Advisor security checks ✅

---

**40.** Question 459 A company wants to use AWS. The company has stringent requirements about low-latency access to on-premises systems and data residency. Which AWS service should the company use to design a solution that meets these requirements?
- A. AWS Wavelength
- B. AWS Transit Gateway
- C. AWS Ground Station
- D. AWS Outposts ✅

---

**41.** Question 460 A company runs an on-premises contact center for customers. The company needs to migrate to a cloud-based solution that can deliver artificial intelligence features to improve user experience. Which AWS service will meet these requirements?
- A. AWS Wavelength
- B. AWS IAM Identity Center (AWS Single Sign-On)
- C. AWS Direct Connect
- D. Amazon Connect ✅

---

**42.** Question 468 A company wants to monitor and block malicious HTTP and HTTPS requests that its Amazon CloudFront distributions receive. Which AWS service should the company use to meet these requirements?
- A. Amazon GuardDuty
- B. Amazon Inspector
- C. AWS WAF ✅
- D. Amazon Detective

---

**43.** Question 474 A company needs to manage multiple logins across AWS accounts within the same organization in AWS Organizations. Which AWS service should the company use to meet this requirement?
- A. Amazon VPC
- B. Amazon GuardDuty
- C. Amazon Cognito
- D. AWS IAM Identity Center ✅

---

**44.** Question 477 A company uses a third-party identity provider (IdP). The company wants to provide its employees with access to AWS accounts and services without requiring another set of login credentials. Which AWS service will meet this requirement?
- A. AWS Directory Service
- B. Amazon Cognito ✅
- C. AWS IAM Identity Center
- D. AWS Resource Access Manager (AWS RAM)

---

**45.** Question 501 A company wants to implement detailed tracking of its cloud costs by department and project. Which AWS feature or service should the company use?
- A. Consolidated billing
- B. Cost allocation tags ✅
- C. AWS Marketplace
- D. AWS Budgets

---

**46.** Question 504 Which AWS service or feature supports governance, compliance, and risk auditing of AWS accounts?
- A. Multi-factor authentication (MFA)
- B. AWS Lambda
- C. Amazon Simple Notification Service (Amazon SNS)
- D. AWS CloudTrail ✅

---

**47.** Question 510 Which benefit of the AWS Cloud helps companies achieve lower usage costs because of the aggregate usage of all AWS users?
- A. No need to guess capacity
- B. Ability to go global in minutes
- C. Economies of scale ✅
- D. Increased speed and agility

---

**48.** Question 532 Which of the following can the AWS Pricing Calculator do?
- A. Project monthly AWS costs. ✅
- B. Calculate historical AWS costs.
- C. Provide in-depth information about AWS pricing strategies.
- D. Provide users with access to their monthly bills.

---

**49.** Question 534 A user has been granted permission to change their own IAM user password. Which AWS services can the user use to change the password? (Choose two.)
- A. AWS Command Line Interface (AWS CLI) ✅
- B. AWS Key Management Service (AWS KMS)
- C. AWS Management Console ✅
- D. AWS Resource Access Manager (AWS RAM)
- E. AWS Secrets Manager

---

**50.** Question 539 Which guidelines are best practices for using AWS Identity and Access Management (IAM)? (Choose two.)
- A. Share access keys.
- B. Create individual IAM users. ✅
- C. Use inline policies instead of customer managed policies.
- D. Grant maximum privileges to IAM users.
- E. Use groups to assign permissions to IAM users. ✅

---

**51.** Question 549 A company's employees are working from home. The company wants its employees to use their personal devices to connect to a managed workstation in the AWS Cloud. Which AWS service should the company use to provide the remote environment?
- A. Amazon WorkSpaces ✅
- B. AWS Cloud9
- C. AWS Outposts
- D. Amazon Lightsail

---

**52.** Which component of the AWS global infrastructure does Amazon CloudFront use to speed up the delivery of content to users across the world?

- A. Amazon VPC
- B. Edge location ✅
- C. Local Zone
- D. AWS Outposts connection

**Explanation:** Amazon CloudFront uses a global network of edge locations to cache and deliver content closer to end users, reducing latency.

---

**53.** A large company wants to track the combined AWS usage costs of all of its linked accounts. How can this be accomplished?

- A. Use AWS Trusted Advisor to generate customized summary reports.
- B. Use AWS Organizations to generate consolidated billing reports ✅
- C. Use AWS Budgets to set utilization targets and receive summary reports
- D. Use the AWS Control Tower dashboard to get a summary report of all linked account costs.

**Explanation:** AWS Organizations consolidated billing combines all member account charges into a single bill paid by the management account, giving visibility into total spending across all linked accounts.

---

**54.** A company wants to migrate its infrastructure to the AWS Cloud. The company needs to collect data for server configuration, utilization, and annual operating costs. Which AWS service will meet these requirements?

- A. AWS Compute Optimizer
- B. AWS Cost Explorer
- C. Migration Evaluator ✅
- D. AWS Pricing Calculator

**Explanation:** Migration Evaluator (formerly TSO Logic) collects on-premises infrastructure data including server configuration, utilization, and costs to provide a business case and projected savings for AWS migration.

---

**55.** A company has deployed its application on AWS. The company wants to create financial reports for current and historical spending and forecast AWS service usage for the next year. Which AWS service or tool can the company use?

- A. AWS Trusted Advisor
- B. AWS Cost Explorer ✅
- C. AWS CloudTrail
- D. AWS Budgets

**Explanation:** AWS Cost Explorer provides interactive reports and graphs for current and historical AWS spending, and includes forecasting capabilities to predict future usage and costs.

---

**56.** Which AWS services or tools can a company use to track its AWS costs? (Choose two.)

- A. AWS X-Ray
- B. AWS Cost and Usage Report ✅
- C. AWS CloudTrail
- D. Cost Explorer ✅
- E. AWS Pricing Calculator

**Explanation:** AWS Cost and Usage Report provides the most detailed billing data available. AWS Cost Explorer provides interactive charts and analysis of historical and forecasted costs. Both are core cost tracking tools.

---

**57.** A company needs to quickly deploy an application to the AWS Cloud. The company wants to upload code to automatically create the application infrastructure. Which AWS service will meet these requirements?

- A. AWS AppSync
- B. AWS Config
- C. AWS Elastic Beanstalk ✅
- D. AWS Outposts

---

**58.** A newly created IAM user has no IAM policy attached. What will happen when the user logs in and attempts to view the AWS resources in the account?

- A. All AWS services will be read-only access by default.
- B. Access to all AWS resources will be denied. ✅
- C. Access to the AWS billing services will be allowed.
- D. Access to AWS resources will be allowed through the AWS CLI

---

**59.** A company needs to ensure that users around the world can access the company's application with low latency. Which advantage of the AWS Cloud will meet this requirement?

- A. Avoid data center costs
- B. Global infrastructure ✅
- C. Larger application leads to cost savings
- D. Pay-as-you-go pricing

---

**60.** A company is developing a new web application. The company must give users the ability to log in to the application through social identity providers. Which AWS service will meet these requirements?

- A. AWS Directory Service
- B. Amazon Cognito ✅
- C. AWS Identity and Access Management (IAM)
- D. AWS IAM Identity Center

---

**61.** Which AWS service is used to pay AWS bills, and monitor usage and budget costs?
- A. AWS Billing and Cost Management. ✅
- B. Consolidated billing.
- C. Amazon CloudWatch.
- D. Amazon QuickSight.
**Explanation:** AWS Billing and Cost Management provides tools to pay your bills, monitor usage, and create budgets with alerts so you stay on top of your AWS spending.

---

**62.** Which AWS service or feature can enhance network security by blocking requests from a particular network for a web application? (Select TWO)
- A. AWS WAF. ✅
- B. AWS Trusted Advisor.
- C. AWS Direct Connect.
- D. AWS Organizations.
- E. Network ACLs. ✅
**Explanation:** AWS WAF lets you create rules to block requests from specific IP ranges at the application layer. Network ACLs act as a stateless firewall at the subnet level to block traffic from specific networks.

---

**63.** The financial benefits of using AWS are: (Select TWO)
- A. Reduced Total Cost of Ownership (TCO). ✅
- B. Increased capital expenditure (capex).
- C. Reduced operational expenditure (opex). ✅
- D. Deferred payment plans for startups.
- E. Business credit lines for startups.
**Explanation:** AWS reduces TCO by eliminating upfront hardware costs and reduces opex by replacing fixed infrastructure costs with variable pay-as-you-go pricing.

---

**64.** What are the benefits of using the AWS Cloud for companies with customers in many countries? (Select TWO)
- A. Companies can deploy applications in multiple AWS Regions to reduce latency. ✅
- B. Amazon Translate automatically translates third-party website interfaces into multiple languages.
- C. Amazon CloudFront has multiple edge locations around the world to reduce latency. ✅
- D. Amazon Comprehend allows users to build applications that can respond to user requests in many languages.
- E. Elastic Load Balancing can distribute application web traffic to multiple AWS Regions around the world.
**Explanation:** Multiple AWS Regions allow you to deploy applications close to your global users. CloudFront's edge locations cache content worldwide, reducing latency for users regardless of their location.

---

**65.** Which of the following are main components of the AWS global infrastructure? (Select TWO)
- A. Resource groups.
- B. Points-of-presence ✅
- C. Security groups.
- D. Regions. ✅
- E. Datacenters.
**Explanation:** AWS global infrastructure consists of Regions, Availability Zones, and Points of Presence (edge locations). Regions are geographic areas and PoPs are used by CloudFront and Route 53 to deliver content with low latency.

---

**66.** What costs are included when comparing AWS TCO with on-premises TCO?
- A. Project management.
- B. Antivirus software licensing.
- C. Data center security. ✅
- D. Software development.
**Explanation:** On-premises TCO includes data center costs such as physical security, power, cooling, and hardware maintenance. These costs disappear when moving to AWS, making it a key comparison point.

---

**67.** How would an AWS customer easily apply common access controls to a large set of users?
- A. Apply an IAM policy to an IAM group. ✅
- B. Apply an IAM policy to an IAM role.
- C. Apply the same IAM policy to all IAM users with access to the same workload.
- D. Apply an IAM policy to an Amazon Cognito user pool.
**Explanation:** IAM groups let you attach a single policy to multiple users at once. Any user added to the group automatically inherits the group's permissions, making access management much easier at scale.

---

**68.** How can a company reduce its Total Cost of Ownership (TCO) using AWS?
- A. By having no operational expenditures.
- B. By having no responsibility for third-party license costs.
- C. By minimizing large capital expenditures. ✅
- D. By having AWS manage applications.
**Explanation:** AWS reduces TCO primarily by eliminating large upfront capital expenditures on hardware. Instead of buying servers, you pay only for what you use, converting capex to opex.

---

**69.** Which of the following will enhance the security of access to the AWS Management Console? (Select TWO)
- A. Security groups.
- B. AWS Certificate Manager.
- C. AWS Secrets Manager.
- D. Password policies. ✅
- E. AWS Multi-Factor Authentication (AWS MFA). ✅
**Explanation:** Strong password policies ensure users create complex passwords that are hard to guess. MFA adds a second layer of verification beyond just a password, significantly reducing the risk of unauthorized access.

---

**70.** Which of the following common IT tasks can AWS cover to free up company IT resources? (Select TWO)
- A. Patching databases software. ✅
- B. Backing up databases. ✅
- C. Creating database schema.
- D. Testing application releases.
- E. Running penetration tests.
**Explanation:** AWS managed database services like RDS handle patching and backups automatically. Schema design and application testing remain the customer's responsibility as they are application-level concerns.

---

**71.** Which IAM entity is associated with an access key ID and secret access key when using AWS CLI?
- A. IAM user. ✅
- B. IAM group.
- C. IAM policy.
- D. IAM role.
**Explanation:** Access keys consist of an access key ID and secret access key and are associated with IAM users for programmatic access via the CLI or API. Roles use temporary credentials and groups cannot have access keys.

---

**72.** What credential components are required to gain programmatic access to an AWS account? (Select TWO)
- A. A user ID.
- B. A secret access key. ✅
- C. A secondary key.
- D. An access key ID. ✅
- E. A primary key.
**Explanation:** Programmatic access to AWS requires both an access key ID which identifies the user and a secret access key which acts as the password. Together they authenticate API and CLI requests.

---

**73.** Which of the following security measures protect access to an AWS account? (Select TWO)
- A. Grant least privilege access to IAM users. ✅
- B. Create one IAM user and share with many developers and users.
- C. Enable Amazon CloudFront.
- D. Enable AWS CloudTrail.
- E. Activate multi-factor authentication (MFA) for privileged users. ✅
**Explanation:** Least privilege ensures users only have the permissions they need, limiting damage if credentials are compromised. MFA adds a second authentication factor making unauthorized access much harder even if a password is stolen.

---

**74.** What can AWS edge locations be used for? (Select TWO)
- A. Delivering content closer to users. ✅
- B. Reducing traffic on the server by caching responses. ✅
- C. Hosting applications.
- D. Running NoSQL database caching services.
- E. Sending notification messages to end users.
**Explanation:** AWS edge locations are used by CloudFront to cache content close to end users for low-latency delivery. Caching at the edge reduces the number of requests that need to go back to the origin server.

---

**75.** A customer is deploying a new application and needs to choose an AWS Region. Which factors could influence the decision? (Select TWO)
- A. Reduced latency to users. ✅
- B. Cooling costs in hotter climates.
- C. Proximity to the customer's office for on-site visits.
- D. Data sovereignty compliance. ✅
- E. The application's presentation in the local language.
**Explanation:** Choosing a Region close to your users reduces latency. Data sovereignty laws may require data to stay within certain geographic boundaries. Cooling costs and office proximity are not relevant AWS Region selection factors.

---

**76.** Which service's PRIMARY purpose is software version control?
- A. AWS Code Artifact.
- B. Amazon CodeStar.
- C. Amazon Cognito.
- D. AWS CodeCommit. ✅
**Explanation:** AWS CodeCommit is a fully managed source control service that hosts secure Git repositories, making it the primary AWS service for software version control.

---

**77.** How can a customer increase security to AWS account logins? (Select TWO)
- A. Use Session Manager
- B. Enable AWS Organizations
- C. Enable Multi-Factor Authentication (MFA) ✅
- D. Configure a strong password policy ✅
- E. Use Amazon Cognito to manage access
- F. Configure AWS Certificate Manager
**Explanation:** MFA requires a second form of verification beyond a password, making unauthorized access much harder. Strong password policies enforce complexity and rotation requirements to reduce the risk of password-based attacks.

---

**78.** A global company with a large number of AWS accounts is seeking a way in which they can centrally manage billing and security policies across all accounts. Which AWS Service will assist them in meeting these goals?

- A. AWS Trusted Advisor.
- B. IAM User Groups.
- C. AWS Config.
- D. AWS Organizations ✅

**Explanation:** AWS Organizations allows you to centrally manage multiple AWS accounts, consolidate billing, and apply Service Control Policies (SCPs) to enforce security and compliance across all accounts.

---

**79.** A company is concerned that they are spending money on underutilized compute resources in AWS. Which AWS feature will help ensure that their applications are automatically adding/removing EC2 compute capacity to closely match the required demand?

- A. AWS Budgets.
- B. AWS Auto Scaling. ✅
- C. AWS Cost Explorer.
- D. Elastic Load Balancer

**Explanation:** AWS Auto Scaling monitors your applications and automatically adjusts EC2 capacity to maintain steady, predictable performance at the lowest possible cost.

---

**80.** What is the AWS feature that provides an additional level of security above the default authentication mechanism of usernames and passwords?

- A. Email verification.
- B. AWS KMS.
- C. AWS MFA. ✅
- D. CloudHSM

**Explanation:** AWS Multi-Factor Authentication (MFA) adds an extra layer of protection on top of your username and password by requiring a second form of authentication, such as a one-time code from a hardware or virtual device.

---

**81.** The principle "design for failure and nothing will fail" is very important when designing your AWS Cloud architecture. Which of the following would help adhere to this principle? (Choose TWO)

- A. Availability Zones. ✅
- B. Elastic Load Balancing. ✅
- C. Penetration testing.
- D. Vertical Scaling.
- E. Multi-factor authentication.

**Explanation:** Deploying across multiple Availability Zones eliminates single points of failure at the infrastructure level. Elastic Load Balancing distributes traffic across healthy instances, automatically routing around failures.

---

**82.** Which of the following is equivalent to a user name and password and is used to authenticate your programmatic access to AWS services and APIs?

- A. Key pairs.
- B. Access Keys. ✅
- C. MFA.
- D. Instance Password.
- E. Encryption Keys

**Explanation:** AWS Access Keys consist of an Access Key ID and a Secret Access Key. They are used to authenticate programmatic requests to AWS APIs via the CLI, SDKs, and direct API calls.

---

**83.** Which of the following is one of the benefits of moving infrastructure from an on-premises data center to AWS?

- A. Automatic data protection.
- B. Reduced Capital Expenditure (CapEx). ✅
- C. AWS holds responsibility for managing customer applications.
- D. Free support for all enterprise customers.

**Explanation:** Moving to AWS shifts spending from capital expenditure (buying hardware) to operational expenditure (paying for what you use). This eliminates large upfront investments and allows you to scale costs with your business.

---

**84.** What tool enables customers without an AWS account to estimate costs for almost all AWS services?

- A. Cost Explorer
- B. TCO Calculator
- C. AWS Budgets
- D. AWS Pricing Calculator ✅

**Explanation:** The AWS Pricing Calculator is a free web-based tool that lets anyone — including those without an AWS account — estimate the cost of AWS services for their specific use case and architecture.

---

**85.** A company wants to ensure that AWS Management Console users are meeting password complexity requirements. How can the company configure password complexity?

- A. Using an AWS IAM user policy
- B. Using an AWS Organizations service control policy (SCP)
- C. Using an AWS IAM account password policy ✅
- D. Using an AWS Security Hub managed insight

**Explanation:** IAM account password policies allow administrators to enforce password requirements for all IAM users, including minimum length, character types, expiration, and reuse restrictions.

---

**86.** Which tool can be used to create alerts when the actual or forecasted cost of AWS services exceeds a certain threshold?

- A. Cost Explorer
- B. AWS Budgets ✅
- C. AWS Cost and Usage Report
- D. AWS CloudTrail

**Explanation:** AWS Budgets allows you to set custom cost and usage budgets and receive alerts via email or SNS when your actual or forecasted costs exceed your defined thresholds.

---

**87.** A company wants to provide one of its employees with access to Amazon RDS. The company also wants to limit the interaction to only the AWS CLI and AWS software development kits (SDKs). Which combination of actions should the company take to meet these requirements while following the principles of least privilege? (Choose two.)

- A. Create an IAM user and provide AWS Management Console access only.
- B. Create an IAM user and provide programmatic access only. ✅
- C. Create an IAM role and provide AWS Management Console access only.
- D. Create an IAM policy with administrator access and attach it to the IAM user.
- E. Create an IAM policy with Amazon RDS access and attach it to the IAM user. ✅

**Explanation:** Programmatic access (access keys) enables CLI and SDK access without Console access. Attaching a policy with only RDS permissions follows least privilege by granting only the minimum permissions required.

---

**88.** A company wants to be notified when its AWS Cloud costs or usage exceed defined thresholds. Which AWS service will support these requirements?

- A. Amazon Macie
- B. Cost Explorer
- C. AWS Budgets ✅
- D. AWS CloudTrail

**Explanation:** AWS Budgets lets you set custom budgets and configure alerts to be sent via email or Amazon SNS when your actual or forecasted costs and usage exceed your defined thresholds.

---

**89.** Which AWS service can be used to privately store and manage versions of source code?

- A. AWS CodeCommit ✅
- B. AWS CodeStar
- C. AWS CodeBuild
- D. AWS CodePipeline

**Explanation:** AWS CodeCommit is a fully managed, private source control service that hosts secure Git repositories, allowing teams to store and version control code without needing to manage their own source control infrastructure.

---

**90.** Which of the following common IT tasks can AWS cover to free up company IT resources? (Select TWO.)

- A. Patching databases software ✅
- B. Testing application releases
- C. Backing up databases ✅
- D. Creating database schema
- E. Running penetration tests

**Explanation:** With managed services like Amazon RDS, AWS handles database patching and automated backups, freeing customer IT teams to focus on higher-value work like schema design and application development.

---

**91.** How does AWS shorten the time to provision IT resources?

- A. It supplies an online IT ticketing platform for resource requests.
- B. It supports automatic code validation services.
- C. It provides the ability to programmatically provision existing resources. ✅
- D. It automates the resource request process from a company's IT vendor list.

**Explanation:** AWS APIs, SDKs, and tools like CloudFormation and the CLI allow resources to be provisioned programmatically in minutes, eliminating the weeks or months required to procure and set up on-premises hardware.

---

**92.** The financial benefits of using AWS are: (Select TWO.)

- A. Reduced Total Cost of Ownership (TCO). ✅
- B. Increased capital expenditure (capex).
- C. Reduced operational expenditure (opex). ✅
- D. Deferred payment plans for startups.
- E. Business credit lines for startups.

**Explanation:** Moving to AWS reduces TCO by eliminating the need to purchase and maintain hardware. It also reduces operational costs through automation, managed services, and economies of scale.

---

**93.** A company will be moving from an on-premises data center to the AWS Cloud. What would be one financial difference after the move?

- A. Moving from variable operational expense (opex) to upfront capital expense (capex).
- B. Moving from upfront capital expense (capex) to variable capital expense (capex).
- C. Moving from upfront capital expense (capex) to variable operational expense (opex). ✅
- D. Elimination of upfront capital expense (capex) and elimination of variable operational expense (opex)

**Explanation:** On-premises requires large upfront capital investment in hardware. AWS shifts this to a variable operational expense model where you pay only for what you use, with no upfront hardware costs.

---

**94.** How should a customer quickly forecast the future costs for running a new web application?

- A. Amazon Aurora Backtrack
- B. Amazon CloudWatch Billing Alarms
- C. AWS Simple Monthly Calculator ✅
- D. AWS Cost and Usage report

**Explanation:** The AWS Simple Monthly Calculator (now the AWS Pricing Calculator) allows customers to estimate the monthly cost of AWS services for a planned architecture before deploying anything.

---

**95.** Which AWS IAM feature is used to associate a set of permissions with multiple users?

- A. Multi-factor authentication
- B. Groups ✅
- C. Password policies
- D. Access keys

**Explanation:** IAM Groups allow you to attach IAM policies to a collection of users. All users in the group inherit those permissions, making it easy to manage access for teams without setting permissions individually.

---

**96.** Which of the following can a customer use to enable single sign-on (SSO) to the AWS Console?

- A. Amazon Connect
- B. AWS Directory Service ✅
- C. Amazon Pinpoint
- D. Amazon Rekognition

**Explanation:** AWS Directory Service integrates with Microsoft Active Directory and enables SSO so users can sign in to the AWS Management Console using their existing corporate credentials.

---

**97.** Which of the following services provides on-demand access to AWS compliance reports?

- A. AWS IAM
- B. AWS Artifact ✅
- C. Amazon GuardDuty
- D. AWS KMS

**Explanation:** AWS Artifact is the go-to service for accessing AWS compliance documentation on demand, including SOC reports, PCI DSS reports, ISO certifications, and other third-party audit reports.

---

**98.** A pharmaceutical company operates its infrastructure in a single AWS Region. The company has thousands of VPCs in various AWS accounts that it wants to interconnect. Which AWS service or feature should the company use to help simplify management and reduce operational costs?

- A. VPC endpoint
- B. VPC peering
- C. AWS Transit Gateway ✅
- D. AWS Direct Connect

**Explanation:** AWS Transit Gateway acts as a cloud router in a hub-and-spoke model, allowing thousands of VPCs and on-premises networks to connect through a single gateway, greatly simplifying management compared to complex VPC peering meshes.

---

**99.** A tech startup wants to protect its workloads running on AWS from SQL injection attacks. Which service can be used to achieve this?

- A. Security groups
- B. Network ACLs
- C. AWS WAF ✅
- D. IAM policy

**Explanation:** AWS WAF (Web Application Firewall) protects web applications from common web exploits like SQL injection and cross-site scripting (XSS). Security groups and NACLs operate at the network level and cannot inspect application-layer content.

---

**100.** Which cloud computing benefit does AWS demonstrate with its ability to offer lower variable costs as a result of high purchase volumes?

- A. Pay-as-you-go pricing
- B. High availability
- C. Global reach
- D. Economies of scale ✅

**Explanation:** Economies of scale refers to the cost advantages AWS gains from operating at massive scale, allowing it to purchase hardware and bandwidth in bulk and pass those lower costs on to customers through reduced pricing.

---

**101.** When comparing AWS with on-premises Total Cost of Ownership (TCO), what costs are included?

- A. Data center security ✅
- B. Business analysis
- C. Project management

**Explanation:** On-premises TCO includes physical costs like data center security, hardware, power, cooling, and facilities. Business analysis and project management are common to both environments and are not differentiating TCO factors.

---

**102.** Which service should be used to estimate the costs of running a new project on AWS?

- A. AWS TCO Calculator
- B. AWS Simple Monthly Calculator ✅
- C. AWS Cost Explorer API

**Explanation:** The AWS Simple Monthly Calculator (now the AWS Pricing Calculator) allows you to estimate the monthly cost of AWS services for a new project or architecture before you deploy anything.

---

**103.** What is an AWS Identity and Access Management (IAM) role?

- A. A user associated with an AWS resource
- B. A group associated with an AWS resource
- C. An entity that defines a set of permissions for use with an AWS resource ✅

**Explanation:** An IAM role is an AWS identity with permission policies that determine what the role can and cannot do in AWS. Unlike users, roles are not associated with a specific person and can be assumed by users, services, or applications that need temporary access.

---

**104.** Which of the following allows users to provision a dedicated network connection from their internal network to AWS?

- A. AWS CloudHSM
- B. AWS Direct Connect ✅
- C. AWS VPN
- D. VPC

**Explanation:** AWS Direct Connect establishes a dedicated private physical connection between your internal network and AWS, bypassing the public internet. This provides more consistent network performance, lower latency, and reduced bandwidth costs.

---

**105.** Which tool can be used to compare the costs of running a web application in a traditional hosting environment to running it on AWS?

- A. AWS Cost Explorer
- B. AWS Budgets
- C. AWS Cost and Usage report
- D. AWS Pricing Calculator ✅

**Explanation:** The AWS Pricing Calculator (which replaced the TCO Calculator) helps estimate and compare the costs of running workloads on AWS versus traditional on-premises or hosting environments, making it ideal for migration cost analysis.

---

**106.** Which AWS service or feature allows a company to visualize, understand, and manage AWS costs and usage over time?

- A. AWS Budgets
- B. AWS Cost Explorer ✅
- C. AWS Organizations

**Explanation:** AWS Cost Explorer provides an interactive interface to visualize, understand, and manage your AWS costs and usage over time. It includes pre-built reports and allows you to filter and group costs by service, region, tag, and more.

---

**107.** Which of the below options are related to the reliability of AWS? (Choose TWO)
- A. Applying the principle of least privilege to all AWS resources.
- B. Automatically provisioning new resources to meet demand. ✅
- C. All AWS services are considered Global Services, and this design helps customers serve their international users.
- D. Providing compensation to customers if issues occur.
- E. Ability to recover quickly from failures. ✅

---

**108.** An organization has a large number of technical employees who operate their AWS Cloud infrastructure. What does AWS provide to help organize them into teams and then assign the appropriate permissions for each team?
- A. IAM roles.
- B. IAM users.
- C. IAM user groups. ✅
- D. AWS Organizations.

---

**109.** What do you gain from setting up consolidated billing for five different AWS accounts under another master account?
- A. AWS services’ costs will be reduced to half the original price.
- B. The consolidated billing feature is just for organizational purpose.
- C. Each AWS account gets volume discounts. ✅
- D. Each AWS account gets five times the free-tier services capacity.

---

**110.** What does the "Principle of Least Privilege" refer to?
- A. You should grant your users only the permissions they need when they need them and nothing more. ✅
- B. All IAM users should have at least the necessary permissions to access the core AWS services.
- C. All trusted IAM users should have access to any AWS service in the respective AWS account.
- D. IAM users should not be granted any permissions; to keep your account safe.

---

**111.** Which of the following must an IAM user provide to interact with AWS services using the AWS Command Line Interface (AWS CLI)?
- A. Access keys. ✅
- B. Secret token.
- C. UserID.
- D. User name and password.

---

**112.** Select TWO examples of the AWS shared controls.
- A. Patch Management. ✅
- B. IAM Management.
- C. VPC Management.
- D. Configuration Management. ✅
- E. Data Center operations.

---

**113.** Which AWS service allows users to identify the changes made to a resource over time?
- A. Amazon Inspector.
- B. AWS Config. ✅
- C. AWS Service Catalog.
- D. AWS IAM.

---

**114.** Which AWS tools assist with estimating costs? (Select three)
- A. Detailed billing report.
- B. Cost allocation tags. ✅
- C. AWS Simple Monthly Calculator. ✅
- D. AWS Total Cost of Ownership (TCO) Calculator. ✅
- E. Cost Estimator.

---

**115.** How does AWS shorten the time to provision IT resources?
- A. It supplies an online IT ticketing platform for resource requests.
- B. It supports automatic code validation services.
- C. It provides the ability to programmatically provision existing resources. ✅
- D. It automates the resource request process from a company’s IT vendor list.

---

**116.** Which AWS IAM feature allows developers to access AWS services through the AWS CLI?
- A. API keys.
- B. Access keys. ✅
- C. User names/Passwords.
- D. SSH keys.

---

**117.** Which service should a customer use to consolidate and centrally manage multiple AWS accounts?
- A. AWS IAM.
- B. AWS Organizations. ✅
- C. AWS Schema Conversion Tool.
- D. AWS Config.

---

**118.** How can a company reduce its Total Cost of Ownership (TCO) using AWS?
- A. By minimizing large capital expenditures. ✅
- B. By having no responsibility for third-party license costs.
- C. By having no operational expenditures.
- D. By having AWS manage applications.

---

**119.** Which of the following will enhance the security of access to the AWS Management Console’? (Select TWO)
- A. AWS Secrets Manager.
- B. AWS Certificate Manager.
- C. AWS Multi-Factor Authentication (AWS MFA). ✅
- D. Security groups.
- E. Password policies. ✅

---

**120.** Which of the following common IT tasks can AWS cover to free up company IT resources? (Select TWO)
- A. Patching databases software. ✅
- B. Testing application releases.
- C. Backing up databases. ✅
- D. Creating database schema.
- E. Running penetration tests.

---

**121.** Which of the following Identity and Access Management (IAM) entities is associated with an access key ID and secret access key when using AWS Command Line Interface (AWS CLI)?
- A. IAM group.
- B. IAM user. ✅
- C. IAM role.
- D. IAM policy.

---

**122.** What credential components are required to gain programmatic access to an AWS account? (Select TWO)
- A. An access key ID. ✅
- B. A primary key.
- C. A secret access key. ✅
- D. A user ID.
- E. A secondary key.

---

**123.** Which of the following security measures protect access to an AWS account? (Select TWO)
- A. Enable AWS CloudTrail.
- B. Grant least privilege access to IAM users. ✅
- C. Create one IAM user and share with many developers and users.
- D. Enable Amazon CloudFront.
- E. Activate multi-factor authentication (MFA) for privileged users. ✅

---

**124.** A customer is deploying a new application and needs to choose an AWS Region. Which of the following factors could influence the customer’s decision? (Select TWO)
- A. Reduced latency to users. ✅
- B. The application’s presentation in the local language.
- C. Data sovereignty compliance. ✅
- D. Cooling costs in hotter climates.
- E. Proximity to the customer’s office for on-site visits.

---

**125.** How can a customer increase security to AWS account logons? (Select TWO)
- A. Configure AWS Certificate Manager
- B. Enable Multi-Factor Authentication (MFA) ✅
- C. Use Amazon Cognito to manage access
- D. Configure a strong password policy ✅
- E. Enable AWS Organizations

---

**126.** Which of the following components of the AWS Global Infrastructure consists of one or more discrete data centers interconnected through low latency links?
- A. Availability Zone ✅
- B. Edge location
- C. Region
- D. Private networking

---

**127.** Which AWS service is used to track record, and audit configuration changes made to AWS resources?
- A. AWS Shield.
- B. AWS Config. ✅
- C. AWS IAM.
- D. Amazon Inspector.

---

**128.** AWS supports which of the following methods to add security to Identity and Access Management (IAM) users? (Select TWO)
- A. Implementing Amazon Rekognition.
- B. Using AWS Shield-protected resources.
- C. Blocking access with Security Groups.
- D. Using Multi-Factor Authentication (MFA). ✅
- E. Enforcing password strength and expiration. ✅

---

**129.** Which AWS Cloud benefit eliminates the need for users to try estimating future infrastructure usage?
- A. Easy and fast deployment of applications in multiple Regions around the world.
- B. Security of the AWS Cloud.
- C. Elasticity of the AWS Cloud. ✅
- D. Lower variable costs due to massive economies of scale.

---

**130.** Compared with costs in traditional and virtualized data centers, AWS has:
- A. Greater variable costs and greater upfront costs.
- B. Fixed usage costs and lower upfront costs.
- C. Lower variable costs and greater upfront costs.
- D. Lower variable costs and lower upfront costs. ✅

---

**131.** How should a customer forecast the future costs for running a new web application?
- A. Amazon Aurora Backtrack.
- B. Amazon CloudWatch Billing Alarms.
- C. AWS Simple Monthly Calculator. ✅
- D. AWS Cost and Usage report.

---

**132.** A global company with a large number of AWS accounts is seeking a way in which they can centrally manage billing and security policies across all accounts. Which AWS Service will assist them in meeting these goals?
- A. AWS Organizations. ✅
- B. AWS Trusted Advisor.
- C. IAM User Groups.
- D. AWS Config.

---

**133.** What is the AWS feature that provides an additional level of security above the default authentication mechanism of usernames and passwords?
- A. Encrypted keys.
- B. Email verification.
- C. AWS KMS.
- D. AWS MFA. ✅

---

**134.** Which of the below is a best-practice when designing solutions on AWS?
- A. Invest heavily in architecting your environment, as it is not easy to change your design later.
- B. Use AWS reservations to reduce costs when testing your production environment.
- C. Automate wherever possible to make architectural (© ) experimentation easier. ✅
- D. Provision a large compute capacity to handle any spikes in load

---

**135.** The principle “design for failure and nothing will fail” is very important when designing your AWS Cloud architecture. Which of the following would help adhere to this principle? (Choose TWO)
- A. Multi-factor authentication.
- B. Availability Zones. ✅
- C. Elastic Load Balancing. ✅
- D. Penetration testing.
- E. Vertical Scaling.

---

**136.** Which of the following is equivalent to a user name and password and is used to authenticate your programmatic access to AWS services and APIs?
- A. Instance Password.
- B. Key pairs.
- C. Access Keys. ✅
- D. MFA.

---

**137.** Which of the following services can help protect your web applications from SQL injection and other vulnerabilities in your application code?
- A. Amazon Cognito.
- B. AWS IAM.
- C. Amazon Aurora.
- D. AWS WAF. ✅

---

**138.** What are the default security credentials that are required to access the AWS management console for an IAM user account?
- A. MFA.
- B. Security tokens.
- C. A user name and password. ✅
- D. Access keys.

---

**139.** A company is migrating its on-premises database to Amazon RDS. What should the company do to ensure Amazon RDS costs are kept to a minimum?
- A. Right-size before and after migration. ✅
- B. Use a Multi-Region Active-Passive architecture.
- C. Combine On-demand Capacity Reservations with Saving Plans.
- D. Use a Multi-Region Active-Active architecture.

---

**140.** An organization runs many systems and uses many AWS products. Which of the following services enables them to control how each developer interacts with these products?
- A. AWS Identity and Access Management. ✅
- B. Amazon RDS.
- C. Network Access Control Lists.
- D. Amazon EMR.

---

**141.** Which statement is correct with regards to AWS service limits? (Choose TWO)
- A. You can contact AWS support to increase the service limits. ✅
- B. Each IAM user has the same service limit.
- C. There are no service limits on AWS.
- D. You can use the AWS Trusted Advisor to monitor your service limits. ✅
- E. The Amazon Simple Email Service is responsible for sending email notifications when usage approaches a service limit.

---

**142.** Which of the following should be considered when performing a TCO analysis to compare the costs of running an application on AWS instead of on-premises?
- A. Application development.
- B. Market research.
- C. Business analysis.
- D. Physical hardware. ✅

---

**143.** A company uses AWS Organizations to manage all of its AWS accounts. Which of the following allows the company to restrict what services and actions are allowed in each individual account?
- A. IAM Principals.
- B. AWS Service Control Policies (SCPs). ✅
- C. IAM policies.
- D. AWS Fargate.

---

**144.** Which of the following statements describes the AWS Cloud’s agility?
- A. AWS allows you to host your applications in multiple regions around the world.
- B. AWS provides customizable hardware at the lowest possible cost.
- C. AWS allows you to provision resources in minutes. ✅
- D. AWS allows you to pay upfront to reduce costs.

---

**145.** Which of the following is used to control network traffic in AWS? (Choose TWO)
- A. Network Access Control Lists (NACLs). ✅
- B. Key Pairs.
- C. Access Keys.
- D. IAM Policies.
- E. Security Groups. ✅

---

**146.** App development companies move their business to AWS to reduce time-to-market and improve customer satisfaction, what are the AWS automation tools that help them deploy their applications faster? (Choose TWO)
- A. AWS CloudFormation. ✅
- B. AWS Migration Hub.
- C. AWS IAM.
- D. AWS Elastic Beanstalk. ✅
- E. Amazon Macie.

---

**147.** Which AWS Service is used to manage user permissions?
- A. Security Groups.
- B. Amazon ECS.
- C. AWS IAM. ✅
- D. AWS Support.

---

**148.** What is the AWS’ recommendation regarding access keys?
- A. Delete all access keys and use passwords instead.
- B. Only share them with trusted people.
- C. Rotate them regularly. ✅
- D. Save them within your application code.

---

**149.** What is the AWS IAM feature that provides an additional layer of security on top of user-name and password authentication?
- A. Key Pair.
- B. Access Keys.
- C. SDK.
- D. MFA. ✅

---

**150.** Why do many startup companies prefer AWS over traditional on-premises solutions? (Choose TWO)
- A. AWS allows them to pay later when their business succeed.
- B. AWS can build complete data centers faster than any other Cloud provider.
- C. Using AWS, they can reduce time-to-market by focusing on business activities rather than on building and managing data centers. ✅
- D. AWS removes the need to invest in operational expenditure.
- E. Using AWS allows companies to replace large capital expenditure with low variable costs. ✅

---

**151.** When running a workload in AWS, the customer is NOT responsible for: (Select TWO)
- A. Running penetration tests.
- B. Reserving capacity.
- C. Data center operations. ✅
- D. Auditing and regulatory compliance.
- E. Infrastructure security. ✅

---

**152.** Which AWS service or feature is used to manage the keys used to encrypt customer data?
- A. AWS KMS. ✅
- B. AWS Service Control Policies (SCPs).
- C. Multi-Factor Authentication (MFA).
- D. Amazon Macie.

---

**153.** What features does AWS offer to help protect your data in the Cloud? (Choose TWO)
- A. Access control. ✅
- B. Physical MFA devices.
- C. Data encryption. ✅
- D. Unlimited storage.
- E. Load balancing.

---

**154.** Which methods can be used by customers to interact with AWS Identity and Access Management (IAM)? (Choose TWO)
- A. AWS CLI. ✅
- B. AWS Security Groups.
- C. AWS SDKs. ✅
- D. AWS Network Access Control Lists.
- E. AWS CodeCommit.

---

**155.** Which of the following are types of AWS Identity and Access Management (IAM) identities? (Choose TWO)
- A. AWS Resource Groups.
- B. IAM Policies.
- C. IAM Roles. ✅
- D. IAM Users. ✅
- E. AWS Organizations.

---

**156.** Which IAM entity can best be used to grant temporary access to your AWS resources?
- A. IAM Users.
- B. Key Pair.
- C. IAM Roles. ✅
- D. IAM Groups.

---

**157.** A company is seeking to better secure its AWS account from unauthorized access. Which of the below options can the customer use to achieve this goal?
- A. Restrict any API call made through SDKs or CLI.
- B. Create one IAM account for each department in the company (Development, QA, Production), and share it across all staff in that department.
- C. Require Multi-Factor Authentication (MFA) for all IAM User access. ✅
- D. Set up two login passwords.

---

**158.** The TCO gap between AWS infrastructure and traditional infrastructure has widened over the recent years. Which of the following could be the reason for that?
- A. AWS helps customers invest more in capital expenditures.
- B. AWS automates all infrastructure operations, so customers save more on human resources costs.
- C. AWS continues to lower the cost of cloud computing for its customers. ✅
- D. AWS secures AWS resources at no additional charge.

---

**159.** Which of the following is a type of MFA device that customers can use to protect their AWS resources?
- A. AWS CloudHSM.
- B. U2F Security Key. ✅
- C. AWS Access Keys.
- D. AWS Key Pair.

---

**160.** Which of the below options is a best practice for making your application on AWS highly available?
- A. Deploy the application to at least two Availability Zones. ✅
- B. Use Elastic Load Balancing (ELB) across multiple AWS Regions.
- C. Deploy the application code on at least two servers in the same Availability Zone.
- D. Rewrite the application code to handle all incoming requests.

---

**161.** Which of the following should be taken into account when performing a TCO analysis regarding the costs of running an application on AWS VS on-premises? (Choose TWO)
- A. Labor and IT costs. ✅
- B. Cooling and power consumption. ✅
- C. Amazon EBS computing power.
- D. Software architecture.
- E. Software compatibility.

---

**162.** Which of the following services can be used to monitor the HTTP and HTTPS requests that are forwarded to Amazon CloudFront?
- A. AWS WAF.
- B. Amazon CloudWatch. ✅
- C. AWS Cloud9.
- D. AWS CloudTrail.

---

**163.** A company wants to grant a new employee long-term access to manage Amazon DynamoDB databases. Which of the following is a recommended best-practice when granting these permissions?
- A. Create an IAM role and attach a policy with Amazon DynamoDB access permissions.
- B. Create an IAM role and attach a policy with Administrator access permissions.
- C. Create an IAM user and attach a policy with Amazon DynamoDB access permissions. ✅
- D. Create an IAM user and attach a policy with Administrator access permissions.

---

**164.** Which of the following will help AWS customers save on costs when migrating their workloads to AWS?
- A. Use servers instead of managed services.
- B. Use existing third-party software licenses on AWS. ✅
- C. Migrate production workloads to AWS edge locations instead of AWS Regions.
- D. Use AWS Outposts to run all workloads in a cost-optimized environment.

---

**165.** Which of the following can be used to enable the Virtual Multi-Factor Authentication? (Choose TWO)
- A. Amazon Connect.
- B. AWS CLI. ✅
- C. AWS Identity and Access Management (IAM). ✅
- D. Amazon SNS.
- E. Amazon Virtual Private Cloud.

---

**166.** What should you do if you see resources, which you don’t remember creating, in the AWS Management Console? (Choose TWO)
- A. Stop all running services and open an investigation.
- B. Give your root account password to AWS Support so that they can assist in troubleshooting and securing the account.
- C. Check the AWS CloudTrail logs and delete all IAM users that have access to your resources.
- D. Open an investigation and delete any potentially compromised IAM users. ✅
- E. Change your AWS root account password and the passwords of any IAM users. ✅

---

**167.** Which of the following is true regarding the AWS availability zones and edge locations?
- A. Edge locations are located in separate Availability Zones worldwide to serve global customers.
- B. An availability zone exists within an edge location to distribute content globally with low latency.
- C. An Availability Zone is a geographic location where AWS provides multiple, physically separated and isolated edge locations.
- D. An AWS Availability Zone is an isolated location within an AWS Region, however edge locations are located in multiple cities worldwide. ✅

---

**168.** A company is developing a mobile application and wants to allow users to use their Amazon, Apple, Facebook, or Google identities to authenticate to the application. Which AWS Service should the company use for this purpose?
- A. Amazon GuardDuty.
- B. Amazon Personalize.
- C. Amazon Cognito. ✅
- D. AWS IAM.

---

**169.** A company is developing an application that will leverage facial recognition to automate photo tagging. Which AWS Service should the company use for facial recognition?
- A. Amazon Comprehend.
- B. AWS IAM.
- C. Amazon Polly.
- D. Amazon Rekognition. ✅

---

**170.** What are some key benefits of using AWS CloudFormation? (Choose TWO)
- A. It helps AWS customers deploy their applications without worrying about the underlying infrastructure.
- B. It applies advanced IAM security features automatically.
- C. It automates the provisioning and updating of your infrastructure in a safe and controlled manner. ✅
- D. It allows you to model your entire infrastructure in just a text file. ✅
- E. It compiles and builds application code in a timely manner.

---

**171.** What does AWS Cost Explorer provide to help manage your AWS spend?
- A. Cost comparisons between AWS Cloud environments and on-premises environments.
- B. Accurate estimates of AWS service costs based on your expected usage.
- C. Consolidated billing.
- D. Highly accurate cost forecasts for up to 12 months ahead. ✅

---

**172.** Which of the following strategies helps protect your AWS root account?
- A. Delete root user access keys if you do not need them. ✅
- B. Apply MFA for the root account and use it for all of your work.
- C. Access the root account only from your personal Mobile Phone.
- D. Only share your AWS account password or access keys with trusted persons.

---

**173.** You have just set up your AWS environment and have created six IAM user accounts for the DevOps team. What is the AWS recommendation when granting permissions to these IAM accounts?
- A. Attach a separate IAM policy for each individual account.
- B. Apply the Principle of Least Privilege. ✅
- C. For security purposes, you should not grant any permission to the DevOps team.
- D. Create six different IAM passwords.

---

**174.** Which of the following has the greatest impact on cost? (Choose TWO)
- A. Compute charges. ✅
- B. The number of services used.
- C. Data Transfer In charges.
- D. Data Transfer Out charges. ✅
- E. The number of IAM roles provisioned.

---

**175.** What does the term “Economies of scale” mean?
- A. It means that you save more when you consume more.
- B. It means as more time passes using AWS, you pay more for its services.
- C. It means that AWS will continuously lower costs as it grows. ✅
- D. It means that you have the ability to pay as you go.

---

**176.** Which of the following are use cases for Amazon EMR? (Choose TWO)
- A. Enables you to backup extremely large amounts of data at very low costs.
- B. Enables you to move Exabyte-scale data from on-premises datacenters into AWS.
- C. Enables you to analyze and process extremely large amounts of data in a timely manner. ✅
- D. Enables you to easily run and scale Apache Spark, Hadoop,and other Big Data frameworks. ✅
- E. Enables you to easily run and manage Docker containers.

---

**177.** Which of the following strategies help analyze costs in AWS?
- A. Using tags to group resources. ✅
- B. Using AWS CloudFormation to automate the deployment of resources.
- C. Deploying resources of the same type in different regions.
- D. Configuring Amazon Inspector to automatically analyze costs and email reports.

---

**178.** What does the Amazon CloudFront service provide? (Choose TWO)
- A. Tracks user activity and APl usage.
- B. Increases application availability by caching at the edge. ✅
- C. Enables faster disaster recovery.
- D. Stores archived data at very low costs.
- E. Delivers content to end users with low latency. ✅

---

**179.** You have migrated your application to AWS recently. How can you view the AWS costs applied to your account?
- A. Using the AWS Cost & Usage Report. ✅
- B. Using the AWS Total Cost of Ownership (TCO) dashboard.
- C. Using the AWS CloudWatch logs dashboard.
- D. Using the Amazon VPC dashboard.

---

**180.** Which AWS Cost Governance best practice recommends refining workloads regularly to make the most of existing AWS resources and reduce costs?
- A. Tagging Enforcement.
- B. Architecture Optimization. ✅
- C. Budgeting Processes.
- D. Resource Controls.

---

**181.** What can you use to assign permissions directly to an IAM user?
- A. IAM Identity.
- B. IAM Group.
- C. IAM Role.
- D. IAM Policy. ✅

---

**182.** A company has infrastructure hosted in an on-premises data center. They currently have an operations team that takes care of identity management. If they decide to migrate to the AWS cloud, which of the following services would help them perform the same role in AWS?
- A. AWS IAM. ✅
- B. AWS Outposts.
- C. AWS Federation.
- D. Amazon Redshift.

---

**183.** Where can AWS account owners get a list of all users in their account, including the status of their AWS credentials?
- A. AWS CloudTrail Trails.
- B. IAM Credential Report. ✅
- C. AWS Artifact reports.
- D. AWS Cost and Usage Report.

---

**184.** Which of the following factors affect Amazon CloudFront cost? (Choose TWO)
- A. Number of Requests. ✅
- B. Traffic Distribution. ✅
- C. Number of Volumes.
- D. Instance type.
- E. Storage Class.

---

**185.** Which feature enables users to sign into their AWS accounts with their existing corporate credentials?
- A. Federation. ✅
- B. Access keys.
- C. IAM Permissions.
- D. WAF rules.

---

**186.** A company is migrating production workloads to AWS, and they are concerned about cost management across different departments. Which option should the company implement to categorize and track AWS spending?
- A. Use the AWS Pricing Calculator service to monitor the costs incurred by each department.
- B. Use Amazon Aurora to forecast AWS spending based on usage.
- C. Apply cost allocation tags to segment AWS costs by different e projects and departments. ✅
- D. Configure AWS Price List API to receive billing updates for each department automatically.

---

**187.** Which statement is true regarding AWS pricing? (Choose TWO)
- A. With the AWS pay-as-you-go pricing model, you don't have to pay any upfront fee. ✅
- B. You have no responsibility for third-party software license costs.
- C. You only pay for the individual services that you need with no long-term contracts. ✅
- D. For some services, you have to pay a startup fee in order to get the service running.
- E. There are no reservations on AWS, you only pay for what you use.

---

**188.** What are the main differences between an IAM user and an IAM role in AWS? (Choose TWO)
- A. An IAM user is uniquely associated with only one person, however a role is intended to be assumable by anyone who needs it. ✅
- B. An IAM user has permanent credentials associated with it, however a role has temporary credentials associated with it. ✅
- C. IAM users are more cost effective than IAM roles.
- D. A role is uniquely associated with only one person, however an IAM user is intended to be assumable by anyone who needs it.
- E. An IAM user has temporary credentials associated with it, however a role has permanent credentials associated with it.

---

**189.** Which of the following actions may reduce Amazon EBS costs? (Choose TWO)
- A. Deleting unused buckets.
- B. Using reservations.
- C. Deleting unnecessary snapshots. ✅
- D. Changing the type of the volume. ✅
- E. Distributing requests to multiple volumes.

---

**190.** Which database service should you use if your application and data schema require "joins" or complex transactions?
- A. Amazon RDS. ✅
- B. AWS Outposts.
- C. Amazon DocumentDB.
- D. Amazon DynamoDB.

---

**191.** The AWS account administrator of your company has been fired. With the permissions granted to him as an administrator, he was able to create multiple IAM user accounts and access keys. Additionally, you are not sure whether he has access to the AWS root account or not. What should you do immediately to protect your AWS infrastructure? (Choose TWO)
- A. Download all the attached policies in a safe place.
- B. Delete all IAM accounts and recreate them.
- C. Use the CloudWatch service to check all API calls that have been made in your account since the administrator was fired.
- D. Rotate all access keys. ✅
- E. Change the email address and password of the root user account and enable MFA. ✅

---

**192.** What is the Amazon ElastiCache service used for? (Choose TWO)
- A. Provide an in-memory data storage service. ✅
- B. Reduce delivery costs using Edge Locations.
- C. Improve web application performance. ✅
- D. Provide a Chef-compatible cache to speed up application response.
- E. Distribute requests to multiple instances.

---

**193.** Which element of the AWS global infrastructure consists of one or more discrete data centers each with redundant power networking and connectivity which are housed in separate facilities?
- A. AWS Regions.
- B. Availability Zones. ✅
- C. Edge locations.
- D. Amazon CloudFront.

---

**194.** Which AWS service or feature can enhance network security by blocking requests from a particular network for a web application on AWS? (Select TWO)
- A. AWS WAF. ✅
- B. AWS Trusted Advisor.
- C. AWS Direct Connect.
- D. AWS Organizations.
- E. Network ACLs. ✅

---

**195.** What are the benefits of using the AWS Cloud for companies with customers in many countries around the world (Select TWO)
- A. Companies can deploy applications in multiple AWS Regions to reduce latency. ✅
- B. Amazon Translate automatically translates third-party website interfaces into multiple languages.
- C. Amazon CloudFront has multiple edge locations around the world to reduce latency. ✅
- D. Amazon Comprehend allows users to build applications that can respond to user requests in many languages.
- E. Elastic Load Balancing can distribute application web traffic to multiple AWS Regions around the world which reduces latency.

---

**196.** (Q1002) Which AWS service or feature provides log information of the inbound and outbound traffic on network interfaces in a VPC?
- A. Amazon CloudWatch Logs
- B. AWS CloudTrail
- C. VPC Flow Logs ✅
- D. AWS Identity and Access Management (IAM)

---

**197.** (Q1010) A company needs to track the activity in its AWS accounts, and needs to know when an API call is made against its AWS resources. Which AWS tool or service can be used to meet these requirements?
- A. Amazon CloudWatch
- B. Amazon Inspector
- C. AWS CloudTrail ✅
- D. AWS IAM

---

**198.** (Q1015) A developer has been hired by a large company and needs AWS credentials.Which are security best practices that should be followed? (Choose two.)
- A. Grant the developer access to only the AWS resources needed to perform the job. ✅
- B. Share the AWS account root user credentials with the developer.
- C. Add the developer to the administrators group in AWS IAM.
- D. Configure a password policy that ensures the developers password cannot be changed.
- E. Ensure the account password policy requires a minimum length. ✅

---

**199.** (Q1017) Which of the following security measures protect access to an AWS account? (Choose two.)
- A. Enable AWS CloudTrail.
- B. Grant least privilege access to IAM users. ✅
- C. Create one IAM user and share with many developers and users.
- D. Enable Amazon CloudFront.
- E. Activate multi-factor authentication (MFA) for privileged users. ✅

---

**200.** (Q1054) Which AWS service supports a hybrid architecture that gives users the ability to extend AWS infrastructure, AWS services, APIs, and tools to data centers, co-location environments, or on-premises facilities?
- A. AWS Snowmobile
- B. AWS Local Zones
- C. AWS Outposts ✅
- D. AWS Fargate
- C. AWS Outposts ✅

---

**201.** (Q1062) To reduce costs, a company is planning to migrate a NoSQL database to AWS. Which AWS service is fully managed and can automatically scale throughput capacity to meet database workload demands? 4 cs a ramets
- A. Amazon Redshift
- B. Amazon Aurora
- C. Amazon DynamoDB ✅
- D. Amazon RDS

---

**202.** (Q1065) Which option is a benefit of the economies of scale based on the advantages of cloud computing?
- A. The ability to trade variable expense for fixed expense
- B. Increased speed and agility
- C. Lower variable costs over fixed costs ✅
- D. Increased operational costs across data centers

---

**203.** (Q1067) A company is developing an application that uses multiple AWS services. The application needs to use temporary, limited-privilege credentials for authentication with other AWS APIs. Which AWS service or feature should the company use to meet these authentication requirements?
- A. Amazon API Gateway
- B. IAM users
- C. AWS Security Token Service (AWS STS) ✅
- D. IAM instance profiles

---

**204.** (Q1071) A company is exploring the use of the AWS Cloud, and needs to create a cost estimate for a project before the infrastructure is provisioned. Which AWS service or feature can be used to estimate costs before deployment?
- A. AWS Free Tier
- B. AWS Pricing Calculator ✅
- C. AWS Billing and Cost Management
- D. AWS Cost and Usage Report

---

**205.** (Q1078) A company is setting up AWS Identity and Access Management (IAM) on an AWS account. Which recommendation complies with IAM security best practices? need.
- A. Use the account root user access keys for administrative tasks.
- B. Grant broad permissions so that all company employees can access the resources they
- C. Turn on multi-factor authentication (MFA) for added security during the login process. ✅
- D. Avoid rotating credentials to prevent issues in production applications.

---

**206.** (Q1087) A user needs programmatic access to AWS resources through the AWS CLI or the AWS API. Which option will provide the user with the appropriate access?
- A. Amazon Inspector
- B. Access keys ✅
- C. SSH public keys
- D. AWS Key Management Service (AWS KMS) keys

---

**207.** (Q1089) A company has an AWS account. The company wants to audit its password and access key rotation details for compliance purposes. Which AWS service or tool will meet this requirement?
- A. IAM Access Analyzer
- B. AWS Artifact
- C. IAM credential report ✅
- D. AWS Audit Manager

---

**208.** (Q1105) Which of the following are benefits of using AWS Trusted Advisor? (Choose two.) es
- A. Providing high-performance container orchestration
- B. Creating and rotating encryption keys
- C. Detecting underutilized resources to save costs ✅
- D. Improving security by proactively monitoring the AWS environment ✅
- E. Implementing enforced tagging across AWS resources

---

**209.** (Q1137) A systems administrator created a new IAM user for a developer and assigned the user an access key instead of a user name and password. What is the access key used for? .
- A. To access the AWS account as the AWS account root user
- B. To access the AWS account through the AWS Management Console
- C. To access the AWS account through a CLI ✅
- D. To access all of a companys AWS accounts

---

**210.** (Q1141) Which actions are best practices for an AWS account root user? (Choose two.) . environment. administrative tasks, instead of using the root user.
- A. Share root user credentials with team members.
- B. Create multiple root users for the account, separated by
- C. Enable multi-factor authentication (MFA) on the root user. ✅
- D. Create an IAM user with administrator privileges for daily ✅
- E. Use programmatic access instead of the root user and password.

---

**211.** (Q1149) A company needs a central user portal so that users can log in to third-party business applications that support Security Assertion Language (SAML) 2.0. Which AWS service will meet this requirement?
- A. AWS Identity and Access Management (IAM)
- B. Amazon Cognito
- C. AWS IAM Identity Center (AWS Single Sign-On) ✅
- D. AWS CLI

---

**212.** (Q1176) A company has teams that have different job roles and responsibilities. The companys employees often change teams. The company needs to manage permissions for the employees so that the permissions are appropriate for the job responsibilities. Which IAM resource should the company use to meet this requirement with the LEAST operational overhead?
- A. IAM user groups ✅
- B. IAM roles
- C. IAM instance profiles
- D. IAM policies for individual users

---

**213.** (Q1177) Which AWS service can a company use to securely store and encrypt passwords for a database? .
- A. AWS Shield
- B. AWS Secrets Manager ✅
- C. AWS Identity and Access Management (IAM)
- D. Amazon Cognito

---

**214.** (Q1180) Which AWS service is used to track, record, and audit configuration changes made to AWS resources?
- A. AWS Shield
- B. AWS Config ✅
- C. AWS IAM
- D. Amazon Inspector

---

**215.** (Q1184) Which AWS service or feature will search for and identify AWS resources that are shared externally?
- A. Amazon OpenSearch Service
- B. AWS Control Tower
- C. AWS IAM Access Analyzer ✅
- D. AWS Fargate

---

**216.** (Q1203) A company wants to integrate its online shopping website with social media login credentials. Which AWS service can the company use to make this integration? ,
- A. AWS Directory Service
- B. AWS Identity and Access Management (IAM)
- C. Amazon Cognito ✅
- D. AWS IAM Identity Center (AWS Single Sign-On)

---

**217.** (Q426) Which AWS service or feature can be used to prevent SQL injection attacks?
- A. Security groups
- B. Network ACLs
- C. AWS WAF ✅
- D. IAM policy

**Explanation:** *(Add explanation here)*

---

**218.** (Q429) Which of the following contribute to total cost of ownership of a workload running in the AWS Cloud? (Choose two.)
- A. Hardware maintenance
- B. Power and cooling
- C. Storage costs ✅
- D. Space for data center
- E. Network costs ✅

**Explanation:** *(Add explanation here)*

---

**219.** (Q432) The AWS global infrastructure consists of Regions, Availability Zones, and what else?
- A. VPCs
- B. Data centers
- C. Dark fiber network links
- D. Edge locations ✅

**Explanation:** *(Add explanation here)*

---

**220.** (Q454) The AWS IAM best practice for granting least privilege is to:
- A. apply an IAM policy to an IAM group and limit the size of the group.
- B. require multi-factor authentication (MFA) for all IAM users.
- C. require each IAM user who has different permissions to have multiple passwords.
- D. apply an IAM policy only to IAM users who require it. ✅

**Explanation:** *(Add explanation here)*

---

**221.** (Q455) A company is planning to configure multi-factor authentication (MFA) for a business application. The company needs to use text messages to distribute one-time passwords to its customers worldwide. Which AWS service should the company use to meet this requirement?
- A. Amazon EventBridge (Amazon CloudWatch Events)
- B. AWS Identity and Access Management (IAM)
- C. Amazon Simple Notification Service (Amazon SNS) ✅
- D. Amazon Connect

**Explanation:** *(Add explanation here)*

---

**222.** (Q459) An external auditor has requested that a company provide a list of all its IAM users, including the status of users' credentials and access keys. What it the SIMPLEST way to provide this information? screenshots to the auditor.
- A. Create an IAM user account for the auditor, granting the auditor administrator permissions.
- B. Take a screenshot of each user's page in the AWS Management Console, then provide the
- C. Download the IAM credential report, then provide the report to the auditor. ✅
- D. Download the AWS Trusted Advisor report, then provide the report to the auditor.

**Explanation:** *(Add explanation here)*

---

**223.** (Q475) A company wants to be notified when its AWS Cloud costs or usage exceed defined thresholds. Which AWS service will support these requirements?
- A. AWS Budgets ✅
- B. Cost Explorer
- C. AWS CloudTrail
- D. Amazon Macie

**Explanation:** *(Add explanation here)*

---

**224.** (Q482) A company wants to provide one of its employees with access to Amazon RDS. The company also wants to limit the interaction to only the AWS CLI and AWS software development kits (SDKs). Which combination of actions should the company take to meet these requirements while following the principles of least privilege? (Choose two.)
- A. Create an IAM user and provide AWS Management Console access only.
- B. Create an IAM user and provide programmatic access only. ✅
- C. Create an IAM role and provide AWS Management Console access only.
- D. Create an IAM policy with administrator access and attach it to the IAM user.
- E. Create an IAM policy with Amazon RDS access and attach it to the IAM user. ✅

**Explanation:** *(Add explanation here)*

---

**225.** (Q492) A company wants to ensure that AWS Management Console users are meeting password complexity requirements. How can the company configure password complexity?
- A. Using an AWS IAM user policy
- B. Using an AWS Organizations service control policy (SCP)
- C. Using an AWS IAM account password policy ✅
- D. Using an AWS Security Hub managed insight

**Explanation:** *(Add explanation here)*

---

**226.** (Q496) What tool enables customers without an AWS account to estimate costs for almost all AWS services?
- A. Cost Explorer
- B. TCO Calculator
- C. AWS Budgets
- D. Simple Monthly Calculator ✅

**Explanation:** *(Add explanation here)*

---

**227.** (Q502) A developer has been hired by a large company and needs AWS credentials. [Which of the following are security best practices? (Choose two.)]
- A. Grant the developer access to only the AWS resources needed to perform the job. ✅
- B. Share the AWS account root user credentials with the developer.
- C. Add the developer to the administrator's group in AWS IAM.
- D. Configure a password policy that ensures the developer's password cannot be changed.
- E. Ensure the account password policy requires a minimum length. ✅

**Explanation:** *(Add explanation here)*

---

**228.** (Q503) Which of the following are benefits of using AWS Trusted Advisor? (Choose two.)
- A. Providing high-performance container orchestration
- B. Creating and rotating encryption keys
- C. Detecting underutilized resources to save costs ✅
- D. Improving security by proactively monitoring the AWS environment ✅
- E. Implementing enforced tagging across AWS resources

**Explanation:** *(Add explanation here)*

---

**229.** (Q518) Which AWS tools automatically forecast future AWS costs?
- A. AWS Support Center
- B. AWS Total Cost of Ownership (TCO) Calculator
- C. AWS Simple Monthly Calculator
- D. Cost Explorer ✅

**Explanation:** *(Add explanation here)*

---

**230.** (Q522) Which of the following assist in identifying costs by department? (Choose two.)
- A. Using tags on resources ✅
- B. Using multiple AWS accounts ✅
- C. Using an account manager
- D. Using AWS Trusted Advisor
- E. Using Consolidated Billing

**Explanation:** *(Add explanation here)*

---

**231.** (Q525) Which task is the responsibility of a company that is using Amazon RDS?
- A. Provision the underlying infrastructure.
- B. Create IAM policies to control administrative access to the service. ✅
- C. Install the cables to connect the hardware for compute and storage.
- D. Install and patch the RDS operating system.

**Explanation:** *(Add explanation here)*

---

**232.** (Q526) A company wants to protect resources that the company hosts on AWS, including Application Load Balancers and Amazon CloudFront distributions. The company wants an AWS service that can provide near real-time visibility into attacks on the company's resources. The service must also have a dedicated AWS team to assist with distributed denial of service (DDoS) attacks. Which AWS service will meet these requirements?
- A. AWS WAF
- B. AWS Shield Standard
- C. Amazon Macie
- D. AWS Shield Advanced ✅

**Explanation:** *(Add explanation here)*

---

**233.** (Q528) Which AWS service provides recommendations to help users optimize costs and follow AWS best practices?
- A. AWS Trusted Advisor ✅
- B. AWS Service Catalog
- C. AWS Ground Station
- D. Amazon GuardDuty

**Explanation:** *(Add explanation here)*

---

**234.** (Q539) A developer wants AWS users to access AWS services by using temporary security credentials. Which AWS service or feature should the developer use to provide these credentials?
- A. IAM policies
- B. IAM user groups
- C. AWS Security Token Service (AWS STS) ✅
- D. AWS IAM Identity Center (AWS Single Sign-On)

**Explanation:** *(Add explanation here)*

---

**235.** (Q544) An Availability Zone consists of:
- A. one or more data centers in a single location. ✅
- B. two or more data centers in multiple locations.
- C. one or more physical hosts in a single data center.
- D. two or more physical hosts in multiple data centers.

**Explanation:** *(Add explanation here)*

---

**236.** (Q562) Which option is an advantage of AWS Cloud computing that minimizes variable costs?
- A. High availability
- B. Economies of scale ✅
- C. Global reach
- D. Agility

**Explanation:** *(Add explanation here)*

---

**237.** (Q563) Which action will help increase security in the AWS Cloud?
- A. Enable programmatic access for all IAM users.
- B. Use IAM users instead of IAM roles to delegate permissions.
- C. Rotate access keys on a reoccurring basis. ✅
- D. Use inline policies instead of customer managed policies.

**Explanation:** *(Add explanation here)*

---

**238.** (Q567) A large company has a workload that requires hardware to remain on premises. The company wants to use the same management and control plane services that it currently uses on AWS. Which AWS service should the company use to meet these requirements?
- A. AWS Device Farm
- B. AWS Fargate
- C. AWS Outposts ✅
- D. AWS Ground Station

**Explanation:** *(Add explanation here)*

---

**239.** (Q571) A company wants to integrate its online shopping website with social media login credentials. Which AWS service can the company use to make this integration?
- A. AWS Directory Service
- B. AWS Identity and Access Management (IAM)
- C. Amazon Cognito ✅
- D. AWS IAM Identity Center (AWS Single Sign-On)

**Explanation:** *(Add explanation here)*

---

**240.** (Q572) A company needs to create graphs that show historical and current costs for the company's AWS account. Which AWS service or tool provides this functionality?
- A. AWS Config
- B. AWS Cost and Usage Report
- C. AWS Budgets
- D. AWS Cost Explorer ✅

**Explanation:** *(Add explanation here)*

---

**241.** (Q579) Which AWS service or feature can a company use to estimate AWS costs before provisioning workloads?
- A. AWS Pricing Calculator ✅
- B. AWS Cost and Usage Report
- C. Cost Explorer
- D. AWS Budgets

**Explanation:** *(Add explanation here)*

---

**242.** (Q595) Which AWS service gives users the ability to run AWS services on premises?
- A. Amazon CloudFront
- B. AWS Outposts ✅
- C. AWS Global Accelerator
- D. Amazon VPC

**Explanation:** *(Add explanation here)*

---

**243.** (Q598) A company is using AWS Identity and Access Management (IAM). Who can manage the access keys of the AWS account root user?
- A. IAM users in the same account that have been granted permission
- B. IAM roles in any account that have been granted permission
- C. IAM users and roles that have been granted permission
- D. The AWS account owner ✅

**Explanation:** *(Add explanation here)*

---

**244.** (Q618) Which AWS service or tool lists all the users in an account and reports on the status of account details, including passwords, access keys, and multi-factor authentication (MFA) devices?
- A. AWS Shield
- B. AWS Trusted Advisor
- C. Amazon Inspector
- D. IAM credential report ✅

**Explanation:** *(Add explanation here)*

---

**245.** (Q621) A user wants to control AWS services by using the AWS CLI. What are the MINIMUM security credentials that the user needs to achieve this goal?
- A. AWS account user name and password
- B. Multi-factor authentication (MFA)
- C. Access keys ✅
- D. Key pairs

**Explanation:** *(Add explanation here)*

---

**246.** (Q624) Which AWS service or feature enables users to block the incoming or outgoing traffic associated with specific IP addresses flowing through a VPC?
- A. Network ACLs ✅
- B. Security groups
- C. AWS Identity and Access Management (IAM)
- D. AWS WAF

**Explanation:** *(Add explanation here)*

---

**247.** (Q628) A company is planning to build a workload in the AWS Cloud. The company needs to estimate the costs of the network, compute, storage, and database for the workload. Which AWS service or tool should the company use to generate this estimate?
- A. AWS Budgets
- B. AWS Organizations
- C. Cost Explorer
- D. AWS Pricing Calculator ✅

**Explanation:** *(Add explanation here)*

---

**248.** (Q629) A user is a new AWS account owner who has no special access requirements. What should this user do with the AWS account root user access keys? AWS services.
- A. Share the keys with all relevant internal users so that those users can programmatically access
- B. Post the keys on GitHub to provide development teams with access to AWS services.
- C. Use the keys for access, but do not share the keys with anyone.
- D. Delete the keys and create IAM users. ✅

**Explanation:** *(Add explanation here)*

---

**249.** (Q643) A company is developing a new web application. The company must give users the ability to log in to the application through social identity providers. Which AWS service will meet these requirements?
- A. AWS Directory Service
- B. Amazon Cognito ✅
- C. AWS Identity and Access Management (IAM)
- D. AWS Single Sign-On

**Explanation:** *(Add explanation here)*

---

**250.** (Q649) Which of the following consists of one or more isolated data centers in the same regional area that are interconnected through low-latency networks?
- A. Availability Zone ✅
- B. Edge location
- C. AWS Region
- D. Private networking

**Explanation:** *(Add explanation here)*

---

**251.** (Q562) A company wants to deploy an application in multiple Availability Zones in a single AWS Region. Which benefit will this deployment provide to the company?
- A. Improved connection performance for global customers
- B. Resilient architecture and a highly available solution ✅
- C. Reduced overall data storage costs
- D. Ability to shut down an Availability Zone during periods of low demand

---

**252.** (Q571) A company wants to centrally manage its employee's access to multiple AWS accounts. Which AWS service or feature should the company use to meet this requirement?
- A. AWS Identity and Access Management Access Analyzer
- B. AWS Secrets Manager
- C. AWS IAM Identity Center ✅
- D. AWS Security Token Service (AWS STS)

---

**253.** (Q572) A university receives a grant to conduct research by using AWS services. The research team needs to make sure the grant money lasts for the entire school year. The team has decided on a monthly allocation that adds up to the total grant amount. Which AWS service or feature will notify the team if spending exceeds the planned amount?
- A. AWS Budgets ✅
- B. Cost Explorer
- C. Cost allocation tags
- D. Cost categories

---

**254.** (Q582) Which of the following actions are controlled with AWS Identity and Access Management (IAM)? (Choose two.)
- A. Control access to AWS service APIs and to other specific resources. ✅
- B. Provide intelligent threat detection and continuous monitoring.
- C. Protect the AWS environment using multi-factor authentication (MFA). ✅
- D. Grant users access to AWS data centers.
- E. Provide firewall protection for applications from common web attacks.

---

**255.** (Q584) A company is using AWS Identity and Access Management (IAM). Who can manage the access keys of the AWS account root user?
- A. IAM users in the same account that have been granted permission
- B. IAM roles in any account that have been granted permission
- C. IAM users and roles that have been granted permission
- D. The AWS account owner ✅

---

**256.** (Q595) A company wants to manage access and permissions for its third-party software as a service (SaaS) applications. The company wants to use a portal where end users can access assigned AWS accounts and AWS Cloud applications. Which AWS service should the company use to meet these requirements?
- A. Amazon Cognito
- B. AWS IAM Identity Center (AWS Single Sign-On) ✅
- C. AWS Identity and Access Management (IAM)
- D. AWS Directory Service for Microsoft Active Directory

---

**257.** (Q605) A developer needs to interact with AWS by using the AWS CLI. Which security feature or AWS service must be provisioned in the developer's account to meet this requirement?
- A. User name and password
- B. AWS Systems Manager
- C. Root password access
- D. AWS access key ✅

---

**258.** (Q618) A company wants to migrate its on-premises infrastructure to the AWS Cloud. Which advantage of cloud computing will help the company reduce upfront costs?
- A. Go global in minutes
- B. Increase speed and agility
- C. Benefit from massive economies of scale
- D. Trade fixed expense for variable expense ✅

---

**259.** (Q620) Which AWS service is used to temporarily provide federated security credentials to access AWS resources?
- A. Amazon GuardDuty
- B. AWS Simple Token Service (AWS STS) ✅
- C. AWS Secrets Manager
- D. AWS Certificate Manager

---

**260.** (Q636) Which AWS service integrates with other AWS services to provide the ability to encrypt data at rest?
- A. AWS Key Management Service (AWS KMS) ✅
- B. AWS Certificate Manager (ACM)
- C. AWS Identity and Access Management (IAM)
- D. AWS Security Hub

---

**261.** (Q641) Which AWS service or tool provides a visualization of historical AWS spending patterns and projections of future AWS costs?
- A. AWS Cost and Usage Report
- B. AWS Budgets
- C. Cost Explorer ✅
- D. Amazon Cloud Watch

---

**262.** (Q650) Which AWS service is always available free of charge to users?
- A. Amazon Athena
- B. AWS Identity and Access Management (IAM) ✅
- C. AWS Secrets Manager
- D. Amazon ElastiCache

---

**263.** (Q666) Which option is an advantage of AWS Cloud computing that minimizes variable costs?
- A. High availability
- B. Economies of scale ✅
- C. Global reach
- D. Agility

---

**264.** (Q695) A company wants to visualize and manage AWS Cloud costs and usage for a specific period_of,time: Which AWS service or feature will meet these requirements?
- A. Cost Explorer ✅
- B. Consolidated billing
- C. AWS Organizations
- D. AWS Budgets

---

