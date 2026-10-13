# Project 04 — File Integrity Monitoring (FIM)

A Python security tool that uses SHA-256 hashes to detect file modifications, new files, and deletions.

## Tools
- Ubuntu Linux
- Python 3
- SHA-256
- JSON and Python logging

## Run
Create baseline: `python3 scripts/create_baseline.py`

Check integrity: `python3 scripts/check_integrity.py`

## Test Results
- Modified file detection: passed
- New file detection: passed
- Deleted file detection: passed
- Timestamped logging: verified

## Limitation
This is a manually executed prototype. A detected change is a signal for investigation, not proof of malicious activity.
