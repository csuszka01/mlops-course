# 1 

    - Csak azokat a kéréseket nem szolgálta ki amikben más vagy más sorrendű oszlopok voltak
    
    - A glucose 0 lehet valid input, ha azt jelzi, hogy nem mérték, de a modellig nem szabad eljutnia ilyen formában. A glucose -50, age 250 bmi 336 nem juthat el a modellig, a data contract szerint invalid értékek
    
    - Nem látjuk melyik modell verzió, alias válaszolt, azt sem hogy milyen magabiztossággal (probability)

 ## 1:
  curl -w '\n%{http_code}\n' -X POST localhost:5540/invocations -H 'Content-Type: application/json' -d '{"dataframe_split": {"columns": ["pregnancies", "glucose", "blood_pressure", "skin_thickness", "insulin", "bmi", "diabetes_pedigree", "age"], "data": [[6, 148, 72, 35, 125, 33.6, 0.627, 50]]}}'

 - pred: 1, status: 200 OK

 ## 2:
  curl -w '\n%{http_code}\n' -X POST localhost:5540/invocations -H 'Content-Type: application/json' -d '{"dataframe_split": {"columns": ["pregnancies", "glucose", "blood_pressure", "skin_thickness", "insulin", "bmi", "diabetes_pedigree", "age"], "data": [[6, 0, 72, 35, 125, 33.6, 0.627, 50]]}}'

  - pred: 0, status: 200 OK

 ## 3:
    curl -w '\n%{http_code}\n' -X POST localhost:5540/invocations -H 'Content-Type: application/json' -d '{"dataframe_split": {"columns": ["pregnancies", "glucose", "blood_pressure", "skin_thickness", "insulin", "bmi", "diabetes_pedigree", "age"], "data": [[6, -50, 72, 35, 125, 33.6, 0.627, 50]]}}'

 - pred: 0, status: 200 OK

 ## 4:
    curl -w '\n%{http_code}\n' -X POST localhost:5540/invocations -H 'Content-Type: application/json' -d '{"dataframe_split": {"columns": ["pregnancies", "glucose", "blood_pressure", "skin_thickness", "insulin", "bmi", "diabetes_pedigree", "age"], "data": [[6, 148, 72, 35, 125, 336, 0.627, 250]]}}'

 - pred: 1, status: 200 OK

 ## 5:
    curl -w '\n%{http_code}\n' -X POST localhost:5540/invocations -H 'Content-Type: application/json' -d '{"dataframe_split": {"columns": ["pregnancies", "glucose", "blood_pressure", "skin_thickness", "insulin", "bmi", "diabetes_pedigree", "age", "cholesterol"], "data": [[6, 148, 72, 35, 125, 33,6, 0.627, 50, 15]]}}'

 - status: 400 Bad request

 - trace:   {"error_code": "BAD_REQUEST", "message": "Invalid input. Provided dataframe_split field is not a valid dataframe representation in 'split' format. Error: '9 columns passed, passed data had 10 columns'", "sqlstate": "KAM00", "error_class": "INVALID_PARAMETER_VALUE"}
    400
 ## 6:
    curl -w '\n%{http_code}\n' -X POST localhost:5540/invocations -H 'Content-Type: application/json' -d '{"dataframe_split": {"columns": ["pregnancies", "glucose", "blood_pressure", "skin_thickness", "insulin", "diabetes_pedigree", "age"], "data": [[6, 148, 72, 35, 125, 0.627, 50]]}}'

 - status: 400 Bad request

 - trace: 
    {"error_code": "BAD_REQUEST", "message": "Encountered an unexpected error while evaluating the model. Verify that the serialized input Dataframe is compatible with the model for inference.", "sqlstate": "KAM00", "error_class": "INVALID_PARAMETER_VALUE", "stack_trace": "Traceback (most recent call last):\n  File \"/home/csuszka/Documents/egyetem/mlops-course/labs/week-09-serving/starter/.venv/lib64/python3.14/site-packages/mlflow/pyfunc/scoring_server/__init__.py\", line 341, in invocations\n    raw_predictions = model.predict(data, params=params)\n  File \"/home/csuszka/Documents/egyetem/mlops-course/labs/week-09-serving/starter/.venv/lib64/python3.14/site-packages/mlflow/pyfunc/__init__.py\", line 845, in predict\n    return self._predict(data, params)\n           ~~~~~~~~~~~~~^^^^^^^^^^^^^^\n  File \"/home/csuszka/Documents/egyetem/mlops-course/labs/week-09-serving/starter/.venv/lib64/python3.14/site-packages/mlflow/pyfunc/__init__.py\", line 895, in _predict\n    return self._predict_fn(data, params=params)\n           ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^\n  File \"/home/csuszka/Documents/egyetem/mlops-course/labs/week-09-serving/starter/.venv/lib64/python3.14/site-packages/mlflow/sklearn/__init__.py\", line 632, in predict\n    return self.sklearn_model.predict(data)\n           ~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^\n  File \"/home/csuszka/Documents/egyetem/mlops-course/labs/week-09-serving/starter/.venv/lib64/python3.14/site-packages/sklearn/pipeline.py\", line 796, in predict\n    Xt = transform.transform(Xt)\n  File \"/home/csuszka/Documents/egyetem/mlops-course/labs/week-09-serving/starter/.venv/lib64/python3.14/site-packages/sklearn/utils/_set_output.py\", line 319, in wrapped\n    data_to_wrap = f(self, X, *args, **kwargs)\n  File \"/home/csuszka/Documents/egyetem/mlops-course/labs/week-09-serving/starter/.venv/lib64/python3.14/site-packages/sklearn/impute/_base.py\", line 617, in transform\n    X = self._validate_input(X, in_fit=False)\n  File \"/home/csuszka/Documents/egyetem/mlops-course/labs/week-09-serving/starter/.venv/lib64/python3.14/site-packages/sklearn/impute/_base.py\", line 375, in _validate_input\n    raise ve\n  File \"/home/csuszka/Documents/egyetem/mlops-course/labs/week-09-serving/starter/.venv/lib64/python3.14/site-packages/sklearn/impute/_base.py\", line 356, in _validate_input\n    X = validate_data(\n        self,\n    ...<6 lines>...\n        copy=self.copy,\n    )\n  File \"/home/csuszka/Documents/egyetem/mlops-course/labs/week-09-serving/starter/.venv/lib64/python3.14/site-packages/sklearn/utils/validation.py\", line 3013, in validate_data\n    _check_feature_names(_estimator, X, reset=reset)\n    ~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/home/csuszka/Documents/egyetem/mlops-course/labs/week-09-serving/starter/.venv/lib64/python3.14/site-packages/sklearn/utils/validation.py\", line 2865, in _check_feature_names\n    raise ValueError(message)\nValueError: The feature names should match those that were passed during fit.\nFeature names seen at fit time, yet now missing:\n- bmi\n\n"} 

 ## 7
    curl -w '\n%{http_code}\n' -X POST localhost:5540/invocations -H 'Content-Type: application/json' -d '{"dataframe_split": {"columns": ["glucose", "pregnancies", "blood_pressure", "skin_thickness", "insulin", "bmi", "diabetes_pedigree", "age"], "data": [[148, 6, 72, 35, 125, 33.6, 0.627, 50]]}}'

 - status: 400 Bad request

 - trace:
    {"error_code": "BAD_REQUEST", "message": "Encountered an unexpected error while evaluating the model. Verify that the serialized input Dataframe is compatible with the model for inference.", "sqlstate": "KAM00", "error_class": "INVALID_PARAMETER_VALUE", "stack_trace": "Traceback (most recent call last):\n  File \"/home/csuszka/Documents/egyetem/mlops-course/labs/week-09-serving/starter/.venv/lib64/python3.14/site-packages/mlflow/pyfunc/scoring_server/__init__.py\", line 341, in invocations\n    raw_predictions = model.predict(data, params=params)\n  File \"/home/csuszka/Documents/egyetem/mlops-course/labs/week-09-serving/starter/.venv/lib64/python3.14/site-packages/mlflow/pyfunc/__init__.py\", line 845, in predict\n    return self._predict(data, params)\n           ~~~~~~~~~~~~~^^^^^^^^^^^^^^\n  File \"/home/csuszka/Documents/egyetem/mlops-course/labs/week-09-serving/starter/.venv/lib64/python3.14/site-packages/mlflow/pyfunc/__init__.py\", line 895, in _predict\n    return self._predict_fn(data, params=params)\n           ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^\n  File \"/home/csuszka/Documents/egyetem/mlops-course/labs/week-09-serving/starter/.venv/lib64/python3.14/site-packages/mlflow/sklearn/__init__.py\", line 632, in predict\n    return self.sklearn_model.predict(data)\n           ~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^\n  File \"/home/csuszka/Documents/egyetem/mlops-course/labs/week-09-serving/starter/.venv/lib64/python3.14/site-packages/sklearn/pipeline.py\", line 796, in predict\n    Xt = transform.transform(Xt)\n  File \"/home/csuszka/Documents/egyetem/mlops-course/labs/week-09-serving/starter/.venv/lib64/python3.14/site-packages/sklearn/utils/_set_output.py\", line 319, in wrapped\n    data_to_wrap = f(self, X, *args, **kwargs)\n  File \"/home/csuszka/Documents/egyetem/mlops-course/labs/week-09-serving/starter/.venv/lib64/python3.14/site-packages/sklearn/impute/_base.py\", line 617, in transform\n    X = self._validate_input(X, in_fit=False)\n  File \"/home/csuszka/Documents/egyetem/mlops-course/labs/week-09-serving/starter/.venv/lib64/python3.14/site-packages/sklearn/impute/_base.py\", line 375, in _validate_input\n    raise ve\n  File \"/home/csuszka/Documents/egyetem/mlops-course/labs/week-09-serving/starter/.venv/lib64/python3.14/site-packages/sklearn/impute/_base.py\", line 356, in _validate_input\n    X = validate_data(\n        self,\n    ...<6 lines>...\n        copy=self.copy,\n    )\n  File \"/home/csuszka/Documents/egyetem/mlops-course/labs/week-09-serving/starter/.venv/lib64/python3.14/site-packages/sklearn/utils/validation.py\", line 3013, in validate_data\n    _check_feature_names(_estimator, X, reset=reset)\n    ~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/home/csuszka/Documents/egyetem/mlops-course/labs/week-09-serving/starter/.venv/lib64/python3.14/site-packages/sklearn/utils/validation.py\", line 2865, in _check_feature_names\n    raise ValueError(message)\nValueError: The feature names should match those that were passed during fit.\nFeature names must be in the same order as they were in fit.\n\n"}

# 3

# 4

