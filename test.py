import streamlit as st
from streamlit_folium import st_folium
import folium

st.set_page_config(page_title="대한민국 여행지도", layout="wide")
st.title("🗺️ 대한민국 여행 지도")
st.write("원하는 도시를 클릭하면 화려한 폭죽과 함께 유명한 장소, 먹거리, 놀거리를 볼 수 있어요!")

# 도시 좌표
cities = {
    "서울": [37.5665, 126.9780],
    "부산": [35.1796, 129.0756],
    "제주": [33.4996, 126.5312],
    "전주": [35.8242, 127.1479],
    "강릉": [37.7519, 128.8761],
    "대전": [36.3504, 127.3845],
    "대구": [35.8714, 128.6014],
    "광주": [35.1595, 126.8526],
}

# 여행 정보 데이터 (생략 가능)
travel_info = { 
    "서울": {"명소":["경복궁","남산타워"],"먹거리":["불고기","비빔밥"],"놀거리":["한강 자전거 타기","명동 쇼핑"]},
    "부산": {"명소":["해운대","광안리 해수욕장"],"먹거리":["밀면","돼지국밥"],"놀거리":["해변 산책","국제시장 쇼핑"]},
    "제주": {"명소":["한라산","성산일출봉"],"먹거리":["흑돼지","갈치조림"],"놀거리":["오름 등반","서핑"]},
    "전주": {"명소":["전주한옥마을","경기전"],"먹거리":["전주비빔밥","콩나물국밥"],"놀거리":["한옥마을 한복체험"]},
    "강릉": {"명소":["경포대","안목해변 커피거리"],"먹거리":["초당두부","강릉커피"],"놀거리":["서핑","바다 열차 타기"]},
    "대전": {"명소":["엑스포과학공원","한밭수목원"],"먹거리":["성심당 빵","칼국수"],"놀거리":["과학관 체험","대전 아쿠아리움"]},
    "대구": {"명소":["팔공산","동성로"],"먹거리":["막창","동인동 찜갈비"],"놀거리":["동성로 쇼핑","이월드"]},
    "광주": {"명소":["무등산","국립아시아문화전당"],"먹거리":["광주 떡갈비","상추튀김"],"놀거리":["문화전당 전시관람","충장로 쇼핑"]},
}

# 지도 표시
m = folium.Map(location=[36.5, 127.8], zoom_start=7)
for city, coord in cities.items():
    folium.Marker(
        location=coord,
        popup=f"{city} 클릭!",
        tooltip=city,
        icon=folium.Icon(color="red", icon="flag")
    ).add_to(m)

map_data = st_folium(m, width=800, height=500)

# 도시 클릭 이벤트 처리
if map_data["last_object_clicked_popup"]:
    selected_city = map_data["last_object_clicked_popup"].replace(" 클릭!", "")

    st.markdown(f"""
    <div style="text-align:center; font-size:40px; color:gold; font-weight:bold;">
        🎆 {selected_city} 여행 정보 🎆
    </div>
    <canvas id="canvas"></canvas>
    <script>
    const canvas = document.getElementById('canvas');
    const ctx = canvas.getContext('2d');
    canvas.width = window.innerWidth;
    canvas.height = 300;

    function random(min, max) {{ return Math.random() * (max - min) + min; }}

    class Firework {{
      constructor() {{
        this.x = random(100, canvas.width-100);
        this.y = canvas.height;
        this.targetY = random(50, 150);
        this.color = `hsl(${random(0, 360)}, 100%, 50%)`;
        this.exploded = false;
        this.particles = [];
      }}
      update() {{
        if (!this.exploded) {{
          this.y -= 5;
          if (this.y <= this.targetY) {{
            this.exploded = true;
            for (let i=0; i<100; i++) {{
              this.particles.push(new Particle(this.x, this.y, this.color));
            }}
          }}
        }}
      }}
      draw() {{
        if (!this.exploded) {{
          ctx.fillStyle = this.color;
          ctx.fillRect(this.x, this.y, 3, 10);
        }} else {{
          this.particles.forEach(p => {{p.update(); p.draw();}});
        }}
      }}
    }}

    class Particle {{
      constructor(x, y, color) {{
        this.x = x;
        this.y = y;
        this.color = color;
        this.angle = random(0, Math.PI*2);
        this.speed = random(1, 6);
        this.life = 100;
      }}
      update() {{
        this.x += Math.cos(this.angle)*this.speed;
        this.y += Math.sin(this.angle)*this.speed;
        this.speed *= 0.95;
        this.life--;
      }}
      draw() {{
        ctx.fillStyle = this.color;
        ctx.fillRect(this.x, this.y, 2, 2);
      }}
    }}

    let fireworks = [];
    function animate() {{
      requestAnimationFrame(animate);
      ctx.fillStyle = 'rgba(0, 0, 0, 0.2)';
      ctx.fillRect(0, 0, canvas.width, canvas.height);
      if (Math.random() < 0.05) fireworks.push(new Firework());
      fireworks.forEach(fw => {{fw.update(); fw.draw();}});
    }}
    animate();
    </script>
    """, unsafe_allow_html=True)

    st.subheader("📍 유명한 명소")
    st.write(", ".join(travel_info[selected_city]["명소"]))

    st.subheader("🍜 먹거리")
    st.write(", ".join(travel_info[selected_city]["먹거리"]))

    st.subheader("🎉 놀거리")
    st.write(", ".join(travel_info[selected_city]["놀거리"]))
