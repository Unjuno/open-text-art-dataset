# Branch protection setup

This repository should protect `main` before accepting external pull requests.

## Recommended settings

Go to:

```text
Repository → Settings → Branches → Branch protection rules → Add rule
```

Set the branch name pattern:

```text
main
```

Enable the following options:

- Require a pull request before merging
- Require approvals: `1`
- Require review from Code Owners
- Require status checks to pass before merging
- Require branches to be up to date before merging
- Required status check: `Validate dataset`
- Do not allow bypassing the above settings
- Restrict who can push to matching branches

## Why this matters

The dataset uses generated JSONL artifacts:

```text
data/samples.jsonl
data/reviewed/v0.1.jsonl
```

The source of truth is:

```text
data/entries/*.json
```

The `Validate dataset` workflow rebuilds JSONL artifacts and runs `git diff --exit-code`. If a contributor edits entries but forgets to rebuild generated files, CI fails. Branch protection should prevent such pull requests from being merged.

## Required workflow

Contributors should run:

```bash
python scripts/build_jsonl.py
make check
```

Maintainers should verify that the `Validate dataset` check is green before merging.

## Notes

If the required check name shown in GitHub differs, use the exact check name displayed in the latest successful Actions run.
