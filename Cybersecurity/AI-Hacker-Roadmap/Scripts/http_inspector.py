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

"""Inspect allowlisted HTTP URLs and optionally save safe response summaries."""

import hashlib
import json
import argparse
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

import requests


ALLOWED_HOSTS = {"localhost", "127.0.0.1", "postman-echo.com"}
TIMEOUT_SECONDS = 10


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Inspect allowlisted HTTP URLs."
    )
    parser.add_argument("urls", nargs="+", help="One or more URLs to inspect")
    parser.add_argument("--output", help="Optional JSON output path")
    return parser.parse_args()


def summarize(url, response) -> dict:
    return {
        "url": url,
        "status": response.status_code,
        "content_type": response.headers.get("Content-Type", "(missing)"),
        "bytes": len(response.content),
        "sha256": hashlib.sha256(response.content).hexdigest()[:12],
    }


def inspect_url(url):
    host = urlparse(url).hostname
    if host not in ALLOWED_HOSTS:
        print(url, "| Blocked by allowlist")
        return None

    try:
        response = requests.get(url, timeout=TIMEOUT_SECONDS)
    except requests.RequestException as error:
        print(url, "| Request failed:", error)
        return None

    item = summarize(url, response)
    print(
        url,
        "|",
        item["status"],
        "|",
        item["content_type"],
        "|",
        item["bytes"],
        "|",
        item["sha256"],
    )
    return item


def save_report(output, results):
    report = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "scope": "allowlisted-hosts-only",
        "results": results,
    }

    output_path = Path(output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", encoding="utf-8") as file:
        json.dump(report, file, ensure_ascii=False, indent=2)

    print("Saved:", output_path)


def main():
    args = parse_arguments()
    results = []

    for url in args.urls:
        item = inspect_url(url)
        if item is not None:
            results.append(item)

    if args.output:
        save_report(args.output, results)


if __name__ == "__main__":
    main()
