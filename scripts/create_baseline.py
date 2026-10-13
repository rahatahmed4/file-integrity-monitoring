import hashlib
import json
from pathlib import Path

project = Path.home() / "cybersecurity-lab/project-04-fim"
folder = project / "monitored_files"
baseline_file = project / "baseline.json"

baseline = {}

for file_path in folder.rglob("*"):
    if file_path.is_file():
        file_hash = hashlib.sha256(file_path.read_bytes()).hexdigest()
        baseline[str(file_path.relative_to(folder))] = file_hash

baseline_file.write_text(json.dumps(baseline, indent=4))

print(f"Baseline created for {len(baseline)} file(s).")
print(f"Saved to: {baseline_file}")
