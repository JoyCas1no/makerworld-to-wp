import requests
from bs4 import BeautifulSoup
from requests.auth import HTTPBasicAuth
import os

# --- Настройки ---
WP_URL = "https://printtechlab.ru/wp-json/wp/v2/pages/56"  # URL страницы WordPress (замени на свой, если нужно)
WP_USER = os.environ["WP_USER"]  # Логин WordPress из секретов
WP_APP_PASSWORD = os.environ["WP_APP_PASSWORD"]  # Пароль приложения из секретов

# --- Парсим MakerWorld ---
url = "https://makerworld.com/ru/popular"
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

models = []
for card in soup.find_all("a", class_="model-card")[:30]:
    title = card.find("div", class_="model-card-title")
    img = card.find("img")
    author = card.find("div", class_="model-card-author")
    models.append({
        "title": title.text.strip() if title else "—",
        "link": "https://makerworld.com" + card["href"],
        "image": img["src"] if img else "—",
        "author": author.text.strip() if author else "—"
    })
print("Найдено моделей:", len(models))

# --- Формируем HTML для WordPress ---
html = '<div class="makerworld-models">'
for m in models:
    html += f'''
    <div class="model-card" style="display:inline-block;width:220px;margin:10px;vertical-align:top;text-align:center;">
        <a href="{m["link"]}" target="_blank">
            <img src="{m["image"]}" alt="{m["title"]}" style="width:200px;height:200px;object-fit:cover;border-radius:12px;">
            <div style="font-weight:600;margin:8px 0 4px 0;">{m["title"]}</div>
            <div style="font-size:14px;color:#888;">{m["author"]}</div>
        </a>
    </div>
    '''
html += '</div>'

# --- Обновляем страницу WordPress через REST API ---
data = {
    "content": html
}

response = requests.post(
    WP_URL,
    auth=HTTPBasicAuth(WP_USER, WP_APP_PASSWORD),
    json=data
)

if response.status_code == 200:
    print("Страница успешно обновлена!")
else:
    print("Ошибка:", response.status_code, response.text)

    print("Ошибка:", response.status_code, response.text)

