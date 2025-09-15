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
    "User-Agent": "Mozilla/5.0",
    "Referer": "https://makerworld.com/",
    "Origin": "https://makerworld.com"
}

response = requests.post(url, json=payload, headers=headers)

print("Status code:", response.status_code)
print("Response length:", len(response.text))
print("Response text (первые 1000 символов):")
print(response.text[:1000])

try:
    data = response.json()
    print("\nJSON успешно разобран!")
    # Покажем структуру
    if isinstance(data, dict):
        print("Ключи:", list(data.keys()))
        for key in data:
            print(f"{key}: {type(data[key])}")
    elif isinstance(data, list):
        print("Это список, длина:", len(data))
        if len(data) > 0:
            print("Первый элемент:", data[0])
except Exception as e:
    print("Ошибка при разборе JSON:", e)
