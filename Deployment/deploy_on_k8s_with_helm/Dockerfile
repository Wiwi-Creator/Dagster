FROM python:3.10-slim


# All packages are hard-pinned to `dagster`, so setting the version on just `DAGSTER` will ensure
# compatible versions.
RUN pip install -U uv
RUN python -m uv pip install \
    dagster==1.7.8 \
    dagster-postgres \
    dagster-gcp \
    dagster-k8s \
    dagster-celery[flower,redis,kubernetes] \
    dagster-celery-k8s

# Get example pipelines
COPY my_project/ /