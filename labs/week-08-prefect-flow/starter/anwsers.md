### 2.

1. - Prefect provides:
        - how long each task took
        - when and what actually ran
        - how many attempts, failed or success
   - DVC provides:
        - content hashes

2. - DVC is single source of truth, with dvc.yaml defining stages, rater than coding it in the python function run_pipeline. Splitting to separate tasks increases observability and more control for tasks that need it. 

### 5.

1. - Gate GO is necessarry, but not enough proof deploying model is the right decision. Human approval is needed, to determine if promotion can proceed.

2. - Run outcomes and performance, failures. Performance to ML engineers, infra fails or issues upon code updates to developers.

3. - Maybe just a warning to a channel on the first fail, and a direct message on the second concurrent fail to ensure notification is read by the pipeline maintaining team.

4. - A job that failed to run in the first place, gets ignored.