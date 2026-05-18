#!/usr/bin/env python3
"""
add_resources.py
Adds a Study Resources header to each topic bank file in banks/topics/.
"""
import os

RESOURCES = {
"ec2": {
    "title": "Amazon EC2 — Elastic Compute Cloud",
    "docs": "https://docs.aws.amazon.com/ec2/",
    "youtube": "https://www.youtube.com/watch?v=iHX-jtKIVNA",
    "skillbuilder": "https://explore.skillbuilder.aws/learn/course/external/view/elearning/134/aws-cloud-practitioner-essentials",
    "note": "Focus on: purchasing options (On-Demand, Reserved, Spot, Dedicated), Auto Scaling, and instance types."
},
"s3": {
    "title": "Amazon S3 — Simple Storage Service",
    "docs": "https://docs.aws.amazon.com/s3/",
    "youtube": "https://www.youtube.com/watch?v=77lMCiiMilo",
    "skillbuilder": "https://explore.skillbuilder.aws/learn/course/external/view/elearning/134/aws-cloud-practitioner-essentials",
    "note": "Focus on: storage classes (Standard, IA, Glacier, Deep Archive, Intelligent-Tiering), versioning, lifecycle policies."
},
"iam": {
    "title": "AWS IAM — Identity and Access Management",
    "docs": "https://docs.aws.amazon.com/iam/",
    "youtube": "https://www.youtube.com/watch?v=SXSqhTn2DuE",
    "skillbuilder": "https://explore.skillbuilder.aws/learn/course/external/view/elearning/134/aws-cloud-practitioner-essentials",
    "note": "Focus on: users, roles, groups, policies, MFA, least privilege principle, root user best practices."
},
"vpc_networking": {
    "title": "Amazon VPC — Virtual Private Cloud",
    "docs": "https://docs.aws.amazon.com/vpc/",
    "youtube": "https://www.youtube.com/watch?v=g2JOHLHh4rI",
    "skillbuilder": "https://explore.skillbuilder.aws/learn/course/external/view/elearning/134/aws-cloud-practitioner-essentials",
    "note": "Focus on: security groups vs Network ACLs, subnets, internet gateway, NAT gateway, VPC endpoints."
},
"databases": {
    "title": "AWS Databases — RDS, DynamoDB, Aurora & more",
    "docs": "https://docs.aws.amazon.com/rds/",
    "youtube": "https://www.youtube.com/watch?v=eMzCI7S1P9M",
    "skillbuilder": "https://explore.skillbuilder.aws/learn/course/external/view/elearning/134/aws-cloud-practitioner-essentials",
    "note": "Focus on: RDS (managed relational), DynamoDB (NoSQL), Aurora (MySQL/PostgreSQL-compatible), Redshift (data warehouse), Neptune (graph)."
},
"shared_responsibility": {
    "title": "AWS Shared Responsibility Model",
    "docs": "https://aws.amazon.com/compliance/shared-responsibility-model/",
    "youtube": "https://www.youtube.com/watch?v=tIb5PGW_t1o",
    "skillbuilder": "https://explore.skillbuilder.aws/learn/course/external/view/elearning/134/aws-cloud-practitioner-essentials",
    "note": "AWS = security OF the cloud (hardware, infrastructure). Customer = security IN the cloud (data, IAM, OS patching on EC2)."
},
"well_architected": {
    "title": "AWS Well-Architected Framework",
    "docs": "https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html",
    "youtube": "https://www.youtube.com/watch?v=x6DIk0_2Goo",
    "skillbuilder": "https://explore.skillbuilder.aws/learn/course/external/view/elearning/134/aws-cloud-practitioner-essentials",
    "note": "6 pillars: Operational Excellence, Security, Reliability, Performance Efficiency, Cost Optimization, Sustainability."
},
"cloud_adoption": {
    "title": "AWS Cloud Adoption Framework (AWS CAF)",
    "docs": "https://aws.amazon.com/cloud-adoption-framework/",
    "youtube": "https://www.youtube.com/watch?v=0RBOgQ9l5Xo",
    "skillbuilder": "https://explore.skillbuilder.aws/learn/course/external/view/elearning/134/aws-cloud-practitioner-essentials",
    "note": "6 perspectives: Business, People, Governance, Platform, Security, Operations. Journey phases: Envision, Align, Launch, Scale."
},
"security_compliance": {
    "title": "AWS Security Services",
    "docs": "https://docs.aws.amazon.com/security/",
    "youtube": "https://www.youtube.com/watch?v=QMBkq6MrT2w",
    "skillbuilder": "https://explore.skillbuilder.aws/learn/course/external/view/elearning/134/aws-cloud-practitioner-essentials",
    "note": "Shield (DDoS), WAF (web app firewall), GuardDuty (threat detection), Inspector (vulnerability), Macie (sensitive data in S3), KMS (encryption keys), Artifact (compliance reports)."
},
"monitoring_audit": {
    "title": "AWS Monitoring & Auditing",
    "docs": "https://docs.aws.amazon.com/cloudwatch/",
    "youtube": "https://www.youtube.com/watch?v=a4dhoTQCyRA",
    "skillbuilder": "https://explore.skillbuilder.aws/learn/course/external/view/elearning/134/aws-cloud-practitioner-essentials",
    "note": "CloudWatch (metrics/logs/alarms), CloudTrail (API activity audit), Config (configuration changes), Trusted Advisor (best practice checks)."
},
"cdn_global": {
    "title": "Amazon CloudFront & Global Infrastructure",
    "docs": "https://docs.aws.amazon.com/cloudfront/",
    "youtube": "https://www.youtube.com/watch?v=AT-nHW3_SVI",
    "skillbuilder": "https://explore.skillbuilder.aws/learn/course/external/view/elearning/134/aws-cloud-practitioner-essentials",
    "note": "CloudFront uses edge locations to cache content. Global Accelerator routes traffic over AWS backbone. Route 53 is DNS."
},
"connectivity": {
    "title": "AWS Hybrid & Network Connectivity",
    "docs": "https://docs.aws.amazon.com/directconnect/",
    "youtube": "https://www.youtube.com/watch?v=eNAMr0pNJAE",
    "skillbuilder": "https://explore.skillbuilder.aws/learn/course/external/view/elearning/134/aws-cloud-practitioner-essentials",
    "note": "Direct Connect = dedicated private line (no internet). VPN = encrypted tunnel over internet (quick setup). Transit Gateway = hub connecting multiple VPCs."
},
"cost_billing": {
    "title": "AWS Cost Management & Billing",
    "docs": "https://docs.aws.amazon.com/cost-management/",
    "youtube": "https://www.youtube.com/watch?v=XHMp5oPMkEE",
    "skillbuilder": "https://explore.skillbuilder.aws/learn/course/external/view/elearning/134/aws-cloud-practitioner-essentials",
    "note": "Cost Explorer (visualize spend), Budgets (alerts), Cost & Usage Report (detailed), Pricing Calculator (estimate), Organizations (consolidated billing)."
},
"serverless_containers": {
    "title": "AWS Serverless & Containers",
    "docs": "https://docs.aws.amazon.com/lambda/",
    "youtube": "https://www.youtube.com/watch?v=97q30JjEq9Y",
    "skillbuilder": "https://explore.skillbuilder.aws/learn/course/external/view/elearning/134/aws-cloud-practitioner-essentials",
    "note": "Lambda (run code without servers), Fargate (serverless containers), ECS (container orchestration), EKS (Kubernetes managed)."
},
"storage": {
    "title": "AWS Storage Services",
    "docs": "https://aws.amazon.com/products/storage/",
    "youtube": "https://www.youtube.com/watch?v=6vNC_BCqFmI",
    "skillbuilder": "https://explore.skillbuilder.aws/learn/course/external/view/elearning/134/aws-cloud-practitioner-essentials",
    "note": "EBS (block, EC2 attached), EFS (shared file NFS), FSx (Windows SMB), Storage Gateway (hybrid), Snowball/Snowmobile (physical data transfer)."
},
"migration": {
    "title": "AWS Migration Services",
    "docs": "https://aws.amazon.com/cloud-migration/",
    "youtube": "https://www.youtube.com/watch?v=id-PY0GBHXA",
    "skillbuilder": "https://explore.skillbuilder.aws/learn/course/external/view/elearning/134/aws-cloud-practitioner-essentials",
    "note": "Application Discovery Service (gather inventory), Migration Hub (track progress), Application Migration Service (rehost servers), DMS (database migration)."
},
"ai_ml": {
    "title": "AWS AI & Machine Learning Services",
    "docs": "https://aws.amazon.com/machine-learning/",
    "youtube": "https://www.youtube.com/watch?v=5wXxNKBcjbI",
    "skillbuilder": "https://explore.skillbuilder.aws/learn/course/external/view/elearning/134/aws-cloud-practitioner-essentials",
    "note": "Rekognition (image/video), Textract (documents), Polly (text-to-speech), Lex (chatbots), Comprehend (NLP), Personalize (recommendations), SageMaker (build/train/deploy ML)."
},
"devops_deploy": {
    "title": "AWS Developer & Deployment Tools",
    "docs": "https://docs.aws.amazon.com/cloudformation/",
    "youtube": "https://www.youtube.com/watch?v=Omppm_YcKpk",
    "skillbuilder": "https://explore.skillbuilder.aws/learn/course/external/view/elearning/134/aws-cloud-practitioner-essentials",
    "note": "CloudFormation (IaC with templates), CDK (IaC with code), Elastic Beanstalk (auto-deploy apps), CodeDeploy/Pipeline/Build (CI/CD pipeline)."
},
"support_plans": {
    "title": "AWS Support Plans",
    "docs": "https://aws.amazon.com/premiumsupport/plans/",
    "youtube": "https://www.youtube.com/watch?v=5hWHJBTMHAI",
    "skillbuilder": "https://explore.skillbuilder.aws/learn/course/external/view/elearning/134/aws-cloud-practitioner-essentials",
    "note": "Basic (free), Developer (business hours email), Business (24/7 phone/chat, 1hr critical), Enterprise On-Ramp (30min), Enterprise (15min + TAM)."
},
"analytics": {
    "title": "AWS Analytics Services",
    "docs": "https://aws.amazon.com/big-data/datalakes-and-analytics/",
    "youtube": "https://www.youtube.com/watch?v=rvVDpKE7Nq4",
    "skillbuilder": "https://explore.skillbuilder.aws/learn/course/external/view/elearning/134/aws-cloud-practitioner-essentials",
    "note": "Athena (query S3 with SQL), Kinesis (streaming data), Glue (ETL), QuickSight (BI dashboards), EMR (big data processing)."
},
"cloud_concepts": {
    "title": "AWS Cloud Computing Concepts",
    "docs": "https://aws.amazon.com/what-is-cloud-computing/",
    "youtube": "https://www.youtube.com/watch?v=mxT233EdY5c",
    "skillbuilder": "https://explore.skillbuilder.aws/learn/course/external/view/elearning/134/aws-cloud-practitioner-essentials",
    "note": "Key benefits: elasticity, agility, pay-as-you-go, economies of scale, global reach, high availability, trade CapEx for OpEx."
},
"general": {
    "title": "AWS General Knowledge",
    "docs": "https://aws.amazon.com/documentation/",
    "youtube": "https://www.youtube.com/@AWSEvents",
    "skillbuilder": "https://explore.skillbuilder.aws/learn/course/external/view/elearning/134/aws-cloud-practitioner-essentials",
    "note": "Review the AWS Cloud Practitioner Essentials course on Skill Builder — it covers all exam topics for free."
},
}

HEADER_TEMPLATE = """# 📚 {title}

> **Study Resources for this Topic:**
>
> - 📖 **Official AWS Docs:** [{docs}]({docs})
> - 🎬 **YouTube Overview:** [{youtube}]({youtube})
> - 🎓 **AWS Skill Builder (Free):** [AWS Cloud Practitioner Essentials]({skillbuilder})
>
> 💡 **Quick Tip:** {note}

---

"""

topics_dir = "/home/grant/Documents/project folder/bb-quiz2/banks/topics"

for fname in sorted(os.listdir(topics_dir)):
    if not fname.endswith('.md'):
        continue
    topic = fname.replace('.md', '')
    fpath = os.path.join(topics_dir, fname)
    
    res = RESOURCES.get(topic, RESOURCES['general'])
    header = HEADER_TEMPLATE.format(
        title=res['title'],
        docs=res['docs'],
        youtube=res['youtube'],
        skillbuilder=res['skillbuilder'],
        note=res['note']
    )
    
    with open(fpath, 'r', encoding='utf-8') as f:
        existing = f.read()
    
    # Only add header if not already present
    if '📚' not in existing:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(header + existing)
        print(f"  Added resources to {fname}")
    else:
        print(f"  Skipped {fname} (already has header)")

import os
print("\nDone!")
