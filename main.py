import requests
from bs4 import BeautifulSoup

def get_news():
    url = "https://news.naver.com/main/ranking/popularDay.naver"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    news_list = soup.select(".rankingnews_box .list_content a")

    result = []
    for idx, item in enumerate(news_list[:100], 1):
        title = item.get_text().strip()
        link = "https://news.naver.com" + item.get("href")
        result.append(f"{idx}. {title}\n{link}\n")

    return "\n".join(result)

if __name__ == "__main__":
    print(get_news())
