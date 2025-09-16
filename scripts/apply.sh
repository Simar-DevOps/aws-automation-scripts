#!/usr/bin/env bash
set -euo pipefail
if [[ ! -f tfplan.bin ]]; then
  echo "tfplan.bin not found. Run ./scripts/plan.sh first." >&2
  exit 1
fi
read -r -p "Apply tfplan.bin to current workspace? (y/N) " ans
[[ "${ans:-N}" =~ ^[Yy]$ ]] || { echo "Aborted."; exit 1; }
terraform apply tfplan.bin
