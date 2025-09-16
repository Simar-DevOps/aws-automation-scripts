#!/usr/bin/env bash
set -euo pipefail
terraform init -input=false
terraform fmt -recursive
terraform validate
