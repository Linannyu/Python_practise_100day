import requests

url = "https://postman-echo.com/get?day=15"
response = requests.get(url, timeout=10)

print("Method:", response.request.method)
print("URL:", response.url)
print("Status:", response.status_code)
