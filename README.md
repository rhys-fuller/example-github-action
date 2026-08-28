# example-github-action

An example repo for testing GitHub Actions.

## Replace DEV with PRD

The workflow at [.github/workflows/replace-dev-with-prd.yml](.github/workflows/replace-dev-with-prd.yml) runs whenever a push is made to the `main` branch (pushes to other branches are ignored).

It:

1. Determines exactly which files were changed by the push (using the before/after commit SHAs from the push event).
2. Runs [.github/scripts/replace_dev_with_prd.py](.github/scripts/replace_dev_with_prd.py) against only those files, replacing every occurrence of the substring `DEV` with `PRD`.
3. Commits and pushes the changes back to `main` if any files were modified.

This repo's `pipelines/` folder contains sample JSON files (e.g. `service_one_DEV`) used to demonstrate the substitution.
