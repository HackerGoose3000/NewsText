# news.py
import requests
from newspaper import Article
import os

_article_cache = {}

def fetch_news():
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={os.getenv('NEWSAPI_KEY')}"
    r = requests.get(url)
    return r.json().get("articles", [])

def summarize_article(url):
    if url in _article_cache:
        return _article_cache[url]
    try:
        a = Article(url)
        a.download()
        a.parse()
        a.nlp()
        _article_cache[url] = a.summary
        return a.summary
    except:
        return None
