import requests

url = "https://makerworld.com/_next/data/2OEbsyoSr72B6dUpa5L-e/ru/3d-models.json"
headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
data = response.json()

models = data["pageProps"]["designs"]

print(f"Найдено моделей: {len(models)}")
print("Пример первой модели:")
print(models[0])
