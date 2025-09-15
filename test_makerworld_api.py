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
print("Status code:", response.status_code)

# Сначала покажем первые 1000 символов текста ответа
print("Raw response (first 1000 chars):")
print(response.text[:1000])

# Попробуем вывести JSON-структуру, если это возможно
try:
    data = response.json()
    print("\nParsed JSON (первые 2 ключа):")
    for k in list(data.keys())[:2]:
        print(f"{k}: {type(data[k])}")
    # Если это список, покажем первый элемент
    if isinstance(data, list) and len(data) > 0:
        print("\nFirst item in list:")
        print(data[0])
    # Если это словарь с ключом 'data' или 'list', покажем его часть
    if isinstance(data, dict):
        for key in ['data', 'list', 'result']:
            if key in data:
                print(f"\nKey '{key}' found, first 1 item(s):")
                if isinstance(data[key], list):
                    print(data[key][0])
                else:
                    print(data[key])
except Exception as e:
    print("Ошибка при разборе JSON:", e)
