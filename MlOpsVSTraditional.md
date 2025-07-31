
# MLflow vs No-MLflow: MLOps Capability Comparison

This document provides a side-by-side comparison of how core MLOps tasks are handled **with MLflow** versus **without MLflow**, particularly in Databricks or production environments.

| **MLOps Task**                  | **With MLflow**                                                   | **Without MLflow**                                                 |
|----------------------------------|---------------------------------------------------------------------|---------------------------------------------------------------------|
| **Experiment Tracking**         | `mlflow.log_param()`, `mlflow.log_metric()`, UI to compare runs     | Manually writing metrics in Excel, text files, or notebooks         |
| **Model Versioning**            | Auto-versioning in Model Registry                                  | Save as `model_v1.pkl`, `model_v2.joblib` in local/DBFS folders     |
| **Model Reproducibility**       | Tracks run code, parameters, environment                           | Requires manual documentation; no guaranteed reproducibility        |
| **Deployment: Batch**           | Load from Registry in Job, run scoring                             | Manually load file paths, hardcoded in notebooks                    |
| **Deployment: Real-Time**       | Use Mosaic AI Model Serving (REST endpoint, serverless)            | Build custom Flask/FastAPI + deploy on VM/K8s + handle infra        |
| **Model Registry**              | `mlflow.register_model()`, manage Staging → Production             | Folder naming or ad-hoc tracking with Google Sheets/Slack           |
| **Stage Promotion & Approval**  | MLflow UI or API (Staging → Prod), tagging, comments               | Manual “flagging” or renaming folders/files                         |
| **Inference Logging**           | Store predictions + inputs via `mlflow.log_metrics()` or Delta     | Need to manually log to CSV/Delta; hard to trace per model version  |
| **Drift Detection**             | Schedule checks via DLT, Delta + logs by model version             | Hard to automate; can't trace drift to model version easily         |
| **CI/CD Integration**           | Bundles + `mlflow.pyfunc` + GitHub Actions                         | Custom Bash scripts; fragile and error-prone                        |
| **Monitoring Dashboards**       | Delta tables + SQL dashboard per model/version                     | One-size-fits-all or no visibility                                  |
| **Rollback to Previous Version**| Click in Registry to revert to previous version                    | Manually reload older model file (if still available)               |
| **Environment Tracking**        | Conda/pip env saved with model artifact                            | Dev vs Prod mismatch risk high                                     |
| **Team Collaboration**          | Tags, comments, stage transitions, ownership                       | Tribal knowledge, Slack threads, informal review                    |

---

## Summary

Without MLflow, you're relying on manual, ad-hoc, and non-reproducible approaches.  
With MLflow, you gain a structured, traceable, and automatable MLOps workflow — especially powerful when integrated into the Databricks ecosystem.
“Here’s the reality. You can do MLOps without MLflow —
but it’s mostly manual, fragile, and unscalable.”

“MLflow provides a consistent layer across tracking, versioning, deployment, and monitoring —
and it works inside Databricks, on AWS, Azure, or even your laptop.”


# MLflow Functional Overview

This table provides a categorized list of **MLflow core functions**, showing the purpose and commonly used APIs in each area.

| **Category**              | **Functionality**                            | **MLflow APIs / Functions**                                                                 |
|---------------------------|-----------------------------------------------|----------------------------------------------------------------------------------------------|
| **Tracking**              | Log and visualize experiments                 | `mlflow.start_run()`, `mlflow.log_param()`, `mlflow.log_metric()`, `mlflow.log_artifact()`   |
|                           | Nested runs and run info                     | `mlflow.set_tag()`, `mlflow.get_run()`, `mlflow.end_run()`                                   |
|                           | Search/filter experiment runs                | `mlflow.search_runs()`                                                                       |
| **Projects**              | Package ML code for reproducibility           | `MLproject` file, `mlflow run <URI>`                                                         |
|                           | Define Conda or Docker environments           | `conda.yaml`, `docker_env` in MLproject                                                      |
| **Models**                | Log trained models                            | `mlflow.log_model()`, `mlflow.sklearn.log_model()`, `mlflow.keras.log_model()`               |
|                           | Load models for inference                     | `mlflow.pyfunc.load_model()`, `mlflow.sklearn.load_model()`                                  |
|                           | Serve models locally                          | `mlflow models serve -m <model_uri>`                                                         |
|                           | Evaluate models                               | `mlflow.evaluate()`                                                                          |
| **Model Registry**        | Register model                                | `mlflow.register_model()`, UI registry                                                       |
|                           | List and transition stages                    | `mlflow.get_registered_model()`, `mlflow.transition_model_version_stage()`                   |
|                           | Add metadata to model versions                | `mlflow.set_model_version_tag()`, `mlflow.delete_registered_model()`                         |
| **Deployment**            | Deploy model to REST endpoint (Databricks)    | Databricks Model Serving + Mosaic AI                                                         |
|                           | Deploy to other platforms                     | `mlflow.azureml`, `mlflow.sagemaker`, `mlflow.docker`, `mlflow.kubernetes`                   |
| **Evaluation & Validation**| Built-in model evaluation metrics             | `mlflow.evaluate()` with default or custom metrics                                            |
| **Pyfunc Interface**      | Create custom wrapper around any model        | `mlflow.pyfunc.PythonModel`, `load_context()`, `predict()`                                   |
| **Environment Logging**   | Save dependencies for reproducibility         | Auto logs `conda.yaml`, `requirements.txt`                                                   |
| **Artifacts**             | Log plots, images, files                      | `mlflow.log_artifact()`, `mlflow.log_artifacts()`                                            |
| **Utilities**             | Set experiment or run-level context           | `mlflow.set_experiment()`, `mlflow.set_tracking_uri()`                                       |

---

## Notes:
- **Tracking**: Works across any Python environment, local or cloud
- **Registry**: Enables model stage transitions and CI/CD integrations
- **Pyfunc**: Universal abstraction that allows serving any model like a function
- **Deployment**: Plug-and-play with Databricks, AWS, Azure, Kubernetes, and more
