import random
import textwrap
import streamlit as st
import plotly.graph_objects as go
import reverse_geocoder as rg

try:
    import wikipedia
    WIKI_AVAILABLE = True
except Exception:
    WIKI_AVAILABLE = False

st.set_page_config(page_title="랜덤 여행지 추천기", page_icon="🌍", layout="centered")

# ---------- 유틸 ----------
CONTINENTS = {
    "KR": "Asia", "JP": "Asia", "CN": "Asia", "VN": "Asia", "TH": "Asia", "MY": "Asia", "SG": "Asia",
    "ID": "Asia", "PH": "Asia", "IN": "Asia", "NP": "Asia", "BD": "Asia", "LK": "Asia",
    "FR": "Europe", "DE": "Europe", "IT": "Europe", "ES": "Europe", "PT": "Europe", "GB": "Europe",
    "US": "North America", "CA": "North America", "MX": "North America",
    "BR": "South America", "AR": "South America", "CL": "South America", "PE": "South America",
    "AU": "Oceania", "NZ": "Oceania",
    "ZA": "Africa", "EG": "Africa", "MA": "Africa", "KE": "Africa", "TZ": "Africa",
}

@st.cache_data(show_spinner=False)
def get_random_coord():
    lat = random.uniform(-60, 75)
    lon = random.uniform(-180, 180)
    return (lat, lon)

@st.cache_data(show_spinner=False)
def nearest_place(lat, lon):
    result = rg.search((lat, lon), mode=1)[0]
    return {
        "name": result.get("name"),
        "admin1": result.get("admin1"),
        "country_code": result.get("cc"),
        "lat": float(result.get("lat")),
        "lon": float(result.get("lon")),
    }

@st.cache_data(show_spinner=False)
def wiki_summary(title: str, lang: str = "ko", sentences: int = 3):
    if not WIKI_AVAILABLE:
        return None
    try:
        wikipedia.set_lang(lang)
        return wikipedia.summary(title, sentences=sentences)
    except Exception:
        return None

@st.cache_data(show_spinner=False)
def describe_place(place: dict):
    name = place.get("name")
    admin1 = place.get("admin1")
    cc = place.get("country_code")

    summary = None
    candidates = [name, f"{name} ({admin1})", admin1]
    for t in candidates:
        if t:
            summary = wiki_summary(t, lang="ko") or wiki_summary(t, lang="en")
        if summary:
            break

    header = f"**추천 여행지**: {name}, {admin1} ({cc})"
    coords = f"위치: {place['lat']:.4f}°, {place['lon']:.4f}°"

    if summary:
        body = textwrap.shorten(summary.replace("\n", " "), width=600, placeholder=" …")
    else:
        body = "이 지역은 근처의 대표 도시에 기반해 추천되었습니다. 자세한 정보는 검색을 통해 확인해 보세요!"

    return f"{header}\n\n{coords}\n\n{body}"

def render_globe(lat: float, lon: float, label: str = "Destination"):
    fig = go.Figure()
    fig.add_trace(go.Scattergeo(
        lon=[lon], lat=[lat],
        text=[label],
        mode="markers+text",
        textposition="top center",
        marker=dict(size=10),
        showlegend=False,
    ))

    fig.update_geos(
        projection_type="orthographic",
        projection_rotation=dict(lon=lon, lat=lat, roll=0),
        showcountries=True,
        showcoastlines=True,
        showocean=True,
        showland=True,
        landcolor="rgb(229, 236, 246)",
        oceancolor="rgb(210, 232, 255)",
        lakecolor="rgb(210, 232, 255)",
        resolution=110,
    )

    fig.update_layout(
        margin=dict(l=0, r=0, t=0, b=0),
        height=520,
    )

    st.plotly_chart(fig, use_container_width=True)

# ---------- UI ----------
st.title("🌍 랜덤 여행지 추천기")
st.caption("버튼 한 번으로 지구본에서 툭! 오늘의 목적지를 추천합니다 ✈️")

col1, col2 = st.columns([2, 1])
with col1:
    continent_filter = st.selectbox(
        "대륙 필터 (선택)",
        ["전체", "Asia", "Europe", "North America", "South America", "Oceania", "Africa"],
        index=0,
        help="원하는 대륙만 골라서 뽑을 수 있어요."
    )
with col2:
    show_wiki = st.toggle("위키 요약 보기", value=True)

if "history" not in st.session_state:
    st.session_state.history = []

btn = st.button("🎲 랜덤 여행지 뽑기", type="primary")

if btn or not st.session_state.history:
    for _ in range(500):
        lat, lon = get_random_coord()
        place = nearest_place(lat, lon)
        cc = place.get("country_code")
        cont = CONTINENTS.get(cc)
        if continent_filter == "전체" or cont == continent_filter:
            st.session_state.history.insert(0, place)
            break

if st.session_state.history:
    place = st.session_state.history[0]
    render_globe(place["lat"], place["lon"], label=place["name"]) 

    desc = describe_place(place) if show_wiki else (
        f"**추천 여행지**: {place['name']}, {place['admin1']} ({place['country_code']})\n\n"
        f"위치: {place['lat']:.4f}°, {place['lon']:.4f}°"
    )
    st.markdown(desc)

    with st.expander("🧭 최근 추천 기록"):
        for i, p in enumerate(st.session_state.history[:10], start=1):
            st.write(f"{i}. {p['name']}, {p['admin1']} ({p['country_code']}) — {p['lat']:.4f}, {p['lon']:.4f}")
else:
    st.info("버튼을 눌러 첫 여행지를 뽑아보세요!")

pip install -r requirements.txt
streamlit run app.py

