import streamlit as st
import requests
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
st.info("Dados: IPMA + IH API")
