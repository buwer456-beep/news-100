import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/news")
def news():
    url = "https://news.naver.com/main/ranking/popularDay.naver"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    news_list = []
    titles = soup.select(".rankingnews_box a")
    for idx, t in enumerate(titles[:100], start=1):
        title = t.get_text(strip=True)
        link = "https://news.naver.com" + t["href"]
        news_list.append({"rank": idx, "title": title, "link": link})

    return jsonify(news_list)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
