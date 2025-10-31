import streamlit as st
import random
import requests

st.set_page_config(page_title="🧬 오늘의 바이오 뉴스", page_icon="🧫", layout="centered")

st.title("🧬 오늘의 바이오 뉴스")
st.markdown("버튼을 누르면 최신 바이오 관련 뉴스를 가져옵니다 🧠")

API_KEY = "72e33d9878c047a5ad99d48e429b470e"
URL = f"https://newsapi.org/v2/everything?q=bio OR biotechnology OR genetics&language=ko&sortBy=publishedAt&apiKey={API_KEY}"

if st.button("🔍 오늘의 바이오 뉴스 보기"):
    response = requests.get(URL)
    data = response.json()

    if data.get("articles"):
        articles = data["articles"]
        news = random.choice(articles)

        st.success(news["title"])
        if news.get("source"):
            st.write(f"📰 출처: {news['source'].get('name', 'Unknown')}")
        if news.get("url"):
            st.markdown(f"[👉 기사 보러가기]({news['url']})")
        if news.get("description"):
            st.markdown("**요약:** " + news["description"])
        if news.get("urlToImage"):
            st.image(news["urlToImage"], use_container_width=True)

        st.balloons()
    else:
        st.error("죄송합니다. 뉴스 데이터를 불러오지 못했습니다 😢")
else:
    st.info("⬆️ 버튼을 눌러 오늘의 바이오 뉴스를 확인하세요!")

st.markdown("---")
st.caption("Made with Streamlit · 바이오 상식 한 스푼 💡")

