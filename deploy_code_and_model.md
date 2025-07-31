

* 📊 **Dataset**: `customer_data.csv` (binary classification)
* ⚙️ **Model**: `RandomForestClassifier`
* 🔁 **MLflow** for tracking
* ✅ Registered model name: `customer_churn_model`

---

### 🔷 Pattern 1: **Deploy Code Pattern**

```python
# train_model_deploy_code.py

import mlflow
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Load dataset
df = pd.read_csv("customer_data.csv")
X = df.drop(columns=["label"])
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(X, y)

# MLflow training and logging
with mlflow.start_run(run_name="code_pattern_training"):
    clf = RandomForestClassifier(n_estimators=100)
    clf.fit(X_train, y_train)
    
    mlflow.log_metric("accuracy", clf.score(X_test, y_test))
    mlflow.sklearn.log_model(
        sk_model=clf,
        artifact_path="model",
        registered_model_name="customer_churn_model"
    )
```

🧠 **Key idea**:

* Code trains the model and logs it **at the same time**
* This job is used for **training, logging, and versioning**

---

### 🔷 Pattern 2: **Deploy Model Pattern**

```python
# score_model_deploy_model.py

import mlflow
import pandas as pd

# Load new data for scoring
df = pd.read_csv("customer_data_scoring.csv")

# Load model from MLflow Registry
model = mlflow.pyfunc.load_model("models:/customer_churn_model/Production")

# Generate predictions
df["prediction"] = model.predict(df)

# Log results (optional)
with mlflow.start_run(run_name="model_pattern_scoring"):
    mlflow.log_metric("scored_rows", len(df))
```

🧠 **Key idea**:

* Model is **pre-trained** and promoted to production
* This job **does not train** — it just runs inference using model URI

---

## 🧪 Same Example — Different Lifecycle Paths

| Lifecycle Stage      | Deploy Code Pattern                  | Deploy Model Pattern                        |
| -------------------- | ------------------------------------ | ------------------------------------------- |
| Model Training       | ✅ Happens every run                  | ❌ No training                               |
| Model Registry       | ✅ Logs & optionally registers        | ✅ Assumes model already registered          |
| Inference Separation | ❌ Mixed with training                | ✅ Clearly separated                         |
| Deployment Trigger   | Code changes retrains model          | Model promotion triggers deployment         |
| Best Used In         | Dev/experimentation, retraining jobs | Prod batch scoring, APIs, serving workloads |

