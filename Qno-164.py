def mock_api(page=1):
    if page > 3:
        return {"data": [], "next_page": None}
    return {"data": [f"user{page*1}", f"user{page*2}"], "next_page": page+1}
results = []
logs = []
page = 1
while page:
    resp = mock_api(page)
    results.extend(resp["data"])
    logs.append(f"Fetched page {page}")
    page = resp.get("next_page")

print("Results:", results)
print("Logs:", logs)