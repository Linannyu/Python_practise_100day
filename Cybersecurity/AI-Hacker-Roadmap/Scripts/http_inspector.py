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
