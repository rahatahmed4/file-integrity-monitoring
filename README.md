# Project 04 — File Integrity Monitoring (FIM)

## Overview
A Python-based Linux security tool that monitors files using SHA-256 cryptographic hashes. It compares current file hashes against a trusted baseline to identify unexpected changes.

## Security Objectives
- Detect modified files.
- Identify newly created files.
- Identify deleted files.
- Record findings with timestamps and severity levels.
- Support basic file-integrity investigation.

## Technologies
- Ubuntu Linux
- Python 3
- SHA-256
- JSON for baseline storage
- Python logging
- Git and GitHub

## Project Structure
```text
project-04-fim/
├── baseline.json
├── monitored_files/
│   └── sample.txt
├── scripts/
│   ├── create_baseline.py
│   └── check_integrity.py
├── logs/
└── README.md
```

## How It Works
1. The baseline script calculates the SHA-256 hash of each monitored file.
2. The hashes are stored in `baseline.json`.
3. The integrity checker calculates the current hashes.
4. It compares the current files against the baseline.
5. It reports new, modified, or deleted files and records findings in a log.

## How to Run

Create or refresh the baseline when the monitored files are in a trusted state:

```bash
python3 scripts/create_baseline.py
```

Check file integrity:

```bash
python3 scripts/check_integrity.py
```

Review recent log entries:

```bash
tail -n 10 logs/fim.log
```

## Validation Results

| Test scenario | Expected detection | Result |
|---|---|---|
| Unchanged file | No findings | Passed |
| Modified file | `MODIFIED` | Passed |
| New file | `NEW` | Passed |
| Deleted file | `DELETED` | Passed |
| Timestamped logging | Findings recorded in log | Verified |

These scenarios were tested in the Ubuntu environment using sample files.

## Limitations and Future Improvements
- The checker must currently be run manually.
- The baseline must be protected from unauthorized modification.
- Changes indicate a need for investigation; they do not prove malicious activity.
- A production implementation should use access controls, automated scheduling, alerting, and secure baseline storage.

## Learning Outcomes
- Working with SHA-256 hashes in Python.
- Reading and writing JSON data.
- Comparing filesystem state against a baseline.
- Investigating file-integrity alerts.
- Using Git and GitHub to maintain a security project.
