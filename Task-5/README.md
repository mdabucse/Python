# Machine Learning Pipeline with Feature Engineering

## Overview

This project implements an **end-to-end Machine Learning pipeline** for customer churn prediction. It covers the complete workflow from **data generation → preprocessing → feature engineering → model training → evaluation → model selection → saving the final model**.

The pipeline is designed to mimic a **real-world production ML system**.

---

## Objective

Predict whether a customer will churn based on:

* Usage behavior
* Billing patterns
* Support activity
* Engagement metrics

---
## Key Features

* Synthetic dataset generation (~12,000 records)
* Missing value handling
* Feature engineering (derived features)
* Model comparison using 5-fold cross-validation
* Multiple ML models:

  * Logistic Regression
  * Random Forest
  * XGBoost
  * Support Vector Machine (SVM)
*  Evaluation using:

  * Accuracy
  * Precision
  * Recall
  * F1 Score
* Best model selection (based on F1)
* Feature importance extraction
* Model saving (`.pkl`)

---

##  Project Structure

```
Task-5/
│
├── data/
│   └── customer_data.csv
├── src/
│   ├── data_ingestion.py
│   ├── preprocessing.py
│   ├── feature_engineering.py
│   ├── train.py
├── main.py
└── README.md
```



## Sample Output

```
=== Data Ingestion ===
Loaded 12,453 records (11 features)
Missing values filled: billing_amount (2.1%), last_login_days_ago (5.4%)
Engineered 3 new features (avg_monthly_spend, support_freq_ratio, tenure_bin...)

=== Model Comparison (5-Fold Cross-Validation) ===
+-------------------------+-----------+-----------+----------+--------+
| Model                   | Accuracy  | Precision | Recall   | F1     |
+-------------------------+-----------+-----------+----------+--------+
| Logistic Regression     | 0.812     | 0.743     | 0.681    | 0.711  |
| Random Forest           | 0.874     | 0.831     | 0.789    | 0.809  |
| XGBoost                 | 0.891     | 0.856     | 0.812    | 0.833  |
| SVM (RBF kernel)        | 0.853     | 0.802     | 0.756    | 0.778  |
+-------------------------+-----------+-----------+----------+--------+

=== Best Model: XGBoost ===
Hyperparameters: {max_depth: 6, learning_rate: 0.05, n_estimators: 350}
```

