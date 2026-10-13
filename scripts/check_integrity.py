import hashlib
import json
import logging
from datetime import datetime, timezone
from pathlib import Path

project = Path.home() / "cybersecurity-lab/project-04-fim"
folder = project / "monitored_files"
baseline_file = project / "baseline.json"
log_file = project / "logs/fim.log"

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s UTC | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%S",
)
logging.Formatter.converter = __import__("time").gmtime

baseline = json.loads(baseline_file.read_text())
current = {}

for file_path in folder.rglob("*"):
    if file_path.is_file():
        file_hash = hashlib.sha256(file_path.read_bytes()).hexdigest()
        name = str(file_path.relative_to(folder))
        current[name] = file_hash

findings = 0

for name in sorted(baseline.keys() | current.keys()):
    if name not in baseline:
        message = f"NEW: {name}"
    elif name not in current:
        message = f"DELETED: {name}"
    elif baseline[name] != current[name]:
        message = f"MODIFIED: {name}"
    else:
        print(f"OK: {name} — no changes detected")
        continue

    findings += 1
    print(message)
    logging.warning(message)

if findings == 0:
    logging.info("Scan complete: no changes detected")

print(f"Scan complete. Findings: {findings}")
print(f"Log saved to: {log_file}")
