import streamlit as st
import requests
from datetime import datetime

# --- Config visual igual teu Figma ---
st.set_page_config(page_title="Maré Póvoa", page_icon="🌊")
st.markdown("""
<style>
    .mare-card { background: white; padding: 15px; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); text-align: center; }
    .ativa { border: 2px solid #1A73E8; }
</style>
""", unsafe_allow_html=True)

st.title("Maré Póvoa")
st.caption(f"Aver-o-Mar • Atualizado {datetime.now().strftime('%H:%M')}")

# --- Previsão Tempo (simulando IPMA) ---
st.subheader("☀️ Previsão hoje")
col1, col2, col3 = st.columns(3)
col1.metric("22°C", "Parc. nublado")
col2.metric("Vento", "12 km/h N")
col3.metric("Água", "17°C")

# --- As 4 marés que tu desenhou ---
st.subheader("🌊 Marés hoje")
c1, c2 = st.columns(2)
with c1:
    st.markdown('<div class="mare-card">Baixa<br><b>06:12</b><br>0.8m</div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div class="mare-card ativa">Preia-mar<br><b>14:32</b><br>3.2m</div>', unsafe_allow_html=True)

c3, c4 = st.columns(2)
with c3:
    st.markdown('<div class="mare-card">Baixa<br><b>20:45</b><br>0.9m</div>', unsafe_allow_html=True)
with c4:
    st.markdown('<div class="mare-card">Preia<br><b>02:15</b><br>3.0m</div>', unsafe_allow_html=True)

# --- Praias próximas (igual Tela 2) ---
st.subheader("🏖️ Praias próximas")
st.success("🟢 Praia da Lagoa - 0.5km - Própria")
st.warning("🟡 Praia de Aver-o-Mar - 2.1km - Atenção")
st.success("🟢 Praia da Fragosa - 1.2km - Própria")

st.info("Aviso: Agitação marítima moderada à tarde")
