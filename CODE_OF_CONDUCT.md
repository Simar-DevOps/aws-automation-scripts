# Contributing

- **Branching:** `feature/*`, `fix/*`, `chore/*`
- **Commits:** Conventional Commits (e.g., `feat: add s3 lifecycle rule`)
- **PRs:** Keep small. Fill the PR template. Link the **plan summary**.

## Local checks
```bash
terraform fmt -recursive
terraform validate
terraform plan -var-file=env/dev.tfvars.example


### `CODE_OF_CONDUCT.md`
```powershell
@'
# Code of Conduct

We follow the Contributor Covenant v2.1: https://www.contributor-covenant.org/version/2/1/code_of_conduct/

For incidents, contact the maintainers.
