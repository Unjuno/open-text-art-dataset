## Summary

Describe what this PR changes.

## Entry checklist

- [ ] I edited or added files under `data/entries/*.json`.
- [ ] I did not manually edit generated JSONL files unless regenerating them with `python scripts/build_jsonl.py`.
- [ ] Each entry is original or clearly licensed for this dataset.
- [ ] Each entry includes meaning, context, plain-text paraphrase, display requirements, and license metadata.
- [ ] I checked that the same `art` string is not already present.
- [ ] I ran `python scripts/validate_entries.py`.
- [ ] I ran `python scripts/build_jsonl.py`.
- [ ] I ran `python scripts/validate_jsonl.py data/samples.jsonl data/reviewed/v0.1.jsonl`.

## Notes for reviewers

Mention any uncertain license, cultural context, display dependency, or possible duplicate here.
