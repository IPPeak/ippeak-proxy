import requests

PROXY_HOST = "YOUR_PROXY_HOST"
PROXY_PORT = "YOUR_PROXY_PORT"
PROXY_USERNAME = "YOUR_PROXY_USERNAME"
PROXY_PASSWORD = "YOUR_PROXY_PASSWORD"

proxy = (
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}"
    f"@{PROXY_HOST}:{PROXY_PORT}"
)

proxies = {
    "http": proxy,
    "https": proxy,
}

session = requests.Session()
session.proxies.update(proxies)

url = "https://httpbin.org/ip"

for i in range(3):
    response = session.get(
        url,
        timeout=30,
    )

    response.raise_for_status()

    print(f"Request {i + 1}:")
    print(response.text)
