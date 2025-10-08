# AWS Automation Scripts — boto3 tools for EC2 / S3 / IAM

[![CI](https://img.shields.io/github/actions/workflow/status/Simar-DevOps/aws-automation-scripts/python-ci.yml?label=Python%20CI&logo=github-actions)](https://github.com/Simar-DevOps/aws-automation-scripts/actions)
(https://github.com/Simar-DevOps/aws-automation-scripts/actions)
![Python](https://img.shields.io/badge/Python-3.11%2B-informational)
![Code style: Black](https://img.shields.io/badge/code%20style-Black-000000.svg)
[![License](https://img.shields.io/badge/License-MIT-informational)](LICENSE)

Small, practical **boto3** helpers for common AWS tasks (EC2, S3, IAM).  
This repo is part of my DevOps bootcamp portfolio.

## What’s here
- `ec2_manage.py` — start/stop EC2 by tag or id  
- `s3_tools.py` — create buckets, upload/download, list buckets/objects  
- `iam_tools.py` — create users, attach policies, create access keys  
- `tests/` — light sanity tests

## Notes
- Designed for clarity over features; easy to extend per task.
- Consistent formatting and linting via Black + Flake8.

## CI / Branch protection
- Every pull request runs **Black**, **Flake8**, and **Pytest**  
  (see .github/workflows/python-ci.yml)
- `main` is protected; PR checks must pass before merge.

## License
MIT © Simarjit Singh
