import requests
from bs4 import BeautifulSoup
import json
import time


def parse():
    search_phrases = ["transportation", "transport",
                      "mobility", "future transportation"]
    articles = []

    def search_parse():
        search_url = "https://search.techcrunch.com/search?p="
        n = 1
        for phrase in search_phrases:
            search_url += phrase
            search_url += "&b={n}"
            n += 10

    def base_parse():
        base_url = "https://techcrunch.com/category/startups/page/"

        for page in range(50, 100):
            try:
                r = requests.get(f"{base_url}{page}")
                soup = BeautifulSoup(r.text, "html.parser")

                for i, article in enumerate(soup.find_all("div", class_="post-block")):
                    title = article.find(
                        "h2", class_="post-block__title").text.replace("\n", "").replace("\t", "").strip()
                    url = article.find(
                        "a", class_="post-block__title__link")["href"]
                    date = article.find(
                        "time", class_="river-byline__time")["datetime"].split("T")[0]

                    article_request = requests.get(url)
                    article_soup = BeautifulSoup(
                        article_request.text, "html.parser")

                    if any(phrase in article_soup.text.lower() for phrase in search_phrases):
                        print("found ")

                        article_text = article_soup.find(
                            "div", class_="article-content").text.replace("\n", "").replace("\t", "").strip()

                        articles.append({
                            "title": title,
                            "text": article_text,
                            "url": url,
                            "date": date
                        })

                print(f"\n{page}\n")

            except Exception as e:
                print(e)

    json.dump(articles, open("articles.json", "w"), indent=4)
