import json
import yaml
with open("wifi_access_points.yaml") as f:
    data = yaml.safe_load(f)
collections = {}
for ap in data:
    key = ap.get("region", ap.get("status", "Unknown"))
    collections.setdefault(key, []).append(ap)
for key, items in collections.items():
    with open(f"{key}_wifi.json", "w") as f:
        json.dump(items, f, indent=2)
print("Wi-Fi access points split and saved.")
        