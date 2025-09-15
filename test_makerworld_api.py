import requests

url = "https://makerworld.com/_next/data/2OEbsyoSr72B6dUpa5L-e/ru/3d-models.json"
headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
print("Status code:", response.status_code)

try:
    data = response.json()
    models = data["pageProps"]["designs"]
    print(f"Найдено моделей: {len(models)}")
    print("Пример первой модели:")
    from pprint import pprint
    pprint(models[0])
except Exception as e:
    print("Ошибка при разборе JSON:", e)
    print("Текст ответа:", response.text[:500])
