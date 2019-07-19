# Python-Standard

[![Build Status](https://travis-ci.org/codecov/Python-Standard.svg?branch=master)](https://travis-ci.org/codecov/Python-Standard) [![codecov](https://codecov.io/gh/codecov/Python-Standard/branch/master/graph/badge.svg)](https://codecov.io/gh/codecov/Python-Standard)

### Last Updated: 07/19/19 16:31:03

## What is this?

This is a **Python** application, with basic unit tests, for which coverage is uploaded to Codecov on a daily basis. It can also serve as an example for how to integrate Codecov into your Python project. If the build is passing for this project, then Codecov's Python report processing is functional and correct on codecov.io.

## Configuration

This project is written in `Python 3.6`. Unit tests are written with the `pytest` framework and coverage reports are generated using `pytest-cov` plugin.

Unit tests: `/test_index.py`

## Reporting Issues

If you've discovered an issue with this repository or with Python processing in general, it is recommended to email support@codecov.io rather than post an issue here. This repository will not be checked regularly for open issues.

## Contributing

If you would like to contribute your own language specific standard to Codecov you can do so as follows:

1. Write a sample repository that contains Docker and docker-compose based orchestration for running your project easily locally
2. Your project should be as simple as possible while providing and testing the following functions:
   - A function that is fully tested and covered by tests
   - A function that is not tested at all
   - A function that contains a conditional with a tested if and/or else condition.
3. A TravisCI configuration that will run the tests and upload coverage to Codecov.

If your standard is accepted by Codecov you can transfer ownership to the Codecov Organization and will be accepted in our current [List of Standards](https://github.com/codecov/standards-scripts#list-of-standards) with credit given to the repository's original author. You can review the List of Standards to see which languages and frameworks currently need a standard submitted. If you create a standard please, email support@codecov.io with the subject line "New <Language> Standard Submission" and the team will review it for acceptance.
