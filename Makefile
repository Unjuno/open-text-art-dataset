.PHONY: build validate validate-entries validate-jsonl validate-policy check duplicates

build:
	python scripts/build_jsonl.py

validate-entries:
	python scripts/validate_entries.py

validate-jsonl:
	python scripts/validate_jsonl.py data/samples.jsonl data/reviewed/v0.1.jsonl

validate-policy:
	python scripts/validate_dataset_policy.py

validate: validate-entries build validate-jsonl validate-policy

duplicates:
	python scripts/report_near_duplicates.py

check: validate duplicates
	git diff --exit-code
