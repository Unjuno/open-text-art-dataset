## Summary

Describe what this PR changes.

## File scope

For normal data-entry PRs, please only change:

```text
data/entries/text-art-*.json
data/samples.jsonl
data/reviewed/v0.1.jsonl
README.md dataset count
```

Generated files and the README dataset count should change only as the result of running `make sync`.

Do not mix normal data-entry changes with changes to workflows, scripts, schemas, or license-policy files. Open a separate maintainer-discussion PR for those changes.

## Entry checklist

- [ ] I edited or added files under `data/entries/text-art-*.json`.
- [ ] I regenerated generated files and README count with `make sync`.
- [ ] I did not manually edit generated JSONL files outside the generated output.
- [ ] Each entry is original or clearly licensed for this dataset.
- [ ] Each entry includes meaning, context, plain-text paraphrase, display requirements, and license metadata.
- [ ] I checked that the same `art` string is not already present.
- [ ] I ran `make check`.

## Notes for reviewers

Mention any uncertain license, cultural context, display dependency, or possible duplicate here.
