### Running Dagster as a service
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





# etl

Welcome to your new Dagster repository.

### Contents

| Name                     | Description                                                                       |
| ------------------------ | --------------------------------------------------------------------------------- |
| `README.md`              | A description and guide for this code repository                                  |
| `setup.py`               | A build script with Python package dependencies for this code repository          |
| `workspace.yaml`         | A file that specifies the location of the user code for Dagit and the Dagster CLI |
| `etl/`       | A Python directory that contains code for your Dagster repository                 |
| `etl_tests/` | A Python directory that contains tests for `etl`                      |

## Getting up and running

 Create a new Python environment and activate.

## Local Development

1. Set the `DAGSTER_HOME` environment variable. Dagster will store run history in this directory.

```base
mkdir ~/dagster_home
export DAGSTER_HOME=~/dagster_home
```

2. Start the [Dagit process](https://docs.dagster.io/overview/dagit). This will start a Dagit web
server that, by default, is served on http://localhost:3000.

```bash
dagit
```

3. (Optional) If you want to enable Dagster
[Schedules](https://docs.dagster.io/overview/schedules-sensors/schedules) or
[Sensors](https://docs.dagster.io/overview/schedules-sensors/sensors) for your jobs, start the
[Dagster Daemon process](https://docs.dagster.io/overview/daemon#main) **in a different shell or terminal**:

```bash
dagster-daemon run
```

## Local Testing

Tests can be found in `etl_tests` and are run with the following command:

```bash
pytest etl_tests
```

As you create Dagster ops and graphs, add tests in `etl_tests/` to check that your
code behaves as desired and does not break over time.

For hints on how to write tests for ops and graphs in Dagster,
[see our documentation tutorial on Testing](https://docs.dagster.io/tutorial/testable).
