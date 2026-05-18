.PHONY: build validate check duplicates

build:
	python scripts/build_jsonl.py

validate:
	python scripts/validate_entries.py
	python scripts/validate_jsonl.py data/samples.jsonl data/reviewed/v0.1.jsonl

duplicates:
	python scripts/report_near_duplicates.py

check: validate build duplicates
	git diff --exit-code
