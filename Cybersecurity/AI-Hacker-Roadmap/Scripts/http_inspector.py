# Day15-16
'''
import requests

url = "https://postman-echo.com/get?day=16"
# url = "https://postman-echo.com/test"

response = requests.get(url, timeout=10)

print("Method:", response.request.method)
print("URL:", response.url)
print("Status:", response.status_code)

content_type = response.headers.get("Content-Type", "(missing)")
server = response.headers.get("Server", "(missing)")
body_bytes = len(response.content)

print("Content-Type:", content_type)
print("Server:", server)
print("Body bytes:", body_bytes)
'''

# Day 20
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

import requests


ALLOWED_HOSTS = {"127.0.0.1", "localhost"}

urls = [
    "http://127.0.0.1:8000/",
    "http://127.0.0.1:8000/about.html",
]

results = []

for url in urls:
    host = urlparse(url).hostname
    if host not in ALLOWED_HOSTS:
        print(url, "| Blocked by allowlist")
        continue

    response = requests.get(url, timeout=10)
    item = {
        "url": url,
        "status": response.status_code,
        "content_type": response.headers.get("Content-Type", "(missing)"),
        "bytes": len(response.content),
        "sha256": hashlib.sha256(response.content).hexdigest()[:12],
    }
    results.append(item)

report = {
    "generated_at": datetime.now(timezone.utc).isoformat(),
    "scope": "localhost-only",
    "results": results,
}

output_path = Path("Scripts/output/day20-results.json")
output_path.parent.mkdir(parents=True, exist_ok=True)

with output_path.open("w", encoding="utf-8") as file:
    json.dump(report, file, ensure_ascii=False, indent=2)

print("Saved:", output_path)
