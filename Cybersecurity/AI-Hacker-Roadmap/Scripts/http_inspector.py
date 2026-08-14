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

# Day 18
from urllib.parse import urlparse
import requests

ALLOWED_HOSTS = {"127.0.0.1", "localhost"}

urls = [
    "http://127.0.0.1:8000/",
    "http://127.0.0.1:8000/about.html",
    "http://127.0.0.1:8000/missing.html",
]

for url in urls:
    host = urlparse(url).hostname
    if host not in ALLOWED_HOSTS:
        print(url, "| Blocked by allowlist")
        continue

    response = requests.get(url, timeout=10)
    content_type = response.headers.get("Content-Type", "(missing)")
    body_bytes = len(response.content)
    print(url, "|", response.status_code, "|", content_type, "|", body_bytes)
