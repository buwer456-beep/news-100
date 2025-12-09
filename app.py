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
import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd

st.title("📰 실시간 네이버 뉴스 Top 100")

# 네이버 뉴스 인기 랭킹 URL
url = "https://news.naver.com/main/ranking/popularDay.naver"

# 요청 헤더 추가 (네이버가 차단하지 않도록)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

# 웹페이지 가져오기
res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, "html.parser")

# 뉴스 제목과 링크 찾기
titles = [tag.text.strip() for tag in soup.select(".rankingnews_box .list_title")]
links = ["https://news.naver.com" + tag["href"] for tag in soup.select(".rankingnews_box .list_title")]

# 표 형태로 정리
news = pd.DataFrame({
    "제목": titles,
    "링크": links
})

# 화면에 출력
st.table(news)

st.write("⏱ 이 데이터는 웹에서 실시간으로 가져옵니다.")
