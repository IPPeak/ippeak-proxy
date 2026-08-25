import requests

PROXY_HOST = "YOUR_PROXY_HOST"
PROXY_PORT = "YOUR_PROXY_PORT"
PROXY_USERNAME = "YOUR_PROXY_USERNAME"
PROXY_PASSWORD = "YOUR_PROXY_PASSWORD"

proxy = (
    f"socks5://{PROXY_USERNAME}:{PROXY_PASSWORD}"
    f"@{PROXY_HOST}:{PROXY_PORT}"
)

proxies = {
    "http": proxy,
    "https": proxy,
}

url = "https://httpbin.org/ip"

response = requests.get(
    url,
    proxies=proxies,
    timeout=30,
)

response.raise_for_status()

print("Proxy IP:")
print(response.text)
