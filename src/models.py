class Course:
    def __init__(self, title, description, instructor, duration, topics=None):
        self.title = title
        self.description = description
        self.instructor = instructor
        self.duration = duration
        self.topics = topics if topics is not None else []

    def __repr__(self):
        return f"<Course {self.title} by {self.instructor}>"

courses = [
    Course("Introduction to Python", "Learn the basics of Python programming.", "John Doe", "4 weeks",
           ["Variables and Data Types", "Control Structures", "Functions", "Object-Oriented Programming"]),
    Course("Web Development with Flask", "Build web applications using Flask.", "Jane Smith", "6 weeks",
           ["Flask Basics", "Routing and Templates", "Forms and Validation", "Database Integration", "Deployment"]),
    Course("Data Science Fundamentals", "An introduction to data science concepts and tools.", "Alice Johnson", "8 weeks",
           ["Statistics Basics", "Python for Data Science", "Data Visualization", "Machine Learning Introduction"]),
    Course("Go Programming Essentials", "Master Go programming language from basics to advanced concepts.", "Robert Chen", "5 weeks",
           ["Go Basics and Syntax", "Goroutines and Concurrency", "Channels and Synchronization", "Web Services with Go", "Testing and Deployment"]),
    Course(
        "Google Cloud Architect",
        "Prepare for the Google Cloud Professional Cloud Architect certification. Learn to design, develop, and manage robust, secure, scalable, and highly available solutions on Google Cloud Platform. This course covers core GCP services, architecture best practices, security, cost optimization, and real-world case studies to get you ready for enterprise-grade cloud deployments.",
        "Sandeep Arora",
        "8 weeks",
        [
            "Cloud Computing Fundamentals",
            "Google Cloud Platform Overview",
            "Compute Engine and Virtual Machines",
            "Cloud Storage and Object Management",
            "Virtual Private Cloud (VPC) Networking",
            "Identity and Access Management (IAM)",
            "Cloud SQL and Relational Databases",
            "BigQuery and Data Analytics",
            "Google Kubernetes Engine (GKE)",
            "Cloud Run and Serverless Containers",
            "Cloud Functions and Event-Driven Architecture",
            "CI/CD with Cloud Build and Artifact Registry",
            "Cloud Monitoring, Logging, and Observability",
            "Security and Compliance on GCP",
            "Cost Management and Budget Optimization",
            "Cloud Architecture Patterns and Best Practices",
            "Disaster Recovery and High Availability",
            "Cloud Migration Strategies",
            "Data Engineering and Pub/Sub",
            "Google Cloud Professional Architect Exam Prep",
        ]
    ),
    Course(
        "AWS Cloud Architect",
        "Prepare for the AWS Certified Solutions Architect certification. Learn to design, deploy, and manage scalable, highly available, and fault-tolerant systems on Amazon Web Services. This course covers core AWS services, architecture best practices, security, cost optimization, and real-world scenarios to get you ready for enterprise-grade cloud solutions.",
        "Sandeep Arora",
        "8 weeks",
        [
            "Cloud Computing Fundamentals",
            "AWS Global Infrastructure Overview",
            "EC2 and Compute Services",
            "S3 and Object Storage",
            "Virtual Private Cloud (VPC) Networking",
            "Identity and Access Management (IAM)",
            "RDS and Relational Databases",
            "DynamoDB and NoSQL Databases",
            "Elastic Load Balancing and Auto Scaling",
            "Amazon ECS and EKS (Container Services)",
            "AWS Lambda and Serverless Architecture",
            "CI/CD with CodePipeline and CodeDeploy",
            "CloudWatch Monitoring and Logging",
            "Security and Compliance on AWS",
            "Cost Management and Budget Optimization",
            "Cloud Architecture Patterns and Best Practices",
            "Disaster Recovery and High Availability",
            "Cloud Migration Strategies",
            "SQS, SNS, and Event-Driven Architecture",
            "AWS Certified Solutions Architect Exam Prep",
        ]
    ),
]