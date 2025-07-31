## 🧠 Databricks-Endorsed MLflow Deployment Patterns

According to **Databricks documentation**:

### 1. **Deploy Code Pattern** *(Recommended)*

* The training code is **deployed through all environments**: dev → staging → production.
* In production, the **model is retrained**, ensuring it’s validated on production data with the same reviewed code.
* Especially suited for environments where model behavior must adapt to new data regularly and code needs repeated testing.
* ✅ Advantages: reproducible, safe retraining, integrated pipelines
* 🔄 Disadvantages: retraining costs, steep learning curve in production environments ([Databricks Docs][1], [Stack Overflow][2])

### 2. **Deploy Model Pattern**

* Code is deployed once, while the **model artifact is promoted** from staging to production.
* Good for scenarios where training is expensive, infrequent, or done centrally.
* Better for environments where model artifacts are reused or wrapped in serving infrastructure.
* ✅ Advantages: simpler handoff, faster deployment
* 🔄 Disadvantages: complex retraining pipeline, requires careful artifact management ([Databricks Docs][1], [Microsoft Learn][3])

---

## 🔁 Side‑by‑Side Comparison

| **Aspect**                | **Deploy Code Pattern**                             | **Deploy Model Pattern**                           |
| ------------------------- | --------------------------------------------------- | -------------------------------------------------- |
| **Purpose**               | Train model each environment                        | Register and promote model artifact                |
| **Training Frequency**    | Frequent retraining in production                   | Artifact reused, no retraining needed              |
| **Code & Model Coupling** | Code packages model                                 | Code and model evolve independently                |
| **Cost (Compute)**        | Higher—training costs across environments           | Lower—single training run                          |
| **Model Ownership**       | Trained by reviewed, tested code in each env        | Developed centrally, promoted                      |
| **CI/CD Fit**             | Strong—code moves through GitOps pipelines          | Strong—artifact promotion triggers serving or jobs |
| **Best For…**             | Organizations with secure access to production data | Centralized model generation, real-time inference  |

---

## 🧪 Code Example (Plain MLflow, Not Bundles)

### ✅ Deploy Code Pattern (`train_and_log.py`)

```python
import mlflow
from sklearn.ensemble import RandomForestClassifier

with mlflow.start_run():
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    mlflow.sklearn.log_model(model, "model", registered_model_name="rf_model_prod")
```

### 🔁 Deploy Model Pattern (`score.py`)

```python
import mlflow
model = mlflow.pyfunc.load_model("models:/rf_model_prod/Production")
preds = model.predict(X_new)
```

