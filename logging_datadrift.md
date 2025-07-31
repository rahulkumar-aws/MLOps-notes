## 🎯 **Monitoring, Drift Detection, and Logging at Scale**

*(Databricks + MLflow aligned)*

---

### 🔍 **Slide Title**:

**Monitoring, Drift Detection & Logging at Scale**

---

### ✅ Key Concepts:

#### 📈 **Model Monitoring**

* Track **predictions**, **input features**, and **model performance** over time
* Use **Databricks Model Serving metrics**, or log via **MLflow Tracking Server**

#### 🌊 **Drift Detection**

* Detect **data drift**: changes in input feature distribution
* Detect **concept drift**: changes in relationship between inputs and labels
* Compare **production input data** vs **training dataset stats**

#### 🪵 **Logging at Scale**

* Use **MLflow Logging API** to capture:

  * `mlflow.log_metric()` → drift scores, prediction stats
  * `mlflow.log_artifact()` → JSON drift reports, model cards
  * `mlflow.log_input()` → production samples (structured logging)

---

### 🔧 Code Snippet: Input Drift Detection

```python
import pandas as pd
import mlflow
from scipy.stats import wasserstein_distance

# Compare training vs production feature distribution
train_data = pd.read_csv("train.csv")["age"]
prod_data = pd.read_csv("prod_batch.csv")["age"]

# Calculate drift (Wasserstein distance)
drift_score = wasserstein_distance(train_data, prod_data)

# Log drift score
with mlflow.start_run():
    mlflow.log_metric("age_drift", drift_score)
```

---

### 🧠 Production Best Practices:

* Run **daily/weekly drift scoring** as a separate MLflow Job
* Persist drift scores in a **feature store table or ML monitoring DB**
* Set **alerts** for major drift via Databricks SQL alerts or Unity Catalog audits

---
