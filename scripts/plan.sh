#!/usr/bin/env bash
set -euo pipefail
TFVARS_FILE="${1:-}" # optional var-file
if [[ -n "$TFVARS_FILE" && -f "$TFVARS_FILE" ]]; then
  terraform plan -input=false -out=tfplan.bin -var-file="$TFVARS_FILE"
else
  terraform plan -input=false -out=tfplan.bin
fi
echo "Plan saved to tfplan.bin"
