
import json
import yaml
data = {"config": {"Site": "Bangalore", "Devices": 12, "Status": "Open"}}
cleaned = {}
for k, v in data["config"].items():
    cleaned[k.lower()] = v
with open("clean_tickets.json", "w") as f:
    json.dump(cleaned, f, indent=2)
print("Cleaned Data:", cleaned)