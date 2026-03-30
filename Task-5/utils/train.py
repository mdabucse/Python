import pandas as pd
from sklearn.model_selection import cross_validate
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

from xgboost import XGBClassifier

from tabulate import tabulate


def train_and_compare(df):
    X = df.drop(columns=['churn', 'customer_id'])
    y = df['churn']

    # Identify Column Types
    categorical_cols = X.select_dtypes(include=['object']).columns
    numeric_cols = X.select_dtypes(exclude=['object']).columns

    # Preprocessing Pipeline
    preprocessor = ColumnTransformer([
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_cols),
        ('num', 'passthrough', numeric_cols)
    ])

    # Models
    models = {
        "Logistic Regression": LogisticRegression(max_iter=500),
        "Random Forest": RandomForestClassifier(n_estimators=150),
        "XGBoost": XGBClassifier(
            max_depth=6,
            learning_rate=0.05,
            n_estimators=200,
            eval_metric='logloss'
        ),
        "SVM (RBF kernel)": SVC(kernel='rbf')
    }

    # Evaluation Metrics
    scoring = ['accuracy', 'precision', 'recall', 'f1']

    results = []

    print("\n=== Model Comparison (5-Fold Cross-Validation) ===")

    for name, model in models.items():
        pipeline = Pipeline([
            ('preprocessor', preprocessor),
            ('model', model)
        ])

        scores = cross_validate(
            pipeline,
            X,
            y,
            cv=5,
            scoring=scoring
        )

        results.append([
            name,
            round(scores['test_accuracy'].mean(), 3),
            round(scores['test_precision'].mean(), 3),
            round(scores['test_recall'].mean(), 3),
            round(scores['test_f1'].mean(), 3)
        ])

    # Print Table
    headers = ["Model", "Accuracy", "Precision", "Recall", "F1"]

    print(tabulate(results, headers=headers, tablefmt="grid"))

    return results