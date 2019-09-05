# Python-Standard

[![Build Status](https://travis-ci.org/codecov/Python-Standard.svg?branch=master)](https://travis-ci.org/codecov/Python-Standard) [![codecov](https://codecov.io/gh/codecov/Python-Standard/branch/master/graph/badge.svg)](https://codecov.io/gh/codecov/Python-Standard)

### Last Updated: 09/05/19 18:33:51

## What is this?

This is a **Python** application, with basic unit tests, for which coverage is uploaded to Codecov on a daily basis. It can also serve as an example for how to integrate Codecov into your Python project. If the build is passing for this project, then Codecov's Python report processing is functional and correct on codecov.io.

## Configuration

This project is written in `Python 3.6`. Unit tests are written with the `pytest` framework and coverage reports are generated using the `pytest-cov` plugin.

Unit tests: `/test_index.py`

Inside `.travis.yml` file:
```yaml
install:
  - pip install codecov
  - pip install pytest-cov
script:
  - pytest --cov=./ --cov-report=xml
  - codecov
```

## Usage

Run unit tests inside a Docker container
```bash
docker-compose up
```

Generate coverage reports via `pytest`
```bash
pytest --cov=./ --cov-report=xml
```

Uploading reports to Codecov
```bash
bash <(curl https://codecov.io/bash)

OR

pip install codecov
codecov
```

## Reporting Issues

If you've discovered an issue with this repository or with Python processing in general, it is recommended to email support@codecov.io rather than post an issue here. This repository will not be checked regularly for open issues.

## Contributing

Contributions are welcome! If you'd like to contribute to this repository, feel free to open a pull request or flag an issue. If you would like to contribute a new lanaguage standard, [you can get more information here](https://github.com/codecov/standards-scripts/blob/master/README.md#contributing). 
