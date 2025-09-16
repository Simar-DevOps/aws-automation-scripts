\# Contributing



Thanks for helping!



\- \*\*Branching:\*\* `feature/\*`, `fix/\*`, `chore/\*`

\- \*\*Commits:\*\* Use Conventional Commits (e.g., `feat: add s3 lifecycle rule`, `fix: correct bucket policy`)

\- \*\*PRs:\*\* Keep small, fill the PR template, link the \*\*plan summary\*\*, call out \*\*risk\*\* and \*\*rollback\*\*.



\## Local checks



```bash

terraform fmt -recursive

terraform validate

terraform plan -var-file=env/dev.tfvars.example



