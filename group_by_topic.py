#!/usr/bin/env python3
"""
group_by_topic.py
Reads all .md banks, categorizes each question by AWS topic/service,
and writes topic-based bank files to banks/topics/.
"""

import re
import os

# --- Topic keyword rules (order matters: first match wins) ---
TOPICS = [
    ("well_architected",  ["well-architected", "well architected", "pillar", "operational excellence",
                            "performance efficiency", "cost optimization", "sustainability",
                            "design principle", "loosely coupled", "decouple"]),
    ("cloud_adoption",    ["cloud adoption framework", "aws caf", " caf ", "caf perspective",
                            "transformation journey", "envision", "align phase", "launch phase",
                            "scale phase", "business perspective", "people perspective",
                            "governance perspective", "platform perspective", "operations perspective",
                            "security perspective"]),
    ("shared_responsibility", ["shared responsibility", "customer responsibility", "aws responsibility",
                                "aws is responsible", "customer is responsible"]),
    ("support_plans",     ["support plan", "developer support", "business support", "enterprise support",
                            "basic support", "technical account manager", "tam", "aws concierge",
                            "infrastructure event management", "iem"]),
    ("ec2",               ["amazon ec2", "ec2 instance", "reserved instance", "spot instance",
                            "on-demand instance", "dedicated host", "dedicated instance",
                            "savings plan", "ec2 pricing", "auto scaling group", "ec2 image builder",
                            "amazon machine image", "ami", "ec2 fleet", "placement group"]),
    ("s3",                ["amazon s3", " s3 ", "s3 bucket", "s3 storage class", "s3 glacier",
                            "glacier deep archive", "s3 standard", "s3 intelligent", "s3 one zone",
                            "s3 versioning", "s3 lifecycle", "s3 transfer acceleration",
                            "object storage", "s3 acl", "s3 express"]),
    ("iam",               ["iam", "identity and access management", "iam user", "iam role",
                            "iam policy", "iam group", "mfa", "multi-factor authentication",
                            "root user", "access key", "least privilege", "iam credential",
                            "sts", "security token service", "federated", "saml",
                            "iam identity center", "single sign-on"]),
    ("vpc_networking",    ["amazon vpc", "virtual private cloud", "subnet", "security group",
                            "network acl", "nacl", "nat gateway", "internet gateway",
                            "vpc endpoint", "vpc flow logs", "vpc peering", "route table",
                            "private subnet", "public subnet"]),
    ("analytics",         ["amazon athena", "amazon kinesis", "aws glue", "amazon quicksight",
                            "amazon emr", "data warehouse", "data lake", "big data", "etl",
                            "amazon msk", "apache kafka", "aws data exchange", "aws lake formation",
                            "kinesis data streams", "kinesis firehose", "kinesis analytics"]),
    ("databases",         ["amazon rds", "amazon dynamodb", "amazon aurora", "amazon redshift",
                            "amazon neptune", "amazon elasticache", "amazon documentdb",
                            "relational database", "nosql database", "database", "olap", "oltp",
                            "multi-az", "read replica", "amazon timestream", "amazon qldb"]),
    ("storage",           ["amazon ebs", "amazon efs", "aws storage gateway", "aws snowball",
                            "aws snowmobile", "aws datasync", "amazon fsx", "elastic block store",
                            "elastic file system", "file storage", "block storage",
                            "snowball edge", "snowcone", "aws snow family", "aws backup"]),
    ("serverless_containers", ["aws lambda", "aws fargate", "amazon ecs", "amazon eks",
                                "elastic container", "serverless", "aws batch",
                                "aws step functions", "container", "docker"]),
    ("security_compliance", ["aws shield", "aws waf", "amazon guardduty", "amazon inspector",
                              "amazon macie", "aws security hub", "aws firewall manager",
                              "aws kms", "key management", "aws cloudhsm", "aws artifact",
                              "ddos", "sql injection", "compliance", "soc report",
                              "pci dss", "iso certif", "encryption", "certificate manager"]),
    ("monitoring_audit",  ["amazon cloudwatch", "aws cloudtrail", "aws config", "aws trusted advisor",
                            "aws health dashboard", "aws personal health", "vpc flow logs",
                            "cloudtrail", "cloudwatch", "audit", "governance", "monitoring",
                            "service quota"]),
    ("cdn_global",        ["amazon cloudfront", "edge location", "aws global accelerator",
                            "amazon route 53", "cloudfront", "content delivery", "latency",
                            "global network", "aws local zones", "aws wavelength", "aws outposts"]),
    ("connectivity",      ["aws direct connect", "aws vpn", "site-to-site vpn", "aws transit gateway",
                            "aws privatelink", "vpn", "direct connect", "on-premises",
                            "hybrid cloud", "hybrid architecture"]),
    ("cost_billing",      ["cost explorer", "aws budgets", "cost and usage report", "billing",
                            "consolidated billing", "aws organizations", "cost allocation",
                            "pricing calculator", "migration evaluator", "savings plan",
                            "compute optimizer", "rightsiz"]),
    ("migration",         ["aws migration hub", "application discovery service",
                            "application migration service", "aws dms", "database migration",
                            "aws datasync", "migrate", "migration"]),
    ("ai_ml",             ["amazon sagemaker", "amazon rekognition", "amazon textract",
                            "amazon polly", "amazon lex", "amazon comprehend", "amazon personalize",
                            "amazon forecast", "amazon kendra", "machine learning", "ml model",
                            "artificial intelligence", "natural language", "image recognition",
                            "speech", "chatbot", "recommendation"]),
    ("devops_deploy",     ["aws cloudformation", "aws cdk", "cloud development kit", "aws codedeploy",
                            "aws codepipeline", "aws codebuild", "aws codecommit", "elastic beanstalk",
                            "infrastructure as code", "iac", "aws app runner", "aws amplify",
                            "aws appconfig"]),
    ("analytics_fallback", ["streaming data", "real-time data", "batch processing"]),
    ("cloud_concepts",    ["economy of scale", "economies of scale", "agility", "elasticity",
                            "scalab", "high availability", "fault toleran", "reliability",
                            "trade fixed", "variable expense", "capital expense", "capex", "opex",
                            "pay-as-you-go", "cloud computing benefit", "advantage of aws",
                            "global infrastructure", "availability zone", "aws region"]),
]

def categorize(text):
    lower = text.lower()
    for topic, keywords in TOPICS:
        for kw in keywords:
            if kw.lower() in lower:
                return topic
    return "general"

def parse_bank(filepath):
    """Returns list of (question_block_text,) strings split by ---"""
    with open(filepath, encoding='utf-8') as f:
        content = f.read()
    # Split on --- separator
    blocks = re.split(r'\n---\n', content)
    questions = []
    for b in blocks:
        b = b.strip()
        if b:
            questions.append(b)
    return questions

def main():
    banks_dir = "/home/grant/Documents/project folder/bb-quiz2/banks"
    topics_dir = os.path.join(banks_dir, "topics")
    os.makedirs(topics_dir, exist_ok=True)

    # Collect all questions grouped by topic
    topic_questions = {}
    total = 0

    for fname in sorted(os.listdir(banks_dir)):
        if not fname.endswith('.md'):
            continue
        fpath = os.path.join(banks_dir, fname)
        questions = parse_bank(fpath)
        source = fname.replace('.md', '')
        for q in questions:
            topic = categorize(q)
            if topic not in topic_questions:
                topic_questions[topic] = []
            topic_questions[topic].append((source, q))
            total += 1

    # Write topic files
    for topic, items in sorted(topic_questions.items()):
        outpath = os.path.join(topics_dir, f"{topic}.md")
        with open(outpath, 'w', encoding='utf-8') as f:
            count = 0
            for source, q in items:
                count += 1
                # Renumber question
                q_renumbered = re.sub(r'^\*\*\d+\.?\*\*', f'**{count}.**', q, count=1)
                f.write(q_renumbered + "\n\n---\n\n")
        print(f"  {topic:<30} {len(items):>4} questions -> {topic}.md")

    print(f"\nTotal: {total} questions across {len(topic_questions)} topics")

if __name__ == '__main__':
    main()
