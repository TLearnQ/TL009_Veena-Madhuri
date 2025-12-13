import yaml
import json

def parse_openapi(file_path):
    with open(file_path, "r") as f:
        spec = yaml.safe_load(f)
    api_title = spec.get("info", {}).get("title")
    paths = spec.get("paths", {})
    endpoints = []
    for path, methods in paths.items():
        for method, details in methods.items():
            endpoints.append({
                "path": path,
                "method": method.upper(),
                "summary": details.get("summary"),
                "auth": spec.get("components", {}).get("securitySchemes", {}),
            })


    return {
        "title": api_title,
        "endpoint_count": len(endpoints),
        "endpoints": endpoints,
    }

if __name__ == "__main__":
    result = parse_openapi("3GPP_API_ASSIGNMENT\yamls\TS24549_NSCE_SliceInfo.yaml")
    print(json.dumps(result, indent=2))
    with open("output.json", "w") as out_file:
        json.dump(result, out_file, indent=2)
        print("Output written to output.json")