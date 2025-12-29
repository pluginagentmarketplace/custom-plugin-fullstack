---
name: data-science-ai
description: Master machine learning, data engineering, AI/LLM development, and MLOps. Use when building data-driven applications, implementing ML models, or managing ML pipelines.
sasmp_version: "1.3.0"
bonded_agent: 01-frontend-mobile
bond_type: PRIMARY_BOND
---

# Data Science & AI Engineering

## Quick Start

Data Science and AI Engineering focus on data analysis, machine learning, and artificial intelligence. The roadmap covers:

### Core Competencies
- **Languages**: Python, R, SQL, Java, Scala
- **ML Frameworks**: TensorFlow, PyTorch, Scikit-learn, Keras
- **Data Tools**: Pandas, NumPy, Matplotlib, Seaborn
- **Data Engineering**: Airflow, Spark, Kafka, Hadoop
- **Databases**: PostgreSQL, MongoDB, BigQuery, Snowflake
- **Cloud**: AWS, Azure, Google Cloud
- **AI/LLMs**: OpenAI, Hugging Face, Ollama, Claude
- **MLOps**: MLflow, Kubeflow, DVC

### ML Fundamentals

**Machine Learning Pipeline**:
```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load data
data = pd.read_csv('data.csv')
X = data.drop('target', axis=1)
y = data['target']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Evaluate
accuracy = model.score(X_test, y_test)
```

**Deep Learning with PyTorch**:
```python
import torch
import torch.nn as nn

class SimpleNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(10, 64)
        self.fc2 = nn.Linear(64, 1)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        return self.fc2(x)
```

**Prompt Engineering for LLMs**:
```python
from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Explain machine learning in simple terms."}
    ]
)
```

## Study Path

1. **Python Fundamentals** (1-2 weeks): Core language and libraries
2. **Data Analysis** (2-3 weeks): Pandas, NumPy, visualization
3. **Machine Learning** (3-4 weeks): Scikit-learn, algorithms, evaluation
4. **Deep Learning** (2-3 weeks): Neural networks, TensorFlow/PyTorch
5. **AI/LLMs** (1-2 weeks): Prompt engineering, fine-tuning
6. **MLOps** (2-3 weeks): Model deployment, monitoring, pipelines

## Key Topics

- Data collection and preprocessing
- Exploratory data analysis (EDA)
- Feature engineering
- Model selection and training
- Hyperparameter tuning
- Evaluation metrics and validation
- Deep learning architectures
- Prompt engineering techniques
- Model deployment and serving
- MLOps and pipelines

## Resources
- Developer Roadmap: https://roadmap.sh/machine-learning
- TensorFlow: https://www.tensorflow.org
- PyTorch: https://pytorch.org
- Scikit-learn: https://scikit-learn.org
- OpenAI: https://openai.com/api
