from dagster import asset
from dagster_k8s import execute_k8s_job, pipeline


@asset
def launch_k8s_job(context):
    # Define the Kubernetes job configuration
    models = "bgdrug"
    image = "asia-east1-docker.pkg.dev/datapool-1806/data-kubernetes/dbt:latest"
    command = ["/bin/bash", "-c"]
    args = [f"dbt test --select {models}"]
    namespace = "default"

    # Execute the Kubernetes job
    execute_k8s_job(
        context=context,
        image=image,
        command=command,
        args=args,
        namespace=namespace,
    )


@pipeline
def my_pipeline():
    launch_k8s_job()
