from urllib.parse import parse_qs, urlparse


def parse_url(url: str) -> dict:
    parsed = urlparse(url)
    return {
        "scheme": parsed.scheme,
        "host": parsed.hostname,
        "port": parsed.port,
        "path": parsed.path,
        "query": parsed.query,
        "parameters": parse_qs(parsed.query),
    }


test_url = "https://postman-echo.com/get?name=lin&day=17&topic=url"
# test_url = "http://127.0.0.1:8000/about.html"
# test_url = "https://postman-echo.com/get?tag=a&tag=b"

result = parse_url(test_url)
print(result)
