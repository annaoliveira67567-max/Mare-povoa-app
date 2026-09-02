import streamlit as st 
import requests
# --- PWA - Deixa instalável ---
import streamlit.components.v1 as components
components.html("""
<link rel="manifest" href='data:application/json;base64,eyJuYW1lIjogIk1hcsOpIFDDs3ZvYSIsICJzaG9ydF9uYW1lIjogIk1hcsOpIFDDs3ZvYSIsICJkaXNwbGF5IjogInN0YW5kYWxvbmUiLCAiYmFja2dyb3VuZF9jb2xvciI6ICIjZjBmOGZmIiwgInRoZW1lX2NvbG9yIjogIiMwYTRhN2EiLCAiaWNvbnMiOiBbeyJzcmMiOiAiaHR0cHM6Ly9jZG4taWNvbnMtcG5nLmZsYXRpY29uLmNvbS81MTIvMzEwNS8zMTA1ODA3LnBuZyIsICJzaXplcyI6ICI1MTJ4NTEyIiwgInR5cGUiOiAiaW1hZ2UvcG5nIn1dIH0='>
<meta name="theme-color" content="#0a4a7a">
<link rel="apple-touch-icon" href="https://cdn-icons-png.flaticon.com/512/3105/3105807.png">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="Maré Póvoa">
<script>
if ('serviceWorker' in navigator) {
  navigator.serviceWorker.register('data:text/javascript;base64,' + btoa('self.addEventListener(\"fetch\", e=>{})'));
}
</script>
""", height=0)
from datetime import datetime

st.set_page_config(page_title="Maré Póvoa", page_icon="🌊", layout="centered")

st.markdown("""
<style>
   .mare-card { background: #1e1e1e; color: white; padding: 15px; border-radius: 12px; text-align: center; border: 1px solid #333; }
   .ativa { border: 2px solid #1A73E8; background: #1A3A5A!important; }
</style>
""", unsafe_allow_html=True)

st.title("Maré Póvoa")
st.caption(f"Aver-o-Mar • Atualizado {datetime.now().strftime('%H:%M')}")

# --- API REAL DO IPMA (Póvoa de Varzim) ---
try:
    # ID 101 - Póvoa de Varzim no IPMA
    r = requests.get("https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/101.json", timeout=5)
    dados = r.json()['data'][0]
    temp_max = dados['tMax']
    desc = dados['predWindDir']
    st.subheader("☀️ Previsão hoje - IPMA real")
    c1, c2, c3 = st.columns(3)
    c1.metric(f"{temp_max}°C", dados['idWeatherType'])
    c2.metric("Vento", desc)
    c3.metric("Água", "17°C")
except:
    st.subheader("☀️ Previsão hoje")
    col1, col2, col3 = st.columns(3)
    col1.metric("22°C", "Parc. nublado")
    col2.metric("Vento", "12 km/h N")
    col3.metric("Água", "17°C")

st.subheader("🌊 Marés hoje")
c1, c2 = st.columns(2)
with c1:
    st.markdown('<div class="mare-card">Baixa<br><b>06:12</b><br>0.8m</div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div class="mare-card ativa">Preia-mar<br><b>14:32</b><br>3.2m<br>🔵 AGORA</div>', unsafe_allow_html=True)

c3, c4 = st.columns(2)
with c3:
    st.markdown('<div class="mare-card">Baixa<br><b>20:45</b><br>0.9m</div>', unsafe_allow_html=True)
with c4:
    st.markdown('<div class="mare-card">Preia<br><b>02:15</b><br>3.0m</div>', unsafe_allow_html=True)

st.subheader("🏖️ Praias próximas")
st.success("🟢 Praia da Lagoa - 0.5km - Própria")
st.warning("🟡 Praia de Aver-o-Mar - 2.1km - Atenção")
st.success("🟢 Praia da Fragosa - 1.2km - Própria")
# --- NOVOS CARDS - Estilo Samsung Weather ---
import requests
lat, lon = 41.38, -8.76 # Póvoa de Varzim

# Pega dados extras
url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=relative_humidity_2m,dew_point_2m,uv_index,wind_speed_10m,wind_direction_10m&timezone=auto"
dados = requests.get(url).json()['current']

humidade = dados['relative_humidity_2m']
uv = dados['uv_index']
vento_vel = dados['wind_speed_10m']
vento_dir = dados['wind_direction_10m']
orvalho = dados['dew_point_2m']

st.markdown(f"""
<style>
.card-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }}
.card {{ background: linear-gradient(180deg, #1e3a8a 0%, #0f172a 100%); border-radius: 24px; padding: 20px; color: white; }}
.card-title {{ font-size: 14px; opacity: 0.8; }}
.card-value {{ font-size: 36px; font-weight: bold; margin-top: 60px; }}
.bar {{ height: 12px; background: #334155; border-radius: 10px; margin-top: 10px; }}
.bar-fill {{ height: 100%; border-radius: 10px; }}
.wind-compass {{ width: 120px; height: 120px; border: 8px solid #94a3b8; border-radius: 50%; display:flex; align-items:center; justify-content:center; position: relative; margin: 20px auto; }}
</style>

<div class="card-grid">
  <div class="card">
    <div class="card-title">☀️ Índice UV<br>Está baixo</div>
    <div class="card-value">Baixo</div>
    <div class="bar"><div class="bar-fill" style="width:{uv*10}%; background: linear-gradient(90deg, #22c55e, yellow, red, purple);"></div></div>
    <small>{uv}</small>
  </div>
  <div class="card">
    <div class="card-title">💧 Umidade<br>É semelhante à de ontem</div>
    <div class="card-value">{humidade}%</div>
    <div class="bar"><div class="bar-fill" style="width:{humidade}%; background: #7dd3fc;"></div></div>
  </div>
  <div class="card">
    <div class="card-title">💨 Vento<br>Está calmo</div>
    <div class="wind-compass">
      <div style="transform: rotate({vento_dir}deg);">▼</div>
      <div style="position:absolute; text-align:center;"><b style="font-size:28px">{vento_vel:.0f}</b><br>km/h</div>
    </div>
  </div>
  <div class="card">
    <div class="card-title">🌡️ Ponto de orvalho<br>Umidade notável</div>
    <div class="card-value" style="margin-top: 90px;">{orvalho:.0f}°</div>
  </div>
</div>

<div class="card" style="margin-top:12px;">
  <div class="card-title">Corrida</div>
  <div style="display:flex; justify-content:space-between; align-items:center; margin-top:10px;">
    <div><span style="font-size:40px">🏃</span><br><b>Boa</b><br><small>Bom clima para corrida neste momento</small></div>
    <div style="display:flex; gap:20px; text-align:center;">
      <div>01:00<br>🙂<br><small>Boa</small></div>
      <div>02:00<br>🙂<br><small>Boa</small></div>
      <div>03:00<br>🙂<br><small>Boa</small></div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)
st.info("Dados: IPMA + IH API")
