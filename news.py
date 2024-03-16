import requests
import json
import pyttsx3

def get_news():
    url = 'http://newsapi.org/v2/top-headlines?sources=spiegel-online&apiKey=ae5ccbe2006a4debbe6424d7e4b569ec'
    news = requests.get(url).json()
    articles = news.get('articles', [])
    return articles[:5]  # Nur die ersten fünf Artikel zurückgeben

def print_news(articles):
    if not articles:
        print("Fehler beim Abrufen der Nachrichten.")
        return
    print("Neueste Nachrichten von Spiegel Online:")
    for idx, article in enumerate(articles, start=1):
        title = article.get('title', 'N/A')
        description = article.get('description', 'N/A')
        print(f"{idx}. {title}")
        print(f"   {description}")
        print()
        speak(f"{title}. {description}")  # Den Text vorlesen

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def get_news_url():
    return 'http://newsapi.org/v2/top-headlines?sources=spiegel-online&apiKey=ae5ccbe2006a4debbe6424d7e4b569ec'

# Die Funktionen werden nur ausgeführt, wenn diese Datei als Hauptskript ausgeführt wird
if __name__ == "__main__":
    articles = get_news()
    print_news(articles)

    url = get_news_url()
    print("URL der News-API:", url)
