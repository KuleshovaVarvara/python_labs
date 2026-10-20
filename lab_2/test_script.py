import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

url = "https://sound-effects.ru/page/2/"
print(f"Отправляем запрос на {url}...")

response = requests.get(url, headers=headers)
print("Статус ответа:", response.status_code)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    titles = soup.find_all('div', class_='waveTitle')
    print(f"Найдено звуков на странице: {len(titles)}")

    for i, title in enumerate(titles[:5]):
        link = title.find('a')
        if link:
            print(f"{i+1}. {link.get('href')}")