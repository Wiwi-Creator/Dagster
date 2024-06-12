### Running Dagster on a docker

```bash
pip install dagster-webserver
```
To run the webserver, use a command like the following

```bash
export DAGSTER_HOME=/opt/dagster/dagster_home
dagster-webserver -h 0.0.0.0 -p 3000
```

### Running the Dagster daemon
If you're using schedules, sensors, or backfills, or want to set limits on the number of runs that can be executed at once

you'll want to also run a dagster-daemon service as part of your deployment.
To run this service locally, run the following command:

```bash
pip install dagster
DAGSTER_HOME=/opt/dagster/dagster_home
dagster-daemon run
```
