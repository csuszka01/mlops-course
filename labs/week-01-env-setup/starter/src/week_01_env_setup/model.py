from __future__ import annotations

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV

from .config import Settings


def train_logistic_regression(x_train, y_train, settings: Settings) -> Pipeline:
    """Train a scaled logistic regression model.

    Follows the standard Scikit-learn pattern: a Pipeline that chains
    preprocessing (StandardScaler) with an estimator, so the exact same
    transformation is applied at training and prediction time.
    https://scikit-learn.org/stable/getting_started.html
    """
    model = Pipeline(
        steps=[
            ("scaler", StandardScaler()),
            (
                "classifier",
                LogisticRegression(
                    max_iter=settings.max_iter,
                    random_state=settings.random_seed,
                ),
            ),
        ]
    )


    model.fit(x_train, y_train)
    return model

def train_random_forest(x_train, y_train, settings):
    model = Pipeline(
            steps=[
                #("scaler", StandardScaler()),
                (
                    "classifier",
                    RandomForestClassifier(
                        random_state=settings.random_seed,
                        n_estimators=80,
                        max_depth=20,
                        max_leaf_nodes=1000,
                        min_samples_split=5
                    ),
                ),
            ]
        )
    param_grid = {
    "classifier__n_estimators": [50, 100, 200],
    "classifier__max_depth": [None, 10, 20, 30],
    "classifier__max_leaf_nodes": [None, 10, 20, 50],
    }
    # 2. Instantiate GridSearchCV with your pipeline
    grid_search = GridSearchCV(
        estimator=model,
        param_grid=param_grid,
        cv=5,  # 5-fold cross-validation
        scoring="accuracy",  # Or your target metric
        n_jobs=-1,  # Use all available CPU cores
    )

    # 3. Fit on your training data
    grid_search.fit(x_train, y_train)

    # Access the best pipeline and hyperparameters
    best_model = grid_search.best_estimator_
    #best_params = grid_search.best_params_
    return best_model

def evaluate_model(model, x_test, y_test) -> dict:
    """Compute standard binary classification metrics on the test set."""
    predictions = model.predict(x_test)
    return {
        "accuracy": round(float(accuracy_score(y_test, predictions)), 4),
        "precision": round(float(precision_score(y_test, predictions)), 4),
        "recall": round(float(recall_score(y_test, predictions)), 4),
        "f1": round(float(f1_score(y_test, predictions)), 4),
    }
