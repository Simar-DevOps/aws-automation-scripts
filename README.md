# AWS Automation Scripts — boto3 tools for EC2 / S3 / IAM

[![Python CI](https://github.com/Simar-DevOps/aws-automation-scripts/actions/workflows/python-ci.yml/badge.svg)](https://github.com/Simar-DevOps/aws-automation-scripts/actions/workflows/python-ci.yml)
![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Repo size](https://img.shields.io/github/repo-size/Simar-DevOps/aws-automation-scripts)

Small, practical Python scripts using **boto3** to manage common AWS tasks (EC2, S3, IAM). CI runs Black, Flake8, and Pytest on every PR.

---

## Contents
- [What’s here](#whats-here)
- [Prerequisites](#prerequisites)
- [Quick start](#quick-start)
- [Usage](#usage)
  - [IAM tools](#iam-tools)
  - [S3 tools](#s3-tools)
- [Development](#development)
- [CI / Branch protection](#ci--branch-protection)
- [License](#license)

---

## What’s here
- `iam_tools.py` — create users, manage inline policies, and create/delete access keys
- `s3_tools.py` — create buckets, upload/download files, list buckets/objects
- `tests/` — minimal sanity test (expand as you add features)
- CI: **Black** (format), **Flake8** (lint), **Pytest** (tests)

---

## Prerequisites
- Python **3.11+** (use the Windows **`py`** launcher or `python3` on macOS/Linux)
- AWS credentials configured locally (e.g., `aws configure` or env vars)

Optional, but recommended for dev:
- A virtual environment (`python -m venv .venv`)

---

## Quick start

```bash
# Windows PowerShell (example)
cd C:\Users\simar\aws-automation-scripts

# Create & activate a venv (optional but recommended)
py -m venv .venv
.\.venv\Scripts\Activate.ps1

# Install deps
py -m pip install --upgrade pip
py -m pip install boto3 black flake8 pytest
