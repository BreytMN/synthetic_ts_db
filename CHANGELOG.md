# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2023-06-11

### Added

- main.py script to generate white noise timeseries database
- Dockerfile to build the script with [python:3.11.4-slim-buster](https://hub.docker.com/_/python)
- docker-compose.yaml with a [PostgreSQL image](https://hub.docker.com/_/postgres) as dependency for the python script.