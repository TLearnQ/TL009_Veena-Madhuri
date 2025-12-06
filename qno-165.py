import json
import os
files = ["report1.json", "report2.json", "report3.json"]
processed = 0
failed = 0
errors = []
for file in files:
    try:
        processed += 1
        with open(file) as f:
            json.load(f)
    except Exception as e:
        failed += 1
        errors.append({"file": file, "error": str(e)})

print("Processed:", processed)
print("Failed:", failed)
print("Errors:", errors)