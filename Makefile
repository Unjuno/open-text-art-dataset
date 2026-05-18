.PHONY: build validate validate-entries validate-jsonl check duplicates

build:
	python scripts/build_jsonl.py

validate-entries:
	python scripts/validate_entries.py

validate-jsonl:
	python scripts/validate_jsonl.py data/samples.jsonl data/reviewed/v0.1.jsonl

validate: validate-entries build validate-jsonl

duplicates:
	python scripts/report_near_duplicates.py

check: validate duplicates
	git diff --exit-code
