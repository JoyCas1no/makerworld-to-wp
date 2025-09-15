import requests

url = "https://event.bblmw.com/web/makerworld"
payload = [
    {
        "sv": 1,
        "app_name": "MakerWorld",
        "app_ver": "",
        "os": "",
        "os_identifier": "",
        "uid": "3796870040"
    }
]
headers = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0"
}

response = requests.post(url, json=payload, headers=headers)
print(response.status_code)
print(response.text)  # или response.json() если получится
