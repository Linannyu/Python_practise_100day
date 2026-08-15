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

# Day 19
import hashlib
from urllib.parse import urlparse

import requests


ALLOWED_HOSTS = {"127.0.0.1", "localhost"}

home_url = "http://127.0.0.1:8000/"
about_url = "http://127.0.0.1:8000/about.html"
urls = [home_url, about_url]


def summarize(response) -> dict:
    return {
        "status": response.status_code,
        "content_type": response.headers.get("Content-Type", "(missing)"),
        "bytes": len(response.content),
        "sha256": hashlib.sha256(response.content).hexdigest()[:12],
    }


summaries = {}

for url in urls:
    host = urlparse(url).hostname
    if host not in ALLOWED_HOSTS:
        print(url, "| Blocked by allowlist")
        continue

    response = requests.get(url, timeout=10)
    summaries[url] = summarize(response)

home_summary = summaries[home_url]
about_summary = summaries[about_url]

print("field | home | about | comparison")
for key in home_summary:
    result = "same" if home_summary[key] == about_summary[key] else "different"
    print(key, "|", home_summary[key], "|", about_summary[key], "|", result)
