import pandas as pd

from config.logging_config import get_logger
from config.settings import SEED_DIR

logger = get_logger(__name__)

OUTPUT_FILE = SEED_DIR / "skill_taxonomy.csv"

def create_skill_taxonomy():

    skills = [{
    "skill_id": 1,
    "skill_name": "Python",
    "category": "Programming",
    "subcategory": "Language",
    "description": "General purpose programming language",
    "importance_level": "Core",
    "is_active": "Yes"
},

{
    "skill_id": 2,
    "skill_name": "R",
    "category": "Programming",
    "subcategory": "Language",
    "description": "Statistical programming language",
    "importance_level": "Core",
    "is_active": "Yes"
},

{
    "skill_id": 3,
    "skill_name": "Java",
    "category": "Programming",
    "subcategory": "Language",
    "description": "Object oriented programming language",
    "importance_level": "Important",
    "is_active": "Yes"
},

{
    "skill_id": 4,
    "skill_name": "C++",
    "category": "Programming",
    "subcategory": "Language",
    "description": "System programming language",
    "importance_level": "Important",
    "is_active": "Yes"
},

{
    "skill_id": 5,
    "skill_name": "JavaScript",
    "category": "Programming",
    "subcategory": "Language",
    "description": "Web programming language",
    "importance_level": "Optional",
    "is_active": "Yes"
},
{
    "skill_id": 6,
    "skill_name": "SQL",
    "category": "Database",
    "subcategory": "Query Language",
    "description": "Structured Query Language",
    "importance_level": "Core",
    "is_active": "Yes"
},

{
    "skill_id": 7,
    "skill_name": "MySQL",
    "category": "Database",
    "subcategory": "Relational Database",
    "description": "Open-source relational database",
    "importance_level": "Core",
    "is_active": "Yes"
},

{
    "skill_id": 8,
    "skill_name": "PostgreSQL",
    "category": "Database",
    "subcategory": "Relational Database",
    "description": "Advanced relational database",
    "importance_level": "Important",
    "is_active": "Yes"
},

{
    "skill_id": 9,
    "skill_name": "SQLite",
    "category": "Database",
    "subcategory": "Embedded Database",
    "description": "Lightweight embedded SQL database",
    "importance_level": "Core",
    "is_active": "Yes"
},

{
    "skill_id": 10,
    "skill_name": "MongoDB",
    "category": "Database",
    "subcategory": "NoSQL Database",
    "description": "Document-oriented database",
    "importance_level": "Important",
    "is_active": "Yes"
},
{
    "skill_id": 11,
    "skill_name": "Pandas",
    "category": "Data Analysis",
    "subcategory": "Python Library",
    "description": "Data manipulation library",
    "importance_level": "Core",
    "is_active": "Yes"
},

{
    "skill_id": 12,
    "skill_name": "NumPy",
    "category": "Data Analysis",
    "subcategory": "Python Library",
    "description": "Numerical computing library",
    "importance_level": "Core",
    "is_active": "Yes"
},

{
    "skill_id": 13,
    "skill_name": "OpenPyXL",
    "category": "Data Analysis",
    "subcategory": "Excel Processing",
    "description": "Excel workbook processing",
    "importance_level": "Important",
    "is_active": "Yes"
},

{
    "skill_id": 14,
    "skill_name": "Polars",
    "category": "Data Analysis",
    "subcategory": "Python Library",
    "description": "High performance dataframe library",
    "importance_level": "Optional",
    "is_active": "Yes"
},

{
    "skill_id": 15,
    "skill_name": "Dask",
    "category": "Data Analysis",
    "subcategory": "Distributed Processing",
    "description": "Parallel dataframe processing",
    "importance_level": "Optional",
    "is_active": "Yes"
},
{
    "skill_id": 16,
    "skill_name": "Matplotlib",
    "category": "Visualization",
    "subcategory": "Python Library",
    "description": "Scientific plotting library",
    "importance_level": "Core",
    "is_active": "Yes"
},

{
    "skill_id": 17,
    "skill_name": "Seaborn",
    "category": "Visualization",
    "subcategory": "Python Library",
    "description": "Statistical visualization library",
    "importance_level": "Core",
    "is_active": "Yes"
},

{
    "skill_id": 18,
    "skill_name": "Plotly",
    "category": "Visualization",
    "subcategory": "Interactive Visualization",
    "description": "Interactive charting library",
    "importance_level": "Important",
    "is_active": "Yes"
},

{
    "skill_id": 19,
    "skill_name": "Power BI",
    "category": "Visualization",
    "subcategory": "Business Intelligence",
    "description": "Business analytics platform",
    "importance_level": "Important",
    "is_active": "Yes"
},

{
    "skill_id": 20,
    "skill_name": "Tableau",
    "category": "Visualization",
    "subcategory": "Business Intelligence",
    "description": "Interactive dashboard platform",
    "importance_level": "Important",
    "is_active": "Yes"
},
{
    "skill_id": 21,
    "skill_name": "Scikit-learn",
    "category": "Machine Learning",
    "subcategory": "ML Library",
    "description": "Machine learning algorithms library",
    "importance_level": "Core",
    "is_active": "Yes"
},

{
    "skill_id": 22,
    "skill_name": "Feature Engineering",
    "category": "Machine Learning",
    "subcategory": "Data Preparation",
    "description": "Creating meaningful input features",
    "importance_level": "Core",
    "is_active": "Yes"
},

{
    "skill_id": 23,
    "skill_name": "Model Evaluation",
    "category": "Machine Learning",
    "subcategory": "Evaluation",
    "description": "Evaluating ML model performance",
    "importance_level": "Core",
    "is_active": "Yes"
},

{
    "skill_id": 24,
    "skill_name": "Classification",
    "category": "Machine Learning",
    "subcategory": "Supervised Learning",
    "description": "Classification algorithms",
    "importance_level": "Core",
    "is_active": "Yes"
},

{
    "skill_id": 25,
    "skill_name": "Regression",
    "category": "Machine Learning",
    "subcategory": "Supervised Learning",
    "description": "Regression algorithms",
    "importance_level": "Core",
    "is_active": "Yes"
},

{
    "skill_id": 26,
    "skill_name": "Clustering",
    "category": "Machine Learning",
    "subcategory": "Unsupervised Learning",
    "description": "Grouping similar observations",
    "importance_level": "Important",
    "is_active": "Yes"
},

{
    "skill_id": 27,
    "skill_name": "Dimensionality Reduction",
    "category": "Machine Learning",
    "subcategory": "Data Reduction",
    "description": "Reducing feature dimensions",
    "importance_level": "Important",
    "is_active": "Yes"
},

{
    "skill_id": 28,
    "skill_name": "Hyperparameter Tuning",
    "category": "Machine Learning",
    "subcategory": "Optimization",
    "description": "Optimizing ML model parameters",
    "importance_level": "Important",
    "is_active": "Yes"
},

{
    "skill_id": 29,
    "skill_name": "Cross Validation",
    "category": "Machine Learning",
    "subcategory": "Validation",
    "description": "Model validation technique",
    "importance_level": "Important",
    "is_active": "Yes"
},

{
    "skill_id": 30,
    "skill_name": "Model Deployment",
    "category": "Machine Learning",
    "subcategory": "Production",
    "description": "Deploying ML models",
    "importance_level": "Optional",
    "is_active": "Yes"
},
{
    "skill_id": 31,
    "skill_name": "TensorFlow",
    "category": "Deep Learning",
    "subcategory": "Framework",
    "description": "Deep learning framework",
    "importance_level": "Important",
    "is_active": "Yes"
},

{
    "skill_id": 32,
    "skill_name": "PyTorch",
    "category": "Deep Learning",
    "subcategory": "Framework",
    "description": "Deep learning framework",
    "importance_level": "Important",
    "is_active": "Yes"
},

{
    "skill_id": 33,
    "skill_name": "Neural Networks",
    "category": "Deep Learning",
    "subcategory": "Concept",
    "description": "Artificial neural network models",
    "importance_level": "Core",
    "is_active": "Yes"
},

{
    "skill_id": 34,
    "skill_name": "CNN",
    "category": "Deep Learning",
    "subcategory": "Computer Vision",
    "description": "Convolutional Neural Networks",
    "importance_level": "Important",
    "is_active": "Yes"
},

{
    "skill_id": 35,
    "skill_name": "RNN",
    "category": "Deep Learning",
    "subcategory": "Sequence Models",
    "description": "Recurrent Neural Networks",
    "importance_level": "Important",
    "is_active": "Yes"
},

{
    "skill_id": 36,
    "skill_name": "LSTM",
    "category": "Deep Learning",
    "subcategory": "Sequence Models",
    "description": "Long Short-Term Memory networks",
    "importance_level": "Important",
    "is_active": "Yes"
},

{
    "skill_id": 37,
    "skill_name": "Transfer Learning",
    "category": "Deep Learning",
    "subcategory": "Model Reuse",
    "description": "Using pre-trained models",
    "importance_level": "Important",
    "is_active": "Yes"
},

{
    "skill_id": 38,
    "skill_name": "Computer Vision",
    "category": "Deep Learning",
    "subcategory": "AI Domain",
    "description": "Image understanding techniques",
    "importance_level": "Important",
    "is_active": "Yes"
},

{
    "skill_id": 39,
    "skill_name": "Natural Language Processing",
    "category": "Deep Learning",
    "subcategory": "AI Domain",
    "description": "Processing human language",
    "importance_level": "Important",
    "is_active": "Yes"
},

{
    "skill_id": 40,
    "skill_name": "Generative AI",
    "category": "Deep Learning",
    "subcategory": "Foundation Models",
    "description": "Large Language Models and Generative AI",
    "importance_level": "Important",
    "is_active": "Yes"
},
{
    "skill_id": 41,
    "skill_name": "Apache Spark",
    "category": "Big Data",
    "subcategory": "Processing",
    "description": "Distributed data processing framework",
    "importance_level": "Important",
    "is_active": "Yes"
},

{
    "skill_id": 42,
    "skill_name": "Hadoop",
    "category": "Big Data",
    "subcategory": "Storage",
    "description": "Distributed storage framework",
    "importance_level": "Important",
    "is_active": "Yes"
},

{
    "skill_id": 43,
    "skill_name": "HDFS",
    "category": "Big Data",
    "subcategory": "Distributed File System",
    "description": "Hadoop Distributed File System",
    "importance_level": "Important",
    "is_active": "Yes"
},

{
    "skill_id": 44,
    "skill_name": "Apache Hive",
    "category": "Big Data",
    "subcategory": "SQL Engine",
    "description": "SQL querying over Hadoop",
    "importance_level": "Optional",
    "is_active": "Yes"
},

{
    "skill_id": 45,
    "skill_name": "Apache Kafka",
    "category": "Big Data",
    "subcategory": "Streaming",
    "description": "Distributed event streaming platform",
    "importance_level": "Important",
    "is_active": "Yes"
},

{
    "skill_id": 46,
    "skill_name": "Apache Airflow",
    "category": "Big Data",
    "subcategory": "Workflow",
    "description": "Workflow orchestration platform",
    "importance_level": "Optional",
    "is_active": "Yes"
},

{
    "skill_id": 47,
    "skill_name": "ETL Pipelines",
    "category": "Big Data",
    "subcategory": "Data Engineering",
    "description": "Extract Transform Load pipelines",
    "importance_level": "Core",
    "is_active": "Yes"
},

{
    "skill_id": 48,
    "skill_name": "Data Warehousing",
    "category": "Big Data",
    "subcategory": "Storage",
    "description": "Analytical data warehouse concepts",
    "importance_level": "Important",
    "is_active": "Yes"
},

{
    "skill_id": 49,
    "skill_name": "Data Lakes",
    "category": "Big Data",
    "subcategory": "Storage",
    "description": "Centralized storage for structured and unstructured data",
    "importance_level": "Important",
    "is_active": "Yes"
},

{
    "skill_id": 50,
    "skill_name": "Apache Parquet",
    "category": "Big Data",
    "subcategory": "Storage Format",
    "description": "Columnar storage format",
    "importance_level": "Optional",
    "is_active": "Yes"
},
{
    "skill_id": 51,
    "skill_name": "AWS",
    "category": "Cloud",
    "subcategory": "Cloud Platform",
    "description": "Amazon Web Services",
    "importance_level": "Important",
    "is_active": "Yes"
},

{
    "skill_id": 52,
    "skill_name": "Microsoft Azure",
    "category": "Cloud",
    "subcategory": "Cloud Platform",
    "description": "Microsoft Azure Cloud",
    "importance_level": "Important",
    "is_active": "Yes"
},

{
    "skill_id": 53,
    "skill_name": "Google Cloud Platform",
    "category": "Cloud",
    "subcategory": "Cloud Platform",
    "description": "Google Cloud Platform",
    "importance_level": "Important",
    "is_active": "Yes"
},

{
    "skill_id": 54,
    "skill_name": "Amazon S3",
    "category": "Cloud",
    "subcategory": "Storage",
    "description": "Cloud object storage",
    "importance_level": "Optional",
    "is_active": "Yes"
},

{
    "skill_id": 55,
    "skill_name": "Amazon RDS",
    "category": "Cloud",
    "subcategory": "Database",
    "description": "Managed relational database service",
    "importance_level": "Optional",
    "is_active": "Yes"
},

{
    "skill_id": 56,
    "skill_name": "AWS Glue",
    "category": "Cloud",
    "subcategory": "ETL",
    "description": "Managed ETL service",
    "importance_level": "Optional",
    "is_active": "Yes"
},

{
    "skill_id": 57,
    "skill_name": "Amazon Athena",
    "category": "Cloud",
    "subcategory": "Analytics",
    "description": "Interactive query service",
    "importance_level": "Optional",
    "is_active": "Yes"
},

{
    "skill_id": 58,
    "skill_name": "Amazon EMR",
    "category": "Cloud",
    "subcategory": "Big Data",
    "description": "Managed Hadoop and Spark service",
    "importance_level": "Optional",
    "is_active": "Yes"
},

{
    "skill_id": 59,
    "skill_name": "Virtual Private Cloud",
    "category": "Cloud",
    "subcategory": "Networking",
    "description": "Cloud networking service",
    "importance_level": "Optional",
    "is_active": "Yes"
},

{
    "skill_id": 60,
    "skill_name": "IAM",
    "category": "Cloud",
    "subcategory": "Security",
    "description": "Identity and Access Management",
    "importance_level": "Optional",
    "is_active": "Yes"
},
{
    "skill_id": 61,
    "skill_name": "Statistics",
    "category": "Mathematics",
    "subcategory": "Statistics",
    "description": "Fundamentals of statistics",
    "importance_level": "Core",
    "is_active": "Yes"
},

{
    "skill_id": 62,
    "skill_name": "Probability",
    "category": "Mathematics",
    "subcategory": "Statistics",
    "description": "Probability concepts",
    "importance_level": "Core",
    "is_active": "Yes"
},

{
    "skill_id": 63,
    "skill_name": "Linear Algebra",
    "category": "Mathematics",
    "subcategory": "Mathematics",
    "description": "Matrices and vectors",
    "importance_level": "Important",
    "is_active": "Yes"
},

{
    "skill_id": 64,
    "skill_name": "Calculus",
    "category": "Mathematics",
    "subcategory": "Mathematics",
    "description": "Differentiation and Integration",
    "importance_level": "Important",
    "is_active": "Yes"
},

{
    "skill_id": 65,
    "skill_name": "Optimization",
    "category": "Mathematics",
    "subcategory": "Optimization",
    "description": "Optimization techniques",
    "importance_level": "Important",
    "is_active": "Yes"
},

{
    "skill_id": 66,
    "skill_name": "Hypothesis Testing",
    "category": "Statistics",
    "subcategory": "Inference",
    "description": "Statistical hypothesis testing",
    "importance_level": "Important",
    "is_active": "Yes"
},

{
    "skill_id": 67,
    "skill_name": "A/B Testing",
    "category": "Statistics",
    "subcategory": "Experimentation",
    "description": "Controlled experiments",
    "importance_level": "Important",
    "is_active": "Yes"
},

{
    "skill_id": 68,
    "skill_name": "EDA",
    "category": "Data Science",
    "subcategory": "Analysis",
    "description": "Exploratory Data Analysis",
    "importance_level": "Core",
    "is_active": "Yes"
},

{
    "skill_id": 69,
    "skill_name": "Data Cleaning",
    "category": "Data Science",
    "subcategory": "Preprocessing",
    "description": "Cleaning and preparing datasets",
    "importance_level": "Core",
    "is_active": "Yes"
},

{
    "skill_id": 70,
    "skill_name": "Data Preprocessing",
    "category": "Data Science",
    "subcategory": "Preprocessing",
    "description": "Preparing data for analysis",
    "importance_level": "Core",
    "is_active": "Yes"
},
{
    "skill_id": 71,
    "skill_name": "Git",
    "category": "Version Control",
    "subcategory": "Version Control",
    "description": "Distributed version control",
    "importance_level": "Core",
    "is_active": "Yes"
},

{
    "skill_id": 72,
    "skill_name": "GitHub",
    "category": "Version Control",
    "subcategory": "Repository",
    "description": "Code hosting platform",
    "importance_level": "Core",
    "is_active": "Yes"
},

{
    "skill_id": 73,
    "skill_name": "Docker",
    "category": "Deployment",
    "subcategory": "Containerization",
    "description": "Container platform",
    "importance_level": "Important",
    "is_active": "Yes"
},

{
    "skill_id": 74,
    "skill_name": "REST API",
    "category": "Deployment",
    "subcategory": "API",
    "description": "RESTful APIs",
    "importance_level": "Important",
    "is_active": "Yes"
},

{
    "skill_id": 75,
    "skill_name": "FastAPI",
    "category": "Deployment",
    "subcategory": "API Framework",
    "description": "Modern Python API framework",
    "importance_level": "Important",
    "is_active": "Yes"
},

{
    "skill_id": 76,
    "skill_name": "Streamlit",
    "category": "Deployment",
    "subcategory": "Dashboard",
    "description": "Python dashboard framework",
    "importance_level": "Core",
    "is_active": "Yes"
},

{
    "skill_id": 77,
    "skill_name": "Linux",
    "category": "Operating System",
    "subcategory": "OS",
    "description": "Linux operating system",
    "importance_level": "Important",
    "is_active": "Yes"
},

{
    "skill_id": 78,
    "skill_name": "Shell Scripting",
    "category": "Operating System",
    "subcategory": "Automation",
    "description": "Linux shell scripting",
    "importance_level": "Optional",
    "is_active": "Yes"
},

{
    "skill_id": 79,
    "skill_name": "CI/CD",
    "category": "Deployment",
    "subcategory": "Automation",
    "description": "Continuous Integration and Deployment",
    "importance_level": "Optional",
    "is_active": "Yes"
},

{
    "skill_id": 80,
    "skill_name": "MLflow",
    "category": "MLOps",
    "subcategory": "Experiment Tracking",
    "description": "Machine learning lifecycle management",
    "importance_level": "Optional",
    "is_active": "Yes"
},
{
    "skill_id": 81,
    "skill_name": "Problem Solving",
    "category": "Professional Skills",
    "subcategory": "Thinking",
    "description": "Analytical problem solving",
    "importance_level": "Core",
    "is_active": "Yes"
},

{
    "skill_id": 82,
    "skill_name": "Critical Thinking",
    "category": "Professional Skills",
    "subcategory": "Thinking",
    "description": "Logical decision making",
    "importance_level": "Core",
    "is_active": "Yes"
},

{
    "skill_id": 83,
    "skill_name": "Communication",
    "category": "Professional Skills",
    "subcategory": "Soft Skill",
    "description": "Professional communication",
    "importance_level": "Important",
    "is_active": "Yes"
},

{
    "skill_id": 84,
    "skill_name": "Presentation Skills",
    "category": "Professional Skills",
    "subcategory": "Soft Skill",
    "description": "Presenting technical work",
    "importance_level": "Important",
    "is_active": "Yes"
},

{
    "skill_id": 85,
    "skill_name": "Business Understanding",
    "category": "Professional Skills",
    "subcategory": "Domain",
    "description": "Understanding business problems",
    "importance_level": "Core",
    "is_active": "Yes"
},

{
    "skill_id": 86,
    "skill_name": "Documentation",
    "category": "Professional Skills",
    "subcategory": "Writing",
    "description": "Technical documentation",
    "importance_level": "Important",
    "is_active": "Yes"
},

{
    "skill_id": 87,
    "skill_name": "Requirement Analysis",
    "category": "Professional Skills",
    "subcategory": "Analysis",
    "description": "Understanding project requirements",
    "importance_level": "Important",
    "is_active": "Yes"
},

{
    "skill_id": 88,
    "skill_name": "Time Management",
    "category": "Professional Skills",
    "subcategory": "Management",
    "description": "Managing learning and work",
    "importance_level": "Important",
    "is_active": "Yes"
},

{
    "skill_id": 89,
    "skill_name": "Decision Making",
    "category": "Professional Skills",
    "subcategory": "Thinking",
    "description": "Evidence-based decision making",
    "importance_level": "Core",
    "is_active": "Yes"
},

{
    "skill_id": 90,
    "skill_name": "Research Skills",
    "category": "Professional Skills",
    "subcategory": "Research",
    "description": "Finding and evaluating information",
    "importance_level": "Core",
    "is_active": "Yes"
},
{
    "skill_id": 91,
    "skill_name": "Networking",
    "category": "Infrastructure",
    "subcategory": "Computer Networks",
    "description": "Networking fundamentals and protocols",
    "importance_level": "Important",
    "is_active": "Yes"
},
    ]
    logger.info("Generating skill taxonomy dataset...")
    df = pd.DataFrame(skills)

    df.to_csv(
        OUTPUT_FILE,
        index=False
    )

    logger.info(f"Generated {len(df)} skills.")
    logger.info(f"Skill taxonomy saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    create_skill_taxonomy()