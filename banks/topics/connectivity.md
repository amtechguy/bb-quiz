# 📚 AWS Hybrid & Network Connectivity

> **Study Resources for this Topic:**
>
> - 📖 **Official AWS Docs:** [https://docs.aws.amazon.com/directconnect/](https://docs.aws.amazon.com/directconnect/)
> - 🎬 **YouTube Overview:** [https://www.youtube.com/watch?v=eNAMr0pNJAE](https://www.youtube.com/watch?v=eNAMr0pNJAE)
> - 🎓 **AWS Skill Builder (Free):** [AWS Cloud Practitioner Essentials](https://explore.skillbuilder.aws/learn/course/external/view/elearning/134/aws-cloud-practitioner-essentials)
>
> 💡 **Quick Tip:** Direct Connect = dedicated private line (no internet). VPN = encrypted tunnel over internet (quick setup). Transit Gateway = hub connecting multiple VPCs.

---

**1.** Question 949 A company's on-premises application deployment cycle was 3-4 weeks. After migrating to the AWS Cloud, the company can deploy the application in 2-3 days. Which benefit has this company experienced by moving to the AWS Cloud?
- A. Elasticity
- B. Flexibility
- C. Agility ✅
- D. Resilience

---

**2.** Question 1245 A company needs an AWS service that provides a clear baseline of what the company runs in its on-premises data centers. The company needs the projected cost to run its on-premises workloads in the AWS Cloud. What AWS service or tool will meet these requirements?
- A. AWS Compute Optimizer
- B. AWS Cost Explorer
- C. AWS Systems Manager Agent (SSM Agent)
- D. Migration Evaluator ✅

---

**3.** Question 1355 Which AWS service will help a company plan a migration to AWS by collecting the configuration, usage, and behavior data of on-premises data centers?
- A. AWS Resource Groups
- B. AWS Application Discovery Service ✅
- C. AWS Service Catalog
- D. AWS Systems Manager

---

**4.** Question 406 A company is moving some of its on-premises IT services to the AWS Cloud. The finance department wants to see the entire bill so it can forecast spending limits. Which AWS service can the company use to set spending limits and receive notifications if those limits are exceeded?
- A. AWS Cost and Usage Reports
- B. AWS Budgets ✅
- C. AWS Organizations consolidated billing
- D. Cost Explorer

---

**5.** Question 455 A user is moving a workload from a local data center to an architecture that is distributed between the local data center and the AWS Cloud. Which type of migration is this?
- A. On-premises to cloud native
- B. Hybrid to cloud native
- C. On-premises to hybrid ✅
- D. Cloud native to hybrid

---

**6.** Question 480 A company runs a legacy workload in an on-premises data center. The company wants to migrate the workload to AWS. The company does not want to make any changes to the workload. Which migration strategy should the company use?
- A. Repurchase
- B. Replatform
- C. Rehost ✅
- D. Refactor

---

**7.** Question 522 A retail company is building a new mobile app. The company is evaluating whether to build the app at an on-premises data center or in the AWS Cloud. Which of the following are benefits of building this app in the AWS Cloud? (Choose two.)
- A. A large, upfront capital expense and low variable expenses
- B. Increased speed for trying out new projects ✅
- C. Complete control over the physical security of the infrastructure
- D. Flexibility to scale up in minutes as the application becomes popular ✅
- E. Ability to pick the specific data centers that will host the application servers

---

**8.** Which AWS service can a company use to send SMS messages and email messages from applications?

- A. AWS Direct Connect
- B. Amazon Simple Email Service (Amazon SES)
- C. Amazon Simple Notification Service (Amazon SNS) ✅
- D. Amazon Simple Queue Service (Amazon SQS)

**Explanation:** Amazon SNS is a fully managed pub/sub messaging service that can send SMS text messages and email notifications from applications to end users.

---

**9.** Which AWS service provides the ability to manage infrastructure as code?
- A. AWS Direct Connect.
- B. AWS CodePipeline.
- C. AWS CloudFormation. ✅
- D. AWS CodeDeploy.
**Explanation:** AWS CloudFormation lets you model and provision AWS infrastructure using JSON or YAML templates, enabling you to treat infrastructure as code with version control, repeatability, and automation.

---

**10.** A company will be moving from an on-premises data center to the AWS Cloud. What would be one financial difference after the move?
- A. Moving from upfront capital expense (capex) to variable operational expense (opex). ✅
- B. Elimination of upfront capital expense (capex) and elimination of variable operational expense (opex).
- C. Moving from upfront capital expense (capex) to variable capital expense (capex).
- D. Moving from variable operational expense (opex) to upfront capital expense (capex).
**Explanation:** On-premises requires large upfront hardware purchases (capex). AWS uses a pay-as-you-go model where you pay only for what you consume each month (opex), eliminating the need for large capital investments.

---

**11.** Which AWS tool or service provides detailed reports on estimated cost savings after migration?
- A. AWS Total Cost of Ownership (TCO) Calculator. ✅
- B. AWS Migration Hub.
- C. Cost Explorer.
- D. AWS Budgets.
- E. Pricing Calculator
**Explanation:** The AWS TCO Calculator helps you compare the cost of running your applications on-premises versus on AWS, providing detailed reports on estimated savings to justify migration decisions.

---

**12.** One of the advantages to moving infrastructure from an on-premises data center to the AWS Cloud is:
- A. It allows the business to leave servers unpatched.
- B. It allows the business to focus on business activities. ✅
- C. It allows the business to eliminate IT bills.
- D. It allows the business to put a server in each customer's data center.
**Explanation:** By offloading infrastructure management to AWS, businesses free up their IT teams to focus on innovation and revenue-generating activities rather than maintaining physical hardware.

---

**13.** Which AWS service can be used to provide an on-demand, cloud-based contact center?

- A. AWS Direct Connect
- B. Amazon Connect ✅
- C. AWS Support Center
- D. AWS Managed Services

**Explanation:** Amazon Connect is an easy-to-use omnichannel cloud contact center that helps companies provide superior customer service at lower cost, with no upfront payments or long-term commitments.

---

**14.** When comparing AWS Cloud with on-premises Total Cost of Ownership, which expenses must be considered? (Choose two.)

- A. Software development
- B. Project management
- C. Storage hardware ✅
- D. Physical servers ✅
- E. Antivirus software license

**Explanation:** On-premises infrastructure requires purchasing physical servers and storage hardware, which represent significant capital expenditures that do not exist when using AWS cloud services.

---

**15.** A user wants guidance on possible savings when migrating from on-premises to AWS. Which tool is suitable for this scenario?

- A. AWS Budgets
- B. Cost Explorer
- C. AWS Total Cost of Ownership (TCO) Calculator ✅

**Explanation:** The AWS TCO Calculator compares the cost of running workloads in on-premises data centers versus on AWS, helping organizations estimate potential savings when considering migration to the cloud.

---

**16.** One of the most important AWS best-practices to follow is the cloud architecture principle of elasticity. How does this principle improve your architecture’s design?
- A. By automatically scaling your on-premises resources based on changes in demand.
- B. By automatically scaling your AWS resources using an Elastic Load Balancer.
- C. By reducing interdependencies between application components wherever possible.
- D. By automatically provisioning the required AWS resources based on changes in demand. ✅

---

**17.** Which AWS service provides the ability to manage infrastructure as code?
- A. AWS CodePipeline.
- B. AWS CodeDeploy.
- C. AWS Direct Connect.
- D. AWS CloudFormation. ✅

---

**18.** A company will be moving from an on-premises data center to the AWS Cloud. What would be one financial difference after the move?
- A. Moving from variable operational expense ( opex ) to upfront capital expense (capex).
- B. Moving from upfront capital expense (capex) to variable capital expense (capex).
- C. Moving from upfront capital expense (capex) to variable operational expense ( opex ). ✅
- D. Elimination of upfront capital expense (capex) and elimination of variable operational expense ( opex ).

---

**19.** A company is planning to migrate from on-premises to the AWS Cloud. When AWS tool or service provides detailed reports on estimated cost savings after migration?
- A. AWS Total Cost of Ownership (TCO) Calculator. ✅
- B. Cost Explorer.
- C. AWS Budgets.
- D. AWS Migration Hub.

---

**20.** One of the advantages to moving infrastructure from an on-premises data center to the AWS Cloud is:
- A. It allows the business to eliminate IT bills.
- B. It allows the business to put a server in each customer’s data center.
- C. It allows the business to focus on business activities. ✅
- D. It allows the business to leave servers unpatched.

---

**21.** Which of the following are valid ways for a customer to interact with AWS services? (Select TWO)
- A. Command line interface. ✅
- B. On-premises.
- C. Software Development Kits. ✅
- D. Software-as-a-service.
- E. Hybrid.

---

**22.** What are the benefits of developing and running a new application in the AWS Cloud compared to on-premises? (Select TWO)
- A. AWS automatically distributes the data globally for higher durability.
- B. AWS will take care of operating the application.
- C. AWS makes it easy to architect for high availability. ✅
- D. AWS can easily accommodate application demand changes. ✅
- E. AWS takes care of application security patching.

---

**23.** Which service is used to ensure that messages between software components are not lost if one or more components fail?
- A. Amazon SQS. ✅
- B. Amazon SES.
- C. AWS Direct Connect.
- D. Amazon Connect.

---

**24.** Which of the following is one of the benefits of moving infrastructure from an on-premises data center to AWS?
- A. Free support for all enterprise customers.
- B. Automatic data protection.
- C. Reduced Capital Expenditure (CapEx). ✅
- D. AWS holds responsibility for managing customer applications.

---

**25.** TYMO Cloud Corp is looking forward to migrating their entire on-premises data center to AWS. What tool can they use to perform a cost-benefit analysis of moving to the AWS Cloud?
- A. AWS Cost Explorer.
- B. AWS TCO Calculator. ✅
- C. AWS Budgets.
- D. AWS Pricing Calculator.

---

**26.** Which of the following is a cloud computing deployment model that connects infrastructure and applications between cloud-based resources and existing resources not located in the cloud?
- A. On-premises.
- B. Mixed.
- C. Hybrid. ✅
- D. Cloud.

---

**27.** Which tool can a non-AWS customer use to compare the cost of on-premises environment resources to AWS?
- A. AWS Cost Explorer.
- B. AWS Pricing Calculator.
- C. AWS Budgets.
- D. AWS TCO Calculator. ✅

---

**28.** You are facing a lot of problems with your current contact center. Which service provides a cloud-based contact center that can deliver a better service for your customers?
- A. Amazon Lightsail.
- B. Amazon Connect. ✅
- C. AWS Direct Connect.
- D. AWS Elastic Beanstalk.

---

**29.** Which of the following Cloud Computing deployment models eliminates the need to run and maintain physical data centers?
- A. On-premises.
- B. IaaS.
- C. PaaS.
- D. Cloud. ✅

---

**30.** (Q1077) An ecommerce company has migrated its IT infrastructure from an on-premises data center to the AWS Cloud. Which cost is the companys direct responsibility?
- A. Cost of application software licenses ✅
- B. Cost of the hardware infrastructure on AWS
- C. Cost of power for the AWS servers
- D. Cost of physical security for the AWS data center

---

**31.** (Q1098) Which AWS service provides the ability to manage infrastructure as code?
- A. AWS CodePipeline
- B. AWS CodeDeploy
- C. AWS Direct Connect
- D. AWS CloudFormation ✅

---

**32.** (Q1106) Which of the following is an advantage that users experience when they move on-premises workloads to the AWS Cloud?
- A. Elimination of expenses for running and maintaining data centers ✅
- B. Price discounts that are identical to discounts from hardware providers
- C. Distribution of all operational controls to AWS
- D. Elimination of operational expenses

---

**33.** (Q497) Which AWS service can be used to provide an on-demand, cloud-based contact center?
- A. AWS Direct Connect
- B. Amazon Connect ✅
- C. AWS Support Center
- D. AWS Managed Services

**Explanation:** *(Add explanation here)*

---

**34.** (Q506) A user has underutilized on-premises resources. Which AWS Cloud concept can BEST address this issue?
- A. High availability
- B. Elasticity ✅
- C. Security
- D. Loose coupling

**Explanation:** *(Add explanation here)*

---

**35.** (Q550) A company wants the ability to accommodate peak application usage without purchasing equipment for on-premises data centers. Which AWS Cloud benefit is the company seeking?
- A. High availability
- B. Security
- C. Reliability
- D. Elasticity ✅

**Explanation:** *(Add explanation here)*

---

**36.** (Q583) Why are AWS CloudFormation templates used?
- A. To reduce provisioning time by using automation. ✅
- B. To transfer existing infrastructure to another company.
- C. To reuse on-premises infrastructure in the AWS Cloud.
- D. To deploy large infrastructure with no cost implications.

---

