# --- Setup (Databricks: use a %pip cell if needed) ---
# %pip install scikit-learn matplotlib pandas numpy

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.inspection import PartialDependenceDisplay
import matplotlib.pyplot as plt
import mlflow

# 1) Make a toy dataset where INCOME positively influences approval probability
rng = np.random.default_rng(42)
n = 5000

income = rng.normal(60_000, 15_000, n).clip(10_000, 150_000)  # annual income
debt_ratio = rng.uniform(0.05, 0.6, n)                        # debt-to-income
credit_score = rng.normal(680, 50, n).clip(500, 850)
age = rng.integers(21, 70, n)

# True underlying logit: income(+) + credit(+) - debt_ratio(-) + small noise
logit = (
    0.00003 * income + 
    0.008 * (credit_score - 650) - 
    2.0 * debt_ratio + 
    0.01 * (age - 30) + 
    rng.normal(0, 0.3, n)
)

p = 1 / (1 + np.exp(-logit))
approved = (rng.uniform(0, 1, n) < p).astype(int)

df = pd.DataFrame({
    "income": income,
    "debt_ratio": debt_ratio,
    "credit_score": credit_score,
    "age": age,
    "approved": approved
})

X = df[["income", "debt_ratio", "credit_score", "age"]]
y = df["approved"]

# 2) Train a simple model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=7, stratify=y)
clf = LogisticRegression(max_iter=2000)
clf.fit(X_train, y_train)

print("Test AUC:", roc_auc_score(y_test, clf.predict_proba(X_test)[:,1]).round(3))

# 3) PDP: show average effect of income on approval probability
fig, ax = plt.subplots(figsize=(7,5))
PartialDependenceDisplay.from_estimator(
    clf,
    X_test,
    features=["income"],
    kind="average",       # average effect across the dataset
    grid_resolution=50,
    ax=ax
)
ax.set_title("PDP: Effect of Income on Loan Approval Probability")
ax.set_ylabel("Predicted approval probability")
ax.set_xlabel("Annual income")
plt.tight_layout()
plt.show()

# 4) (Optional) Log the PDP to MLflow (works on Databricks)
with mlflow.start_run(run_name="pdp_income_example"):
    mlflow.log_metric("test_auc", roc_auc_score(y_test, clf.predict_proba(X_test)[:,1]))
    mlflow.sklearn.log_model(clf, "model")
    mlflow.log_artifact(local_path=None)  # no-op; just to show structure
    mlflow.log_figure(fig, "pdp_income.png")
